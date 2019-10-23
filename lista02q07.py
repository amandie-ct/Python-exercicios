2#-------------------------------------------------------------------------------
# Name:        Lista 02 - Questão 07
# Author:      Amanda Carvalho
# Receba um número e imprima se ele é primo ou não.
#-------------------------------------------------------------------------------

# 1) Um número primo é divisível apenas por 1 e ele mesmo. É possível encontrar
# um número primo calculando sua quantidade de divisores, com o operador %.
# 2) Definir as variáveis: número que será recebido (num), intervalo de números
# pelos quais o número será dividido (intervalo) e quantidade de divisores,
# iniciando por zero (divisores)
# 3) Se o resto da divisão do número pelo intervalo for zero, a quantidade de
# divisores aumenta em 1. Intervalo recebe mais um pra dar continuidade ao loop
# 4) Se a quantidade de divisores encontrados for 2, imprimir que o número
# é primo. Senão, não é primo.

num = int(input("Digite um número: "))
intervalo = 1
divisores = 0

while num != -1 and intervalo < num:
    if num % intervalo == 0:
        divisores += 1
    intervalo += 1
if divisores <= 2:
    print(f"O número {num} é primo.")
else:
    print (f"O número {num} não é primo.")


