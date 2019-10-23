#-------------------------------------------------------------------------------
# Name:        Lista 02 - Questão 08
# Author:      Amanda Carvalho
# Receba um número qualquer e determine um par de números que multiplicado seja
# igual ao número
#-------------------------------------------------------------------------------

# 1) Definir a variável que vai receber o número (n)
# 2) Definir os intervalos com o for: o primeiro vai de 1 a n e o segundo vai de
# n a 1, invertido. Para isso, foi colocado o valor -1 depois da definição do
# intervalo em y
# 3) Se o produto de x e y resultar em n, imprimir os números.

n = int(input("Digite um número: "))

for x in range (1, n):
    for y in range (n, 1, -1):
        if x * y == n:
            print (f"{x} * {y} = {n}")