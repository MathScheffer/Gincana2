from typing import Union

from fastapi import FastAPI

app = FastAPI()


class Banco:
    banco = []


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/create")
def create(user: dict):

    if type(user) != dict:
        return {"Message": "O tipo de dado enviado não é um dicionário."}

    valid_fields = ["nome", "email", "senha"]
    for k, v in user.items():
        if not (k in valid_fields):
            return {"Message": f'Campo {k} invalido.'}

    if not type(user["nome"]) is str:
        return {"Message": "O Nome deverá ser uma string"}
    if not type(user["email"]) is str:
        return {"Message": "O Email deverá ser uma string"}
    if not type(user["email"]) is str:
        return {"Message": "O Email deverá ser uma string"}

    Banco.banco.append({
        "nome": user["nome"],
        "email": user["email"],
        "senha": user["senha"]
    })

    return {"nome": user["nome"], "email": user["email"]}


@app.post("/login")
def login(nome: str, senha: str):
    if not type(nome) is str:
        return {"Message": "O Nome deverá ser uma string"}

    if (len(Banco.banco) == 0):
        return {"Message": "Não há usuários cadastrados"}

    for user in Banco.banco:
        for k, v in user.items():
            if user["nome"] == nome and user["senha"] == senha:
                return {"nome": user["nome"], "senha": user["senha"]}
        return {"Message": "Usuario nao encontrado."}


@app.put("/editar")
def edit(nome: str, obj: object):
    if (type(nome) != str):
        return {"Message": "Nome deve ser uma string."}

    objIndex = -1
    for i in range(len(Banco.banco)):
        if Banco.banco[i]["nome"] == nome:
            objIndex = i
            break

    if objIndex == -1:
        return {"Message": f'Usuario {nome} não encontrado.'}
        
    valid_fields = ["nome", "email", "senha"]
    for k, v in obj.items():
        if k in valid_fields:
            Banco.banco[objIndex][k] = v
        else:
            return {"Message": f'Campo {k} invalido.'}


    return {"Message": "Usuario atualizado" , "Resultado": {"nome":Banco.banco[objIndex]["nome"], "email":Banco.banco[objIndex]["email"] }}


@app.delete("/deletar")
def delete(nome: str):

    for i in range(len(Banco.banco)):
        if Banco.banco[i]["nome"] == nome:
            Banco.banco.pop(i)
            return {"Message": f'Usuario {nome} deletado com sucesso.'}

    return {"Message": f'Usuario {nome} não encontrado.'}
