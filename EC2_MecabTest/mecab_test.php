<?php
$text = '明日は運動会に行く予定です。お弁当が楽しみです。';

// この書き方だと通らない
// MeCab\Taggerが正解
$MeCab = new MeCabTagger();
$nodes = $MeCab->parseToNode($text);

foreach ($nodes as $n) {
    echo "---------------------------". "n";
    echo "[" . $n->getSurface() . "]" . "n";
    echo $n->getFeature() . "n";
}
?>