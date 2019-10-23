#-------------------------------------------------------------------------------
# Name:        Lista 02 - Questão 03
# Author:      Amanda Carvalho
# Receba um inteiro n como entrada e imprima os n números de Fibonacci.
#-------------------------------------------------------------------------------

# 1) Na sequência de Fibonacci, o número seguinte é a soma dos dois anteriores:
# 0 + 1 = 1, 1 + 1 = 2, 2 + 1 = 3... portanto, n1 + n2 = próximo número. Após
# realizar essa soma, o n2 passa a ser o primeiro número, e o novo valor, resul-
# tado da soma, torna-se o segundo número. Esses valores serão somados novamente,
# gerando a sequência.
# 2) Definir as variáveis n, n1 e n2
# 3) Definir o loop com o for, no qual o termo que será impresso para formar a
# sequência de fibonacci é o n2.

n = int(input("Digite um número: "))

n1 = 0
n2 = 1

for x in range (1, n+1):

    print(n2)

    proximo = n1 + n2
    n1 = n2
    n2 = proximo


