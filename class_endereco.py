#importa a classe error do modulo mysql.connector -> utilizada para capturar e tratar erros relacionados ao banco de dados
from mysql.connector import Error

#classe que irá gerenciar a conexão com o banco de dados
class Endereco:
    #método construtor da classe para conectar no banco de dados e os parametros
    def __init__(self, mydb):
        self.connection = mydb
        self.cursor = None
        if self.connection and self.connection.is_connected():
            self.cursor = self.connection.cursor()
            print("Conexão Realizada com sucesso!")
        else:
            print("Falha na conexão!")

    def inserir_endereco(self, cidade, bairro, rua, numero):
        if self.cursor:
            try:
                query = "INSERT INTO ENDERECO (CIDADE, BAIRRO, RUA, NUMERO) VALUES (%s, %s, %s);"
                self.cursor.execute(query, (cidade, bairro, rua, numero))
                self.connection.commit()
                print(f"O endereço cidade: {cidade}, bairro: {bairro}, rua: {rua} e numero: {numero} foi inserido com suecesso!")
            except Error as e:
                print(f"Erro ao inseir endereço {e}")

    def listar_endereco(self):
        if self.cursor:
            try:
                cursor = self.connection.cursor()
                query = "SELECT cidade, bairro, rua, numero FROM ENDERECO;"
                cursor.execute(query)
                result = cursor.fetchall()
                for linha in result:
                    cidade, bairro, rua, numero = linha
                    print(f"{cidade}, {bairro}, {rua}, {numero}")
            except Error as e:
                print(f"Erro ao buscar os dados na tabela {e}")

    # def listagem_especifica(self, id):
    #     if self.cursor:
    #         try:
    #             cursor = self.connection.cursor()
    #             query = "select * from endereco,  where id_cidade = %s;"
    #             dados = (id,)
    #             cursor.execute(query,dados)
    #             result = cursor.fetchall()
    #             for linha in result:
    #                 print(linha)
    #         except Error as e:
    #             print("Erro ao listar endereço")

    # def fechar_conexao(self):
    #     print("Retornando ao mennu principal!")
    #     if self.connection and self.connection.is_connected():
    #         self.cursor.close()
    #         self.connection.close()
    #         print("Conexão foi finalizada.")