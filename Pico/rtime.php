<?php
if ($_SERVER["REQUEST_METHOD"] = "GET") {
        $readingdate = $_GET['date'];
        $readingtime = $_GET['time'];
        $readingmode = $_GET['mode'];
        $readingreaction = $_GET['reaction'];

        $server = "<DB IP>";
        $user_name = "<DB Username>";
        $pass_word = "<DB Password>";
        $database = "<DB Data base>";

        $conn = new mysqli($server, $user_name, $pass_word, $database);

        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
        }

        $sql = "INSERT INTO Logs (Date, Time, Mode, Reaction) VALUES ('$readingdate', '$readingtime', '$readingmode', '$readingreaction')";
        if (mysqli_query($conn, $sql)) {
                echo "New record created successfully";
        } else {
                echo "Error: " . $sql . "<br>" . mysqli_error($conn);
        }

        mysqli_close($conn);
        }

?>