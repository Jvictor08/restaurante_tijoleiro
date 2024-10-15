# local onde vou definir as informações da conexão
import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    database = 'bd_tijoleiro',
    user = 'root',
    password = "root"  
)


