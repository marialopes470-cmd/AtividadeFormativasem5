projetos = []  

while True:
    comando = input("Digite um comando aqui: ").upper()

    if comando == "ABOUT":
        print("Boas-vindas ao software da Maria das Graças.")
    elif comando == "QUIT":
        print("Saindo do nosso software.")
        break
    elif comando == "ADD":
        quantidade_projetos = int(input("Informe quantos projetos gostaria de cadastrar: "))

        if quantidade_projetos <= 0:
            print("A quantidade de projetos digitada é inválida. Tente novamente.")

            lista[]
        else:
            for i in range(3):
                nome_projeto = input("Digite o nome do projeto que deseja cadastrar: ")

                cadastro_projeto = {
                    "Nome":f"projeto teste {i +1}",
                    "Concluido" : False,
                    "Historico": []

                 
                }
                lista.append(nome_projeto)
                if len(lista) == 0:
                    print("A lista esta vazia.")
                    else:
                        for elemento in lista:
                            print("Detalhe do projeto:")
                            for chave, valor in elemento.items():
                                print(f"{chave}: {valor}")
                                print()
        #UPDATE
        projeto_para_modificar = input ("Qual o nome do projeto que você deseja modificar?: ")
             for projeto in lista:
                if projeto ["Nome"] != projeto_para_modificar:
                    continue

                projeto_para_modificar = projeto
                 break
            if projeto_para_modificar is not None:
                nome = input ("Digite o novo nome do projeto.")
                status = bool(input("Fnalizou o projeto?Digitr 1 para sim, e 0 para não."))
                projeto_para_modificar ["nome"] = nome
                projeto_para_modificar["status"] = status

                data_mudanca = input ("Qual o dia de hoje?")
                entrada_atualizacao = (data_mudanca,projeto_para_modificar["nome"], projeto_para_modificar["status"])
                projeto_para_modificar["historico"].append(entrada_atualizacao)

                #op aqui
            else:
                print("Não encontrei o projeto.")

            
            #DELETE
            nome_projeto_para_remover = input ("Qual o bome do projeto que você gostaria de remover?:")
            projeto_para_remover = None


            for projeto in lista:
                if projeto["Nome"] != nome_projeto_para_remover:
                    continue

                projeto_para_remover = projeto
                 break   

            if projeto_para_remover is not None:
                lista.remove(projeto_para_remover)
                print(f"Projeto {projeto_para_remover['Nome']} removido com sucesso!")
            else:
                print("Não encontrei o projeto.")
                       

                print(f"Parabéns! Cadastramos o projeto '{nome_projeto}'")
    elif comando == "LIST":
        if projetos == []:
            print("Nenhum projeto cadastrado.")
        else:
            print("Projetos cadastrados:")
            numero = 1
            
            for projeto in projetos:
                print(numero, projeto)
                numero = numero + 1
    else:
        print("Comando não reconhecido. Tente novamente. 
print("Até logo!")
