#-------------------------------------------------------------------------------
# Name:        Lista 02 - Questão 02
# Author:      Amanda Carvalho
# Receba uma lista de números inteiros e imprima o produto dos números
# ímpares e a soma dos números pares
#-------------------------------------------------------------------------------

# 1) Definir as variáveis: número, soma, produto. O produto deve iniciar com 1
# porque qualquer número vezes zero é igual a zero
# 2) Definir a condição para encerrar o loop: quando for digitado -1
# 3) Inserir os operadores lógicos: primeiro, deve-se ignorar o -1. Se o resto
# da divisão por 2 for 0, o número é par e será somado. Senão, será multiplicado
# 4) Imprimir a soma e o produto dos números.

num = 0
soma = 0
produto = 1

while num != -1:
    num = int(input("Digite um número: "))
    if num != -1:
     if num % 2 == 0:
        soma = soma + num
     else:
        produto = produto * num
print (f"A soma dos números pares é {soma}, o produto dos números ímpares é {produto}")