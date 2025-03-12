<?php
header('Content-Type: application/json');

$input = json_decode(file_get_contents('php://input'), true);

// Здесь вы можете сохранить данные в базу данных
// Например, используя PDO для работы с MySQL

// Пример сохранения в базу данных
try {
    $pdo = new PDO('mysql:host=localhost;dbname=your_database', 'username', 'password');
    $stmt = $pdo->prepare("INSERT INTO user_info (full_name, education, skills, contact, about_me) VALUES (?, ?, ?, ?, ?)");
    $stmt->execute([$input['fullName'], $input['education'], $input['skills'], $input['contact'], $input['aboutMe']]);
    
    echo json_encode(['status' => 'success']);
} catch (PDOException $e) {
    echo json_encode(['status' => 'error', 'message' => $e->getMessage()]);
}
?>