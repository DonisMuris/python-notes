# Entrada
dist_alvo = int(input())
combustivel = int(input())

dist_atual = 0

while dist_atual < dist_alvo:
    # Calcula soma dos pares menores que a distância atual
    prox_k = dist_atual + 1
    soma_pares = 0
    for i in range(prox_k):
        if i % 2 == 0:  # número par
            soma_pares += i
    soma_pares += 1  # mais 1 conforme regra

    # Consumo dessa iteração
    consumo = dist_alvo / soma_pares

    # Verifica se tem combustível suficiente
    if combustivel < consumo:
        break

    # Atualiza distância e combustível
    dist_atual = prox_k
    combustivel -= consumo

    # Mostra como inteiros
    print(int(dist_atual), int(combustivel))
