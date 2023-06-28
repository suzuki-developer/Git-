<?php
require_once 'db_connect.php';

try {
    $userInputText = $_POST['inputText'];

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
    if(!empty($nouns)) {
      $stmt = $pdo->prepare("INSERT INTO usersWord (word) VALUES (:word)");
      foreach ($nouns as $noun) {
        $stmt->bindValue(':word', $noun);
        $stmt->execute();
      }
    }
    echo "テキストの名詞抽出と保存が完了しました。";
    header("Location: results.php?sendWord=".urlencode(implode(",", $nouns)));
    exit;
  } catch (PDOException $e) {
    echo "エラーが発生しました";
  }
?>
