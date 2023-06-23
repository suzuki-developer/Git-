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

            if(isset($_GET['sendWord1']) && !empty($_GET['sendWord1']) && isset($_GET['sendWord2']) && !empty($_GET['sendWord2'])) {
                $getWord1 = $_GET['sendWord1'];
                $getWord2 = $_GET['sendWord2'];

                echo "<h2>あなたが入力した単語: $getWord1</h2>";
                echo "<h2>あなたが入力した単語: $getWord2</h2>";

                $stmt1 = $pdo->prepare("SELECT COUNT(*) AS count FROM usersWord WHERE word = :word1");
                $stmt1->bindValue(':word1', $getWord1);
                $stmt1->execute();
                $count1 = $stmt1->fetchColumn();
                echo "<p>あなたが入力した単語は: $count1 件登録されています</p>";

                $stmt2 = $pdo->prepare("SELECT COUNT(*) AS count FROM usersWord WHERE word = :word2");
                $stmt2->bindValue(':word2', $getWord2);
                $stmt2->execute();
                $count2 = $stmt2->fetchColumn();
                echo "<p>あなたが入力した単語は: $count2 件登録されています</p>";

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
