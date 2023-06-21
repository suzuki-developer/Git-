<?php
// ---------------------------
// アクセス数をセッションで管理
// ---------------------------
session_start();

if (!isset($_SESSION['accessCounter'])) {
    $_SESSION['accessCounter'] = 0;
}

$_SESSION['accessCounter']++;

echo "アクセス数: " . $_SESSION['accessCounter'];

?>

