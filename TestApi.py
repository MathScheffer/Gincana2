import pytest
from Api import *


class ApiTests:

    def __init__(self, nome, email, senha) -> None:
        self.nome = nome
        self.email = email
        self.senha = senha

    def createUserTest(self):
        Banco.banco = []

    def loginTest(self):
        Banco.banco = []
        assert login(self.nome, self.senha) == {
            "Message": "Não há usuários cadastrados"
        }, "Teste falhou por haver usuário indesejado cadastrado."

        Banco.banco.append({
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha
        })

        assert login(self.nome, self.senha) == {
            "nome": self.nome,
            "senha": self.senha
        }, f'Usuário {self.nome} não encontrado.'

        assert login(123, self.senha) == {
            "Message": "O Nome deverá ser uma string"
        }, "Erro: login aceitou usuario como número."

    def editUserTest(self):
        Banco.banco = []

    def deleteUserTest(self):
        Banco.banco = []

    
