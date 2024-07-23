# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
n = int(input('Digite um valor:'))
#a = n - 1
#s = n + 1
#print(f'Analisando o valor {n}, seu antecessor é {a} e o sucessor é {s}') primeira forma
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, (n-1), (n+1)))
"""def teste(x):
    nome = 'lucas'
    resultado = f'{nome}{x}'
    return resultado
qtd = 0
print(teste(qtd))
while qtd <= 100:
    resultado = teste(n)
    resultado = f'{resultado}-{qtd}'
    print(resultado)
    qtd += 1"""
