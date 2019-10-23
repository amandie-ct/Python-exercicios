#-------------------------------------------------------------------------------
# Name:        Lista 02 - Questão 10
# Author:      Amanda Carvalho
# Após receber o primeiro elemento de uma PA e e sua razão, imprima todos os termos
#até o n-ésimo. O valor de n também deve ser informado.
#-------------------------------------------------------------------------------

# 1) O enésimo termo é igual ao termo inicial somado ao total de termos menos um,
# vezes a razão da progressão. Ou seja, an = a1 + (n - 1) * r
# 2) Receber o termo inicial, a razão e o total de termos através do input, e
# depois calcular o enésimo termo através da fórmula da P.A.
# 3) Para imprimir os termos, criar um loop com o for.

inicial = int(input("Digite o termo inicial: "))
razao = int(input("Digite a razão de crescimento da progressão: "))
total_termos = int(input("Digite o termo limite: "))
an = inicial + (total_termos - 1) * razao

for x in range (inicial, an + 1, razao):
    print (x)

print(f"O enésimo termo é {an}.")
