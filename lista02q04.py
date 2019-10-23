#-------------------------------------------------------------------------------
# Name:        Lista 02 - Questão 04
# Author:      Amanda Carvalho
# Imprima o 5º número maior do que 100 que é divisível por 3 e 7 ao mesmo tempo.
#-------------------------------------------------------------------------------

# 1) Definir uma variável para armazenar a quantidade de números divisíveis por
# 3 e 7 ao mesmo tempo, e uma variável para armazenar o valor inicial (100)
# 2) Lógica com while - enquanto múltiplos for diferente de 5, se o número for
# divisível for 3 e 7, a variável múltiplos recebe + 1. Quando múltiplos atinge
# o valor 5, o loop termina e x é impresso com o valor encontrado.


multiplos = 0
x = 100

while multiplos != 5:
    x += 1
    if x % 3 == 0 and x % 7 == 0:
        multiplos += 1

print (f"O quinto número maior que 100 e divisível por 3 e 7 é {x}.")