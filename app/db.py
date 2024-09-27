import os
from sqlalchemy import Integer, create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configurações do banco de dados
DATABASE_URL = f"mysql+mysqlconnector://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

# Criando a engine e a sessão
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

# Base para modelos
Base = declarative_base()

# Modelo de Endereço
class Endereco(Base):
    __tablename__ = 'enderecos'

    id = Column(Integer, primary_key=True)
    cep = Column(String)
    logradouro = Column(String)
    bairro = Column(String)
    cidade = Column(String)
    uf = Column(String)

# Função para obter todos os endereços
def obter_todos_enderecos():
    session = Session()
    enderecos = session.query(Endereco).all()  # Obtém todos os endereços
    session.close()

    return [
        {
            "id": endereco.id,
            "cep": endereco.cep,
            "logradouro": endereco.logradouro,
            "bairro": endereco.bairro,
            "cidade": endereco.cidade,
            "uf": endereco.uf
        }
        for endereco in enderecos
    ]

# Função para inserir um endereço no banco de dados
def inserir_endereco(cep, logradouro, bairro, cidade, uf):
    session = Session()
    novo_endereco = Endereco(cep=cep, logradouro=logradouro, bairro=bairro, cidade=cidade, uf=uf)
    session.add(novo_endereco)
    session.commit()
    session.close()

# Função para obter um endereço a partir do CEP
def obter_endereco_por_cep(id):
    session = Session()
    endereco = session.query(Endereco).filter_by(id=id).first()  # Obtém um único resultado
    session.close()
    return endereco

# Função para atualizar um endereço no banco de dados
def atualizar_endereco_db(id, cep, logradouro, bairro, cidade, uf):
    session = Session()
    endereco = session.query(Endereco).filter_by(id=id).first()  # Encontra o endereço
    if endereco:
        endereco.cep = cep
        endereco.logradouro = logradouro
        endereco.bairro = bairro
        endereco.cidade = cidade
        endereco.uf = uf
        session.commit()
    session.close()

# Função para deletar um endereço no banco de dados
def deletar_endereco_db(id):
    session = Session()
    endereco = session.query(Endereco).filter_by(id=id).first()  # Encontra o endereço
    if endereco:
        session.delete(endereco)  # Remove o endereço encontrado
        session.commit()
    session.close()
