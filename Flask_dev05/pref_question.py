# ===========================
# 必要なライブラリのインポート
# ===========================
import random
import os

# =========================
# app.pyで使えるように関数化
# =========================
def pref_location():    
    # --------------------
    # 辞書を作成して初期化
    # --------------------
    pref_city_dict = {} # {都道府県: 県庁所在地}の辞書
    pref_url_dict = {}  # {都道府県: URL}の辞書

    # ------------------
    # ファイルパスの取得
    # ------------------

    # # os.path.abspath() このファイルの絶対パスを取得
    # dir2 = os.path.abspath((__file__))
    # print(dir2)
    # # 'C:\\Users\\suzuki-s\\Desktop\\Git-practice\\Flask\\Flask_dev05\\pref_question.py'

    # # os.path.dirname() 指定されたパスからディレクトリ部分を取得
    # # 相対パスで指定された場合やスクリプトファイルがカレントディレクトリではない場合には正しい結果が得られない
    # dir1 = os.path.dirname((__file__))
    # print(dir1)
    # # 'C:\\Users\\suzuki-s\\Desktop\\Git-practice\\Flask\\Flask_dev05'

    # このファイルの絶対パスから、ディレクトリパスの取得
    script_dir = os.path.dirname(os.path.abspath(__file__))
    print(script_dir)
    # 'C:\\Users\\suzuki-s\\Desktop\\Git-practice\\Flask\\Flask_dev05'

    # os.path.join() 複数のパス要素を連結して新しいパスを作成
    # 絶対パスを作成して変数に格納
    file_path = os.path.join(script_dir, 'prefectural_office_location.txt')
    print(file_path)
    # 'C:\\Users\\suzuki-s\\Desktop\\Git-practice\\Flask\\Flask_dev05\\prefectural_office_location.txt'

    # ---------------------
    # テキストファイルの取得
    # ---------------------
    # with open() 指定したファイルを開いて閉じる
    with open(file_path, encoding='utf=8') as f:
        print(f)

        # ----------
        # 辞書の作成
        # ----------
        for i in f: # テキストファイルを1行ずつ読み込む
            # rstrip()関数で改行コードを削除した後、
            # split()関数の引数で指定したカンマで分割された文字列をリスト形式で格納
            txt_lines = i.rstrip().split(',')
            print("------テキストファイルの中身------")    
            print(txt_lines)

            pref = txt_lines[0] # 0番目の要素（都道府県）を変数に格納
            print("------都道府県------")
            print(pref)   

            city = txt_lines[1] # 1番目の要素（県庁所在地）を変数に格納
            print("------県庁所在地------")
            print(city) 

            url = txt_lines[2]  # 2番目の要素（URL）を変数に格納
            print("------URL------")
            print(url)

            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            # 辞書について
            # 辞書名[キー] = 値　で辞書にキーと値を追加する
            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            
            # 都道府県:所在地となる辞書を作成
            if pref not in pref_city_dict:  # prefが辞書のキーとして存在しない場合
                pref_city_dict[pref] = city # prefをキー: cityを値　として辞書に追加
            print("------都道府県:所在地となる辞書------")
            print(pref_city_dict)     
            
            # 都道府県:URLとなる辞書を作成
            if url not in pref_url_dict: 
                pref_url_dict[pref] = url
            print("------都道府県:URLとなる辞書------")
            print(pref_url_dict)           
      
        
    # ---------------------------------------------------
    # random.choiceを使うために都道府県が入ったリストを作成
    # ---------------------------------------------------
    pref_name = []
    for i in pref_city_dict.keys():
        pref_name.append(i)
    print("------都道府県が入ったリスト------")
    print(pref_name)

    # --------------------------------------------------------
    # ランダムに選択された都道府県名に対応する、都市名とURLを取得
    # --------------------------------------------------------
    # 都道府県をキーにする
    random_pref = random.choice(pref_name)
    print(random_pref)

    # 都市名
    city_name = pref_city_dict[random_pref]
    print(city_name)

    # URL
    pref_url = pref_url_dict[random_pref]
    print(pref_url)

    return random_pref, city_name, pref_url

# ==========
# 動作確認用
# ==========
if __name__ == '__main__':
    p, c, u = pref_location()
    print(p, c, u)
