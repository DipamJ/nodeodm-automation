<?php
$host = 'localhost';
$username = 'root';
$password = 'Winter.123'; // Use your actual password
$dbname = 'nodeodm_results';
$port = 3306; 

// Fetch the file ID from the URL
$file_id = isset($_GET['id']) ? intval($_GET['id']) : 0;

// Database connection
$dsn = "mysql:host=$host;port=$port;dbname=$dbname";
try {
    $pdo = new PDO($dsn, $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Fetch file details from the database
    $stmt = $pdo->prepare("SELECT * FROM odm_outputs WHERE output_id = ?");
    $stmt->execute([$file_id]);
    $file = $stmt->fetch(PDO::FETCH_ASSOC);

    if ($file) {
        $file_path = 'C:/Users/dipam/NodeODMProject/' . $file['file_location'];

        if (file_exists($file_path)) {
            header('Content-Description: File Transfer');
            header('Content-Type: application/octet-stream');
            header('Content-Disposition: attachment; filename="'.basename($file_path).'"');
            header('Content-Length: ' . filesize($file_path));
            flush(); // Flush system output buffer
            readfile($file_path);
            exit;
        } else {
            echo "File not found.";
        }
    } else {
        echo "Invalid file ID.";
    }
} catch (PDOException $e) {
    echo "Database error: " . $e->getMessage();
    exit;
}
?>
