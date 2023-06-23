<?php
require_once 'function.php';

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
        $sendResult = read_db($host, $db, $user, $password);
        header('Location: ' . $redirectUrl);
        exit();
    }

    elseif ($selectServer === 'onlyDB') {
        $host     = '3.26.30.103';
        $db       = 'EC2_dev04';
        $user     = 'test2'; 
        $password = 'test'; 
        $pdo = db_connect($host, $db, $user, $password);
        echo "onlyDBサーバーに接続しました";
        echo '<br>';
        $sendResult = read_db($host, $db, $user, $password);
        header('Location: result.html?sendResult=' . urlencode($sendResult));
    }
}

