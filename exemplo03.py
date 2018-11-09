# -*- coding: utf-8 -*-


from sqlalchemy import create_engine,and_,or_
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker



if __name__ == '__main__':
    #padrao pra usar banco
    engine = create_engine("sqlite:///lab05-ex01.sqlite")
    Session = sessionmaker(bind=engine)
    session = Session()
    Base = automap_base()
    Base.prepare(engine, reflect=True)


    #https://www.pythonsheets.com/notes/python-sqlalchemy.html


    #para cada tabela do banco uma linha dessa
    Pessoa = Base.classes.Pessoa
    Telefone = Base.classes.Telefones

    #Select * from Contato
    lista_de_pessoas = session.query(Pessoa).all()
    lista_de_telefones = session.query(Telefone).all()
    lista_join = session.query(Pessoa).join(Telefone).all() #natural join
    #lista_join = session.query(Pessoa).join(Telefone, Pessoa.idPessoa==Telefones.idPessoa).all() inner join

    for linha in lista_join:
        print("Nome {}".format(linha.nome))
        for tel in linha.telefones_collection:
            print("Telefone: {}".format(tel.numero))

    print("-------------------------------------------------")

    for linha in lista_de_pessoas:
        print('Id: {}\t Nome: {}\t'.format(linha.idPessoa, linha.nome))

    print("-------------------------------------------------")

    for linha in lista_de_telefones:
        print('Id: {}\t numero: {}\t idPessoa: {}'.format(linha.idTelefone,linha.numero,linha.idPessoa))
   # pessoa = session.query(Contato).filter(and_(Contato.nome == 'Haddad',Contato.telefone == '34257345')).first()

    print("-------------------------------------------------")
    pessoas = session.query(Pessoa).all()

    for linha in pessoas:
        print('{}\t{}'.format(linha.idPessoa,linha.nome))
        telefones = session.query(Telefone).filter(Telefone.idPessoa == linha.idPessoa)
        for tel in telefones:
            print('{}'.format(tel.numero))

    print("-------------------------------------------------")

    pessoas = session.query(Pessoa).filter(Pessoa.nome.ilike('J%')).all()
    for pessoa in pessoas:
        print('{}\t{}'.format(pessoa.idPessoa,pessoa.nome))
    #print('O telefone do {} é : {}'.format(pessoa.nome,pessoa.telefone))

    # pessoa.nome = 'Haddad'
    # session.commit()