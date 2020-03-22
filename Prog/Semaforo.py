import time

#Parametros:
#semaforo [vermelho, amarelo, verde]
#[1] Vermelho = 5 segundos
#[2] Amarelo = 2 segundos
#[3] Verde = 3 segundos

#Estado inicial:
sem1 = {'Vermelho': 0, 'Amarelo': 0, 'Verde': 1}
sem2 = {'Vermelho': 1, 'Amarelo': 0, 'Verde': 0}

tempos = [5,2,3]

#Funcao para retornar o estado atual do semaforo
def estadoAtual(obj):
    for cor, valor in obj.items():
        if valor == 1:
            return cor

def trocaVermelhoVerde(obj):
    obj['Vermelho'] = 0
    obj['Verde'] = 1

def trocaAmareloVermelho(obj):
    obj['Amarelo'] = 0
    obj['Vermelho'] = 1

def trocaVerdeAmarelo(obj):
    obj['Verde'] = 0
    obj['Amarelo'] = 1

#Funcao para escrever o estado atual dos semaforos
def saida():
    print ('+---------------------------+')
    print ('|SEMAFORO 01: {0}'.format(estadoAtual(sem1)))
    print ('|SEMAFORO 02: {0}'.format(estadoAtual(sem2)))
    print ('+---------------------------+')

while (True):

    saida()
    
    time.sleep(tempos[2])
    trocaVerdeAmarelo(sem1)
    saida()
    
    time.sleep(tempos[1])
    trocaAmareloVermelho(sem1)
    trocaVermelhoVerde(sem2)
    saida()
    
    time.sleep(tempos[2])
    trocaVerdeAmarelo(sem2)
    saida()
    
    time.sleep(tempos[1])
    trocaAmareloVermelho(sem2)
    trocaVermelhoVerde(sem1)
