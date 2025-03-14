window.onload = function() {
    const loggedIn = localStorage.getItem('loggedIn');
    const loginButton = document.getElementById('loginButton');

    if (loggedIn) {
        loginButton.innerText = 'Аккаунт'; // Change button text if logged in
    } else {
        loginButton.innerText = 'Войти'; // Default button text
    }

    document.getElementById('registrationForm').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission

        const username = document.getElementById('username').value;
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;

        fetch('register.php', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: new URLSearchParams({
                'username': username,
                'email': email,
                'password': password
            })
        })
        .then(response => response.text())
        .then(data => {
            document.getElementById('message').innerText = data;
        })
        .catch((error) => {
            console.error('Ошибка:', error);
            document.getElementById('message').innerText = 'Ошибка при регистрации.';
        });
    });
};
