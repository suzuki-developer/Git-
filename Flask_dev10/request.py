import requests

def get(url):
    response = requests.get(url)
    print(url)
    print(response.status_code)
    print(response.text)

def post(url, data):
    response = requests.post(url, data=data)
    print(url)
    print(response.status_code)
    print(response.text)

if __name__ == '__main__':
    print('======request.pyを実行します======')

    url = 'http://127.0.0.1:5000/api/hello'
    print('------hello パラメータなし-------')
    get(url)
    
    url = 'http://127.0.0.1:5000/api/hello?name=yourName'
    print('------hello パラメータあり------')
    get(url)


    url = 'http://127.0.0.1:5000/api/articles'
    print('------articles 全件取得-------')
    get(url)

    url = 'http://127.0.0.1:5000/api/articles/1'
    print('------articles ID1取得------')
    get(url)

    url = 'http://127.0.0.1:5000/api/articles/7'
    print('------articles ID100(存在しないID)取得------')
    get(url)

    url = 'http://127.0.0.1:5000/api/articles'
    data = {
        'title' : 'TypeScriptはじめました',
        'link'  : 'https://www.true-fly.com/entry/2022/03/09/073000',
    }
    print('------articles 登録------')
    post(url, data)

    print('======全ての処理が終わりました======')

