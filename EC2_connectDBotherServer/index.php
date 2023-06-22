<?php
// -----------------------------------------------------------
// 現状のサーバ（LAMP）→　新規サーバー（onlyDB）のDB　アクセス
// DB接続して接続が完了したら、「接続に完了しました」と表示させる
// -----------------------------------------------------------

$host     = '3.26.30.103';
$db       = 'EC2_dev04';
$user     = 'test2'; 
$password = 'test'; 

try {
    $pdo = new PDO("mysql:host=$host; dbname=$db; charset=utf8", $user, $password);
    echo '現状のサーバ（LAMP）から新規サーバー（onlyDB）のDBへのアクセスが完了しました';
} catch (PDOException $e) {
    echo '接続に失敗しました';
}
?>
