Enunciado
Faça um programa em Python que simule a análise de uma eleição. Ao iniciar o programa, o usuário deve informar o nome de cada candidato separado por vírgulas. Em seguida, o usuário deve informar qual operação ele deseja fazer, dentre as seguintes: (1) registrar votos de uma seção eleitoral, (2) listar o total de votos de cada seção eleitoral, (3) listar o total de votos recebidos por cada candidato, (4) listar os candidatos em ordem decrescente do número de votos recebidos, (5) indicar se terá segundo turno e (6) sair do programa. Ao final de qualquer operação entre 1 e 5 o programa deve aguardar a próxima operação. O programa só termina a execução quando o usuário escolher a operação 6.

Entrada:

Os nomes dos candidatos separados por vírgula. A partir desse momento, o sistema está pronto para o uso, e aguarda um número de 1 a 6 indicando a operação a ser realizada. Enquanto o número 6 não for escolhido, o sistema aguardará novas operações ao término das operações anteriores. A operação 1 tem como entrada as quantidades de votos de cada candidato, separadas por vírgula. A ordem deve ser a mesma usada para informar os nomes dos candidatos. As demais operações, de 2 a 6, não têm entrada de dados.

 

Saída:

As operações 2 a 5 apresentam as seguintes saídas:

- Operação 2: números inteiros, um por linha, indicando o total de votos de cada seção, na mesma ordem que as seções foram registradas via opção 1.
- Operação 3: números inteiros, um por linha, indicando o total de votos de cada candidato, na mesma ordem usada para informar os nomes dos candidatos.
- Operação 4: nomes dos candidatos, um por linha, em ordem decrescente do número de votos recebidos pelos candidatos.
- Operação 5: "Segundo turno." caso o candidato em 1o. lugar não some mais de 50% dos votos. "Sem segundo turno." caso contrário.

 

Exemplos:

Entrada:

Joao,Pedro,Paulo
1
30,20,10
1
10,50,40
2
6

 

Saida:

60
100

 

 

Entrada:

Joao,Pedro,Paulo
1
30,20,10
1
10,50,40
3
6

 

Saida:

40
70
50

 

Entrada:

Joao,Pedro,Paulo
1
30,20,10
1
10,50,40
4
5
6

 

Saida:

Pedro
Paulo
Joao
Segundo turno.

Dicas
Use os conceitos de subprogamação vistos na aula 11.

Exemplos de Entrada e Saída
Entrada	
Joao,Pedro,Paulo
1
30,20,10
1
10,50,40
2
6
Saída	
60
100
Entrada	
Joao,Pedro,Paulo
1
30,20,10
1
10,50,40
3
6
Saída	
40
70
50
Entrada	
Joao,Pedro,Paulo
1
30,20,10
1
10,50,40
4
5
6
Saída	
Pedro
Paulo
Joao
Segundo turno.
