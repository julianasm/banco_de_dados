from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = "DELETE FROM contatos WHERE nome = %s"
args = ('Bia',)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        cursor.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'{cursor.rowcount} registro(s) deletado(s).')
