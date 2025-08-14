nomes = []
tipos = []
quantidades = []

while True:
    opcao = int(raw_input())

    if opcao == -1:
        break

    elif opcao == 1:
        nome = raw_input()
        tipo = raw_input()
        quantidade = int(raw_input())
        nomes.append(nome)
        tipos.append(tipo)
        quantidades.append(quantidade)

    elif opcao == 2:
        nome_busca = raw_input()
        encontrado = False
        for i in range(len(nomes)):
            if nomes[i] == nome_busca:
                print tipos[i]
                print quantidades[i]
                encontrado = True
                break
        if not encontrado:
            print "Nao cadastrado"

    elif opcao == 3:
        tipo_busca = raw_input()
        soma = 0
        encontrado = False
        for i in range(len(tipos)):
            if tipos[i] == tipo_busca:
                soma += quantidades[i]
                encontrado = True
        if encontrado:
            print soma
        else:
            print "Nao cadastrado"

    elif opcao == 4:
        if len(quantidades) > 0:
            print sum(quantidades)
        else:
            print "Nao cadastrado"

    else:
        print "Invalido"
