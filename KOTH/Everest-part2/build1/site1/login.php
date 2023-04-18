<?php
    $config = include('config.php');
    if($_POST['username'] == 'npurja' && $_POST['password'] == $config['password2']){
        header('Location: success.php');
        //set session
        session_start();
        $_SESSION['username'] = 'npurja';
    }else{
        //say login failed
        echo('Login failed. Please try again.');
    }

    
?>