from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from starlette.responses import FileResponse
from app.routes import auth
from app.database import engine, Base
from fastapi.responses import FileResponse

# Criação do aplicativo FastAPI
app = FastAPI()

# Montando a pasta 'static' para arquivos CSS e JS
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/", response_class=FileResponse)
async def serve_login_page():
    return "app/templates/login.html"

# Incluindo o roteador de autenticação
app.include_router(auth.router, prefix="/api")

# Criação das tabelas no banco de dados
Base.metadata.create_all(bind=engine)

# Evento de inicialização para imprimir o link de acesso
@app.on_event("startup")
async def startup_event():
    print("🚀 Server is running! Access the login page at: http://127.0.0.1:8000/")
