ids = []
descricoes = []
prioridades = []
status = []

contador_id = 0

while True:
	try:
		opcao = int(input())
	except:
		continue
		
	if opcao == -1:
		break
		
	elif opcao == 1:
		descricao = input()
		prioridade = input()
		contador_id += 1
		ids.append(contador_id)
		descricoes.append(descricao)
		prioridades.append(prioridade)
		status.append("pendente")
		
	elif opcao == 2:
		for pr in ["a", "m", "b"]:
			for i in range(len(ids)):
				if prioridades[i] == pr:
					print(ids[i])
					print(descricoes[i])
					print(prioridades[i])
					print(status[i])
		
	elif opcao == 3:
		try:
			codigo = int(input())	
		except:
			continue
		encontrado = False
		for i in range(len(ids)):
			if ids[i] == codigo:
				status[i] = "pronta"
				encontrado = True
		if not encontrado: 
			print("Tarefa inexistente")
		
	elif opcao == 4:
		for pr in ["a", "m", "b"]:
			for i in range(len(ids)):
				if prioridades[i] == pr and status[i] == "pendente":
					print(ids[i])
					print(descricoes[i])
					print(prioridades[i])
					print(status[i])
		
	elif opcao == 5:
		try:
			codigo = int(input())
		except:
			continue
		encontrado = False
		for i in range(len(ids)):
			if ids[i] == codigo:
				del ids[i]
				del descricoes[i]
				del prioridades[i]
				del status[i]
				encontrado = True
				break
		if not encontrado:
			print("Tarefa inexistente")
			
	elif opcao == 6:
		try:
			codigo = int(input())
			nova_prioridade = input()
		except:
			continue
		encontrado = False
		for i in range(len(ids)):
			if ids[i] == codigo:
				prioridades[i] = nova_prioridade
				encontrado = True
		if not encontrado:
			print("Tarefa inexistente")
			
	else:
		print("Invalido")
