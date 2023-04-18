<?php
  $servername = 'database';
  $username  = 'level2';
  $password = 'level2';
  $database = 'level2';
  $flag = "SummitCTF{1nj3ct10n_1s_4w3s0m3}";

  // Create connection
  $conn = new mysqli($servername, $username, $password, $database);

  // Check connection
  if ($conn->connect_error) {
      die("Unable to connect to MYSQL server");
  }
?>
