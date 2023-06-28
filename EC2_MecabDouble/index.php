<!DOCTYPE html>
<html>
<head>
    <title>Text Comparison</title>
</head>
<body>
    <h1>名詞数比較</h1>
    <h2>比較をしたい文書を入力してください</h2>
    <form action="mecab_name.php" method="post">
        <label for="textA">Text A:</label>
        <br>
        <textarea id="textA" name="textA" rows="4" cols="50"></textarea>
        <br>
        <label for="textB">Text B:</label>
        <br>
        <textarea id="textB" name="textB" rows="4" cols="50"></textarea>
        <br>
        <input type="submit" value="比較する">
    </form>
</body>
</html>
