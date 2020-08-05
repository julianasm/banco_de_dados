from bd import nova_conexao

sql = "SELECT * FROM contatos WHERE nome like '%a'"
# pega nomes que contem letra 'a'

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)
    
    for x in cursor:
        print(x)
    # cada valor percorrido no cursor é uma tupla que contem os dados
