<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>単語カウンター（入力画面）</h1>
    <p>「〇〇は△△です」の形式で入力してください</p>
    <form action="save_word.php" method="POST">
        <label for="inputWord">単語入力:</label>
        <input type="text" id="inputWord" name="inputWord">
        <button type="submit">送信</button>
    <form>
</body>
</html>