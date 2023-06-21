<?php
// -----------------------------------------------------------
// DB接続して接続が完了したら、「接続に完了しました」と表示させる
// -----------------------------------------------------------

$host     = 'localhost';
$db       = 'EC2_dev01';
$user     = 'root'; 
$password = 'suzuki'; 

try {
    $pdo = new PDO("mysql:host=$host; dbname=$db; charset=utf8", $user, $password);
    echo '接続に完了しました';
} catch (PDOException $e) {
    echo '接続に失敗しました';
}
?>
