<?php
$str = "すもももももももものうち";
$mecab = new \MeCab\Tagger(array('-O' => 'chasen'));
echo $mecab->parse($str) . PHP_EOL;