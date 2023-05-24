#######################
# モジュールのインポート
#######################
from flask import Flask, request, abort

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import os
import random


##########################
# Flaskのインスタンスを作成
##########################
app = Flask(__name__)


#############################################################
# チャンネルアクセストークンとチャンネルシークレットを変数に格納
#############################################################
ACSESS_TOKEN = "0bH4egRAJHoEZSNl37lF2zPMBj7VY/fDOlbwlR/aQ2fep8PoW+3M8yJ4lUrYfm1vSCyFXCURAahLPHBpqy1o7dYwZ0JLuX2qsb4RZE6ywf02esBSKzjoQ8tB1MV6AaiL5KFmFexvBiMafkbIiJ76JQdB04t89/1O/w1cDnyilFU="
SECRET = "4d81f5e0f50a2dfb5e863b61e498309f"

line_bot_api = LineBotApi(ACSESS_TOKEN)
handler = WebhookHandler(SECRET)


#########################################################
# FlaskアプリケーションにPOSTメソッドのエンドポイントを追加
# LINEのMessaging APIから送信されたWebhookを受信するため
#########################################################
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
# テキストメッセージを受け取った際に実行される処理
################################################
# 占いを実行する関数
def uranai():
    results = ["大吉", "中吉", "小吉", "末吉", "凶", "大凶"]
    return random.choice(results)

# LINE Botからの応答
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text in ["占う", "今日", "占い", "運勢"]:
        result = uranai()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="今日の運勢は" + result + "です！")
        )
    else:
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="占う、今日、占い、運勢のいずれかを入力してください！")
        )

#######################################################
# アプリケーションをテストするためのローカルサーバーを開始
#######################################################
if __name__ == "__main__":
    app.run(host="localhost", port=8000)