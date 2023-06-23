<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css">
    <title>Document</title>
</head>
<body>
    <h1>単語カウンター（結果画面）</h1>
    <?php
        require_once 'db_connect.php';

        try {
            $pdo = db_connect();

            if(isset($_GET['sendWord1']) && !empty($_GET['sendWord1']) && isset($_GET['sendWord2']) && !empty($_GET['sendWord2'])) {
                $getWord1 = $_GET['sendWord1'];
                $getWord2 = $_GET['sendWord2'];

                $stmt1 = $pdo->prepare("SELECT COUNT(*) AS count FROM usersWord WHERE word = :word1");
                $stmt1->bindValue(':word1', $getWord1);
                $stmt1->execute();
                $count1 = $stmt1->fetchColumn();
                echo "<h2 class='inputWord1'>あなたが入力した単語1: $getWord1</h2>";
                echo "<p>あなたが入力した単語1は「 $count1 」回使われています</p>";

                $stmt2 = $pdo->prepare("SELECT COUNT(*) AS count FROM usersWord WHERE word = :word2");
                $stmt2->bindValue(':word2', $getWord2);
                $stmt2->execute();
                $count2 = $stmt2->fetchColumn();
                echo "<h2 class='inputWord2'>あなたが入力した単語2: $getWord2</h2>";
                echo "<p>あなたが入力した単語2は「 $count2 」回使われています</p>";

                // // 名前の順
                // $stmt3 = $pdo->prepare("SELECT word, COUNT(*) AS count FROM usersWord GROUP BY word ORDER BY word");
                // 使用回数順
                $stmt3 = $pdo->prepare("SELECT word, COUNT(*) AS count FROM usersWord GROUP BY word ORDER BY count DESC");

                $stmt3->execute();
                $wordCountList = $stmt3->fetchAll(PDO::FETCH_ASSOC);
                // var_dump($wordCountList);

                if (!empty($wordCountList)) {
                    echo "<h2>使われている単語一覧</h2>";
                    echo "<ul>";
                    foreach ($wordCountList as $wordCount) {
                        $word = $wordCount['word'];
                        $count = $wordCount['count'];
                        
                        if ($word === $getWord1) {
                            echo "<li class='inputWord1'>「 $word 」は「 $count 」回使われています</li>";
                        } elseif ($word === $getWord2) {
                            echo "<li class='inputWord2'>「 $word 」は「 $count 」回使われています</li>";
                        } else {
                            echo "<li>「 $word 」は 「 $count 」 回使われています</li>";
                        }
                        
                    }
                    echo "</ul>";
                }
            } 
        } catch (PDOException $e) {
            echo "エラーが発生しました";
        }
    ?>
    <a href="index.php">戻る</a>
</body>
</html>
