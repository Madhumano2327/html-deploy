import streamlit as st

# Create a login page using HTML and JavaScript
def login_page():
    html_code = """
    <html>
    <body>
    <h2>Login Page</h2>
    <form id="login-form">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username"><br><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password"><br><br>
        <button type="submit">Login</button>
    </form>
    <div id="login-status"></div>

    <script>
        const loginForm = document.getElementById('login-form');
        const loginStatus = document.getElementById('login-status');

        loginForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;

            // Send login request to server using AJAX or fetch API
            fetch('/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ username, password })
            })
            .then((response) => response.json())
            .then((data) => {
                if (data.success) {
                    loginStatus.textContent = 'Login successful!';
                    // Redirect to main app page
                    window.location.href = '/app';
                } else {
                    loginStatus.textContent = 'Invalid username or password';
                }
            })
            .catch((error) => console.error(error));
        });
    </script>
    </body>
    </html>
    """

    st.components.v1.html(html_code, height=500)

# Create a Streamlit app
def main():
    login_page()
