#importa a classe error do modulo mysql.connector -> utilizada para capturar e tratar erros relacionados ao banco de dados
from mysql.connector import Error

#classe que irá gerenciar a conexão com o banco de dados
class Contato:
    #método construtor da classe para conectar no banco de dados e os parametros
    def __init__(self, mydb):
        self.connection = mydb
        self.cursor = None
        if self.connection and self.connection.is_connected():
            self.cursor = self.connection.cursor()
            print("Conexão Realizada com sucesso!")
        else:
            print("Falha na conexão!")

    def inserir_contato(self, desc):
        if self.cursor:
            try:
                query = "INSERT INTO tb_meio_de_contato (DESC_PLATAFORMA) VALUES (%s);"
                self.cursor.execute(query, (desc,))
                self.connection.commit()
                print(f"O meio de contato {desc} foi inserido com suecesso!")
            except Error as e:
                print(f"Erro ao inseir meio de contato {e}")

    def listar_contato(self):
        if self.cursor:
            try:
                cursor = self.connection.cursor()
                query = "SELECT desc_plataforma FROM tb_meio_de_contato where ativo = 1;"
                cursor.execute(query)
                result = cursor.fetchall()
                for linha in result:
                    desc_plataforma = linha
                    print(f"{desc_plataforma}")
            except Error as e:
                print(f"Erro ao buscar os dados na tabela {e}")


    def listar_contato_completo(self):
        if self.cursor:
            try:
                cursor = self.connection.cursor()
                query = "SELECT idtb_meio_de_contato, desc_plataforma, ativo FROM tb_meio_de_contato;"
                cursor.execute(query)
                result = cursor.fetchall()
                for linha in result:
                    idtb_meio_de_contato, desc_plataforma, ativo = linha
                    print(f"{idtb_meio_de_contato}, {desc_plataforma}, {ativo}")
            except Error as e:
                print(f"Erro ao buscar os dados na tabela {e}")

    def listar_contato_especifico(self, id):
            if self.cursor:
                try:
                    cursor = self.connection.cursor()
                    query = "select * from tb_meio_de_contato where idtb_meio_de_contato = %s;"
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
                query = "select ativo, case when ativo = 1 then 'S' when ativo = 0 then 'N' end as status_ativo from tb_meio_de_contato where idtb_meio_de_contato = %s;"
                dados = id,
                cursor.execute(query, dados)
                result = cursor.fetchone()
                return result[0]
            except Error as e:
                print(f"Erro ao rodar a listagem especifica do desativa/ativa! ERROR: {e}")

    def alterar_contato(self, desc, id):
        if self.cursor:
            try:
                cursor = self.connection.cursor()
                query = "update tb_meio_de_contato set desc_plataforma = %s where idtb_meio_de_contato = %s;"
                dados = (desc, id)
                cursor.execute(query,dados)
                self.connection.commit()
                print("Alteração realizada com sucesso")
            except Error as e:
                print(f"Ocorreu um erro ao alterar o contato {id} Erro: {e}")

    def desativar_contato(self, id):
        if self.cursor:
            try:
                cursor = self.connection.cursor()
                query = "update tb_meio_de_contato set ativo = 0 where idtb_meio_de_contato = %s;"
                dados = (id,)
                cursor.execute(query, dados)
                print(f"Contato id: {id} desativado com sucesso!")
                self.connection.commit()
            except Error as e:
                print(f"Erro ao desativar endereço selecionado: {e}")

    def ativar_contato(self, id):
        if self.cursor:
            try:
                cursor = self.connection.cursor()
                query = "update tb_meio_de_contato set ativo = 1 where idtb_meio_de_contato = %s;"
                dados = (id,)
                cursor.execute(query, dados)
                print(f"Contato id: {id} ativado com sucesso!")
                self.connection.commit()
            except Error as e:
                print(f"Erro ao ativar endereço selecionado: {e}")





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