print('calculo IMC:')
p = float(input('Dígite seu peso: '))
a = float(input('dígite sua altura: '))
imc = p / (a**2)
if imc < 18.5:
    print('Seu IMC é de {:.2f} e você está abaixo do peso!'.format(imc))
elif 18.5 < imc < 25:
    print('Seu IMC é de {:.2f} e você está no peso ideal!'.format(imc))
elif 25 < imc < 30:
    print('Seu IMC é de {:.2f} e você está com sobrepeso!'.format(imc))
elif 30 < imc < 40:
    print('Seu IMC é de {:.2f} e você está com obesidade!'.format(imc))
elif imc > 40:
    print('Seu IMC é de {:.2f} é você está com Obesidade mórbida!'.format(imc))