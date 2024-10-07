#importa o modulo mysql.connector que é usado para conectar e interagir com o banco de dados
#import mysql.connector

#importa a classe error do modulo mysql.connector -> utilizada para capturar e tratar erros relacionados ao banco de dados
from mysql.connector import Error

#classe que irá gerenciar a conexão com o banco de dados
class Cliente:
    #método construtor da classe para conectar no banco de dados e os parametros
    def __init__(self, mydb):
        self.connection = mydb
        self.cursor = None
        if self.connection and self.connection.is_connected():
            self.cursor = self.connection.cursor()
            print("Conexão Realizada com sucesso!")
        else:
            print("Entrou no else da conexão!")

    def inserir_cliente(self, nome, telefone):
        if self.cursor:
            try:
                query = "INSERT INTO CLIENTE (NOME, TELEFONE) VALUES (%s, %s);"
                self.cursor.execute(query, (nome, telefone))
                self.connection.commit()
                print(f"Cliente {nome} inserido com suecesso!")
            except Error as e:
                print(f"Erro ao inseir clientes {e}")

    def listar_cliente(self):
        if self.cursor:
            try:
                cursor = self.connection.cursor()
                query = "select id_cliente, nome, telefone from cliente where ativo = 1;"
                cursor.execute(query)
                result = cursor.fetchall()
                for linha in result:
                    id_cliente, nome, telefone = linha
                    print(f"{id_cliente}, {nome}, {telefone}")
            except Error as e:
                print(f"Erro ao buscar os dados na tabela {e}")

    def listagem_especifica(self, id):
        if self.cursor:
            try:
                cursor = self.connection.cursor()
                query = "select * from cliente where id_cliente = %s;"
                dados = (id,)
                cursor.execute(query,dados)
                result = cursor.fetchall()
                for linha in result:
                    print(linha)             
            except Error as e:
                print(f"Erro ao rodar listagem especifica! ERROR: {e}")

    def listagem_especitia_ativa_desativa(self, id):
        if self.cursor:
            try:
                cursor = self.connection.cursor()
                query = "select ativo, case when ativo = 1 then 'S' when ativo = 0 then 'N' end as status_ativo from cliente where id_cliente = %s;"
                dados = id,
                cursor.execute(query, dados)
                result = cursor.fetchone()
                return result[0]
            except Error as e:
                print(f"Erro ao rodar a listagem especifica do desativa/ativa! ERROR: {e}")

    def alterar_cliente(self, nome, telefone, id):
        if self.cursor:
            try:
                cursor = self.connection.cursor()
                query = "update cliente set nome = %s, telefone = %s where id_cliente = %s"
                dados = (nome, telefone, id)
                cursor.execute(query,dados)
                self.connection.commit()
                print("Alteração realizada com sucesso")
            except Error as e:
                print(f"Ocorreu um erro ao alterar o cliente id {id}")

    def desativar_cliente(self, id):
        if self.cursor:
            try:
                cursor = self.connection.cursor()
                query = "update cliente set ativo = 0 where id_cliente = %s;"
                dados = (id,)
                cursor.execute(query, dados)
                print(f"Cliente id: {id} desativado com sucesso!")
                self.connection.commit()
            except Error as e:
                print("Erro ao desativar cliente selecionado")

    def ativar_cliente(self, id):
        if self.cursor:
            try:
                cursor = self.connection.cursor()
                query = "update cliente set ativo = 1 where id_cliente = %s;"
                dados = (id,)
                cursor.execute(query, dados)
                print(f"Cliente id: {id} ativado com sucesso!")
                self.connection.commit()
            except Error as e:
                print("Erro ao ativar cliente selecionado")

"""    def fechar_conexao(self):
        if self.connection and self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("Conexão foi finalizada.")"""