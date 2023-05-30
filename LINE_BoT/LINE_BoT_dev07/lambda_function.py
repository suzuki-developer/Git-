# ------------------------
# ライブラリのインストール
# ------------------------
import json           # JSONフォーマットを扱うライブラリ
import os             # OSや環境変数にアクセスするライブラリ
import urllib.request # URLを扱うためのライブラリ
import logging        # ログを出力するライブラリ

# ----------------
# ログに関する設定
# ----------------
logger = logging.getLogger()  # ロガーを取得
logger.setLevel(logging.INFO) # ログレベルを設定


# ----------------------
# リクエストに関する記述
# ----------------------
LINE_CHANNEL_ACCESS_TOKEN = os.environ['LINE_CHANNEL_ACCESS_TOKEN'] # ボットの認証情報である「Channel Access Token」を環境変数から取得

REQUEST_URL = 'https://api.line.me/v2/bot/message/reply'    # LINEボットがメッセージを受信した場合に送信するメッセージのエンドポイントのURLを設定
REQUEST_METHOD = 'POST'                                     # HTTPリクエストのメソッドをPOSTに設定（メッセージを送信するから）
REQUEST_HEADERS = {                                         # リクエストヘッダに含まれる内容
    'Authorization': 'Bearer ' + LINE_CHANNEL_ACCESS_TOKEN, # LINE Messaging APIを使うための認証
    'Content-Type':'application/json'                       # JSON形式でデータを送る
}

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Tips
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# LINEチャンネルの管理者は、LINE Messaging APIの利用を申請し、チャンネルアクセストークンを取得する必要があります。
# APIを利用する際に、Authorization ヘッダに Bearer {チャンネルアクセストークン} という形式で、チャンネルアクセストークンを含める必要がある。
# Bearerは、OAuth認証フローにおいてアクセストークンを取得したユーザーを認証するための認証方式の1つ
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# -----------------------------
# 返信するテキストメッセージ情報
# -----------------------------
REQUEST_MESSAGE = [
    {
        'type': 'text',
        'text': 'こんちには！'
    }
]

# -----------------------------------
# AWS Lambdaで呼び出されるハンドラ関数
# -----------------------------------
def lambda_handler(event, context): 
    if 'body' in event:
        body = json.loads(event['body'])
    else:
        body = event

    # Lambda関数が起動された際のイベント内容をログに出力
    logger.info(event) 

    # メッセージの送信に必要な情報を辞書型で格納
    params = {
        # LINE Messaging APIから送信されたイベントへの応答に必要なトークンを指定
        'replyToken': json.loads(event['body'])['events'][0]['replyToken'], 
        # 返信メッセージの設定
        'messages': REQUEST_MESSAGE                                         
    }

    # HTTPリクエスト登録
    request = urllib.request.Request(       # HTTPリクエストのオブジェクトを生成
        REQUEST_URL,                        # 送信先のURL
        json.dumps(params).encode('utf-8'), # 返答に必要なパラメータが格納されたparamsオブジェクトをJSON形式の文字列バイトコードに変換
        method=REQUEST_METHOD,              # HTTPメソッドを POST に設定
        headers=REQUEST_HEADERS             # HTTPヘッダーに必要な情報を設定
    ) 

    # リクエスト実行
    response = urllib.request.urlopen(request, timeout=10)

    # 正常終了
    return 0


