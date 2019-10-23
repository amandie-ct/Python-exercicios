#-------------------------------------------------------------------------------
# Name: Lista 02 - Questão 05
# Author:      Amanda Carvalho
# Receba n números inteiros positivos e imprima a média deles.
#-------------------------------------------------------------------------------

# 1) Média é a soma dos números dividida pela quantidade de números. Portanto,
# media = soma / quantidade
# 2) Definir variáveis: soma, quantidade e input para receber os números
# 3) Usar operadores lógicos para ignorar o valor -1. Depois, definir a soma
# soma é a quantidade armazenada em soma + o número digitado. A quantidade é o
# valor armazenado em quantidade +1 a cada número digitado
# 4) Imprimir o cálculo da média.

soma = 0
quantidade = 0
num = 0

while num != -1:

    num = int(input("Digite o próximo número: "))
    if num != -1:
     soma = soma + num
     quantidade += 1

print (f"A média dos números inseridos é {soma/quantidade}")