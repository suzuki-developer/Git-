import config
import hmac
import hashlib
import base64
import json
import requests
from http.server import BaseHTTPRequestHandler, HTTPServer

# チャンネルのアクセストークンとチャンネルシークレットを設定
CHANNEL_ACCESS_TOKEN = 'your_channel_access_token'
CHANNEL_SECRET = 'your_channel_secret'


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # サーバーからのPOSTリクエストを処理
        content_length = int(self.headers['content-length'])
        post_data = self.rfile.read(content_length) 
        self.send_response(200) # サーバーレスポンスに成功のコードを設定
        self.end_headers()

        # 署名の検証
        signature = self.headers['X-Line-Signature'] 
        if not self.check_request_signature(post_data, signature):
            print("invalid signature")
            return

        # LINEプラットフォームからの受信イベントのリストを取得する
        body_dict = json.loads(post_data.decode('utf-8'))  
        events = body_dict['events']

        # すべての受信イベントに対して処理を実行する
        for event in events:
            reply_token, message_text = None, None

            if event['type'] == 'message':
                message_type = event['message']['type']
                if message_type == 'text':
                    reply_token = event['replyToken']  
                    message_text = event['message']['text']

            if reply_token and message_text:
                # テキストメッセージに対するオウム返しの処理を行う
                self.reply_message(reply_token, message_text)

    def check_request_signature(self, body, signature):
        # request signature の検証
        hash = hmac.new(CHANNEL_SECRET.encode('utf-8'),body, hashlib.sha256).digest()
        signature_answer = base64.b64encode(hash).decode('utf-8')
        return signature == signature_answer

    def reply_message(self, reply_token, message_text):
        # LINEにメッセージを返信
        url = "https://api.line.me/v2/bot/message/reply"

        headers = {
                "Content-Type": "application/json",
                "Authorization": "Bearer " + CHANNEL_ACCESS_TOKEN
        }

        data = {
            "replyToken": reply_token,
            "messages": [
                {"type": "text", "text": message_text}
            ]
        }

        requests.post(url, headers=headers,data=json.dumps(data))


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    # サーバーの起動
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print('server running at localhost:', 8000)
    httpd.serve_forever()


if __name__ == '__main__':
    run()
