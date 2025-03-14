<?php
require_once 'config.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = trim($_POST['username']);
    $email = trim($_POST['email']);
    $password = password_hash(trim($_POST['password']), PASSWORD_BCRYPT);
    $full_name = trim($_POST['fullName']);
    $education = trim($_POST['education']);
    $skills = trim($_POST['skills']);
    $contact = trim($_POST['contact']);
    $about_me = trim($_POST['aboutMe']);

    $sql = "INSERT INTO users (username, email, password, full_name, education, skills, contact, about_me) VALUES (?, ?, ?, ?, ?, ?, ?, ?)";
    $stmt = $db->prepare($sql);
    $stmt->bind_param("ssssssss", $username, $email, $password, $full_name, $education, $skills, $contact, $about_me);

    if ($stmt->execute()) {
        echo "Данные успешно сохранены!";
    } else {
        echo "Ошибка: " . $stmt->error;
    }

    $stmt->close();
    mysqli_close($db);
}
?>