# #####################################################
# 詳細画面（detail.html）で表示する地図を生成するファイル
# -----------------------------------------------------
# ユーザーが入力する緯度経度を使って生成する
# #####################################################

# =====================
# ライブラリのインポート
# =====================
import folium # APIを使用せずに地図を使用できる


# =============================
# 地図を表示するための関数を作成
# =============================
def create_map(latitude, longitude):
    """
    Summary line:
        緯度と経度から、地図オブジェクトを作成する

    args:
        param1 (int): 緯度
        param2 (int): 経度

    Returns:
        HTML形式の地図オブジェクト

    """
    # foliumに渡すリストの作成
    ido_keido = []              
    ido_keido.append(latitude)  
    ido_keido.append(longitude) 

    # 地図オブジェクトの作成
    map = folium.Map(location=ido_keido, zoom_start=15)

    # ポイントマーカーの表示
    folium.Marker(
        location=ido_keido,
        icon = folium.Icon(color='red', icon='star')
    ).add_to(map)

    # 作図した地図オブジェクトをHTML形式に変更
    map = map._repr_html_()

    return map


# ==========
# 動作確認用
# ==========
if __name__ == '__main__':
    map = create_map(35.71688122378675, 140.22492881671042)
    print(map)