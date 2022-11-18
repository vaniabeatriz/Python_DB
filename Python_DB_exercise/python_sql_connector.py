import mysql.connector
import os

connection = mysql.connector.connect(
    host=os.getenv('MYSQL_HOST'),
    user=os.getenv('MYSQL_USERNAME'),
    password=os.getenv('MYSQL_PASSWORD'),
    database='pythonsql',
)
cursor = connection.cursor()

# CRUD

#  CREATE
nome_produto = "todynho"
valor = 3
command = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'  # the SQL command here
cursor.execute(command)
connection.commit()  # to edit/add a new info to the database

#  READ
command = f'SELECT * FROM vendas'
cursor.execute(command)
result = cursor.fetchall()  # to read the database
print(result)
#
#  UPDATE
# nome_produto = "todynho"
# valor = 6
# command = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
# cursor.execute(command)
# connection.commit()  # update the info in the database

# #  DELETE
# nome_produto = "todynho"
# valor = 6
# command = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
# cursor.execute(command)
# connection.commit()  # edit the database
#
cursor.close()
connection.close()
