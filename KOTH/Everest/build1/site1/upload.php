<?php
$target_dir = "/var/www/html/uploads/";
$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
$uploadOk = 1;
$imageFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));

// Check if image file is a actual image or fake image
if(isset($_POST["submit"])) {
  //$check = getimagesize($_FILES["fileToUpload"]["tmp_name"]); How this should be done ;)
  $extension = explode('.', $_FILES['fileToUpload']['name']);
  $extension = $extension[1];
  $extension = strtolower($extension);
  if($extension != 'jpg' && $extension != 'png'){
    echo "Sorry, only JPG and PNG files are allowed.";
    $uploadOk = 0;
  }
  else {
    echo "File is an image - " . $check["mime"] . ".";
    $uploadOk = 1;
  }
}

// Check if file already exists
if (file_exists($target_file)) {
  echo "Sorry, file already exists.";
  $uploadOk = 0;
}

// Check file size
if ($_FILES["fileToUpload"]["size"] > 500000) {
  echo "Sorry, your file is too large.";
  $uploadOk = 0;
}

// Check if $uploadOk is set to 0 by an error
if ($uploadOk == 0) {
  echo "Sorry, your file was not uploaded.";
// if everything is ok, try to upload file
} else {
  //upload the file to the server
  if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
    echo "The file ". htmlspecialchars( basename( $_FILES["fileToUpload"]["name"])). " has been uploaded.";
  } else {
    echo "Sorry, there was an error uploading your file.";
  }
}
?>
    
