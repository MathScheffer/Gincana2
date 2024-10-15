Rodar a fastapi:
Crie um ambiente virtual:
`python -m venv env`
Rode o ambiente virtual:
./env/Scripts/activate
Instale as dependências:
`pip install -r requirements.txt`
Instale o fastapi[standar]
`pip install "fastapi[standard]"`

Rode o projeto:
`fastapi dev Api.py`

## Regras para Teste

A Api utiliza uma classe Banco com um atributo estático banco, que é um array que armazena os objetos para substituir conexão com banco de dados.
Para realizar os testes unitários, é necessário que, para cada teste, resete o banco conforme ilustrado abaixo (atribuindo um array vazio a ele).

Como nos testes unitários queremos testar as funções do sistema, podemos apenas dar um append no atributo estático se quisermos que nosso teste interaja com a base de dados:
![Dica](./doc%20api.png)

## Swagger

A fastapi garante um swagger automático (pode haver defeitos aqui), ficando no endereço http://127.0.0.1:8000/docs.
