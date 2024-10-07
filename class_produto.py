#importa a classe error do modulo mysql.connector -> utilizada para capturar e tratar erros relacionados ao banco de dados
from mysql.connector import Error

#classe que irá gerenciar a conexão com o banco de dados
class Produto:
    #método construtor da classe para conectar no banco de dados e os parametros
    def __init__(self, mydb):
        self.connection = mydb
        self.cursor = None
        if self.connection and self.connection.is_connected():
            self.cursor = self.connection.cursor()
            print("Conexão Realizada com sucesso!")
        else:
            print("Falha na conexão!")

    def inserir_produto(self, descricao, tamanho, valor):
        if self.cursor:
            try:
                query = "INSERT INTO PRODUTOS (DESCRICAO, TAMANHO, VALOR) VALUES (%s, %s, %s);"
                self.cursor.execute(query, (descricao, tamanho, valor))
                self.connection.commit()
                print(f"O produto {descricao} foi inserido com suecesso!")
            except Error as e:
                print(f"Erro ao inseir clientes {e}")
    
    def listar_produto(self):
        if self.cursor:
            try:
                cursor = self.connection.cursor()
                query = "SELECT id_produto, descricao, tamanho, valor FROM PRODUTOS;"
                cursor.execute(query)
                result = cursor.fetchall()
                for linha in result:
                    id_produto, descricao, tamanho, valor = linha
                    print(f"{id_produto}, {descricao}, {tamanho}, R${valor}")
            except Error as e:
                print(f"Erro ao buscar os dados na tabela {e}")

    def listagem_especifica(self, id):
        if self.cursor:
            try:
                cursor = self.connection.cursor()
                query = "select * from produtos where id_produto = %s;"
                dados = (id,)
                cursor.execute(query,dados)
                result = cursor.fetchall()
                for linha in result:
                    print(linha)
            except Error as e:
                print("Erro ao listar produtos")

    def listagem_especitia_ativa_desativa(self, id):
        if self.cursor:
            try:
                cursor = self.connection.cursor()
                query = "select ativo, case when ativo = 1 then 'S' when ativo = 0 then 'N' end as status_ativo from produtos where id_produto = %s;"
                dados = id,
                cursor.execute(query, dados)
                result = cursor.fetchone()
                return result[0]
            except Error as e:
                print(f"Erro ao rodar a listagem especifica do desativa/ativa! ERROR: {e}")

    def alterar_produto(self, descricao, tamanho, valor, id_produto):
        if self.cursor:
            try:
                cursor = self.connection.cursor()
                query = "update produtos set descricao = %s, tamanho = %s, valor = %s where id_produto = %s"
                dados = (descricao, tamanho, valor, id_produto)
                cursor.execute(query,dados)
                self.connection.commit()
                print("Alteração realizada com sucesso")
            except Error as e:
                print(f"Ocorreu um erro ao alterar o cliente id {id_produto}")

    def desativar_produto(self, id):
        if self.cursor:
            try:
                cursor = self.connection.cursor()
                query = "update produtos set ativo = 0 where id_produto = %s;"
                dados = (id,)
                cursor.execute(query, dados)
                print(f"Produto id: {id} desativado com sucesso!")
                self.connection.commit()
            except Error as e:
                print("Erro ao desativar produto selecionado")

    def ativar_produto(self, id):
        if self.cursor:
            try:
                cursor = self.connection.cursor()
                query = "update produtos set ativo = 1 where id_produto = %s;"
                dados = (id,)
                cursor.execute(query, dados)
                print(f"Produto id: {id} ativado com sucesso!")
                self.connection.commit()
            except Error as e:
                print("Erro ao ativar cliente selecionado")

"""
    def fechar_conexao(self):
        print("Retornando ao mennu principal!")
        if self.connection and self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("Conexão foi finalizada.")"""