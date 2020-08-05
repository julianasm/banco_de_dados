from bd import nova_conexao

sql = "SELECT * FROM contatos WHERE tel = '99763-3485'"

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)
    
    for x in cursor:
        print(x)
    # cada valor percorrido no cursor é uma tupla que contem os dados
