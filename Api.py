from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/login")
def login(nome: str, senha: str):
    if type(nome) != str:
            return {"Message": "O Nome deverá ser uma string"}
    return {"Nome":nome, "Senha":senha}

@app.put("/editar")
def login(obj: object):
    valid_fields = ["nome","email","senha"]
    for k, v in obj.items():       
      if  not (k in valid_fields):
          return {"Message":f'Campo {k} invalido.'}
    return obj