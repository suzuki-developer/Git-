## リアルタイムで更新される時計を作る
- phpでは不可
- JavaScriptを使用して1秒ごとに画面を更新させる必要がある
- 参考
    - 現在時刻をテキストでリアルタイムに表示し続ける時計を作る方法
    - https://www.nishishi.com/javascript-tips/realtime-clock-setinterval.html


## 実装手順
1. 現在時刻を格納するDateオブジェクトを作成
2. Dateオブジェクトから「年」・「時」・「分」・「秒」を取り出し
3. 時計として表示する文字列を作成
4. 描画用の領域にある文字列を書き換え
5. 上記1～4を、1秒毎に繰り返す。


## new Date()
- Date クラスのインスタンスを作成
- このオブジェクトには、年、月、日、時、分、秒、ミリ秒などの情報が含まれている


## document.getElementById("RealtimeClockArea").innerHTML = msg;
- 指定されたid属性を持つHTML要素を取得する
    - 今回なら、RealtimeClockAreaというidを持つ要素を取得している

- document.getElementById()
    - HTMLの要素には、id 属性を設定することができる
    - IDに基づいて要素を取得するために使用される

- innerHTML 
    - HTML要素の中にあるテキストやHTMLコードを設定したり取得したりするためのプロパティ
    - RealtimeClockArea というidを持つ要素の中に、変数 msg の値を表示するという意味