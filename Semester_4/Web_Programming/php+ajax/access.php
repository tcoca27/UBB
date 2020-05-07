<?php
require_once('connection.php');
session_start();

    if (isset($_POST['Login'])) {

    if (empty($_POST['username']) || empty($_POST['password'])) {

        header("location:login.php?Empty=Please input your username and password");
    } else {

        $username = $_POST['username'];
        $password = $_POST['password'];
        $query = "SELECT * FROM user WHERE username = '$username' AND password = '$password'";
        $result = mysqli_query($connection, $query);

        if (mysqli_fetch_assoc($result)) {

            $_SESSION['User'] = $_POST['username'];
            header("location:welcome.php");
        } else {
            header("location:login.php?Invalid=Incorrect username and password!");
        }

    }

    } else {
		echo 'Not working now';
	}
>