<?php
$target = 97;

$flg = true;
for($i=2; $i<$target; $i++) {
  if($target % $i == 0) {
    $flg = false;
    break;
  }
}

if ($flg) {
  echo $target. "は素数です。";
} else {
  echo $target. "は素数ではありません。";
}
?>
