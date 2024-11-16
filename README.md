# Documentação da Aplicação de Login com FastAPI

## Visão Geral

Esta aplicação é uma API de autenticação construída usando FastAPI, que permite o gerenciamento de login e autenticação de usuários. A aplicação possui uma interface web simples para o login e foi desenvolvida com Python e JavaScript, usando um banco de dados para armazenar as informações dos usuários.

## Estrutura do Projeto

- app/: Diretório principal da aplicação.

  - database.py: Configuração e conexão com o banco de dados.

  - main.py: Ponto de entrada da aplicação, responsável por iniciar o servidor FastAPI e incluir as rotas.

  - models.py: Define os modelos de dados utilizados pela aplicação, como a tabela de usuários.

  - schemas.py: Define os esquemas utilizados para validação e transferência de dados entre a API e o banco de dados.

  - utils.py: Contém funções utilitárias, como funções de hash para senhas.

  - routes/auth.py: Define as rotas relacionadas à autenticação, incluindo login e registro de usuários.

  - static/: Contém arquivos estáticos, como CSS, imagens e JavaScript para a interface do usuário.

  - templates/login.html: Template HTML para a página de login.
 
## Estrutura das pastas da aplicação
```
login-api/
├── app/
│   ├── database.py            # Configuração e conexão com o banco de dados
│   ├── main.py                # Ponto de entrada da aplicação
│   ├── models.py              # Modelos de dados da aplicação
│   ├── schemas.py             # Esquemas para validação e transferência de dados
│   ├── utils.py               # Funções utilitárias
│   ├── routes/
│   │   ├── auth.py            # Rotas relacionadas à autenticação
│   ├── static/
│   │   ├── css/
│   │   │   ├── style.css      # Estilização do front-end
│   │   ├── img/               # Imagens utilizadas na interface
│   │   │   ├── apple.svg
│   │   │   ├── google.svg
│   │   │   ├── Inatel Branco.png
│   │   ├── js/
│   │       ├── script.js      # Scripts JavaScript para interatividade
│   ├── templates/
│   │   ├── login.html         # Template HTML para o login
├── requirements.txt           # Dependências da aplicação
```

## Dependências

As dependências do projeto estão listadas no arquivo requirements.txt. Para instalar as dependências, execute:
```
pip install -r requirements.txt
```

## Funcionalidades

1. Registro de Usuário: Possibilidade de registrar um novo usuário com nome, e-mail e senha.

2. Login: Autenticação de usuários registrados.

3. Hash de Senhas: As senhas são hashadas para maior segurança, utilizando funções definidas em utils.py.

## Configuração do Banco de Dados

O arquivo database.py é responsável pela configuração do banco de dados, utilizando SQLAlchemy para gerenciar a conexão e as operações no banco de dados.

## Endpoints Principais

- /auth/register: Endpoint para registrar novos usuários.

- /auth/login: Endpoint para autenticar usuários e gerar tokens de acesso.

- Verifique em `http://127.0.0.1:8000/docs#/`

# Como Executar

1. Instale as Dependências:
```
pip install -r requirements.txt
```

2. Configure o Banco de Dados: Verifique as configurações de conexão no arquivo database.py e ajuste conforme necessário.

3. Execute a Aplicação:
```
uvicorn app.main:app --reload
```

A aplicação estará disponível em `http://127.0.0.1:8000`

## Front-end

A aplicação possui uma interface básica para login, localizada em templates/login.html, e utiliza CSS e JavaScript em static/ para estilizar e fornecer funcionalidades interativas.

## Segurança

As senhas dos usuários são armazenadas de forma segura utilizando hashing.

Tokens de acesso são gerados para autenticar os usuários nas requisições subsequentes.

