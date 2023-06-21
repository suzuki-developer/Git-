<?php
// -------------------------------------------------------------
// アクセス数が素数の時、あなたは素数番目のユーザーですと表示させる
// -------------------------------------------------------------

require_once 'db_connect.php';

$pdo = db_connect();

$stmt = $pdo->prepare("SELECT count FROM access_log");
$stmt->execute();
$result = $stmt->fetch(PDO::FETCH_ASSOC);

if ($result) {
    $accessCount = $result['count'] + 1;
    $stmt = $pdo->query("UPDATE access_log SET count = $accessCount");
    $stmt->execute();
    
    $flg = true;
    for($i=2; $i<$accessCount; $i++) {
        if($accessCount % $i == 0) {
            $flg = false;
            break;
        }
    }

    if ($flg) {
        echo "あなたは" . $accessCount ."人目のアクセスです";
    } else {
        echo "素数以外！";
    }

} else {
    echo "あなたは初めてのアクセスです";
    $stmt = $pdo->prepare("INSERT INTO access_log (count) VALUES (1)");
    $stmt->execute();
}

