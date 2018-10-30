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
    lista_join = session.query(Pessoa).join(Telefone).all()

    for linha in lista_join:
        print("Nome {}".format(linha.nome))
        for tel in linha.telefones_collection:
            print("Telefone: {}".format(tel.numero))

    print("-------------------------------------------------")

    for linha in lista_de_pessoas:
        print('Id: {}\t Nome: {}\t'.format(linha.idPessoa, linha.nome))

    print("-------------------------------------------------")

    for linha2 in lista_de_telefones:
        print('Id: {}\t numero: {}\t idPessoa: {}'.format(linha2.idTelefone,linha2.numero,linha2.idPessoa))
   # pessoa = session.query(Contato).filter(and_(Contato.nome == 'Haddad',Contato.telefone == '34257345')).first()



    #print('O telefone do {} é : {}'.format(pessoa.nome,pessoa.telefone))

    # pessoa.nome = 'Haddad'
    # session.commit()