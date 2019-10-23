#-------------------------------------------------------------------------------
# Name:        Lista 02 - Questão 06
# Author:      Amanda Carvalho
# Receba um número e imprima se ele é triangular. Um número é triangular quando
# é o resultado do produto de três números consecutivos.
#-------------------------------------------------------------------------------

# 1) Um número triangular = a * b * c, onde a < b < c. Podemos dizer que a = x,
# b = x + 1 e c = x + 2
# 2) Criar um input para receber o número a testar se é triangular
# 3) Criar um loop com o while para verificar se números consecutivos multipli-
# cados serão equivalentes ao número digitado no input. Se essa condição for
# satisfeita, imprimir que o número é triangular.

num = int(input("Digite um número: "))
x = 1
triangular = 0

while triangular < num:
    triangular = x * (x + 1) * (x + 2)
    x += 1

if triangular == num:
    print (f"O número {num} é triangular.")
else:
    print(f"O número {num} não é triangular.")
