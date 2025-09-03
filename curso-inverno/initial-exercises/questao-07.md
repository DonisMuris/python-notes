Enunciado
Faça um programa em Python que permita análises de autonomia de diferentes automóveis sob diferentes condições de transito (urbano e rodoviário). A autonomia indica quantos kilometros o carro é capaz de percorrer com um litro de combustível em uma determinada condição de trânsito. Para cada automóvel, são feitas três medições em cada uma das condições de trânsito. Ao iniciar o programa, o usuário pode escolher as seguintes opções: (1) cadastrar um novo automóvel, (2) exibir a autonomia média geral, (3) exibir a autonomia média considerando somente trânsito urbano, (4) listar os automóveis em ordem decrescente de autonomia média. Ao final de qualquer opção entre 1 e 4, o programa deve aguardar a próxima opção. O programa só termina a execução quando o usuário escolher a opção 5.

Entrada:

Ao iniciar, o sistema espera a entrada de um número de 1 a 5 indicando a opção escolhida pelo usuário. Enquanto o número 5 não for escolhido, o sistema aguardará novas opções ao término da execução da opção anterior. A única opção que tem entrada adicional é a 1. Ao escolher a opção 1, o usuário informa os seguintes dados separados por ponto e vírgula: o modelo do automóvel (string), três medidas da sua autonomia em trânsito urbano e três medidas da sua autonomia em transito rodoviário. Cada medida é um número real em km / litro. Por exemplo, um automóvel Golf com autonomias de 8.2, 10.1 e 9.3 km/l em transito urbano e 14.6, 12.5 e 13.4 km/l em transito rodoviário seria representado por uma linha contendo a seguinte informação: "Golf;8.2;10.1;9.3;14.6;12.5;13.4".

Saída:

As opções 2 a 4 apresentam as seguintes saídas:

- Opção 2: um número real que representa a autonomia média considerando todas as medições de todos os automóveis cadastrados em todas as condições de trânsito.

- Opção 3: um número real que representa a autonomia média considerando somente trânsito urbano.

- Opção 4: modelos dos automóveis, um por linha, ordenados decrescentemente pela autonomia média, considerando tanto trânsito urbano quanto rodoviário.



Todos os números reais de entrada e saída devem ter somente uma casa decimal.

Exemplos:

Entrada

1
Civic;8.0;10.0;9.0;13.5;12.0;13.5
1
Opala;4.5;4.0;6.5;10.0;9.0;8.0
1
Prius;15.0;14.0;18.0;17.0;22.0;21.0
2
5

 

Saida:

11.9

 

Entrada:

1
Civic;8.0;10.0;9.0;13.5;12.0;13.5
1
Opala;4.5;4.0;6.5;10.0;9.0;8.0
1
Prius;15.0;14.0;18.0;17.0;22.0;21.0
3
5

 

Saida:

9.9

 

Entrada:

1
Civic;8.0;10.0;9.0;13.5;12.0;13.5
1
Opala;4.5;4.0;6.5;10.0;9.0;8.0
1
Prius;15.0;14.0;18.0;17.0;22.0;21.0
4
5

 

Saida:

Prius
Civic
Opala

 

Dicas
Tente implementar seu próprio método de ordenação simples, como o bubble sort. Será útil para fixar os conceitos de listas e matrizes.

 

Como a plataforma usa uma versão um pouco antiga do Python, não é possível usar f-strings para formatar as strings. A formatação será necessária para escolher a quantidade de casas decimais a serem mostradas. Por conta disso, utilizem a função format() para fazer essa formatação. Exemplo:

valor = 35.28

print('{:.1f}'.format(valor))

 

No exemplo acima, será impresso 35.3 (uma casa decimal).

Exemplos de Entrada e Saída
Entrada	
1
Civic;8.0;10.0;9.0;13.5;12.0;13.5
1
Opala;4.5;4.0;6.5;10.0;9.0;8.0
1
Prius;15.0;14.0;18.0;17.0;22.0;21.0
2
5
Saída	
11.9
Entrada	
1
Civic;8.0;10.0;9.0;13.5;12.0;13.5
1
Opala;4.5;4.0;6.5;10.0;9.0;8.0
1
Prius;15.0;14.0;18.0;17.0;22.0;21.0
3
5
Saída	
9.9
Entrada	
1
Civic;8.0;10.0;9.0;13.5;12.0;13.5
1
Opala;4.5;4.0;6.5;10.0;9.0;8.0
1
Prius;15.0;14.0;18.0;17.0;22.0;21.0
4
5
Saída	
Prius
Civic
Opala
