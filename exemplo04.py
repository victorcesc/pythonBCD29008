
#de classes gerar o banco, pratica MVC


from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("sqlite:///lab05-ex04.sqlite")
Session = sessionmaker(bind = engine)
Base = declarative_base()


class Pessoa(Base):
    __tablename__='Pessoa'
    idPessoa = Column(Integer,primary_key=True,autoincrement=True)
    nome = Column(String)

    def __init__(self, nome):
        self.nome = nome

class Telefone(Base):
    __tablename__='Telefone'
    idTelefone = Column(Integer,primary_key=True,autoincrement=True)
    numero = Column(String)
    idPessoa = Column(Integer,ForeignKey('Pessoa.idPessoa'))
    pessoa = relationship('Pessoa',backref='Telefone')

 #self = this em java, declaracao do construtor
    def __init__(self,numero,pessoa):
        self.numero = numero
        self.pessoa = pessoa

    #to string
    #def __str__(self):


if __name__ == '__main__':

    Base.metadata.create_all(engine)

    session = Session()

    victor = Pessoa('Victor')

    victor.nome = 'Victor'

    session.add(victor)

    victor_telefone = Telefone('(48) 98181-1010',victor)

    session.commit()
    session.close()