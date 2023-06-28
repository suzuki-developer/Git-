<?php
require_once 'db_connect.php';

// テストケース
$userInputText = "福岡県西方沖地震は、2005年3月20日、福岡県北西沖の玄界灘で発生したマグニチュード7.0、最大震度6弱の地震。震源に近い福岡市西区の玄界島で住宅の半数が全壊する被害となったのをはじめ、同区能古島、西浦、宮浦、東区志賀島などの沿岸地区で大きな被害となった。死者1名、負傷者約1,200名、住家全壊約140棟。福岡市付近では有史以来最も大きな地震となった。";

// -------------------------------------
// テストケースから名詞を抽出してDBに保存
// -------------------------------------
try {
    // 名詞の抽出
    $mecab = new MeCab\Tagger();
    $nodes = $mecab->parseToNode($userInputText);
    $nouns = [];
    foreach ($nodes as $n) {
        $features = explode(',', $n->getFeature());
        if ($features[0] === '名詞') {
            $nouns[] = $n->getSurface();
        }
    }

    $pdo = db_connect();
    $stmt = $pdo->prepare("DELETE FROM usersWord");
    $stmt->execute();

    // DBに保存
    if (!empty($nouns)) {
        $stmt = $pdo->prepare("INSERT INTO usersWord (word) VALUES (:word)");
        foreach ($nouns as $noun) {
            $stmt->bindValue(':word', $noun);
            $stmt->execute();
        }
    }
    echo "テキストの名詞抽出と保存が完了しました。";
} catch (PDOException $e) {
    echo "エラーが発生しました";
}

// -------------------------------------------------------
// テストケースの中の各名詞の数とDBに保存された名詞の数を照合
// -------------------------------------------------------
try {
    $pdo = db_connect();
    $uniqueWords = array_unique($nouns); // 重複を排除した単語の配列

    echo "<h2>テスト入力された単語: </h2>";
    echo "<ul>";
    foreach ($uniqueWords as $word) {
        echo "<li>$word: ";
        $stmt = $pdo->prepare("SELECT COUNT(*) AS count FROM usersWord WHERE word = :word");
        $stmt->bindValue(':word', $word);
        $stmt->execute();
        $countInDB = $stmt->fetchColumn();

        $countInInputText = 0;
        foreach ($nouns as $n) {
            if ($n === $word) {
                $countInInputText++;
            }
        }
        echo "<p>テスト入力された文章の中では「 $countInInputText 」回使われていました</li>";
        echo "<p>データベースには「 $countInDB 」件登録されました</li>";

        if ($countInInputText == $countInDB) {
            echo "<p><b><span style='color: blue;'>一致しました</span></b></p>";
        } else {
            echo "<p><b><span style='color: red;'>一致しません</span></b></p>";
        }
        echo "<br><br>";
    }

    // データベース内の単語を削除
    $stmt = $pdo->prepare("DELETE FROM usersWord");
    $stmt->execute();
} catch (PDOException $e) {
    echo "エラーが発生しました";
}
