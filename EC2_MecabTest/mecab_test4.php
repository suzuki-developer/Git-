<?php
// echo "Hello world";
$str = "すもももももももものうち";

// MeCabオブジェクトの作成
$mecab = new MeCab\Tagger();

// 文字列を解析してノードの配列を取得
$nodes = $mecab->parseToNode($str);
var_dump($nodes);

// ノードの情報を表示
foreach ($nodes as $n) {
    echo "{$n->getSurface()} : {$n->getFeature()}" . PHP_EOL;
}
?>