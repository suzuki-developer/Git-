<?php
require_once 'db_connect.php';

try {
    $pdo = db_connect();

    $userInputWord = $_POST['inputWord'];

    if(!empty($userInputWord)) {
      $separeter_1 = "は";
      $separeter_2 = "です";

      $wordArray_1 = explode($separeter_1, $userInputWord);
      $separatedWord_1 = $wordArray_1[0];

      $wordArray_2 = explode($separeter_2, $wordArray_1[1]);
      $separatedWord_2 = $wordArray_2[0];

      $stmt = $pdo->prepare("INSERT INTO usersWord (word) VALUES (:word1), (:word2)");
      $stmt->bindvalue(':word1', $separatedWord_1);
      $stmt->bindvalue(':word2', $separatedWord_2);
      $stmt->execute();
    }
    header("Location: results.php?sendWord1=$separatedWord_1&sendWord2=$separatedWord_2");
    exit;
  } catch (PDOException $e) {
    echo "エラーが発生しました";
  }