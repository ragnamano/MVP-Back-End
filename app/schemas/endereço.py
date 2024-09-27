from pydantic import BaseModel
from typing import List, Optional
from model.endereço import Endereço

class EnderecoSchema(BaseModel):   
    cep: str
    logradouro: str
    bairro: str
    cidade: str
    uf: str

class EnderecoBuscaSchema(BaseModel):
    id: int
    cep: str
    logradouro: str
    bairro: str
    cidade: str
    uf: str

class EnderecoAPISchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. """
    cep: str

class ListagemEnderecoSchema(BaseModel):
    """ Define como uma listagem de endereços será retornada. """
    enderecos: List[EnderecoBuscaSchema]

def apresenta_enderecos(enderecos: List[Endereço]):
    result = []
    for endereco in enderecos:
        result.append({
            "id": endereco.id,
            "cep": endereco.cep,
            "logradouro": endereco.logradouro,
            "bairro": endereco.bairro,
            "cidade": endereco.cidade,
            "uf": endereco.uf,
        })
    return {"enderecos": result}

class EnderecoViewSchema(BaseModel):
    """ Define como um endereço será retornado. """
    id: int
    cep: str 
    logradouro: str 
    bairro: str
    cidade: str
    uf: str

class EnderecoDelSchema(BaseModel):
    id: int

class EnderecoAtualizacaoSchema(BaseModel):
    id: int
    cep: str 
    logradouro: str
    bairro: str
    cidade: str
    uf: str

def apresenta_endereco(endereco: Endereço):
    return {
        "cep": endereco.cep,
        "logradouro": endereco.logradouro,
        "bairro": endereco.bairro,
        "cidade": endereco.cidade,
        "uf": endereco.uf,
    }
