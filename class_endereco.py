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
                query = "INSERT INTO tb_endereco (CIDADE, BAIRRO, RUA, NUMERO) VALUES (%s, %s, %s, %s);"
                self.cursor.execute(query, (cidade, bairro, rua, numero))
                self.connection.commit()
                print(f"O endereço cidade: {cidade}, bairro: {bairro}, rua: {rua} e numero: {numero} foi inserido com suecesso!")
            except Error as e:
                print(f"Erro ao inseir endereço {e}")

    def listar_endereco(self):
        if self.cursor:
            try:
                cursor = self.connection.cursor()
                query = "SELECT cidade, bairro, rua, numero FROM tb_endereco where ativo = 1;"
                cursor.execute(query)
                result = cursor.fetchall()
                for linha in result:
                    cidade, bairro, rua, numero = linha
                    print(f"{cidade}, {bairro}, {rua}, {numero}")
            except Error as e:
                print(f"Erro ao buscar os dados na tabela {e}")

    def listar_endereco_completo(self):
        if self.cursor:
            try:
                cursor = self.connection.cursor()
                query = "SELECT idtb_endereco, cidade, bairro, rua, numero FROM tb_endereco;"
                cursor.execute(query)
                result = cursor.fetchall()
                for linha in result:
                    id ,cidade, bairro, rua, numero = linha
                    print(f"{id}, {cidade}, {bairro}, {rua}, {numero}")
            except Error as e:
                print(f"Erro ao buscar os dados na tabela {e}")

    def listar_especifico(self, id):
        if self.cursor:
            try:
                cursor = self.connection.cursor()
                query = "select * from tb_endereco where idtb_endereco = %s;"
                dados = (id,)
                cursor.execute(query,dados)
                result = cursor.fetchall()
                for linha in result:
                    print(linha)
            except Error as e:
                print("Erro ao listar endereço")

    def listar_especifico_ativa_desativa(self, id):
        if self.cursor:
            try:
                cursor = self.connection.cursor()
                query = "select ativo, case when ativo = 1 then 'S' when ativo = 0 then 'N' end as status_ativo from tb_endereco where idtb_endereco = %s;"
                dados = id,
                cursor.execute(query, dados)
                result = cursor.fetchone()
                return result[0]
            except Error as e:
                print(f"Erro ao rodar a listagem especifica do desativa/ativa! ERROR: {e}")

    def alterar_endereco(self, cidade, bairro, rua, numero, id):
        if self.cursor:
            try:
                cursor = self.connection.cursor()
                query = "update tb_endereco set cidade = %s, bairro = %s, rua = %s, numero = %s where idtb_endereco = %s;"
                dados = (cidade, bairro, rua, numero, id)
                cursor.execute(query,dados)
                self.connection.commit()
                print("Alteração realizada com sucesso")
            except Error as e:
                print(f"Ocorreu um erro ao alterar o endereco id {id}")

    def desativar_endereco(self, id):
        if self.cursor:
            try:
                cursor = self.connection.cursor()
                query = "update tb_endereco set ativo = 0 where idtb_endereco = %s;"
                dados = (id,)
                cursor.execute(query, dados)
                print(f"Endereço id: {id} desativado com sucesso!")
                self.connection.commit()
            except Error as e:
                print("Erro ao desativar endereço selecionado")

    def ativar_endereco(self, id):
        if self.cursor:
            try:
                cursor = self.connection.cursor()
                query = "update tb_endereco set ativo = 1 where idtb_endereco = %s;"
                dados = (id,)
                cursor.execute(query, dados)
                print(f"Endereço id: {id} ativado com sucesso!")
                self.connection.commit()
            except Error as e:
                print("Erro ao ativar endereço selecionado")

    # def fechar_conexao(self):
    #     print("Retornando ao mennu principal!")
    #     if self.connection and self.connection.is_connected():
    #         self.cursor.close()
    #         self.connection.close()
    #         print("Conexão foi finalizada.")