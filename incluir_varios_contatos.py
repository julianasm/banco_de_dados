from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = 'INSERT INTO contatos (nome, tel) VALUES (%s, %s)'
args = (
    ('Ana', '99763-3485'),
    ('Bia', '98634-3204'),
    ('Leo', '92132-4523'),
    ('Mel', '97273-2323'),
    ('Lia', '92345-4456'),
    ('Luca','90988-2375'),
)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro {e.msg}')
    else:
        print(f'Foram incluídos {cursor.rowcount} registros!')
