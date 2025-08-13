
texto = input().strip().replace("_", " ")
lista = input().strip().replace("_", " ")

texto = texto.replace(".", "").replace(",", "").replace(";", "")
texto_lower = texto.lower()
lista_lower = lista.lower()

# Contar palavras do texto
espacos = texto.find(" ")
qtd = 1
pos = 0
while pos != -1:
    pos = texto.find(" ", pos + 1)
    if pos != -1:
        qtd += 1
print qtd

# Contar ocorrências das palavras da lista
if lista != "":
    palavras_lista = lista.split(" ")
    palavras_lista_lower = lista_lower.split(" ")
    i = 0
    while i < len(palavras_lista):
        palavra = palavras_lista_lower[i]
        cont = 0
        pos = texto_lower.find(palavra)
        while pos != -1:
            # garantir que é palavra inteira
            antes = (pos == 0) or (texto_lower[pos-1] == " ")
            depois = (pos + len(palavra) == len(texto_lower)) or (texto_lower[pos + len(palavra)] == " ")
            if antes and depois:
                cont += 1
            pos = texto_lower.find(palavra, pos + 1)
        print palavras_lista[i], cont
        i += 1
