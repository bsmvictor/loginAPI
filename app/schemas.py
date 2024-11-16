from pydantic import BaseModel

class UserCreate(BaseModel):
    nome: str
    sobrenome: str
    email: str
    password: str

class UserOut(BaseModel):
    id: int
    nome: str
    sobrenome: str
    email: str

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: str
    password: str

