from typing import Union

from fastapi import FastAPI

app = FastAPI()

banco = []


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/create")
def create(nome: str, email: str, senha: str):

    if not type(nome) is str:
        return {"Message": "O Nome deverá ser uma string"}
    if not type(email) is str:
        return {"Message": "O Email deverá ser uma string"}
    if not type(email) is str:
        return {"Message": "O Email deverá ser uma string"}

    banco.append({"nome": nome, "email": email, "senha": senha})

    return {"nome": nome, "email": email}


@app.post("/login")
def login(nome: str, senha: str):
    if not type(nome) is str:
        return {"Message": "O Nome deverá ser uma string"}

    if (len(banco) == 0):
        return {"Message": "Não há usuários cadastrados"}

    for user in banco:
        print(user)
        for k, v in user.items():
            if user["nome"] == nome and user["senha"] == senha:
                return {"nome": user["nome"], "senha": user["senha"]}
        return {"Message": "Usuario nao encontrado."}


@app.put("/editar")
def edit(obj: object):
    valid_fields = ["nome", "email", "senha"]
    for k, v in obj.items():
        if not (k in valid_fields):
            return {"Message": f'Campo {k} invalido.'}
    return obj


@app.put("/deletar")
def delete(nome: str):
    valid_fields = ["nome", "email", "senha"]
    for k, v in obj.items():
        if not (k in valid_fields):
            return {"Message": f'Campo {k} invalido.'}
    return obj
