"""1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência."""

num = int(input("Digite um número: "))
n1, n2 = 0, 1
while n1 < num:
    n1, n2 = n2, n1 + n2

if n1 == num:
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} NÂO pertence à sequência de Fibonacci.")