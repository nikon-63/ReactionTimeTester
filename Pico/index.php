<?php

$user = '<DB Username>';
$password = '<DB Password>';
$database = '<DB Data base>';
$servername='<DB IP>';



$mysqli = new mysqli($servername, $user, $password, $database);

// Checking for connections
if ($mysqli->connect_error) {
	die('Connect Error (' .
	$mysqli->connect_errno . ') '.
	$mysqli->connect_error);
}


$sql = " SELECT * FROM Logs ORDER BY ID DESC ";
$result = $mysqli->query($sql);
$mysqli->close();
?>



<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <!-- Refresh the page to show new data -->
        <meta http-equiv="refresh" content="1" > 
        <title>Reaction Time</title>
        <style>
                table {
                    margin: 0 auto;
                    font-size: large;
                    border: 1px solid black;
                }

                h1 {
                    text-align: center;
                    color: #000000;
                    font-size: xx-large;
                    font-family: 'Gill Sans', 'Gill Sans MT',
                    ' Calibri', 'Trebuchet MS', 'sans-serif';
                }

                td {
                    background-color: #22f5f5;
                    border: 1px solid black;
                }

                th,
                td {
                    font-weight: bold;
                    border: 1px solid black;
                    padding: 10px;
                    text-align: center;
                }

                td {
                    font-weight: lighter;
                }
        </style>
        </head>

    <body>
        <section>
            <h1>Reaction Time</h1>
            <table>
                <tr>
                    <th>Date</th>
                    <th>Time</th>
                    <th>Mode</th>
                    <th>Reaction</th>
                </tr>
                
                <?php
                    while($rows=$result->fetch_assoc())
                    {
                ?>
                <tr>

                    <td><?php echo $rows['Date'];?></td>
                    <td><?php echo $rows['Time'];?></td>
                    <td><?php echo $rows['Mode'];?></td>
                    <td><?php echo $rows['Reaction'];?></td>
                </tr>
                <?php
                    }
                ?>
            </table>
        </section>
    </body>
</html>