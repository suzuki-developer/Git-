<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>単語カウンター</h1>
    <?php
        require_once 'db_connect.php';

        try {
            $pdo = db_connect();

            if(isset($_GET['sendWord']) && !empty($_GET['sendWord'])) {
                $getWord = $_GET['sendWord'];
                echo "<h2>あなたが入力した単語: $getWord</h2>";

                $stmt = $pdo->prepare("SELECT COUNT(*) AS count FROM usersWord WHERE word = :word");
                $stmt->bindValue(':word', $getWord);
                $stmt->execute();
                $count = $stmt->fetchColumn();
                echo "<p>あなたが入力した単語は: $count 件登録されています</p>";
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
