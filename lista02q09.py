#-------------------------------------------------------------------------------
# Name:        Lista 02 - Questão 09
# Author:      Amanda Carvalho
# Imprima uma tabela de equivalência entre cada grau Celsius e seu respectivo
# grau Fahrenheit. Os limites da tabela são de 0 a 100 ºC.
#-------------------------------------------------------------------------------

# 1) Definir variáveis Celsius e Fahrenheit
# 2) Imprimir o título da tabela
# 3) Usar o comando for para fazer o loop para os valores de 0-100 ºC e aplicar
# a fórmula de correspondência entre as variáveis
# 4) Imprimir os valores

celsius = 0
fahrenheit = 0

print ("ºC - ºF")

for celsius in range (0, 101):
    fahrenheit = (celsius * 9/5) + 32
    print(celsius, fahrenheit)