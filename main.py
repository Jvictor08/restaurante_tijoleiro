#pagina principal do projeto. 
from class_conexao import mydb
from class_cliente import Cliente
from class_produto import Produto


print("Bem vindo!!")
result = 0
while result != 1 or result != 2 or result != 3 or result != 4:
    print("(1)Area Cliente, (2)Area Produto, (5)Sair ")
    result = int(input("Escolha uma das opções: "))

    # PARTE DOS CLIENTES

    if result == 1:
        print("Você entrou na opção cliente verifique as opções")
        result1 = 0
        while result1 != 1 or result1 != 2 or result1 != 3 or result1 != 4 or result1 != 5:
            print("1- Cadastro de novo cliente, 2- Listagem dos clientes, 3- Alteração de cliente, 4- Desativar/Ativar cliente, 5- Voltar para Menu inicial")
            result1 = int(input("Escolha uma opção do menu: "))
            #  CRIAÇÃO DE CLIENTE
            if result1 == 1:
                print("Cadastro do cliente")
                nome = input("Digite o nome do cliente (Digite 0 para cancelar): ").upper()
                telefone = input("Digite o telefone do cliente (Digite 0 para cancelar): ")
                if nome == '0' or telefone == '0':
                    print("Operação cancelada.")
                    break
                else:
                    novo_cadastro = Cliente(mydb)
                    novo_cadastro.inserir_cliente(nome,telefone)
                continue

            #LISTAGEM DE CLIENTE

            if result1 == 2:
                print("Você entrou na listagem de clientes!")
                listagem = Cliente(mydb)
                listagem.listar_cliente()
                continue

            #ALTERAÇÃO DE CLIENTE

            if result1 == 3:
                print("Você entrou na alteração de cliente!")
                id = input("informe o id do cliente que deseja alterar(Digite 0 para cancelar): ")
                if id == '0':
                    print("Operação cancelada!")
                    break
                else:
                    altera = Cliente(mydb)
                    altera.listagem_especifica(id)
                    confirma = input("Confirme com 'S' ou 'N' se é este registro que deseja alterar: ").upper()
                    if confirma == 'S':
                        nome = input("Digite o nome do cliente: ").upper()
                        telefone = input("Digite o novo telefone do cliente: ")
                        altera.alterar_cliente(nome, telefone, id)
                        print(f"Cliente id:{id} alterado com sucesso!")
                        altera.listagem_especifica(id)
                    else:
                        print("Alteração abortada.")
                        continue

            # DESATIVAÇÃO E ATIVAÇÃO DE CLIENTE

            if result1 == 4:
                print("Você entrou na ativação/desativação de clientes!")
                desativa = Cliente(mydb)
                id_cliente = (input("Digite o id do cliente que deseja desativar (Digite 0 para cancelar): "))
                if id_cliente =='0':
                    print("Desativação cancelada!")
                    continue
                else:
                    retorno = desativa.listagem_especitia_ativa_desativa(id_cliente)
                    if retorno == 1:
                        print("Atualmente este cliente está ativo.")
                        resp = input("Deseja desativa-lo? (S/N) ").upper()
                        if resp == 'S':            
                            desativa.desativar_cliente(id_cliente)
                        else:
                            print("Desativação abortada")
                            continue
                    elif retorno == 0:
                        print("Ataualmente este cliente está desativado.")
                        resp = input("Deseja ativa-lo? (S/N) ").upper()
                        if resp == 'S':
                            desativa.ativar_cliente(id_cliente)
                        else:
                            print("Ativação abortada")
                            continue
                    else:
                        print("Status inválido verifique na tabela")
                    continue

            # RETORNAR AO MENU PRINCIPAL

            if result1 == 5:
                print("Retornando ao menu principal")
                break

    # AQUI É A PARTE DOS PRODUTOS.

    elif result == 2:
        print("Você entrou na opção cliente verifique as opções")
        result2 = 0
        while result2 != 1 or result2 != 2 or result2 != 3 or result2 != 4 or result2 != 5:
            print("1- Cadastro de novo produto, 2- Listagem dos produtos, 3- Alteração de produto, 4- Desativar produto, 5- Voltar para Menu inicial")
            result2 = int(input("Escolha uma opção do menu: "))

            #CADASTRO DE PRODUTO

            if result2 == 1:
                print("Cadastro de Produto")
                descricao = input("Digite a descricao do produto (Digite 0 para cancelar): ").upper()
                tamanho = input("Digite o tamanho do produto (Digite 0 para cancelar): ").upper()
                valor = float(input(f"Digite o valor do produto: "))
                if descricao == '0' or tamanho == '0':
                    print("Operação cancelada.")
                    break
                else:
                    novo_cadastro = Produto(mydb)
                    novo_cadastro.inserir_produto(descricao,tamanho, valor)
                continue

            #LISTAGEM DE PRODUTO

            elif result2 == 2:
                print("Listagem de produtos")
                listagem = Produto(mydb)
                listagem.listar_produto()
                continue

            #ALTERAÇÃO DE PRODUTO

            elif result2 == 3:
                print("Você entrou na alteração de produtos!")
                id_produto = input("informe o id do produto que deseja alterar(Digite 0 para cancelar): ")
                if id_produto == '0':
                    print("Operação cancelada!")
                    break
                else:
                    altera = Produto(mydb)
                    altera.listagem_especifica(id_produto)
                    confirma = input("Confirme com 'S' ou 'N' se é este registro que deseja alterar: ").upper()
                    if confirma == 'S':
                        descricao = input("Digite a nova descrição do produto: ").upper()
                        tamanho = input("Digite o novo tamanho do produto: ").upper()
                        valor = float(input("Digite o novo valor do produto: "))
                        altera.alterar_produto(descricao, tamanho, valor, id_produto)
                        
                        print(f"Produto {descricao} alterado com sucesso!")
                        altera.listagem_especifica(id_produto)
                    else:
                        print("Alteração abortada.")
                        continue

            # DESATIVAÇÃO/ATIVAÇÃO DE PRODUTO
            

            elif result2 == 4:
                print("Você entrou na desativação/ativação de produtos!")
                desativa = Produto(mydb)
                id_produto = (input("Digite o id do produto que deseja desativar (Digite 0 para cancelar): "))
                if id_produto =='0':
                    print("Desativação cancelada")
                    continue
                else:
                    retorno = desativa.listagem_especitia_ativa_desativa(id_produto)
                    if retorno == 1:
                        print("Atualmente este produto está ativo.")
                        resp = input("Deseja desativa-lo? (S/N) ").upper()
                        if resp == 'S':            
                            desativa.desativar_produto(id_produto)
                        else:
                            print("Desativação abortada")
                            continue
                    elif retorno == 0:
                        print("Ataualmente este produto está desativado.")
                        resp = input("Deseja ativa-lo? (S/N) ").upper()
                        if resp == 'S':
                            desativa.ativar_produto(id_produto)
                        else:
                            print("Ativação abortada")
                            continue
                    else:
                        print("Status inválido verifique na tabela")
                    continue

        # RETORNAR AO MENU PRINCIPAL

            elif result2 == 5:
                print("Retornando ao menu principal")
                break
    elif result == 3:
        print("Outra funcionalidade")
    


    