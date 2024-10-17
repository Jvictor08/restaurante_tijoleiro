#pagina principal do projeto. 
from class_conexao import mydb
from class_cliente import Cliente
from class_produto import Produto
from class_endereco import Endereco
from class_meio_de_contato import Contato
from class_finalidade import Finalidade


print("Bem vindo!!")
result = 0
while result != 1 or result != 2 or result != 3 or result != 4:
    print("(1)Endereço, (2)Cliente, (3)Contato, (4)Finalidade, (5)Produtos, (6)Sair ")
    result = int(input("Escolha uma das opções: "))

    if result == 1:
        print("Você entrou na opção de cadastro de endereços")
        result1 = 0
        while result1 != 1 or result1 != 2 or result1 != 3 or result1 != 4 or result1 != 5:
            print("(1)Cadastro de novo endereço, (2)Listagem de endereços, (3)Alteração de endereço, (4)Desativação de endereço, (5)Voltar ao menu inicial")
            result1 =  int(input("Escolha uma opção do menu: "))
            # ENDEREÇO
            if result1 == 1:
                print("Cadastro de endereço")
                cidade = input("Digite a cidade do cliente(Digite 0 para cancelar): ").upper()
                bairro = input("Digite o bairro do cliente: ").upper()
                rua = input("Digite a rua do cliente: ").upper()
                numero = input("Digite o numero do cliente: ").upper()
                if cidade == '0' or bairro == '0' or rua == '0' or numero == '0':
                    print("Operação cancelada.")
                    break
                else:
                    novo_cadastro = Endereco(mydb)
                    novo_cadastro.inserir_endereco(cidade,bairro,rua,numero)
                continue

            elif result1 == 2:
                print("Listagem de endereços")
                listagem = Endereco(mydb)
                listagem.listar_endereco()
                continue

            elif result1 == 3:
                print("Você entrou na alteração de endereço!")
                altera = Endereco(mydb)
                altera.listar_endereco_completo()
                id = input("informe o id do endereço que deseja alterar(Digite 0 para cancelar): ")
                if id == '0':
                    print("Operação cancelada!")
                    break
                else:
                    altera.listar_especifico(id)
                    confirma = input("Confirme com 'S' ou 'N' se é este registro que deseja alterar: ").upper()
                    if confirma == 'S':
                        cidade = input("Digite a cidade do cliente: ").upper()
                        bairro = input("Digite o bairro do cliente: ").upper()
                        rua = input("Digite a rua do cliente: ").upper()
                        numero = input("Digite o numero do cliente: ").upper()
                        altera.alterar_endereco(cidade, bairro, rua, numero, id)
                        print(f"Cliente id:{id} alterado com sucesso!")
                        altera.listar_especifico(id)
                    else:
                        print("Alteração abortada.")
                        continue
            
            elif result1 == 4:
                print("Você entrou na ativação/desativação de endereços!")
                desativa = Endereco(mydb)
                desativa.listar_endereco_completo()
                id = (input("Digite o id do endereço que deseja desativar (Digite 0 para cancelar): "))
                if id =='0':
                    print("Desativação cancelada!")
                    continue
                else:
                    retorno = desativa.listar_especifico_ativa_desativa(id)
                    if retorno == 1:
                        print("Atualmente este endereço está ativo.")
                        resp = input("Deseja desativa-lo? (S/N) ").upper()
                        if resp == 'S':            
                            desativa.desativar_endereco(id)
                        else:
                            print("Desativação abortada")
                            continue
                    elif retorno == 0:
                        print("Ataualmente este endereço está desativado.")
                        resp = input("Deseja ativa-lo? (S/N) ").upper()
                        if resp == 'S':
                            desativa.ativar_endereco(id)
                        else:
                            print("Ativação abortada")
                            continue
                    else:
                        print("Status inválido verifique na tabela")
                    continue

            elif result1 == 5:
                print("Retornando ao menu principal")
                break
    # CLIENTES
    if result == 2:
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
    
    # CONTATO

    elif result == 3:
        print("Você entrou nas formas de contato")
        result3 = 0
        while result3 != 1 or result3 != 2 or result3 != 3 or result3 != 4 or result3 != 5:
            print("(1)Cadastro, (2)Listagem, (3)Alteração (4)Desativar (5)Voltar")
            result3 = int(input("Escolha uma opção do menu: "))
            if result3 == 1:
                print("Cadastro de forma de contato")
                desc = input("Digite a descrição do meio de contato(Digite 0 para cancelar): ").upper()
                if desc == '0':
                    print("Operação cancelada.")
                    break
                else:
                    novo_contato = Contato(mydb)
                    novo_contato.inserir_contato(desc)
                continue

            elif result3 == 2:
                print("Listagem dos contatos")
                listagem = Contato(mydb)
                listagem.listar_contato()
                continue

            elif result3 == 3:
                print("Você entrou na alteração de contato!")
                altera = Contato(mydb)
                altera.listar_contato_completo()
                id = input("informe o id do contato que deseja alterar(Digite 0 para cancelar): ")
                if id == '0':
                    print("Operação cancelada!")
                    break
                else:
                    altera.listar_contato_especifico(id)
                    confirma = input("Confirme com 'S' ou 'N' se é este registro que deseja alterar: ").upper()
                    if confirma == 'S':
                        desc = input("Digite a descrição do contato: ").upper()
                        altera.alterar_contato(desc, id)
                        print(f"Contato id:{id} alterado com sucesso!")
                        altera.listar_contato_especifico(id)
                    else:
                        print("Alteração abortada.")
                        continue

            elif result3 == 4:
                print("Você entrou na ativação/desativação de endereços!")
                desativa = Contato(mydb)
                desativa.listar_contato_completo()
                id = (input("Digite o id do contato que deseja ativar/desativar (Digite 0 para cancelar): "))
                if id =='0':
                    print("Desativação cancelada!")
                    continue
                else:
                    retorno = desativa.listar_especifico_ativa_desativa(id)
                    if retorno == 1:
                        print("Atualmente este contato está ativo.")
                        resp = input("Deseja desativa-lo? (S/N) ").upper()
                        if resp == 'S':            
                            desativa.desativar_contato(id)
                        else:
                            print("Desativação abortada")
                            continue
                    elif retorno == 0:
                        print("Ataualmente este contato está desativado.")
                        resp = input("Deseja ativa-lo? (S/N) ").upper()
                        if resp == 'S':
                            desativa.ativar_contato(id)
                        else:
                            print("Ativação abortada")
                            continue
                    else:
                        print("Status inválido verifique na tabela")
                    continue

            elif result3 == 5:
                print("Retornando ao menu principal")
                break

    # AQUI É A PARTE DAS FINALIDADES 
    elif result == 4:  
        print("Você entrou nas finalidades")
        result4 = 0
        while result4 != 1 or result4 != 2 or result4 != 3 or result4 != 4 or result4 != 5:
            print("(1)Cadastro, (2)Listagem, (3)Alteração (4)Desativar (5)Voltar")
            result4 = int(input("Escolha uma opção do menu: "))
            if result4 == 1:
                print("Cadastro de finalidade")
                desc = input("Digite a descrição da finalidade(Digite 0 para cancelar): ").upper()
                if desc == '0':
                    print("Operação cancelada.")
                    break
                else:
                    novo_contato = Finalidade(mydb)
                    novo_contato.inserir_finalidade(desc)
                continue

            elif result4 == 2:
                print("Listagem das finalidades")
                listagem = Finalidade(mydb)
                listagem.listar_finalidade()
                continue
            
            elif result4 == 3:
                print("Você entrou na alteração de finalidade!")
                altera = Finalidade(mydb)
                altera.listar_finalidade_completo()
                id = input("informe o id da finalidade que deseja alterar(Digite 0 para cancelar): ")
                if id == '0':
                    print("Operação cancelada!")
                    break
                else:
                    altera.listar_finalidade_especifico(id)
                    confirma = input("Confirme com 'S' ou 'N' se é este registro que deseja alterar: ").upper()
                    if confirma == 'S':
                        desc = input("Digite a descrição da finalidade: ").upper()
                        altera.alterar_finalidade(desc, id)
                        print(f"Contato id:{id} alterado com sucesso!")
                        altera.listar_finalidade_especifico(id)
                    else:
                        print("Alteração abortada.")
                        continue
            
            elif result4 == 4:
                print("Você entrou na ativação/desativação de finalidades!")
                desativa = Finalidade(mydb)
                desativa.listar_finalidade_completo()
                id = (input("Digite o id da finalidade que deseja ativar/desativar (Digite 0 para cancelar): "))
                if id =='0':
                    print("Ativação/Desativação cancelada!")
                    continue
                else:
                    retorno = desativa.listar_especifico_ativa_desativa(id)
                    if retorno == 1:
                        print("Atualmente esta finalidade está ativa.")
                        resp = input("Deseja desativa-lo? (S/N) ").upper()
                        if resp == 'S':            
                            desativa.desativar_contato(id)
                        else:
                            print("Desativação abortada")
                            continue
                    elif retorno == 0:
                        print("Ataualmente esta finalidade está desativada.")
                        resp = input("Deseja ativa-lo? (S/N) ").upper()
                        if resp == 'S':
                            desativa.ativar_contato(id)
                        else:
                            print("Ativação abortada")
                            continue
                    else:
                        print("Status inválido verifique na tabela")
                    continue

            elif result4 == 5:
                print("Retornando ao menu principal")
                break
            
    # AQUI É A PARTE DOS PRODUTOS.
    elif result == 5:
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

            elif result2 == 6:
                print("Retornando ao menu principal")
                break

    


    