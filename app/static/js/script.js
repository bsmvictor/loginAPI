let isRegistering = false;

function toggleForm() {
    isRegistering = !isRegistering;

    document.getElementById("form-title").textContent = isRegistering ? "Criar Conta" : "Entrar na Conta";
    document.getElementById("toggle-text").innerHTML = isRegistering
        ? 'Já tem uma conta? <a href="#" onclick="toggleForm()" style="color: var(--link-color); text-decoration: none;">Entrar</a>'
        : 'Não tem uma conta? <a href="#" onclick="toggleForm()" style="color: var(--link-color); text-decoration: none;">Criar uma conta</a>';

    document.getElementById("name-group").style.display = isRegistering ? "block" : "none";
    document.getElementById("lastname-group").style.display = isRegistering ? "block" : "none";
    document.getElementById("submit-button").textContent = isRegistering ? "Cadastrar" : "Entrar";
}

async function submitForm() {
    if (isRegistering) {
        await register();
    } else {
        await login();
    }
}

const apiBaseUrl = "http://127.0.0.1:8000/api";

async function register() {
    const nome = document.getElementById("first-name").value;
    const sobrenome = document.getElementById("last-name").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    try {
        const response = await fetch(`${apiBaseUrl}/register`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ nome, sobrenome, email, password })
        });

        if (response.ok) {
            alert("Usuário cadastrado com sucesso!");
            toggleForm(); // Alterna para a tela de login
        } else {
            const errorData = await response.json();
            alert(`Erro: ${errorData.detail}`);
        }
    } catch (error) {
        console.error("Erro de registro:", error);
        alert("Erro ao tentar registrar o usuário.");
    }
}

async function login() {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    try {
        const response = await fetch(`${apiBaseUrl}/login`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ email, password })
        });

        if (response.ok) {
            alert("Login bem-sucedido!");
        } else {
            const errorData = await response.json();
            alert(`Erro: ${errorData.detail}`);
        }
    } catch (error) {
        console.error("Erro de login:", error);
        alert("Erro ao tentar fazer login.");
    }
}
