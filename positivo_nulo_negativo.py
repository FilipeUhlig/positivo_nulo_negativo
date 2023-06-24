"""
Programa: positivo_nulo_negativo
Descrição: Este programa verifica se um número é positivo, nulo ou negativo.
Data : 23/06/2023
Versão: 0.0.1
"""

#Atribuição de variáveis



x = 0

#Entrada de dados

x = float(input("Qual o número desejado? "))

#Processamento de dados

if x > 0:
    print(f"O número {x} é positivo.")

elif x < 0:
    print(f"O número {x} é negativo.")

else:
    print(f"O número {x} é nulo.")

#Saida de dadaos