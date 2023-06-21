<?php
// -------------------------------
// DBに登録されている「名前」を表示
// -------------------------------

require_once 'db_connect.php';

try {
    $pdo = db_connect();

    $stmt   = $pdo->query('SELECT name FROM userProfile');
    $result = $stmt->fetchAll(PDO::FETCH_ASSOC);

    echo 'DBに登録されている名前' . '<br>';
    foreach($result as $row) {
        echo $row['name'] . '<br>';
    }    
} catch (PDOException $e) {
        echo '接続に失敗しました';
    }