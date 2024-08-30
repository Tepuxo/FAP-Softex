#Exerc´ıcio 003: Ler as idades de 2 homens e de 2 mulheres (considere que as idades dos homens
#ser˜ao sempre diferentes entre si, bem como as das mulheres). Calcule e escreva a soma das
#idades do homem mais velho com a mulher mais nova, e o produto das idades do homem mais
#novo com a mulher mais velha.

num1 = int(input('Informe a idade do primeiro homem: '))
num2 = num1
while num1 == num2:
    num2 = int(input('Informe a idade do segundo homem: '))

num3 = int(input('Informe a idade da primeira mulher: '))
num4 = num3
while num3 == num4:
    num4 = int(input('Informe a idade da segunda mulher: '))

resul1 = num1 + num4
resul2 = num2 * num3

print(f'A soma da idade do homem mais velho {num1} com a mulher mais nova {num4}é: {resul1}')
print(f'O produto da idade do homem mais novo {num2} com a mulher mais velha {num3}é: {resul2}')