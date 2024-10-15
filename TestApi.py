import pytest
from Api import *


class ApiTests:

    def __init__(self, nome, email, senha) -> None:
        self.nome = nome
        self.email = email
        self.senha = senha

    def getUserTest(self):
        Banco.banco = []
        assert getAll() == [], "Retornou dados indesejados"

        Banco.banco.append({
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha
        })

        assert getAll() == [{
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha
        }], "Não retornou os dados adicionados."
    def createUserTest(self):
        Banco.banco = []

        user = User(nome=self.nome, email=self.email, senha=self.senha)
        assert create(123) == {
            "Message": "O tipo de dado enviado não é um dicionário."
        }, "Aceitou tipo de dado que não seja dicionário."

        assert create(1) == {
            "Message": "O tipo de dado enviado não é um dicionário."
        }, "Aceitou tipo de dado que não seja dicionário."

        assert create(user) == {
            "nome": self.nome,
            "email": self.email
        }

        assert len(Banco.banco) > 0, "Usuário não foi cadastrado"
    def loginTest(self):
        Banco.banco = []
        

        user= UserLogin(
            nome= self.nome,
            senha= self.senha
        )
        assert login(user) == {
            "Message": "Não há usuários cadastrados"
        }, "Teste falhou por haver usuário indesejado cadastrado."

        Banco.banco.append({
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha
        })


        assert login(user) == {
            "nome": self.nome,
            "senha": self.senha
        }, f'Usuário {self.nome} não encontrado.'

        user.nome = 123
        assert login(user) == {
            "Message": "O Nome deverá ser uma string"
        }, "Erro: login aceitou usuario como número."

    def editUserTest(self):
        Banco.banco = []

        user = UserEdit(email=self.email, senha=self.senha)
        assert edit(2, user) == {
            "Message": "Nome deve ser uma string."
        }, "Aceitou nome como inteiro."

        Banco.banco.append({
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha
        })

        assert edit("Xablau", user) == {
            "Message": 'Usuario Xablau não encontrado.'
        }, "Achou usuario indesejado."

       
        assert edit(self.nome, user) == {"Message": "Usuario atualizado" , "Resultado":{"nome": self.nome, "email":self.email}}

    def deleteUserTest(self):
        Banco.banco = []
        assert delete(self.nome) == {
            "Message": f'Usuario {self.nome} não encontrado.'
        }, "Teste falhou pois encontrou usuario indesejado."

        Banco.banco.append({
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha
        })
        assert delete(self.nome) == {
            "Message": f'Usuario {self.nome} deletado com sucesso.'
        }, "Teste falhou pois não encontrou usuario desejado para deletar."

    
