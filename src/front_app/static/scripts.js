window.addEventListener('DOMContentLoaded', event => {
    const sidebarToggle = document.body.querySelector('#sidebarToggle');
    if (sidebarToggle) {
        sidebarToggle.addEventListener('click', event => {
            event.preventDefault();
            document.body.classList.toggle('sb-sidenav-toggled');
            localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
        });
    }

    var registerForm = document.getElementById('registerForm');
    if (registerForm) {
        registerForm.addEventListener('submit', function(event) {
            event.preventDefault();
    
            var firstName = document.getElementById('registerFirstName').value;
            var lastName = document.getElementById('registerLastName').value;
            var email = document.getElementById('registerEmail').value;
            var password = document.getElementById('registerPassword').value;
            var passwordConfirm = document.getElementById('registerPasswordConfirm').value;
        
            if (password !== passwordConfirm) {
                alert('Passwords do not match.');
                return;
            }
        
            var data = {
                first_name: firstName,
                last_name: lastName,
                email: email,
                password: password
            };
        
            fetch('http://auth-app-svc.default.svc.cluster.local/register', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            })
            .then(response => response.json())
            .then(data => {
                if (data.message) {
                    alert(data.message);
                } else if (data.error) {
                    alert(data.error);
                }
            })
            .catch((error) => {
                console.error('Error:', error);
            });
        });
    }

    var loginForm = document.getElementById('loginForm');
    if (loginForm) {
        loginForm.addEventListener('submit', function(event) {
            event.preventDefault();
    
            var email = document.getElementById('loginEmail').value;
            var password = document.getElementById('loginPassword').value;
        
            if (!email || !password) {
                alert('Please fill in all fields');
            } else {
                var data = {
                    email: email,
                    password: password
                };
        
                console.log('Sending login request', data);
        
                fetch('http://auth-app-svc.default.svc.cluster.local:80/login', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(data)
                })
                .then(response => {
                    console.log('Received response', response);
                    if (response.ok) { 
                        console.log('Login successful, redirecting');
                        window.location.href = 'index.html';
                    } else {
                        return response.json();
                    }
                })
                .then(data => {
                    if (data && data.error) {
                        alert(data.error);
                    }
                })
                .catch((error) => {
                    console.error('Error:', error);
                });
            }    
        });
    }
});