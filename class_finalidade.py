#importa a classe error do modulo mysql.connector -> utilizada para capturar e tratar erros relacionados ao banco de dados
from mysql.connector import Error

#classe que irá gerenciar a conexão com o banco de dados
class Finalidade:
    #método construtor da classe para conectar no banco de dados e os parametros
    def __init__(self, mydb):
        self.connection = mydb
        self.cursor = None
        if self.connection and self.connection.is_connected():
            self.cursor = self.connection.cursor()
            print("Conexão Realizada com sucesso!")
        else:
            print("Falha na conexão!")

    def inserir_finalidade(self, desc_finalidade, ativo):
        if self.cursor:
            try:
                query = "INSERT INTO FINALIDADE (DESC_FINALIDADE, ATIVO) VALUES (%s, %s, %s);"
                self.cursor.execute(query, (desc_finalidade, ativo))
                self.connection.commit()
                print(f"A finalidade {desc_finalidade} foi inserido com suecesso!")
            except Error as e:
                print(f"Erro ao inseir finalidade {e}")

    def listar_finalidade(self):
        if self.cursor:
            try:
                cursor = self.connection.cursor()
                query = "SELECT desc_finalidade, ativo FROM FINALIDADE;"
                cursor.execute(query)
                result = cursor.fetchall()
                for linha in result:
                    desc_finalidade, ativo = linha
                    print(f"{desc_finalidade}, {ativo}")
            except Error as e:
                print(f"Erro ao buscar os dados na tabela {e}")

    # def listagem_especifica(self, id):
    #     if self.cursor:
    #         try:
    #             cursor = self.connection.cursor()
    #             query = "select * from finalidade where id_finalidade = %s;"
    #             dados = (id,)
    #             cursor.execute(query,dados)
    #             result = cursor.fetchall()
    #             for linha in result:
    #                 print(linha)
    #         except Error as e:
    #             print("Erro ao listar finalidade")

    # def fechar_conexao(self):
    #     print("Retornando ao mennu principal!")
    #     if self.connection and self.connection.is_connected():
    #         self.cursor.close()
    #         self.connection.close()
    #         print("Conexão foi finalizada.")