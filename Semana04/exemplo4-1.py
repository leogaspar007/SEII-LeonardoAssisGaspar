#!/usr/bin/python3

val1 = int(input("- Digite um número inteiro:"))
val2 = int(input("- Digite outro número inteiro:"))

maior =[]
menor =[]

if val1 > val2:
    maior = val1
    menor = val2
else:
    maior = val2
    menor = val1

print('\nValores digitados: Maior: ', maior, 'Menor: ', menor)

mmc = 0

for k in range(1, maior+1):
    aux = k * menor
    if (aux % maior) ==0:
        mmc = aux

print('\n\n>> MMC: ', mmc)