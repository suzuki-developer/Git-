<?php
$host     = 'localhost';
$db       = 'EC2_dev01';
$user     = 'root'; 
$password = 'suzuki'; 

function db_connect() {
    global $host, $db, $user, $password;
    try {
        $pdo = new PDO("mysql:host=$host; dbname=$db; charset=utf8", $user, $password);
        echo '接続に完了しました' . '<br>';
        return $pdo;
    } catch (PDOException $e) {
        echo '接続に失敗しました';
    }
}
?>
