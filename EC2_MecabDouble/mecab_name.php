<?php
// ---------------------------
// 名詞のみを抽出して配列に保存
// ---------------------------
$inputTextA = $_POST['textA'];
$inputTextB = $_POST['textB'];

$mecab = new MeCab\Tagger();


$nodesA = $mecab->parseToNode($inputTextA);
$nounsA = [];
foreach ($nodesA as $n) {
    $features = explode(',', $n->getFeature());
    if ($features[0] === '名詞') {
        $nounsA[] = $n->getSurface();
    }
}

$nodesB = $mecab->parseToNode($inputTextB);
$nounsB = [];
foreach ($nodesB as $n) {
    $features = explode(',', $n->getFeature());
    if ($features[0] === '名詞') {
        $nounsB[] = $n->getSurface();
    }
}

header("Location: result.php?sendWordA=" . urlencode(implode(',', $nounsA)) . "&sendWordB=" . urlencode(implode(',', $nounsB)));
exit;
?>
