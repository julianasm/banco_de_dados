from bd import nova_conexao
from mysql.connector.errors import ProgrammingError

sql = "INSERT INTO grupos (descricao) VALUES (%s)"
args = (
    ('Casa',),
    ('Trabalho',),
)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'Foram incluidos {cursor.rowcount}')
