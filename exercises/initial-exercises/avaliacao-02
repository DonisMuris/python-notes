
mapa = [
    ["INICIO", "O", "O", "X"],
    ["X", "P3", "O", "P1"],
    ["X", "X", "P2", "X"]
]


movimentos = {
    "D": (0, 1),   
    "E": (0, -1),  
    "C": (-1, 0),  
    "B": (1, 0)    
}


pos = (0, 0)
pos_anterior = None

while True:
    comando = input().strip()  
    
    if comando not in movimentos:
        print("E")
        break

    dx, dy = movimentos[comando]
    nova_pos = (pos[0] + dx, pos[1] + dy)

    if not (0 <= nova_pos[0] < len(mapa) and 0 <= nova_pos[1] < len(mapa[0])):
        print("X")
        break

    if nova_pos == pos_anterior:
        print("V")
        break

    pos_anterior = pos
    pos = nova_pos

    conteudo = mapa[pos[0]][pos[1]]

    if conteudo == "X":
        print("X")
        break
    elif conteudo == "P1":
        print("P1")
        break
    elif conteudo == "P2":
        print("P2")
        break
    elif conteudo == "P3":
        print("P3")
        break
