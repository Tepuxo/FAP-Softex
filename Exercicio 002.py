#Exercıcio 002: Ler 2 valores e se o segundo valor informado for ZERO, deve ser lido um novo
#valor, ou seja, para o segundo valor n˜ao pode ser aceito o valor zero e imprimir o resultado da
#divis˜ao do primeiro valor lido pelo segundo valor lido. (utilizar a estrutura REPETIR)

num1 = int(input('Informe o primeiro valor: '))
num2 = int(0)
while num2 == 0:
    num2 = int(input('Informe o segundo valor: '))
resultado = num1/num2
print(f'O resultado de {num1} dividido por {num2} é {resultado}')
