<?php
$text = '明日は運動会に行く予定です。お弁当が楽しみです。';

$MeCab = new MeCab\Tagger();
$nodes = $MeCab->parseToNode($text);

foreach ($nodes as $n) {
    echo "---------------------------". "\n";
    echo "[" . $n->getSurface() . "]" . "\n";
    echo $n->getFeature() . "\n";
}
?>

