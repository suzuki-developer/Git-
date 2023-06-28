<?php
// 文章
$text = "私はリンゴが好きです。夏にはスイカも食べます。";

// MeCabオブジェクトの作成
$mecab = new MeCab\Tagger();

// 文章を解析してノードの配列を取得
$nodes = $mecab->parseToNode($text);

// 名詞のみを抽出して表示
foreach ($nodes as $n) {
    // 名詞の場合のみ表示
    $features = explode(',', $n->getFeature());
    if ($features[0] === '名詞') {
        echo $n->getSurface() . PHP_EOL;
    }
}
?>
