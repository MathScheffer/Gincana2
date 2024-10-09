import pytest
from Api import *


class ApiTests:
    def __init__(self, nome = "Joel", email = "joel@gmail.com", senha="123") -> None:
      self.nome = nome
      self.email = email
      self.senha = senha

    def loginTest(self):
        assert login(self.nome, self.senha) == {"Nome":self.nome, "Senha":self.senha}
        assert login(123, self.senha) == {"Message": "O Nome deverá ser uma string"}

"""     def editUser(self):
       assert login({"nome": self.nome, "email": self.email}) == {"nome":self.nome, "email":self.email} """