# -*- coding: utf-8 -*-

import sqlite3

if __name__ == '__main__':
    print("kumusta sa mundo")
    conexao = sqlite3.connect('teste.sqlite')
    cursor = conexao.cursor()

    pessoa = ('bolsonaro','99999999', )


    cursor.execute("SELECT * FROM Contato WHERE nome = ? AND telefone = ?",pessoa)
    #print(cursor.fetchall())


    for linha in cursor.fetchall():
        print('Id: {}\t Nome: {}\t Telefone: {}'.format(linha[0],linha[1],linha[2]))



    cursor.close()
    conexao.close()


print("fora do if")
