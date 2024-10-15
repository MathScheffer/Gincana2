from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

# Declare a variable as a str
# and get editor support inside the function
def main(user_id: str):
    return user_id


# A Pydantic model
class User(BaseModel):
    nome: str
    email: str
    senha: str

class UserLogin(BaseModel):
    nome: str
    senha: str

class UserEdit(BaseModel):
    email: str
    senha: str


app = FastAPI()

banco = []


class Banco:
    banco = []


@app.get("/")
def getAll():
    return Banco.banco


@app.post("/create")
def create(user: User):
    print(type(user))
    if type(user) != User:
        return {"Message": "O tipo de dado enviado não é um dicionário."}

    valid_fields = ["nome", "email", "senha"]
    for k, v in user.__dict__.items():
        if not (k in valid_fields):
            return {"Message": f'Campo {k} invalido.'}

    if not type(user.nome) is str:
        return {"Message": "O Nome deverá ser uma string"}
    if not type(user.email) is str:
        return {"Message": "O Email deverá ser uma string"}
    if not type(user.email) is str:
        return {"Message": "O senha deverá ser uma string"}

    Banco.banco.append({
        "nome": user.nome,
        "email": user.email,
        "senha": user.senha
    })

    return {"nome":  user.nome, "email": user.email}


@app.post("/login")
def login(user: UserLogin):
    valid_fields = ["nome", "senha"]
    for k, v in user.__dict__.items():
        if not (k in valid_fields):
            return {"Message": f'Campo {k} invalido.'}
        
    if not type(user.nome) is str:
        return {"Message": "O Nome deverá ser uma string"}

    if (len(Banco.banco) == 0):
        return {"Message": "Não há usuários cadastrados"}

    for u in Banco.banco:
        for k, v in u.items():
            if u["nome"] == user.nome and u["senha"] == user.senha:
                print(f'Nome: {u["nome"]} == {user.nome}\nSenha: {u["senha"]} == {user.senha}')
                return {"nome": u["nome"], "senha": u["senha"]}
        return {"Message": "Usuario nao encontrado."}


@app.put("/editar")
def edit(nome: str, obj: UserEdit):
    if (type(nome) != str):
        return {"Message": "Nome deve ser uma string."}

    objIndex = -1
    for i in range(len(Banco.banco)):
        if Banco.banco[i]["nome"] == nome:
            objIndex = i
            break

    if objIndex == -1:
        return {"Message": f'Usuario {nome} não encontrado.'}
        
    for k, v in obj.__dict__.items():
        if v:
            Banco.banco[objIndex][k] = v


    return {"Message": "Usuario atualizado" , "Resultado": {"nome":Banco.banco[objIndex]["nome"], "email":Banco.banco[objIndex]["email"] }}


@app.delete("/deletar")
def delete(nome: str):

    for i in range(len(Banco.banco)):
        if Banco.banco[i]["nome"] == nome:
            del Banco.banco[i]
            return {"Message": f'Usuario {nome} deletado com sucesso.'}

    return {"Message": f'Usuario {nome} não encontrado.'}
