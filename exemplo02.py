# -*- coding: utf-8 -*-


from sqlalchemy import create_engine,and_,or_
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker



if __name__ == '__main__':
    #padrao pra usar banco
    engine = create_engine("sqlite:///teste.sqlite")
    Session = sessionmaker(bind=engine)
    session = Session()
    Base = automap_base()
    Base.prepare(engine, reflect=True)


    #https://www.pythonsheets.com/notes/python-sqlalchemy.html


    #para cada tabela do banco uma linha dessa
    Contato = Base.classes.Contato

    #Select * from Contato
    lista_de_contatos = session.query(Contato).all()

    for linha in lista_de_contatos:
        print('Id: {}\t Nome: {}\t Telefone: {}'.format(linha.idContato, linha.nome, linha.telefone))


    pessoa = session.query(Contato).filter(and_(Contato.nome == 'Haddad',Contato.telefone == '34257345')).first()



    print('O telefone do {} é : {}'.format(pessoa.nome,pessoa.telefone))

    # pessoa.nome = 'Haddad'
    # session.commit()