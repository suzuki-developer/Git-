<!DOCTYPE html>
<html>
<head>
    <title>Result</title>
</head>
<body>
    <?php
    echo"<h2>テキストエリアAに入力された名詞</h2>";
    $getWordsA = $_GET['sendWordA'];
    $wordsA = explode(',', $getWordsA);
    $uniqueWordsA = array_unique($wordsA); // 重複を排除した単語の配列

    echo "<h3>テキストエリアAに入力された単語ごとの出現回数</h3>";
    foreach ($uniqueWordsA as $word) {
        $countInGetWordsA = 0;
        foreach ($wordsA as $w) {
            if ($w === $word) {
                $countInGetWordsA++;
            }
        }
        echo "$word: $countInGetWordsA 回<br>";
    }


    echo"<h2>テキストエリアBに入力された名詞</h2>";
    $getWordsB = $_GET['sendWordB'];
    $wordsB = explode(',', $getWordsB);
    $uniqueWordsB = array_unique($wordsB); // 重複を排除した単語の配列  
    
    echo "<h3>テキストエリアBに入力された単語ごとの出現回数</h3>";
    foreach ($uniqueWordsB as $word) {
        $countInGetWordsB = 0;
        foreach ($wordsB as $w) {
            if ($w === $word) {
                $countInGetWordsB++;
            }
        }
        echo "$word: $countInGetWordsB 回<br>";
    }


    // 共通する単語を抽出
    $commonWords = array_intersect($uniqueWordsA, $uniqueWordsB);

    echo "<h2>テキストエリアAとテキストエリアBの共通する名詞</h2>";
    echo "<ul>";
    if (empty($commonWords)) {
        echo "共通する名詞はありません。";
    } else {
        foreach ($commonWords as $commonWord) {
            echo "<li>$commonWord: ";
            echo "<p>テキストエリアAでは 「 $countInGetWordsA 」回使われており、テキストエリアBでは 「 $countInGetWordsB 」回使われています。</li>";
        }
    }
    ?>
    <br>
    <a href="index.php">戻る</a>
</body>
</html>
