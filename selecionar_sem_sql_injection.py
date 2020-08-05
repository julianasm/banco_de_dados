# evita que o input do usuario seja interpretado como um comando sql
# evita sql injection --> ataque ao banco de dados

from bd import nova_conexao

sql = "SELECT * FROM contatos WHERE nome like %s"

with nova_conexao() as conexao:
    nome = input('Contato a localizar: ')
    args = (f'%{nome}%',)
    # simbolos percentuais indicam que esta contido
    # percentual no inico = termina com aquele nome
    # percentual no final = comeca com aquele nome
    # --> deve ser inserido no parametro e nao na definicao do sql

    cursor = conexao.cursor()
    cursor.execute(sql, args)
    #sql injection é evitado ao passar os parametros de forma separada (como neste exemplo)

    for x in cursor:
        print(x)
