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
    MessageEvent, TextMessage, TextSendMessage, ImageMessage, ImageSendMessage
)


###########################
# Flaskのインスタンスを作成
###########################
app = Flask(__name__)


#############################################################
# チャンネルアクセストークンとチャンネルシークレットを変数に格納
#############################################################
ACSESS_TOKEN = "jgSlAgaYlIuGNWjSItzuaQNVKjQTc2irNvER0crF1tJVqWy0MfZgh9Fufqoj7x2vYWm64dqp17UQWkGzXvX/7B4CmccGHZlL4GFT2gZDlRTbuDal3XukdATQq4eJ6QlvDnGmNp5ZHcMXgTR8AzPWRAdB04t89/1O/w1cDnyilFU="
SECRET = "57cfc3b3f79202c8293029652abc14d1"

line_bot_api = LineBotApi(ACSESS_TOKEN)
handler = WebhookHandler(SECRET)


###########################################################################
# /callbackエンドポイントで受信したPOSTリクエストを処理するcallback関数を定義
###########################################################################
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True) 
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)                     
    except InvalidSignatureError:
        print("Invslid signature. Please check your channel access token/channel secret.")
        abort(400)
    
    return 'OK'  

################################################
# テキストメッセージを受け取った際に実行される関数
################################################
# 第一引数は固定
# 第二引数は返信するメッセージを指定

# # オウム返しを行う
# @handler.add(MessageEvent, message=TextMessage)
# def handle_message(event):
#     line_bot_api.reply_message(                  # line_bot_apiから.reply_message()を呼ぶことでメッセージの返信を行う
#         event.reply_token,
#         TextSendMessage(text=event.message.text) # event.message.text ⇒ ユーザーが送信したメッセージ
#     )

# 画像をリプライする（ユーザーが何を発言してもルフィの画像が返ってくる）
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(                  
        event.reply_token,
        ImageSendMessage(
        original_content_url='https://1.bp.blogspot.com/-tVeC6En4e_E/X96mhDTzJNI/AAAAAAABdBo/jlD_jvZvMuk3qUcNjA_XORrA4w3lhPkdQCNcBGAsYHQ/s1048/onepiece01_luffy.png',
        preview_image_url='https://1.bp.blogspot.com/-tVeC6En4e_E/X96mhDTzJNI/AAAAAAABdBo/jlD_jvZvMuk3qUcNjA_XORrA4w3lhPkdQCNcBGAsYHQ/s1048/onepiece01_luffy.png',
        )
    )



#######################################################
# アプリケーションをテストするためのローカルサーバーを開始
#######################################################
if __name__ == "__main__":
    app.run(host="localhost", port=8000)