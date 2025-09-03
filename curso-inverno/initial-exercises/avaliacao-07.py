carros = []  

def media_lista(lista):
    return sum(lista) / float(len(lista))

while True:
    try:
        opcao = int(raw_input())
    except:
        break

    if opcao == 1:
        dados = raw_input().split(";")
        modelo = dados[0]
        urbano = [float(dados[1]), float(dados[2]), float(dados[3])]
        rodov = [float(dados[4]), float(dados[5]), float(dados[6])]
        carros.append([modelo, urbano, rodov])

    elif opcao == 2:
        total_valores = 0.0
        cont = 0
        for carro in carros:
            total_valores += sum(carro[1]) + sum(carro[2])
            cont += len(carro[1]) + len(carro[2])
        if cont > 0:
            print("{:.1f}".format(total_valores / cont))

    elif opcao == 3:
        total_urbano = 0.0
        cont = 0
        for carro in carros:
            total_urbano += sum(carro[1])
            cont += len(carro[1])
        if cont > 0:
            print("{:.1f}".format(total_urbano / cont))

    elif opcao == 4:
        medias = []
        for carro in carros:
            todas = carro[1] + carro[2]
            medias.append([carro[0], media_lista(todas)])
        
        n = len(medias)
        for i in range(n-1):
            for j in range(n-i-1):
                if medias[j][1] < medias[j+1][1]:
                    medias[j], medias[j+1] = medias[j+1], medias[j]

        for item in medias:
            print(item[0])

    elif opcao == 5:
        break
