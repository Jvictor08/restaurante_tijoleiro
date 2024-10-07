#importa a classe error do modulo mysql.connector -> utilizada para capturar e tratar erros relacionados ao banco de dados
from mysql.connector import Error

#classe que irá gerenciar a conexão com o banco de dados
class meio_de_contato:
    #método construtor da classe para conectar no banco de dados e os parametros
    def __init__(self, mydb):
        self.connection = mydb
        self.cursor = None
        if self.connection and self.connection.is_connected():
            self.cursor = self.connection.cursor()
            print("Conexão Realizada com sucesso!")
        else:
            print("Falha na conexão!")

    def inserir_meioDeContato(self, desc_plataforma, ativo):
        if self.cursor:
            try:
                query = "INSERT INTO MEIO_DE_CONTATO (DESC_PLATAFORMA, ATIVO) VALUES (%s, %s, %s);"
                self.cursor.execute(query, (desc_plataforma, ativo))
                self.connection.commit()
                print(f"O meio de contato {desc_plataforma} foi inserido com suecesso!")
            except Error as e:
                print(f"Erro ao inseir meio de contato {e}")

    def listar_meio_de_contato(self):
        if self.cursor:
            try:
                cursor = self.connection.cursor()
                query = "SELECT desc_meio_de_contato, ativo FROM MEIO_DE_CONTATO;"
                cursor.execute(query)
                result = cursor.fetchall()
                for linha in result:
                    desc_meio_de_contato, ativo = linha
                    print(f"{desc_meio_de_contato}, {ativo}")
            except Error as e:
                print(f"Erro ao buscar os dados na tabela {e}")

    # def listagem_especifica(self, id):
    #     if self.cursor:
    #         try:
    #             cursor = self.connection.cursor()
    #             query = "select * from desc_meio_de_contato where id_meio_de_contato = %s;"
    #             dados = (id,)
    #             cursor.execute(query,dados)
    #             result = cursor.fetchall()
    #             for linha in result:
    #                 print(linha)
    #         except Error as e:
    #             print("Erro ao listar meio de contato")

    # def fechar_conexao(self):
    #     print("Retornando ao mennu principal!")
    #     if self.connection and self.connection.is_connected():
    #         self.cursor.close()
    #         self.connection.close()
    #         print("Conexão foi finalizada.")