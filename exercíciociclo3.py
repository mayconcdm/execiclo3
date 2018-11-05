peso = float(input('Digite seu peso (KG): '))
altura = float(input('Qual sua altura em (M): '))
imc = peso  (altura ** 2)
print('Seu imc é de: {:.1f}'.format(imc))
if imc < 18.5:
    print('VOCÊ ESTÁ ABAIXO DO PESO!')
elif imc > 18.5 and imc <= 25:
    print('PARABÉNS, VOCÊ ESTÁ NA FAIXA DE PESO IDEAL!')
elif imc <= 30:
    print('VOCÊ ESTÁ COM SOBREPESO!')
elif imc <= 40:
    print('CUIDADO, VOCÊ ESTÁ COM OBESIDADE!')
else:
    print('VOCÊ ESTÁ COM OBESIDADE MORBITA')﻿