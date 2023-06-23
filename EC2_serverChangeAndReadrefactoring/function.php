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