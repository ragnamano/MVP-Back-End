from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from  model.base import Base


class Endereço(Base):
    __tablename__ = 'enderecos'

    id = Column(Integer, primary_key=True)
    cep = Column(String(140), unique=True)
    logradouro = Column(String(140), unique=True)
    bairro = Column(String(140), unique=True)
    cidade = Column(String(140), unique=True)
    uf = Column(String(140), unique=True)

    def to_dict(self):
        return {
            "cep": self.cep,
            "logradouro": self.logradouro,
            "bairro": self.bairro,
            "cidade": self.cidade,
            "uf": self.uf
        }