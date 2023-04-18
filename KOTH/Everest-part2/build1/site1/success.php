<?php

session_start();
if (!isset($_SESSION['username'])) {
    
    header("Location: index.html");
}

echo base64_decode("U3VtbWl0Q1RGe1czbGMwbWVfVDBfN2hlX2IzZzFubjFuZyEhfQ==");


?>
<html>
<h2> Upload Your Cool Climber Pics! </h2>
<form action='upload.php' method='post' enctype='multipart/form-data'>
    Select image to upload:
<input type='file' name='fileToUpload' id='fileToUpload'>
<input type='submit' value='Upload Image' name='submit'>
</form>
<style>
    body {
        background-color: #000000;
        color: #ffffff;
    }
    h2 {
        color: #ffffff;
    }
    input {
        background-color: #ffffff;
        color: #000000;
    }
</style>
</html>