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
        return $pdo;
    } catch (PDOException $e) {
        echo '接続に失敗しました1';
    }
}

function read_db($host, $db, $user, $password) {
    try {
        $pdo = db_connect($host, $db, $user, $password);
    
        $stmt   = $pdo->query('SELECT name FROM userProfile');
        $result = $stmt->fetchAll(PDO::FETCH_ASSOC);
    
        echo 'DBに登録されている名前' . '<br>';
        foreach($result as $row) {
            echo $row['name'] . '<br>';
        }    
    } catch (PDOException $e) {
            echo '接続に失敗しました2';
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
        echo '<br>';
        read_db($host, $db, $user, $password);
    }

    elseif ($selectServer === 'onlyDB') {
        $host     = '3.26.30.103';
        $db       = 'EC2_dev04';
        $user     = 'test2'; 
        $password = 'test'; 
        $pdo = db_connect($host, $db, $user, $password);
        echo "onlyDBサーバーに接続しました";
        echo '<br>';
        read_db($host, $db, $user, $password);
    }
}

