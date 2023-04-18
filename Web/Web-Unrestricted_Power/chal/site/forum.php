<!DOCTYPE html>
<html>
<head>
  <title>Forum</title>
</head>
<body>
<style type="text/css">
.form-style-2{
	max-width: 500px;
	padding: 20px 12px 10px 20px;
	font: 13px Arial, Helvetica, sans-serif;
}
.form-style-2-heading{
	font-weight: bold;
	font-style: italic;
	border-bottom: 2px solid #ddd;
	margin-bottom: 20px;
	font-size: 15px;
	padding-bottom: 3px;
}
.form-style-2 label{
	display: block;
	margin: 0px 0px 15px 0px;
}
.form-style-2 label > span{
	width: 100px;
	font-weight: bold;
	float: left;
	padding-top: 8px;
	padding-right: 5px;
}
.form-style-2 span.required{
	color:red;
}
.form-style-2 .tel-number-field{
	width: 40px;
	text-align: center;
}
.form-style-2 input.input-field, .form-style-2 .select-field{
	width: 48%;	
}
.form-style-2 input.input-field, 
.form-style-2 .tel-number-field, 
.form-style-2 .textarea-field, 
 .form-style-2 .select-field{
	box-sizing: border-box;
	-webkit-box-sizing: border-box;
	-moz-box-sizing: border-box;
	border: 1px solid #C2C2C2;
	box-shadow: 1px 1px 4px #EBEBEB;
	-moz-box-shadow: 1px 1px 4px #EBEBEB;
	-webkit-box-shadow: 1px 1px 4px #EBEBEB;
	border-radius: 3px;
	-webkit-border-radius: 3px;
	-moz-border-radius: 3px;
	padding: 7px;
	outline: none;
}
.form-style-2 .input-field:focus, 
.form-style-2 .tel-number-field:focus, 
.form-style-2 .textarea-field:focus,  
.form-style-2 .select-field:focus{
	border: 1px solid #0C0;
}
.form-style-2 .textarea-field{
	height:100px;
	width: 55%;
}
.form-style-2 input[type=submit],
.form-style-2 input[type=button]{
	border: none;
	padding: 8px 15px 8px 15px;
	background: #FF8500;
	color: #fff;
	box-shadow: 1px 1px 4px #DADADA;
	-moz-box-shadow: 1px 1px 4px #DADADA;
	-webkit-box-shadow: 1px 1px 4px #DADADA;
	border-radius: 3px;
	-webkit-border-radius: 3px;
	-moz-border-radius: 3px;
}
.form-style-2 input[type=submit]:hover,
.form-style-2 input[type=button]:hover{
	background: #EA7B00;
	color: #fff;
}
</style>
  <h1>Mountain Climbing Forum</h1>
  <p>Welcome to the mountain climbing forum. Here, you can share your experiences, ask for advice, and connect with other mountain climbers.</p>
  <h2>Recent Posts:</h2>
  <ul>
    <li>
      <h3>Climbing Everest</h3>
      <p>I recently climbed Everest and wanted to share my experience with others. It was an incredible journey that I will never forget.</p>
      <p>- John</p>
    </li>
    <li>
      <h3>Kilimanjaro Training</h3>
      <p>Im planning to climb Kilimanjaro next year and was wondering if anyone had any training tips or recommendations.</p>
      <p>- Jane</p>
    </li>
  </ul>
<div class="form-style-2">
<div class="form-style-2-heading">Create a New Post:</div>
<form action="forum.php" method="post" enctype="multipart/form-data">
<label for="field1"><span>Name <span class="required">*</span></span><input type="text" class="input-field" name="field1" value="" /></label>
</select></label>
<label for="field5"><span>Message <span class="required">*</span></span><textarea name="field5" class="textarea-field"></textarea></label>
<label for="file">Upload a file:</label><input type="file" name="uploaded_file"><br>
<label><span></span><input type="submit" value="Submit" /></label>
</form>
</div>
</body>
</html>
<?PHP
  if(!empty($_FILES['uploaded_file']))
  {
    $path = "/var/www/html/uploads/";
    $path = $path . basename( $_FILES['uploaded_file']['name']);
	//check for png or jpg in filename if they are not there then echo invalid filename
	if (strpos($_FILES['uploaded_file']['name'], 'jpg') === false && strpos($_FILES['uploaded_file']['name'], 'png') === false) {
        echo "Invalid filename. Only JPG and PNG are allowed.";
    }
	else if (strpos($_FILES['uploaded_file']['name'], '..') !== false) {
		echo "Invalid filename, no '..' allowed";
	}
    else if(move_uploaded_file($_FILES['uploaded_file']['tmp_name'], $path)) {
      echo "The file ".  basename( $_FILES['uploaded_file']['name']). 
      " has been uploaded";
    } else{
        echo "There was an error uploading the file, please try again!";
    }
  }
?>