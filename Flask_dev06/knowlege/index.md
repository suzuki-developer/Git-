## flashメッセージについて 
- 使用する場合はwithとセットで使用する
- messages フラッシュメッセージのリストを格納
- get_flashed_messages() 複数のフラッシュメッセージをリストとして返す
- 例
```
    {% with messages = get_flashed_messages() %}
        {% if messages %}
            {% for message in messages %}
                <p style="background-color: lightblue;">
                <b>{{ message }}</b></p>
            {% endfor %}
        {% endif %}          
    {% endwith %}
```

## 表について
- table              表全体
- th    table header 表のタイトル（見出し）
- tr    table row    表の枠組み
- td    table data   セル
