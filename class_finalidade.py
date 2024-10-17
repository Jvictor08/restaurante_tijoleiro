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

    def inserir_finalidade(self, desc_finalidade):
        if self.cursor:
            try:
                query = "INSERT INTO tb_finalidade (DESC_FINALIDADE) VALUES (%s);"
                self.cursor.execute(query, (desc_finalidade,))
                self.connection.commit()
                print(f"A finalidade {desc_finalidade} foi inserido com suecesso!")
            except Error as e:
                print(f"Erro ao inseir dados {e}")

    def listar_finalidade(self):
        if self.cursor:
            try:
                cursor = self.connection.cursor()
                query = "SELECT desc_finalidade FROM tb_finalidade where ativo = 1;"
                cursor.execute(query)
                result = cursor.fetchall()
                for linha in result:
                    desc_finalidade = linha
                    print(f"{desc_finalidade}")
            except Error as e:
                print(f"Erro ao buscar os dados na tabela {e}")

    def listar_finalidade_completo(self):
        if self.cursor:
            try:
                cursor = self.connection.cursor()
                query = "SELECT idtb_finalidade, desc_finalidade, ativo FROM tb_finalidade;"
                cursor.execute(query)
                result = cursor.fetchall()
                for linha in result:
                    idtb_finalidade, desc_finalidade, ativo = linha
                    print(f"{idtb_finalidade}, {desc_finalidade}, {ativo}")
            except Error as e:
                print(f"Erro ao buscar os dados na tabela {e}")


    def listar_finalidade_especifico(self, id):
        if self.cursor:
            try:
                cursor = self.connection.cursor()
                query = "select * from tb_finalidade where idtb_finalidade = %s;"
                dados = (id,)
                cursor.execute(query,dados)
                result = cursor.fetchall()
                for linha in result:
                    print(linha)
            except Error as e:
                print(f"Erro ao listar dados: {e}")

    def listar_especifico_ativa_desativa(self, id):
        if self.cursor:
            try:
                cursor = self.connection.cursor()
                query = "select ativo from tb_finalidade where idtb_finalidade = %s;"
                dados = id,
                cursor.execute(query, dados)
                result = cursor.fetchone()
                return result[0]
            except Error as e:
                print(f"Erro ao rodar a listagem especifica do desativa/ativa! ERROR: {e}")

    def alterar_finalidade(self, desc, id):
        if self.cursor:
            try:
                cursor = self.connection.cursor()
                query = "update tb_finalidade set desc_finalidade = %s where idtb_finalidade = %s;"
                dados = (desc, id)
                cursor.execute(query,dados)
                self.connection.commit()
                print("Alteração realizada com sucesso")
            except Error as e:
                print(f"Ocorreu um erro ao realizar a alteração. Erro: {e}")

    def desativar_contato(self, id):
        if self.cursor:
            try:
                cursor = self.connection.cursor()
                query = "update tb_finalidade set ativo = 0 where idtb_finalidade = %s;"
                dados = (id,)
                cursor.execute(query, dados)
                print(f"Registro id: {id} desativado com sucesso!")
                self.connection.commit()
            except Error as e:
                print(f"Erro ao desativar registro: {e}")

    def ativar_contato(self, id):
        if self.cursor:
            try:
                cursor = self.connection.cursor()
                query = "update tb_finalidade set ativo = 1 where idtb_finalidade = %s;"
                dados = (id,)
                cursor.execute(query, dados)
                print(f"Registo id: {id} ativado com sucesso!")
                self.connection.commit()
            except Error as e:
                print(f"Erro ao ativar registro: {e}")

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