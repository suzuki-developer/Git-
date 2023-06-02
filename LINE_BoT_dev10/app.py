#######################################################################
# config.pyの読み込み（チャンネルアクセストークンとチャンネルシークレット）
#######################################################################
import config


########################################################################
# Flask、LINE Messaging APIで必要なライブラリやクラスや例外処理のインポート
########################################################################
from flask import Flask, request, abort

from linebot import(
    LineBotApi, WebhookHandler
)
from linebot.exceptions import(
    InvalidSignatureError
)
from linebot.models import(
    MessageEvent, TextMessage, TextSendMessage
)


###########################
# Flaskのインスタンスを作成
###########################
app = Flask(__name__)


#############################################################
# チャンネルアクセストークンとチャンネルシークレットを変数に格納
#############################################################
line_bot_api = LineBotApi(config.LINE_CHANNEL_ACCESS_TOKEN) # config.pyで設定したチャンネルアクセストークン
handler = WebhookHandler(config.LINE_CHANNEL_SECRET)        # config.pyで設定したチャンネルシークレット


###################################################################################################
# @app.routeデコレーターは、/callbackエンドポイントで受信したPOSTリクエストを処理するcallback関数を定義
###################################################################################################
# デバッグ用
@app.route("/")
def hello_world():
   return "hello world!"

@app.route("/callback", methods=['POST'])                   # callback 関数のエンドポイントを /callback に設定し、POSTリクエストを受け取る
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']         # request.headersを使って、X-Line-Signatureヘッダーの値を取得（リクエストの署名を検証し、不正な場合はエラーメッセージを返し、要求を中止する）

    # get request body as text
    body = request.get_data(as_text=True)                   
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)                     # handler.handleで取得したボディと署名を渡して、Webhookハンドラーを呼び出す
    except InvalidSignatureError:
        print("Invslid signature. Please check your channel access token/channel secret.")
        abort(400)
    
    return 'OK'                                             # 正常に受信した場合は文字列'OK'を返して、LINE Platformに成功を伝える


#################################################################
# テキストメッセージを受け取った際に実行される関数（今回はオウム返し）
#################################################################

# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# handler.add
# 特定のイベントに対する処理を定義
# MessageEventというイベントタイプが通知され、かつそのメッセージがTextMessageであるときに、handle_message関数が呼び出され、オウム返しのように同じメッセージが返信される
# ユーザーが何らかのアクションをLINE Botに対して行い結果としてサーバーに情報が送信されることをイベントと呼ぶ
# -------------------------------------------------------------------------------------------------------------------------------------------------------------
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.reply_token == "00000000000000000000000000000000":
        return
    
    # LINE側からメッセージを返信する部分
    line_bot_api.reply_message(
        event.reply_token,                   # メッセージの返信先の情報
        TextMessage(text=event.message.text) # 返信するメッセージの内容（event.message.textの部分は、LINEから受け取った値が格納されている）
    )

#######################################################
# アプリケーションをテストするためのローカルサーバーを開始
#######################################################
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

