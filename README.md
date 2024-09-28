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

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis de ambiente:

```bash
DB_HOST=localhost
DB_PORT=3306
DB_USER=seu_usuario
DB_PASS=sua_senha
DB_NAME=nome_do_banco
