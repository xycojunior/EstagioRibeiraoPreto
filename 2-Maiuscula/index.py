"""Escreva um programa que verifique, em uma string, a existência da letra a, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre."""

texto = input("Digite uma palavra: ")

# Conta a ocorrência da letra 'a' (maiúscula e minúscula)
contagem_a = texto.lower().count('a')
if contagem_a > 0:
    print(f"A letra 'a' aparece {contagem_a} vez(es) em {texto}.")
else:
    print("A letra 'a' não aparece em {texto}.")