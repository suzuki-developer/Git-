<?php
$host     = '3.26.30.103';
$db       = 'EC2_dev04';
$user     = 'test2'; 
$password = 'test'; 

function db_connect() {
    global $host, $db, $user, $password;
    try {
        $pdo = new PDO("mysql:host=$host; dbname=$db; charset=utf8", $user, $password);
        echo '現状のサーバ（LAMP）から新規サーバー（onlyDB）のDBへのアクセスが完了しました' . '<br>';
        return $pdo;
    } catch (PDOException $e) {
        echo '接続に失敗しました';
    }
}
?>
