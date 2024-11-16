from passlib.context import CryptContext

# Criação do contexto de criptografia usando bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Função para gerar o hash de uma senha
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

# Função para verificar se uma senha fornecida corresponde ao hash armazenado
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
