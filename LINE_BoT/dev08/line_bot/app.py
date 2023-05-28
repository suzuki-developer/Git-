import os
import logging
from chalice import Chalice
from chalice import BadRequestError

from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger()
app = Chalice(app_name='line_bot')
handler = WebhookHandler(os.environ.get('LINE_CHANNEL_SECRET'))
line_bot_api = LineBotApi(os.environ.get('LINE_CHANNEL_ACCESS_TOKEN'))


@app.route('/callback', methods=['POST'])
def callback():
    try:
        request = app.current_request

        # get X-Line-Signature header value
        signature = request.headers['x-Line-Signature']

        # get request body as text
        body = request.raw_body.decode('utf8')

        # handle webhook body
        handler.handle(body, signature)
    except Exception as err:
        logger.exception(err)
        raise BadRequestError('Invalid signature. Please check your channel access token/channel secret.')

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    """おうむ返しする処理"""
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))