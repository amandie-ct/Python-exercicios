#-------------------------------------------------------------------------------
# Name:        Lista 02 - Questão 01
# Author:      Amanda Carvalho
# Receba uma lista de números inteiros e imprima o menor e o maior deles.
#-------------------------------------------------------------------------------

# 1) Definir onde serão armazenados os valores: variáveis menor, maior e num
# 2) Definir o limite do loop através do comando while, no caso, o valor -1
# 3) Se o número digitado for maior que o valor armazenado na variável maior,
# maior recebe o novo valor. Se o número digitado for inferior ao valor da
# variável menor, menor recebe o novo valor
# 4) Imprimir os valores menor e maior

menor = 1000000
maior = 0
num = 0

while num != -1:
    num = int(input("Digite um número: "))
    if num > maior:
        maior = num
    if num < menor and num != -1:
        menor = num
print(f"O menor número é {menor}. O maior número é {maior}.")