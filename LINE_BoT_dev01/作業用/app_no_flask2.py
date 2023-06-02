import config
import hmac
import hashlib
import base64
import json
import requests
import urllib.parse
from http.server import BaseHTTPRequestHandler, HTTPServer

# ローカル環境で実行するためのウェブサーバーのポートを指定
PORT = 8000
# チャンネルのアクセストークンとチャンネルシークレットを設定
CHANNEL_ACCESS_TOKEN = 'your_channel_access_token'
CHANNEL_SECRET = 'your_channel_secret'

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        body_size = int(self.headers['Content-Length'])
        body_raw = self.rfile.read(body_size)
        body = json.loads(body_raw)
        signature = self.headers['X-Line-Signature']

        if not verify_signature(body_raw, signature):
            print("Invalid signature.")
            return

        for event in body['events']:
            event_type = event['type']
            if event_type == 'message':
                message_type = event['message']['type']
                if message_type == 'text':
                    reply_token = event['replyToken']
                    message_text = event['message']['text']
                    reply_message(reply_token, message_text)

    def log_message(self, format, *args):
        return

def verify_signature(body, signature):
    # LINEから送信されたリクエストの署名を検証する
    hash = hmac.new(CHANNEL_SECRET.encode('utf-8'), body, hashlib.sha256).digest()
    signature_answer = base64.b64encode(hash).decode('utf-8')
    return signature == signature_answer

def reply_message(reply_token, message):
    # LINE Platformへの返信メッセージを作成する
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {CHANNEL_ACCESS_TOKEN}'
    }
    data = {
        'replyToken': reply_token,
        'messages': [{'type': 'text', 'text': message}]
    }
    data_json = json.dumps(data).encode('utf-8')
    response = requests.post('https://api.line.me/v2/bot/message/reply', headers=headers, data=data_json)

    return response

def run_server():
    # サーバを起動する
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, RequestHandler)
    print('server running at localhost:', PORT)
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
