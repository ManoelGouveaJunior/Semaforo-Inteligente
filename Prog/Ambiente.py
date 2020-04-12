import os
import time
import numpy as np
from datetime import date
from random import randint as rand

class Q_Learning()
    def __init__:
        ACOES = [0,1,2] # 0 = Sem acao, 1 = Diminuir timer, 2 = Aumentar Timer
        TAM_ESPACO_OBS = [3,3]

        q_table = np.random.uniform (low=-1, high=0, size=(TAM_ESPACO_OBS + [len(ACOES)]))
        
class Semaforo():
    def __init__(self):

        self.estado = {'Verde': 1, 'Amarelo': 0, 'Vermelho': 0}

    def estadoAtual(self):
        for cor, valor in self.estado.items():
            if valor == 1:
                return cor

    def trocaVermelhoVerde(self):
        self.estado['Vermelho'] = 0
        self.estado['Verde'] = 1

    def trocaAmareloVermelho(self):
        self.estado['Amarelo'] = 0
        self.estado['Vermelho'] = 1

    def trocaVerdeAmarelo(self):
        self.estado['Verde'] = 0
        self.estado['Amarelo'] = 1

    def trocaVerdeVermelho(self):
        self.estado['Verde'] = 0
        self.estado['Vermelho'] = 1

class Ambiente():
    def __init__(self):
        #Objetos
        self.sem1 = Semaforo()
        self.sem2 = Semaforo()

        #sincronizar semaforos
        self.sem2.trocaVerdeVermelho()
                
        #Atributos
        self.fila1 = 0
        self.fila2 = 0
        self.saida1 = 0
        self.saida2 = 0
        self.estadoSem1 = self.sem1.estadoAtual()
        self.estadoSem2 = self.sem2.estadoAtual()
        self.percFila1 = 0.0
        self.percFila2 = 0.0

        #Timer Inicial
        self.timer = [1,1,1] # Verde = 3s / Amarelo = 2s / Vermelho = 5s -> Timer definido para 1s para testes.

        #Arquivo
        self.path = 'Teste' + '_' + str(date.today().strftime('%d%m%Y')) + '.csv'

        with open(self.path, 'w') as file:
            #Header
            file.write('Fila 1,Fila 2,Delta Fila 1,Delta Fila 1 (%),Delta Fila 2,Delta Fila 2 (%),Estado Semaforo 1,Estado Semaforo 2' + '\n')
            
            #Ja faz a gravacao dos dados iniciais
            file.write(str(self.fila1) + ',' + str(self.fila2) + ',' + str(self.saida1) + ',' + str(self.percFila1) + ',' + str(self.saida2) + ',' + str(self.percFila2) + ',' + self.estadoSem1 + ',' + self.estadoSem2 + '\n')

    def gravarDados(self):
        with open(self.path, 'a') as file:
            file.write(str(self.fila1) + ',' + str(self.fila2) + ',' + str(self.saida1) + ',' + str(self.percFila1) + ',' + str(self.saida2) + ',' + str(self.percFila2) + ',' + self.estadoSem1 + ',' + self.estadoSem2 + '\n')

    def setEstados (self):
        self.estadoSem1 = self.sem1.estadoAtual()
        self.estadoSem2 = self.sem2.estadoAtual()

    def gerarFila (self):

        if self.sem1.estadoAtual() == 'Vermelho':
            filaInicial = self.fila1
            self.saida1 = rand(0,10)
            self.fila1 = int(self.fila1) + self.saida1

            if filaInicial > 0:
                self.percFila1 = round(((self.fila1/filaInicial)-1)*100,2)
            elif filaInicial == 0 and self.fila1 > 0:
                self.percFila1 = 100.0
            else:
                self.percFila1 = 0.0
                
        elif self.sem2.estadoAtual() == 'Vermelho':
            filaInicial = self.fila2
            self.saida2 = rand(0,10)
            self.fila2 = int(self.fila2) + self.saida2

            if filaInicial > 0:
                self.percFila2 = round(((self.fila2/filaInicial)-1)*100,2)
            elif filaInicial == 0 and self.fila2 > 0:
                self.percFila2 = 100.0
            else:
                self.percFila2 = 0.0
            
    def diminuirFila (self):
        
        if self.sem1.estadoAtual() == 'Verde' and self.fila1 > 0:

            filaInicial = self.fila1
            
            if self.fila1 >= 10:
                self.saida1 = rand(0,10)
            else:
                self.saida1 = rand(0,self.fila1)

            self.fila1 = self.fila1 - self.saida1

            if filaInicial > 0:
                self.percFila1 = round(((self.fila1/filaInicial)-1)*100,2)
            elif filaInicial == 0 and self.fila1 > 0:
                self.percFila1 = 100.0
            else:
                self.percFila1 = 0.0

            self.saida1 = self.saida1 * (-1)

        elif self.sem2.estadoAtual() == 'Verde' and self.fila2 > 0:

            filaInicial = self.fila2

            if self.fila2 >= 10:
                self.saida2 = rand(0,10)
            else:
                self.saida2 = rand(0,self.fila2)

            self.fila2 = self.fila2 - self.saida2

            if filaInicial > 0:
                self.percFila2 = round(((self.fila2/filaInicial)-1)*100,2)
            elif filaInicial == 0 and self.fila2 > 0:
                self.percFila2 = 100.0
            else:
                self.percFila2 = 0.0

            self.saida2 = self.saida2 * (-1)
                
        if self.sem1.estadoAtual() == 'Amarelo' and self.fila1 > 0:

            filaInicial = self.fila1
            
            if self.fila1 >= 5:
                self.saida1 = rand(0,5)
            else:
                self.saida1 = rand(0,self.fila1)

            self.fila1 = self.fila1 - self.saida1

            if filaInicial > 0:
                self.percFila1 = round(((self.fila1/filaInicial)-1)*100,2)
            elif filaInicial == 0 and self.fila1 > 0:
                self.percFila1 = 100.0
            else:
                self.percFila1 = 0.0

            self.saida1 = self.saida1 * (-1)
            
        elif self.sem2.estadoAtual() == 'Amarelo' and self.fila2 > 0:

            filaInicial = self.fila2
            
            if self.fila2 >= 10:
                self.saida2 = rand(0,10)
            else:
                self.saida2 = rand(0,self.fila2)

            self.fila2 = self.fila2 - self.saida2

            if filaInicial > 0:
                self.percFila2 = round(((self.fila2/filaInicial)-1)*100,2)
            elif filaInicial == 0 and self.fila2 > 0:
                self.percFila2 = 100.0
            else:
                self.percFila2 = 0.0

            self.saida2 = self.saida2 * (-1)

    def ciclo (self):
        time.sleep (self.timer[0])
        self.gerarFila()
        self.diminuirFila()
        self.sem1.trocaVerdeAmarelo()
        self.setEstados()
        self.gravarDados()
        
        time.sleep (self.timer[1])
        self.gerarFila()
        self.diminuirFila()
        self.sem1.trocaAmareloVermelho()
        self.sem2.trocaVermelhoVerde()
        self.setEstados()
        self.gravarDados()

        time.sleep(self.timer[0])
        self.gerarFila()
        self.diminuirFila()
        self.sem2.trocaVerdeAmarelo()
        self.setEstados()
        self.gravarDados()

        time.sleep (self.timer[1])
        self.gerarFila()
        self.diminuirFila()
        self.sem2.trocaAmareloVermelho()
        self.sem1.trocaVermelhoVerde()
        self.setEstados()
        self.gravarDados()

    def formataArq (self):
        linhas = []
        
        with open(self.path, 'r') as file:
            for line in file.readlines():
                linhas.append(line.replace(',',';'))

        with open ('formatado.csv', 'w') as fil:
            fil.writelines(linhas)

#testes
env = Ambiente()
env.ciclo()
env.ciclo()
env.ciclo()
env.ciclo()
env.ciclo()
env.ciclo()
env.formataArq()

