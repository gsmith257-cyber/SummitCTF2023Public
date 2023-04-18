<!DOCTYPE html>
<html>
  <head>
    <title>Caesar's Mountain Photos</title>
    <meta charset="utf-8">
  </head>
  <body>
    <h1>Caesar's Mountain Photos</h1>

    <form action="photos.php" method="post" enctype="multipart/form-data">
      <label for="photo">Upload a photo of Caesar's Mountain:</label>
      <input type="file" name="photo" id="photo">

      <input type="submit" value="Upload">
    </form>
  </body>
</html>

<?php
if(isset($_FILES['photo'])) {
  $file_name = $_FILES['photo']['name'];
  $file_tmp = $_FILES['photo']['tmp_name'];
  move_uploaded_file($file_tmp,"uploads/".$file_name);
  echo "File uploaded successfully.";
}
?>
