import pytest
from Api import *


class ApiTests:

    def __init__(self, nome, email, senha) -> None:
        self.nome = nome
        self.email = email
        self.senha = senha

    """before_each:
        banco = []
        banco.append({
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha
        })
    """

    def createUserTest(self):
        assert create(self.nome, self.email, self.senha) == {
            "nome": self.nome,
            "email": self.email
        }

    def loginTest(self):
        assert login(self.nome, self.senha) == {
            "Message": "Não há usuários cadastrados"
        }
        banco.append({
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha
        })

        assert login(self.nome, self.senha) == {
            "nome": self.nome,
            "senha": self.senha
        }

        assert login(123, self.senha) == {
            "Message": "O Nome deverá ser uma string"
        }

    def editUserTest(self):
        assert login({
            "nome": self.nome,
            "email": self.email
        }) == {
            "nome": self.nome,
            "email": self.email
        }

    def deleteUserTest(self):
        pass
