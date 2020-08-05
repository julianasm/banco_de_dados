from bd import nova_conexao

sql = 'SELECT tel, nome FROM contatos'
# traz todos mas só mostra 1
# LIMIT 3 OFFSET 10 
with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)

    print(cursor.fetchone())
