## foliumオブジェクト
- foliumには[緯度、経度]のリストで渡す必要がある
- 例
```
    ido_keido = []              
    ido_keido.append(latitude)  
    ido_keido.append(longitude) 
```

- 地図オブジェクトの作成
    - location 緯度経度をリストで渡す
    - zoom     デフォルトの表示尺度を指定
- 例
```
    map = folium.Map(location=ido_keido, zoom_start=15)
```