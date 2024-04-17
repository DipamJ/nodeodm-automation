<?php
$host = 'localhost';
$port = 3306; // Use your configured port if it's not the default
$dbname = 'nodeodm_results';
$username = 'root';
$password = 'Winter.123';

// Data Source Name
$dsn = "mysql:host=$host;port=$port;dbname=$dbname";
try {
    $pdo = new PDO($dsn, $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Could not connect to the database $dbname :" . $e->getMessage());
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NodeODM Outputs</title>
    <!-- Include Bootstrap CSS -->
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <style>
        /* Additional styles can be added here */
        body {
            padding-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container mt-4">
        <h1>NodeODM Outputs</h1>
        <input class="form-control mb-4" id="tableSearch" type="text" placeholder="Type to search...">
        <table class="table table-bordered table-striped">
            <thead>
                <tr>
                    <th>File Name</th>
                    <th>Size</th>
                    <th>Download</th>
                </tr>
            </thead>
            <tbody id="tableBody">
                <?php
                $query = "SELECT * FROM odm_outputs"; // Adjust based on your actual table name and structure
                $stmt = $pdo->query($query);

                while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
                    echo "<tr>";
                    echo "<td>" . htmlspecialchars($row['file_name']) . "</td>"; // Adjust column name as necessary
                    echo "<td>" . htmlspecialchars($row['file_size']) . " bytes</td>"; // Adjust column name as necessary
                    echo "<td><a href='download.php?id=" . $row['output_id'] . "' class='btn btn-primary'>Download</a></td>";
                    echo "</tr>";
                }
                ?>
            </tbody>
        </table>
    </div>
    <!-- Include jQuery and Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.4.0/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    <script>
        $(document).ready(function(){
            $("#tableSearch").on("keyup", function() {
                var value = $(this).val().toLowerCase();
                $("#tableBody tr").filter(function() {
                    $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
                });
            });
        });
    </script>
</body>
</html>
