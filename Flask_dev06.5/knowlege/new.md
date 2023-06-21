## セキュリティ対策について
- target属性を_blankにすることでリンク先で別タブを展開する
- rel属性のnoopener noreferrerを使ってリンク元の情報が送られないようにする
- ※別タブでリンクページを展開したい場合に使う
- 例
    ```
            <a href="https://www.google.co.jp/maps/"
            target="_blank" rel="noopener noreferrer"
            class="button">Google Maps</a>
    ```