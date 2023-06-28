<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>名詞カウンター</h1>
    <?php
    // ------------------------------------
    // この場合だと、同じ単語が重複してしまう
    // ------------------------------------
    error_reporting(E_ALL);
    ini_set('display_errors', 1);
    
        require_once 'db_connect.php';

        try {
            $pdo = db_connect();

            if(isset($_GET['sendWord']) && !empty($_GET['sendWord'])) {
                $getWords = $_GET['sendWord'];
                echo "------getgetWordsの中身を出力------";
                echo "<br>";                
                echo $getWords;
                echo "<br>";
                echo "------Wordsの中身を出力------";
                echo "<br>";
                $words = explode(",", $getWords);
                var_dump($words);

                echo "<h2>あなたが入力した単語: </h2>";
                echo "<ul>";

                foreach ($words as $word) {
                    echo "<li>$word: ";
                    $stmt = $pdo->prepare("SELECT COUNT(*) AS count FROM usersWord WHERE word = :word");
                    $stmt->bindValue(':word', $word);
                    $stmt->execute();
                    $count = $stmt->fetchColumn();
                    echo "<p>あなたが入力した単語はデータベースに $count 件登録されています</li>";
                }
            } else {
                echo "<p>単語が入力されていません</p>";
            }
        } catch (PDOException $e) {
            echo "エラーが発生しました";
        }
    ?>
    <a href="index.php">戻る</a>
</body>
</html>
