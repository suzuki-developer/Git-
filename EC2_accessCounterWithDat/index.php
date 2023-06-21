<?php
// ----------------------------
// アクセス数をdatファイルで管理
// ----------------------------

$accessCounterFile = 'accessCounterRecord.dat';

$fileHandle = fopen($accessCounterFile, 'r+');
if(flock($fileHandle, LOCK_EX)) {
    $accessCount = (int)fread($fileHandle, filesize($accessCounterFile));
    $accessCount++;
    rewind($fileHandle);
    fwrite($fileHandle, $accessCount);
    flock($fileHandle, LOCK_UN);
}

fclose($fileHandle);

echo "あなたは" . $accessCount . "人目のアクセスです";
?>