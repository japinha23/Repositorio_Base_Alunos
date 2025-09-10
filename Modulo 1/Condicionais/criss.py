# = dividindo o peso de uma pessoa (em quilogramas) pela sua altura (em metros) ao quadrado

#nessa parte ficam as variaveis, e aonde a pessoa vai digitar os dados dela, q isso acontece com o input

nome = input('Nome do paciente: ')
peso = float(input('Peso do paciente: '))
altura = float(input('Altura do paciente'))

IMC = peso / (altura * altura)
#o if, o elif e o else vao separar o imc por condiçoes 
if IMC >= 40:
    print (f'{nome} tem IMC igual a  {IMC} , classificado como Obesidade grau 3')
elif IMC >= 35:
    print (f'{nome} tem IMC igual a  {IMC} , classificado como Obesidade grau 2')
elif IMC >= 30:
    print (f'{nome} tem IMC igual a  {IMC} , classificado como Obesidade grau 1')
elif IMC >= 25:
    print (f'{nome} tem IMC igual a  {IMC} , classificado como Sobrepeso')
elif IMC >= 18.5:
    print (f'{nome} tem IMC igual a  {IMC} , classificado como Peso normal')
else:
    print (f'{nome} tem IMC igual a  {IMC} , classificado como Abaixo do peso')
