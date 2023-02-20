<?php
    // Check if the user submitted the login form
    if (isset($_POST['name']) && isset($_POST['password'])) {

        // Get the username and password from the form
        $username = $_POST['name'];
        $password = $_POST['password'];

        $servername = "localhost";
        $username_db = "root"; 
        $password_db = "AWNYGELL030910"; 
        $dbname = "db1"; 

        // Create connection
        $conn = new mysqli($servername, $username_db, $password_db, $dbname);

        // Check connection
        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
        }

        // Retrieve the user record
        $sql = "SELECT * FROM users WHERE name = '$username' AND password = '$password'";
        $result = $conn->query($sql);

        if ($result->num_rows > 0) {
            // User found, redirect to home page or perform other tasks
            header("location: ./home.html");
            exit;
        } else {
            // User not found, show error message or perform other tasks
            $error .= '<p class="error">The password is not valid.</p>';
        }
        
        // Close the database connection
        $conn->close();
    }
?>
