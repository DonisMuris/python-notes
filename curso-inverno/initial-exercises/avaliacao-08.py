
def registrar_votos(candidatos, secoes, votos_por_candidato):
    votos = raw_input().split(",")
    votos = [int(v) for v in votos]

    secoes.append(votos)

    for i in range(len(candidatos)):
        votos_por_candidato[i] += votos[i]

def listar_votos_secoes(secoes):
    for s in secoes:
        print(sum(s))

def listar_votos_candidatos(votos_por_candidato):
    for v in votos_por_candidato:
        print(v)

def listar_ordem_decrescente(candidatos, votos_por_candidato):
    pares = []
    for i in range(len(candidatos)):
        pares.append([candidatos[i], votos_por_candidato[i]])

    n = len(pares)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if pares[j][1] < pares[j + 1][1]:
                pares[j], pares[j + 1] = pares[j + 1], pares[j]

    for p in pares:
        print(p[0])

def verificar_segundo_turno(votos_por_candidato):
    total_votos = sum(votos_por_candidato)
    if total_votos == 0:
        print("Segundo turno.")
        return

    mais_votado = max(votos_por_candidato)
    if mais_votado > (total_votos / 2.0):
        print("Sem segundo turno.")
    else:
        print("Segundo turno.")

candidatos = raw_input().split(",")
secoes = []
votos_por_candidato = [0] * len(candidatos)

while True:
    opcao = int(raw_input())
    if opcao == 1:
        registrar_votos(candidatos, secoes, votos_por_candidato)
    elif opcao == 2:
        listar_votos_secoes(secoes)
    elif opcao == 3:
        listar_votos_candidatos(votos_por_candidato)
    elif opcao == 4:
        listar_ordem_decrescente(candidatos, votos_por_candidato)
    elif opcao == 5:
        verificar_segundo_turno(votos_por_candidato)
    elif opcao == 6:
        break
