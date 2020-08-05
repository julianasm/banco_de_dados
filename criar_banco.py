from mysql.connector import connect

conexao = connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='45145edimar',
    auth_plugin='mysql_native_password'
)

cursor = conexao.cursor()
# CREATE DATABASE IF NOT EXISTS
cursor.execute('CREATE DATABASE agenda')
