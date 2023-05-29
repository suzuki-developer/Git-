import config
import os
import json
import hashlib
import hmac
import base64
import requests
from http.server import BaseHTTPRequestHandler, HTTPServer

class LINEBotHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # 環境変数から「CHANNEL_ACCESS_TOKEN」と「CHANNEL_SECRET」の取得
        CHANNEL_ACCESS_TOKEN = os.environ["CHANNEL_ACCESS_TOKEN"]
        CHANNEL_SECRET = os.environ["CHANNEL_SECRET"]
        
        # リクエストヘッダーから「X-Line-Signature」の取得
        signature = self.headers['X-Line-Signature']
        # リクエストヘッダーから「Content-Length」の取得
        content_length = int(self.headers['Content-Length'])
        # リクエストボディの取得
        body = self.rfile.read(content_length)
        
        # LINE APIから送られたデータが正しいか検証
        hash = hmac.new(CHANNEL_SECRET.encode('utf-8'), body, hashlib.sha256).digest()
        signature_answer = base64.b64encode(hash).decode('utf-8')
        if signature != signature_answer:
            self.send_response(400)
            self.end_headers()
            self.wfile.write('Bad Request'.encode())
            return
        
        # LINE APIから送られてきたメッセージの取得
        data = json.loads(body)
        message = data["events"][0]["message"]["text"]
        
        # メッセージをオウム返し
        reply_token = data["events"][0]["replyToken"]
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + CHANNEL_ACCESS_TOKEN
        }
        payload = {
            "replyToken": reply_token,
            "messages": [
                {
                    "type": "text",
                    "text": message
                }
            ]
        }
        response = requests.post("https://api.line.me/v2/bot/message/reply", headers=headers, json=payload)
        self.send_response(response.status_code)
        self.end_headers()
        self.wfile.write(response.content)

if __name__ == "__main__":
    server = HTTPServer(('0.0.0.0', 8080), LINEBotHandler)
    server.serve_forever()