# ===========================
# 必要なライブラリのインポート
# ===========================
import wikipedia

# =====================================================
# ユーザーが入力したワードを受け取り、検索結果の概要を返す
# =====================================================
def wiki(word):
    wikipedia.set_lang('ja')                      # 使用言語を日本語に設定

    # ----------
    # 通常の処理
    # ----------
    try:
        candidate_list = wikipedia.search(word)       # wordで検索を行い候補となるページのリストを返す
        print("------ユーザー入力値------")
        print(word)
        print('------ユーザー入力値の検索結果------')
        print(candidate_list)

        if not candidate_list:                        # 検索結果がなかった場合
            result = '該当する結果がありませんでした。'
        else:
            # リストのインデックス[0]が最も適した候補になる
            # wikipedia.page()でページを取得する
            search_page = wikipedia.page(candidate_list[0]) 
            print('------取得したページの0番目------')
            print(search_page)

            # 取得したページの概要部分の取り出し
            result = search_page.summary
            print('------取得したページの概要------')
            print(result)

            # 結果を返す
            return result
    
    # -------------------------
    # 曖昧さ回避が出た場合の処理
    # -------------------------
    except wikipedia.exceptions.DisambiguationError as e:
        print( '検索結果が曖昧です:', e.options)                                 # e.optionsで曖昧さ回避のリストを取得
        result = '検索結果が曖昧です。次の候補があります:' + ', '.join(e.options) # 候補リストの要素をカンマで区切って文字列に結合
        print('------曖昧さ回避の結果------')
        print(result)

        # 結果を返す
        return result

# ==========
# 動作確認用
# ==========
# このファイル単体で実行すると、鬼滅の刃の検索結果を表示する
if __name__ == '__main__':
    print(wiki('鬼滅の刃'))