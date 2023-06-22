<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form action="" method="POST">
        <input type="radio" name="server" value="LAMP">LAMPサーバー
        <input type="radio" name="server" value="onlyDB">onlyDBサーバー
        <br>
        <input type="submit" value="切り替え">
        <br>
</body>
</html>

<?php
function db_connect($host, $db, $user, $password) {
    try {
        $pdo = new PDO("mysql:host=$host; dbname=$db; charset=utf8", $user, $password);
        // echo "サーバーに接続しました";
        return $pdo;
    } catch (PDOException $e) {
        echo '接続に失敗しました';
    }
}


if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $selectServer = $_POST['server'];

    if ($selectServer === 'LAMP') {
        $host     = 'localhost';
        $db       = 'EC2_dev01';
        $user     = 'root'; 
        $password = 'suzuki'; 
        $pdo = db_connect($host, $db, $user, $password);
        echo "LAMPサーバーに接続しました";
    }

    elseif ($selectServer === 'onlyDB') {
        $host     = '3.26.30.103';
        $db       = 'EC2_dev04';
        $user     = 'test2'; 
        $password = 'test'; 
        $pdo = db_connect($host, $db, $user, $password);
        echo "onlyDBサーバーに接続しました";
    }
}

