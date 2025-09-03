Descrição do Trabalho
Nesta avaliação iremos treinar os conceitos da aula 09, sobre manipulação de listas.

 
Tópicos
 iterações    listas  

Faça um programa para gerenciar uma lista de atividades a fazer. O programa deve permitir que novas tarefas sejam adicionadas à lista, que tarefas existentes sejam marcadas como "prontas" e que tarefas existentes sejam removidas da lista.
 
O programa irá funcionar baseado em um menu de opções. Ele deve continuar aguardando novas opções enquanto a opção escolhida for diferente de -1.

- A opção 1 irá permitir que uma nova tarefa seja cadastrada.
    - Cada tarefa inserida deve ter as seguintes informações dadas pelo usuário: descrição e prioridade. Cada uma em uma linha.
    - A prioridade pode ser alta, média, ou baixa. Representadas pelas letras a, m, ou b, respectivamente.
    - Cada tarefa criada também terá um status, que inicialmente será "pendente".
    - Ao ser criada, cada tarefa terá um número correspondente e sequencial que será utilizado para identificar a tarefa. A primeira tarefa cadastrada terá o número 1, a segunda 2, terceira 3, etc.
    - Exemplo para cadastrar uma tarefa de prioridade alta:
        - Usuário escolhe a opção 1.
        - Usuário insere a descrição da tarefa: Estudar
        - Usuário insere a prioridade da tarefa: a
    - Exemplo para cadastrar uma tarefa de prioridade média:
        - Usuário escolhe a opção 1.
        - Usuário insere a descrição da tarefa: Comer
        - Usuário insere a prioridade da tarefa: m
    - Outro exemplo para cadastrar uma tarefa de prioridade alta:
        - Usuário escolhe a opção 1.
        - Usuário insere a descrição da tarefa: Trabalho
        - Usuário insere a prioridade da tarefa: a
- A opção 2 irá permitir a listagem de todas as tarefas existentes. As tarefas exibidas devem estar ordenadas por prioridade.  Ou seja, primeiro devem ser exibidas as tarefas com prioridade a, depois m, depois b. Caso existam tarefas com a mesma prioridade, o segundo critério de ordenação deverá ser o código identificador das mesmas. Ou seja, se duas tarefas têm prioridade "m", e códigos identificadores 2 e 3, respectivamente, então primeiro deverá ser exibida a tarefa com código 2 e depois a tarefa com código 3.
    - As informações a serem exibidas sobre as tarefas são: número de identificação, descrição, prioridade (a, m ou b) e status (pendente ou pronta). Nessa ordem, uma por linha.
    - Exemplo:
        - Usuário escolhe a opção 2.
        - Programa imprime: 1
        - Programa imprime: Estudar
        - Programa imprime: a
        - Programa imprime: pendente
        - Programa imprime: 3
        - Programa imprime: Trabalho
        - Programa imprime: a
        - Programa imprime: pendente
        - Programa imprime: 2
        - Programa imprime: Comer
        - Programa imprime: m
        - Programa imprime: pendente
- A opção 3 irá permitir marcar uma tarefa como pronta.
    - Ao escolher a opção 3, o usuário deve informar qual é a tarefa a ser marcada como pronta, utilizando o identificador numérico da mesma.
    - Caso não exista uma tarefa com o código identificador informado, imprimir "Tarefa inexistente".
    - Exemplo:
        - Usuário escolhe a opção 3.
        - Usuário insere o identificador: 1
- A opção 4 irá permitir a listagem das tarefas cadastradas que estão com o status "pendente". As informações a serem exibidas sobre cada tarefa são as mesmas da opção 2. Além disso, a ordenação também deve ser a mesma que a opção 2.
    - Exemplo:
        - Usuário escolhe a opção 4.
        - Programa imprime: 3
        - Programa imprime: Trabalho
        - Programa imprime: a
        - Programa imprime: pendente
        - Programa imprime: 2
        - Programa imprime: Comer
        - Programa imprime: m
        - Programa imprime: pendente
- A opção 5 irá permitir a remoção de tarefas cadastradas. Para isso, o usuário deverá informar o código identificador da tarefa que deseja remover.
    - Caso não exista uma tarefa com o código identificador informado, imprimir "Tarefa inexistente".
    - A remoção de uma tarefa não deve afetar os identificadores numéricos sequenciais até o momento. Ou seja, se o usuário adicionou 4 tarefas até o momento e decidiu remover uma tarefa, a próxima tarefa cadastrada terá o código identificador 5.
    - Exemplo:
        - Usuário escolhe a opção 5.
        - Usuário insere o identificador: 2
- A opção 6 irá permitir modificar a prioridade de uma tarefa existente. Para isso, o usuário deverá informar o código identificador da tarefa e a nova prioridade.
    - Caso não exista uma tarefa com o código identificador informado, imprimir "Tarefa inexistente".
    - Exemplo:
        - Usuário escolhe a opção 6.
        - Usuário insere o identificador: 1
        - Usuário insere a nova prioridade: m
- Se uma opção inválida for escolhida, deve exibir a mensagem "Invalido".



# Exemplo

- Usuário escolhe a opção 1 (inserir tarefa).
- Usuário insere a descrição da tarefa: Estudar
- Usuário insere a prioridade da tarefa: a
- Usuário escolhe a opção 1 (inserir tarefa).
- Usuário insere a descrição da tarefa: Comer
- Usuário insere a prioridade da tarefa: m
- Usuário escolhe a opção 1 (inserir tarefa).
- Usuário insere a descrição da tarefa: Dormir
- Usuário insere a prioridade da tarefa: b
- Usuário escolhe a opção 1 (inserir tarefa).
- Usuário insere a descrição da tarefa: Trabalho
- Usuário insere a prioridade da tarefa: a
- Usuário escolhe a opção 2 (listar todas as tarefas).
- Programa imprime: 1
- Programa imprime: Estudar
- Programa imprime: a
- Programa imprime: pendente
- Programa imprime: 4
- Programa imprime: Trabalho
- Programa imprime: a
- Programa imprime: pendente
- Programa imprime: 2
- Programa imprime: Comer
- Programa imprime: m
- Programa imprime: pendente
- Programa imprime: 3
- Programa imprime: Dormir
- Programa imprime: b
- Programa imprime: pendente
- Usuário escolhe a opção 3 (marcar tarefa como pronta).
- Usuário insere o identificador: 1
- Usuário escolhe a opção 4 (listar tarefas pendentes).
- Programa imprime: 4
- Programa imprime: Trabalho
- Programa imprime: a
- Programa imprime: pendente
- Programa imprime: 2
- Programa imprime: Comer
- Programa imprime: m
- Programa imprime: pendente
- Programa imprime: 3
- Programa imprime: Dormir
- Programa imprime: b
- Programa imprime: pendente
- Usuário escolhe a opção 5 (remover tarefa).
- Usuário insere o identificador: 2
- Usuario escolhe a opção 2 (listar todas as tarefas).
- Programa imprime: 1
- Programa imprime: Estudar
- Programa imprime: a
- Programa imprime: pronta
- Programa imprime: 4
- Programa imprime: Trabalho
- Programa imprime: a
- Programa imprime: pendente
- Programa imprime: 3
- Programa imprime: Dormir
- Programa imprime: b
- Programa imprime: pendente
- Usuário escolhe a opção 6 (modificar prioridade de uma tarefa).
- Usuário insere o identificador: 3
- Usuário insere a nova prioridade: m
- Usuario escolhe a opção 4 (listar tarefas pendentes).
- Programa imprime: 4
- Programa imprime: Trabalho
- Programa imprime: a
- Programa imprime: pendente
- Programa imprime: 3
- Programa imprime: Dormir
- Programa imprime: m
- Programa imprime: pendente
- Usuário escolhe a opção -1 (sair).
- Programa termina
