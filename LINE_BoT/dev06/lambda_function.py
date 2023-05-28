import os
import sys
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage
)
from linebot.exceptions import (
    LineBotApiError, InvalidSignatureError
)
import logging

logger = logging.getLogger()
logger.setLevel(logging.ERROR)

channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)

if channel_secret is None:
    logger.error('Specify LINE_CHANNEL_SECRET as enviroment variable')
    sys.exit(1)

if channel_access_token is None:
    logger.error('Specify LINE_CHANNEL_ACCESS_TOKEN as enviroment variable')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

def lambda_handler(event, content):
    if "x-line-signature" in event["headers"]:
        signature = event["headers"]["x-line-signature"]
    elif "x-line-signature" in event["headers"]:
        signature = event["headers"]["x-line-signature"]
    body = event["body"]
    ok_json = {"isBase64Encoded": False,
               "statusCode": 200,
               "headers":{},
               "body": ""}
    error_json = {"isBase64Encoded": False,
                  "statusCode": 500,
                  "headers":{},
                  "body": "Error"}

    try:
        handler.handle(body, signature)
    except LineBotApiError as e:
        logger.error("Got exception from LINE Messaging API: %s\n" % e.message)
        for m in e.error.details:
            logger.error("  %s: %s" % (m.property, m.message))
        return error_json   
    except InvalidSignatureError:
        return error_json
    
    return ok_json

@handler.add(MessageEvent, message=TextMessage)
def message(line_event):
    text = line_event.message.text
    line_bot_api.reply_message(line_event.reply_token, TextSendMessage(text=text))