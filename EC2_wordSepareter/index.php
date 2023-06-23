<?php
$userInputWord = "私は鈴木です";
$separeter_1 = "は";
$separeter_2 = "です";

// 「私は鈴木です」を"は"で区切る
// 「私」「鈴木です」の配列ができる
$wordArray_1 = explode($separeter_1, $userInputWord);
var_dump($wordArray_1);
$separatedWord_1 = $wordArray_1[0];
echo $separatedWord_1;
echo "<br>";

// 「鈴木です」を"です"で区切る
// 「鈴木」「」の配列が出来る
$wordArray_2 = explode($separeter_2, $wordArray_1[1]);
var_dump($wordArray_2);
$separatedWord_2 = $wordArray_2[0];
echo $separatedWord_2;
echo "<br>";

