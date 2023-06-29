<!DOCTYPE html>
<html>
<head>
    <title>Result</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>＜名詞数比較：結果画面＞</h1>
    <ul>
        <li>抽出された「名詞」と「使用された回数」を表示します</li>
        <li>抽出した名詞を「あいうえお順」で表示します</li>
        <li>左右のテキストエリアで共通する名詞は「赤」で表示します</li>
        <li>各テキストエリアから抽出された名詞のうち、共通するものを下にまとめて表示します</li>
    </ul>
    <?php
        $getWordsA = $_GET['sendWordA'];
        $wordsA = explode(',', $getWordsA);
        $uniqueWordsA = array_unique($wordsA); 
        sort($uniqueWordsA, SORT_NATURAL | SORT_FLAG_CASE); // テキストエリアAの単語をあいうえお順にソート

        $getWordsB = $_GET['sendWordB'];
        $wordsB = explode(',', $getWordsB);
        $uniqueWordsB = array_unique($wordsB); 
        sort($uniqueWordsB, SORT_NATURAL | SORT_FLAG_CASE); // テキストエリアBの単語をあいうえお順にソート

        $commonWords = array_intersect($uniqueWordsA, $uniqueWordsB);
    ?>

    <!-- 重複を避けて名詞ごとに何回使われていたのか表示 -->
    <div class="list-wrapper">
        <div class="list-container">
            <?php
                echo"<h2>テキストエリアAに入力された名詞</h2>";
                echo "<ul>";
                foreach ($uniqueWordsA as $word) {
                    $countInGetWordsA = 0;
                    foreach ($wordsA as $w) {
                        if ($w === $word) {
                            $countInGetWordsA++;
                        }
                    }
                    $highlightedWord = in_array($word, $commonWords) ? "<span style='color:red;'>$word</span>" : $word;
                    $highlightedCount = in_array($word, $commonWords) ? "<span style='color:red;'>$countInGetWordsA</span>" : $countInGetWordsA;
                    echo "<li>$highlightedWord: $highlightedCount 回</li>";
                }
                echo "</ul>";
            ?>
        </div>

        <div class="list-container">
            <?php
                echo"<h2>テキストエリアBに入力された名詞</h2>";
                echo "<ul>";
                foreach ($uniqueWordsB as $word) {
                    $countInGetWordsB = 0;
                    foreach ($wordsB as $w) {
                        if ($w === $word) {
                            $countInGetWordsB++;
                        }
                    }
                    $highlightedWord = in_array($word, $commonWords) ? "<span style='color:red;'>$word</span>" : $word;
                    $highlightedCount = in_array($word, $commonWords) ? "<span style='color:red;'>$countInGetWordsB</span>" : $countInGetWordsB;
                    echo "<li>$highlightedWord: $highlightedCount 回</li>";
                }
                echo "</ul>";
            ?>
        </div>
    </div>

    <!-- 共通する単語を表示 -->
    <?php
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
        echo "</ul>"; 
    ?>

    <br>
    <a href="index.php">戻る</a>
</body>
</html>
