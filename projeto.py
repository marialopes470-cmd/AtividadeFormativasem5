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
        else:
            for n in range(quantidade_projetos):
                nome_projeto = input("Digite o nome do projeto: ")
                projetos.append(nome_projeto)
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
        print("Comando não reconhecido. Tente novamente.")

print("Até logo!")
