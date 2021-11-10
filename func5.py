#Faça um programa que tenha uma função notas() que pode receber várias notas de aluno e vai
#retornar um dicionário com as seguintes informações:
#quantidade de notas, a maior nota, menor nota, media da turma

from random import randint
#import numpy
from typing import Union, Any

turma=[]

def notas():
    x = randint(1,50)
    cont=0
    for i in range(x):
        turma.append(randint(1,10))
        cont=i+cont
        med: Union[float, Any]=(cont/x)

    print('A quantidade de notas é {}'.format(x))
    print('A media da turma é {}'.format(med))
    return x,med

notas()