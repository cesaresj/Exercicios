#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e
#somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda
#função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

numeros = []
from random import randint
def sorteia():
    for i in range(5):
        numeros.append(randint(1,1000))
    print (numeros)
    return numeros

def somaPar():
    cont=0
    for i in numeros:
        if(i%2==0):
            cont=i+cont
    print(cont)
    return cont

sorteia()
somaPar()




