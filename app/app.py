from http.client import HTTPException
import requests
from flask import abort, redirect
from flask_cors import CORS
from flask_openapi3 import OpenAPI, Info, Tag
from db import Session, Endereco, atualizar_endereco_db, deletar_endereco_db, obter_endereco_por_cep, obter_todos_enderecos  # Importa a sessão e o modelo Endereco
from schemas.endereço import *
from schemas.error import ErrorSchema
from dotenv import load_dotenv

info = Info(title="API Endereços cadastrados", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)
load_dotenv()

home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
endereço_tag = Tag(name="Endereço", description="Consulta, cadastro, leitura, atualização e exclusão de endereços")

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

@app.get('/', tags=[home_tag])
def home():
    return redirect('/openapi')

#GET Lista todos endereços
@app.get('/enderecos', tags=[endereço_tag],
         responses={200: ListagemEnderecoSchema, 404: ErrorSchema})
def listar_enderecos():
    enderecos = obter_todos_enderecos()
    if not enderecos:
        return {"message": "Nenhum endereço encontrado."}, 404
    return {"enderecos": enderecos}, 200

#POST consulta na API externa
@app.post('/ConsultarEndereçoViaCEP', tags=[endereço_tag],
          responses={"200": EnderecoViewSchema, "400": ErrorSchema})
def busca_endereco_por_cep(form: EnderecoAPISchema):
    cep = form.cep
    dados_endereco = consultar_cep(cep)

    if dados_endereco is None or 'erro' in dados_endereco:
        abort(400, "CEP inválido ou não encontrado.")

    endereco = Endereco(  # Usando a classe Endereco do SQLAlchemy
        cep=dados_endereco.get('cep'),
        logradouro=dados_endereco.get('logradouro'),
        bairro=dados_endereco.get('bairro'),
        cidade=dados_endereco.get('localidade'),
        uf=dados_endereco.get('uf'),
    )

    return apresenta_endereco(endereco), 200

#POST Cadastra um nomo endereço
@app.post('/CadastraEndereço', tags=[endereço_tag],
          responses={"200": EnderecoViewSchema, "400": ErrorSchema})
def cadastrar_endereco(form: EnderecoSchema):
    try:
        endereco = Endereco(  # Usando a classe Endereco do SQLAlchemy
            cep=form.cep,
            logradouro=form.logradouro,
            bairro=form.bairro,
            cidade=form.cidade,
            uf=form.uf,
        )
        session = Session()
        session.add(endereco)
        session.commit()
        return {"status": "success", "data": apresenta_endereco(endereco)}, 200
    except Exception as e:
        abort(400, f"Erro ao cadastrar endereço: {str(e)}")

#PUT Atualiza endereço
@app.put('/endereco/atualizar', tags=[endereço_tag],
         responses={200: EnderecoViewSchema, 404: ErrorSchema, 400: ErrorSchema})
def atualizar_endereco(form: EnderecoAtualizacaoSchema):
    id = form.id
    endereco = obter_endereco_por_cep(id)

    if not endereco:
        abort(404, "Endereço não encontrado.")

    atualizar_endereco_db(id, form.cep, form.logradouro, form.bairro, form.cidade, form.uf)
    return {"status": "success", "data": "Endereço atualizado com sucesso."}, 200

@app.delete('/endereco/deletar', tags=[endereço_tag],
             responses={200: EnderecoDelSchema, 404: ErrorSchema})
def deletar_endereco(form: EnderecoDelSchema):
    id = form.id
    endereco = obter_endereco_por_cep(id)
    if not endereco:
        abort(404, "Endereço não encontrado.")

    deletar_endereco_db(id)
    return {"status": "success", "message": "Endereço deletado com sucesso."}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)  # Certifique-se de que a porta está correta
