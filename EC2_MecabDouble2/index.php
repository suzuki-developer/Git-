<!DOCTYPE html>
<html>
<head>
    <title>Text Comparison</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>＜名詞数比較：入力画面＞</h1>
    <ul>
        <li>このwebアプリでは、各テキストエリアに入力された文章の中から「名詞」のみを抽出します</li>
        <li>各テキストエリアで共通する「名詞」がどれだけあるかも分かります</li>
        <li>各テキストエリアに文章を入力して「比較する」ボタンを押下して下さい</li>
    </ul>
    <br>
    <form action="mecab_name.php" method="post">
        <div class="form-wrapper">
            <div class="text-area">
                <label for="textA">テキストエリアA:</label>
                <br>
                <textarea id="textA" name="textA" rows="25" cols="50"></textarea>
            </div>
            <div class="text-area">    
                <label for="textB">テキストエリアB:</label>
                <br>
                <textarea id="textB" name="textB" rows="25" cols="50"></textarea>
            </div>
        </div>
        <br>
        <input type="submit" value="比較する">
    </form>
</body>
</html>
