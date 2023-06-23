<?php
require_once 'db_connect.php';

try {
    $pdo = db_connect();

    $userInputWord = $_POST['inputWord'];

    if(!empty($userInputWord)) {
      $stmt = $pdo->prepare("INSERT INTO usersWord (word) VALUES (:word)");
      $stmt->bindvalue(':word', $userInputWord);
      $stmt->execute();
    }
    header("Location: results.php?sendWord=$userInputWord");
    exit;
  } catch (PDOException $e) {
    echo "エラーが発生しました";
  }