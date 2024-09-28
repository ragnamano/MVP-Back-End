# API de Endereços Cadastrados

Esta API permite o cadastro, consulta, atualização e remoção de endereços utilizando um banco de dados e a API externa ViaCEP para busca de informações de endereços por CEP.

## Funcionalidades

- Listar todos os endereços cadastrados.
- Consultar um endereço utilizando a API externa ViaCEP.
- Cadastrar novos endereços.
- Atualizar endereços cadastrados.
- Deletar endereços do banco de dados.

## Requisitos

- Python 3.x
- Docker
- Docker Compose
- Banco de dados MySQL ou MariaDB
- Bibliotecas Python listadas no `requirements.txt`

## Configuração do Ambiente

Clone o repositorio do Github
Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis de ambiente:

```
# Configurações da API
PYTHONUNBUFFERED=1
PORT=8081

# Configurações do Banco de Dados
DB_HOST=db
DB_PORT=3306
DB_USER=root
DB_PASS=admin
DB_NAME=mvp
```

## Execução

No diretorio rais, execute o comando:

```
docker-compose up --build
```

Para acessar a documentação no Swagger, execute o comando:

´´´
http://localhost:8001/openapi
´´´
