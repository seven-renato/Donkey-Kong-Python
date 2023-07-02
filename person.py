from graphics import *
from time import *
import random
import pygame
pygame.init()
class Mario:
    def __init__(self, x, y, win, raio):
        self.x = x
        self.y = y
        self.win = win
        self.contEntradaGravidade = 0
        self.Mario = Image(Point(x, y), "./assets/mario/mario_rwalk0.png")
        self.Mario.draw(win)
        self.velocidadeY = 0
        self.raio = 6
        self.numPulos = 0
        self.lado = False
        self.contR = 0
        self.contL = 0
        self.cont = 0
        self.desceu = False
        self.escada_menor = False
        self.die = False
        self.ganhou = False
        self.caiuAndar = False
        self.testeDeLevel = 0
        self.numeroDeMovidasEmY = 0
        self.alturasubida = 0
        self.moveuEmY = False
        self.subiuPelo5 = False
        self.desceuPelo5 = False
        self.timeAnterior = time()

    def move(self):
        timeAtual = time()
        if timeAtual - self.timeAnterior > 0.7:
            podeSubir = True
        else:
            podeSubir = False
        print(podeSubir)
        center = self.Mario.getAnchor()
        tecla = self.win.checkKey()
        cont = 0
        cont2 = 0
        teste = False
        if self.moveuEmY:
            if self.alturasubida == 1:
                self.moverEmY(0, -65, self.estaSeMovendo)
            if self.alturasubida == 2:
                self.moverEmY(0, -85, self.estaSeMovendo)
            if self.alturasubida == 3:
                self.moverEmY(0, 65, self.estaSeMovendo)
            if self.alturasubida == 4:
                self.moverEmY(0, 85, self.estaSeMovendo)                
        if tecla == 'Right' and self.numPulos == 0 and not self.moveuEmY and podeSubir:            
            self.contR += 1 # Contador de passos para a direita
            self.Mario.undraw()# Desenha ele olhando para direita
            self.Mario = Image(self.Mario.getAnchor(
            ), "./assets/mario/mario_rwalk0.png").draw(self.win)            
            for val in self.vet: # Acha a posição na matriz
                # print(val)
                for element in val:
                    if element == 1:
                        if cont == len(self.vet[cont2])-1:
                            teste = False
                        else:
                            teste = True
                        break
                    cont += 1
                if teste:
                    break
                cont2 += 1
                cont = 0
            if teste: # Se não tiver no final da matriz o teste = True
                if self.vet[cont2+1][cont+1] in [3, 4]: # Verificar qual numero está embaixo do Mario
                    if self.level in [1]: # Verifica o nivel que o Mario está para andar corretamente
                        if self.contR % 2 == 0:
                            self.andar(10, -0.7)
                        else:
                            self.Mario.move(10, -0.7)
                        # print("Entrei aqui!")
                    if self.level in [2, 4, 6]:
                        if self.contR % 2 == 0:
                            self.andar(10, 0.7)
                        else:
                            self.Mario.move(10, 0.7)
                    if self.level in [3, 5]:
                        if self.contR % 2 == 0:
                            self.andar(10, -0.7)
                        else:
                            self.Mario.move(10, -0.7)
                elif self.vet[cont2+1][cont+1] == 8:
                    self.andar(30,0) # Para chegar no final da tela
                    self.caiuAndar = True
                    self.velocidadeY = 5 # Para conseguir mover-se até o proximo andar
                    self.cont = 0                    
                    self.posDescida = len(self.vet[0]) - 1
                    self.desceu = True
                    if self.level == 2:
                        self.testeDeLevel = 1 # Andar que está atualmente
                    elif self.level == 4:
                        self.testeDeLevel = 3
                    elif self.level == 6:
                        self.testeDeLevel = 5               
                else: # Se não, anda reto
                    # print(self.Mario.getAnchor())
                    if self.contR % 2 == 0:
                        self.andar(10, 0) 
                    else:
                        self.Mario.move(10, 0)
                self.vet[cont2][cont] -= 1
                self.vet[cont2][cont+1] += 1
                # #print(self.vet)
            cont = 0
            cont2 = 0
            teste = False
            self.lado = False
        if tecla == 'Left' and self.numPulos == 0 and not self.moveuEmY and podeSubir:
            self.contL += 1
            self.Mario.undraw()
            self.Mario = Image(center, "./assets/mario/mario_lwalk0.png")
            self.Mario.draw(self.win)            
            for val in self.vet:
                for element in val:
                    if element == 1:
                        if cont == 0:
                            teste = False
                        else:
                            teste = True
                        break
                    cont += 1
                if teste:
                    break
                cont2 += 1
                cont = 0
            if teste:
                if self.vet[cont2+1][cont-1] in [3, 4]:
                    if self.level in [1]:
                        if self.contL % 2 == 0:
                            self.andar(-10, 0.7)
                        else:
                            self.Mario.move(-10, 0.7)
                        # print("Entrei aqui!")
                    if self.level in [2, 4, 6]:
                        if self.contL % 2 == 0:
                            self.andar(-10, -0.7)
                        else:
                            self.Mario.move(-10, -0.7)
                    if self.level in [3, 5]:
                        if self.contL % 2 == 0:
                            self.andar(-10, 0.7)
                        else:
                            self.Mario.move(-10, 0.7)
                elif self.vet[cont2+1][cont-1] == 8:
                    self.andar(-30,0)
                    self.caiuAndar = True
                    self.velocidadeY = 5
                    self.cont = 0                    
                    self.posDescida = 0
                    self.desceu = True
                    if self.level == 3:
                        self.testeDeLevel = 2
                    elif self.level == 5:
                        self.testeDeLevel = 4
                elif self.vet[cont2+1][cont-1] == 9: # Para morrer se estiver do lado do DK
                    self.die = True
                    self.morrer()
                else:
                    # print(self.Mario.getAnchor())
                    if self.contL % 2 == 0:
                        self.andar(-10, 0)
                    else:
                        self.Mario.move(-10, 0)
                self.vet[cont2][cont] -= 1
                self.vet[cont2][cont-1] += 1
                # #print(self.vet)
            cont = 0
            cont2 = 0
            teste = False
            self.lado = True
        
        if tecla == "Up" and not self.moveuEmY and podeSubir:
            self.Mario.undraw()
            self.Mario = Image(center, "./assets/mario/mario_lwalk1.png")
            self.Mario.draw(self.win)
            update(60)
            for val in self.vet:
                for element in val:
                    if element == 1:
                        teste = True
                        break
                    cont += 1
                if teste:
                    break
                cont2 += 1
                cont = 0
            if teste and self.numPulos == 0: # Verificar se não está pulando, para não subir na escada enquanto pula
                self.estaSeMovendo = True
                if self.vet[cont2-1][cont] == 4: # Verifica valor em cima
                    self.timeAnterior = time()
                    self.moveuEmY = True
                    self.escada_menor = True
                    # self.Mario.move(0,-63)
                    self.alturasubida = 1
                    self.moverEmY(0, -65, self.moveuEmY)
                    self.posSubida = cont
                    # print(self.Mario.getAnchor())
                    self.cont = 0
                if self.vet[cont2-1][cont] == 5:
                    self.timeAnterior = time()
                    self.moveuEmY = True
                    self.escada_menor = False
                    # self.Mario.move(0,-83)
                    self.alturasubida = 2
                    if self.level == 4:
                        self.subiuPelo5 = True # Variável, para corrigir erro do nivel 4, que acabava por subir acima do eixo
                    self.moverEmY(0, -85, self.moveuEmY)
                    self.posSubida = cont
                    self.cont = 0
                    # print(self.Mario.getAnchor())                                
            cont = 0
            cont2 = 0
            teste = False
        if tecla == "Down" and not self.moveuEmY and podeSubir:
            self.Mario.undraw()
            self.Mario = Image(center, "./assets/mario/mario_lwalk1.png")
            self.Mario.draw(self.win)
            update(60)
            for val in self.vet:
                for element in val:
                    if element == 1:
                        teste = True
                        break
                    cont += 1
                if teste:
                    break
                cont2 += 1
                cont = 0
            if teste and self.numPulos == 0:
                self.estaSeMovendo = True
                if self.vet[cont2+1][cont] == 4:
                    self.timeAnterior = time()
                    self.moveuEmY = True
                    # self.Mario.move(0,+63)
                    self.moverEmY(0, 65, self.moveuEmY)
                    # print(self.Mario.getAnchor())
                    self.cont = 0
                    self.level -= 1
                    self.desceu = True
                    self.alturasubida = 3
                    self.posDescida = cont
                if self.vet[cont2+1][cont] == 5:
                    if self.level == 5:
                        print("falou"*1000)
                        self.desceuPelo5 = True
                    self.timeAnterior = time()
                    self.moveuEmY = True
                    # self.Mario.move(0,83)
                    self.moverEmY(0, 85, self.moveuEmY)
                    # print(self.Mario.getAnchor())
                    self.cont = 0
                    self.level -= 1
                    self.desceu = True
                    self.alturasubida = 4
                    self.posDescida = cont                
            cont = 0
            cont2 = 0
            teste = False
#Point(506.0, 571.0)
        if tecla == 'space':
            self.jump()

        if tecla == "k":
            self.morrer()

    def jump(self):
        center = self.Mario.getAnchor()
        vet = [Image(center, "./assets/mario/mario_ljump.png"),
               Image(center, "./assets/mario/mario_rjump.png")]
        if self.numPulos == 0: # Teste para ver se está pulando, para não pular mais de uma vez
            if self.lado: # Variável para saber o lado que está pulando
                self.Mario.undraw()
                self.Mario = vet[0]
                self.Mario.draw(self.win)
            else:
                self.Mario.undraw()
                self.Mario = vet[1]
                self.Mario.draw(self.win)
            self.velocidadeY = -3 # Acrescente velocidade em y Para que a def gravidade o mova           
            self.numPulos += 1

    def moverEmY(self, posx, posy, boolean):
        if boolean:
            self.numeroDeMovidasEmY += 1
            vet = [Image(self.Mario.getAnchor(), "./assets/mario/mario_ladder_left.png"), Image(self.Mario.getAnchor(), "./assets/mario/mario_ladder_right.png"),
                Image(self.Mario.getAnchor(), "./assets/mario/mario_back.png")]
            if self.numeroDeMovidasEmY == 1: # Numero de braçadas na escada
                self.Mario.undraw()
                self.Mario = vet[0].draw(self.win)
                update(60) 
            if self.numeroDeMovidasEmY == 2: 
                self.Mario.undraw()
                self.Mario = vet[1].draw(self.win)
                self.Mario.move(posx, posy/4)
                update(60)
            if self.numeroDeMovidasEmY == 3:
                self.Mario.undraw()
                self.Mario = vet[0].draw(self.win)
                self.Mario.move(posx, posy/4) # Se move, apenas 1/4 em y
                update(60)
            if self.numeroDeMovidasEmY == 4:
                self.Mario.undraw()
                self.Mario = vet[1].draw(self.win)
                self.Mario.move(posx, posy/4)
                update(60)
            if self.numeroDeMovidasEmY == 5: # Ultima braçada
                self.Mario.undraw()
                self.Mario = vet[0].draw(self.win)
                self.Mario.move(posx, posy/4)
                update(60)
                center = self.Mario.getAnchor()
                self.Mario.undraw()
                self.Mario = Image(center, "./assets/mario/mario_lwalk0.png") # Desenha ele parado apos subir toda a escada
                self.Mario.draw(self.win)
                update(60)
                self.moveuEmY = False # Quando dá a 5 braçada, a estado de estar se movendo em y acabou!
                self.numeroDeMovidasEmY = 0 # Numero de braçadas 0
                self.alturasubida = 0 # Altura que subir reinicia 
                self.estaSeMovendo = False 
            


    def andar(self, posx, posy):
        if self.lado:
            vet = [Image(self.Mario.getAnchor(), "./assets/mario/mario_lwalk1.png"),
                   Image(self.Mario.getAnchor(), "./assets/mario/mario_lwalk2.png")]
        else:
            vet = [Image(self.Mario.getAnchor(), "./assets/mario/mario_rwalk1.png"),
                   Image(self.Mario.getAnchor(), "./assets/mario/mario_rwalk2.png")]
        self.Mario.undraw()
        self.Mario = vet[0].draw(self.win)
        update(64)
        self.Mario.move(posx, posy)
        self.Mario.undraw()
        center = self.Mario.getAnchor()
        if self.lado:
            self.Mario = Image(center, "./assets/mario/mario_lwalk0.png").draw(self.win)
        else:
            self.Mario = Image(center, "./assets/mario/mario_rwalk0.png").draw(self.win)

    def morrer(self):
        pygame.mixer.music.load("./sounds/morreu.wav") # Musica de morte
        pygame.mixer.music.play()
        vet = [Image(self.Mario.getAnchor(), "./assets/mario/mario_die0.png"),
                Image(self.Mario.getAnchor(), "./assets/mario/mario_dieup.png"), Image(self.Mario.getAnchor(), "./assets/mario/mario_dieright.png")
                ,Image(self.Mario.getAnchor(), "./assets/mario/mario_diedown.png"),Image(self.Mario.getAnchor(), "./assets/mario/mario_dieleft.png"),Image(self.Mario.getAnchor(), "./assets/mario/mario_die1.png")]
        self.Mario.undraw()
        self.Mario = vet[0].draw(self.win)
        update(64)
        sleep(0.5)
        cont = 1    
        while True:
            if cont == 5:
                break                  
            self.Mario.undraw()
            self.Mario = vet[cont].draw(self.win)
            update(64)
            sleep(0.5)
            cont += 1            
        center = self.Mario.getAnchor()
        self.Mario.undraw()
        self.Mario = vet[cont].draw(self.win)
        self.die = True

    def getPosicao(self): # Saber a posição que está localizado dentro da matriz
        if not self.moveuEmY:
            center = self.Mario.getAnchor()
            posy = center.getY()
            if (posy + self.raio >= 620 or self.testeDeLevel == 1) and self.cont == 0:
                self.cont += 1
                self.level = 1
                self.testeDeLevel = 0
                # print("entrei1")
                if self.desceu:
                    self.vet = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2],
                                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]]
                    self.vet[1][0] -= 1
                    self.vet[1][self.posDescida] += 1
                    self.desceu = False
                else:
                    self.vet = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2],
                                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]]
            if (posy + self.raio < 591 and posy + self.raio > 500 or self.testeDeLevel == 2) and self.cont == 0:
                # print("entrei2")
                self.cont += 1
                self.level = 2
                self.testeDeLevel = 0
                self.vet = [[3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 3, 3, 3, 3, 8, 8, 8]]
                if self.desceu:
                    self.vet[1][self.posDescida] += 1
                    self.desceu = False
                else:
                    self.vet[1][self.posSubida] += 1
                    self.desceu = False
                self.testeDeLevel = 0
            if (posy + self.raio < 500 and posy + self.raio > 409 or self.testeDeLevel == 3) and self.cont == 0:
                # print("entrei3")
                self.cont += 1
                self.level = 3
                self.testeDeLevel = 0
                self.vet = [[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [8, 8, 8, 8, 3, 3, 3, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]]
                if self.desceu == False:
                    self.vet[1][self.posSubida] += 1
                    # print("Entrei pro 3 ")
                else:
                    self.vet[1][self.posDescida] += 1
                    self.desceu = False
                    # print("Desci pro 2 aa ")
            if (posy + self.raio < 409 and posy + self.raio > 318 or self.testeDeLevel == 4) and self.cont == 0:
                # print("entrei4")
                if self.desceuPelo5:
                    self.Mario.move(0,-8)
                    self.desceuPelo5 = False
                self.testeDeLevel = 0
                #self.Mario.move(0,-4)
                self.cont += 1
                self.level = 4
                self.vet = [[3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 3, 3, 3, 3, 8, 8, 8]]
                if self.desceu == False:
                    self.vet[1][self.posSubida] += 1
                else:
                    self.vet[1][self.posDescida] += 1
                    self.desceu = False

            if (posy + self.raio < 320 and self.raio + posy > 240 or self.testeDeLevel == 5) and self.cont == 0:
                # print("entrei5")
                if self.subiuPelo5:
                    self.Mario.move(0,8)
                    self.subiuPelo5 = False                
                self.cont += 1
                self.testeDeLevel = 0
                self.level = 5
                self.vet = [[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [8, 8, 8, 8, 3, 3, 3, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]]
                if self.desceu == False:
                    self.vet[1][self.posSubida] += 1
                else:
                    self.vet[1][self.posDescida] += 1
                    self.desceu = False
            if posy + self.raio < 240 and posy + self.raio > 160 and self.cont == 0:
                # print("entrei6")
                self.cont += 1
                self.testeDeLevel = 0
                self.level = 6
                self.vet = [[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 9, 9, 9, 9, 9, 9, 9, 9, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 3, 3, 3, 8, 8, 8]]
                self.vet[1][self.posSubida] += 1
            if posy + self.raio < 155 and self.cont == 0:
                # print("entrei7")
                self.Mario.move(0,10)
                self.cont += 1
                self.testeDeLevel = 0
                self.level = 7
                self.vet = [[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3]]
                self.vet[1][self.posSubida] += 1
                self.ganhou = True 

    def gravidade(self):        
        center = self.Mario.getAnchor()
        if self.velocidadeY < 2.9 and self.velocidadeY !=0 and self.numPulos != 0:
            # Como sempre estamos, chamando a gravidade(), sempre verificamos esse teste para ver se deve-se mover ou não em y
            self.velocidadeY += 0.1 # Como é -3, sempre vai movendo 0.1 + a velocidade y
            self.Mario.move(0, self.velocidadeY)
            self.contEntradaGravidade = 0
        elif self.caiuAndar and self.velocidadeY > 3.9:
            self.velocidadeY -= 0.1
            self.Mario.move(0, self.velocidadeY)
            self.contEntradaGravidade = 0
        else:
            self.contEntradaGravidade += 1 # Teste para ver se  entrou alguma vez já dentro da gravidade, para não entrar muitas vezes no mesmo if
            if self.contEntradaGravidade == 1:            
                self.velocidadeY = 0
                self.numPulos = 0
                self.caiuAndar = False
                # print(self.velocidadeY)
                if self.die:
                    pass
                elif self.lado:
                    self.Mario.undraw()
                    self.Mario = Image(center, "./assets/mario/mario_lwalk0.png")
                    self.Mario.draw(self.win)
                else:
                    self.Mario.undraw()
                    self.Mario = Image(center, "./assets/mario/mario_rwalk0.png")
                    self.Mario.draw(self.win)
    
    def undraw(self):
        self.Mario.undraw()
        pass

    def getCenter(self):
        return self.Mario.getAnchor()

    def getRadius(self):
        return 10

class Princesa:
    def __init__(self, x, y, win):
        self.x = x
        self.y = y
        self.win = win
        self.Princesa = Image(Point(x, y), "./assets/princesa/idle.png").draw(win)

    def idle(self, boolean):
        vet = [Image(self.Princesa.getAnchor(), "./assets/princesa/idle.png"), Image(self.Princesa.getAnchor(), "./assets/princesa/idle1.png"),
               Image(self.Princesa.getAnchor(), "./assets/princesa/help.png")]
        if boolean:
            try:
                self.Help.undraw()
            except:
                pass
            self.Help = Image(Point(self.x+50,self.y-20), "./assets/princesa/help.png").draw(self.win)
            self.Princesa.undraw()
            self.Princesa = vet[1].draw(self.win)
            update(64)
        else:
            self.Princesa.undraw()
            self.Princesa = Image(self.Princesa.getAnchor(), "./assets/princesa/idle.png").draw(self.win)
            self.Help.undraw()

class Donkey:
    def __init__(self,x,y,win):
        self.win = win
        self.Donkey = Image(Point(x,y),"./assets/donkey/donkey2.png").draw(win)
        self.Anchor = Point(x,y)
        self.cont = 0

    def inicia(self, valor): # Para jogar o barril azull
        if valor == 1:
            self.Donkey.undraw()
            self.Donkey = Image(self.Anchor,"./assets/donkey/donkey0.png").draw(self.win) 
            update(64)
        if valor == 2:
            self.Donkey.undraw()
            self.Donkey = Image(self.Anchor,"./assets/donkey/dkidle0.png").draw(self.win)
            update(64)

    def jogarBarril(self,valor):
        if valor == 1:
            self.Donkey.undraw()
            self.Donkey = Image(self.Anchor,"./assets/donkey/donkey2.png").draw(self.win) # ele olhando para esquerda
            update(60)
        if valor == 2:
            self.Donkey.undraw()
            self.Donkey = Image(self.Anchor,"./assets/donkey/donkey1.png").draw(self.win) # ele parado no meio
            update(60)
        if valor == 3:
            self.Donkey.undraw()
            self.Donkey = Image(self.Anchor,"./assets/donkey/donkey3.png").draw(self.win) # ele olhando para direita
            update(60)
        if valor == 4:
            self.Donkey.undraw()
            self.Donkey = Image(self.Anchor,"./assets/donkey/dkidle0.png").draw(self.win) # ele parado no meio
            update(60)
            

class Barril:
    def __init__(self,x,y,win):
        self.win = win
        self.Barril = Image(Point(x,y),"./assets/barril/barril.png").draw(win)
        self.Anchor = Point(x,y)
        self.level = 6
        self.raio = 10
        self.caiu = False
        self.cont = 0
        self.levelCaiu = 0
        self.acabou = False
        self.caiuescada4 = False
        self.caiuescada5 = False
        self.posDescida = 0
        self.controdadas = 1

    def getPosicao(self):
        if self.caiuescada4 and self.levelCaiu != 1:
            self.caiu = True
            self.level -= 1
            self.levelCaiu = 1
            self.cont = 0
            self.Barril.move(0,62)
        elif self.caiuescada5 and self.levelCaiu != 1:
            self.caiu = True
            self.level -= 1
            self.levelCaiu = 1
            self.cont = 0
            self.Barril.move(0,75)
        elif (self.Barril.getAnchor().getX() + self.raio > 580 or self.caiuescada4) and self.levelCaiu != 1:
            self.caiu = True
            self.level -= 1
            self.levelCaiu = 1
            self.cont = 0
            if self.level == 5:
                self.Barril.move(0,50)
            else:
                self.Barril.move(0,57)
            print("-------->",self.level)
        elif self.Barril.getAnchor().getX() + self.raio < 35 and self.levelCaiu != 1:
            if self.level != 1:
                self.caiu = True
                self.level -= 1
                self.levelCaiu = 1
                self.cont = 0
                self.Barril.move(0,57)
                print("-------->",self.level)
            else:
                self.acabou = True


        if self.Barril.getAnchor().getX() + self.raio < 600 and self.level == 6 and self.cont != 1:
            self.cont = 1 
            self.vet = [[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 9, 9, 9, 9, 9, 9, 9, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 8, 8, 8]]
            
        if (self.Barril.getAnchor().getX() + self.raio < 600 or self.caiuescada4 or self.caiuescada5) and self.level == 5 and self.cont != 1:
            self.caiu = False
            self.cont = 1 
            if self.caiuescada4:
                self.Barril.move(0,15)
            self.caiuescada5 = False
            self.caiuescada4 = False
            self.levelCaiu = 0
            self.vet = [[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [8, 8, 8, 8, 3, 3, 3, 3, 3, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]]
            self.vet[1][self.posDescida] += 1
            self.posDescida = 0
        if (self.Barril.getAnchor().getX() + self.raio < 40 or self.caiuescada4 or self.caiuescada5) and self.level == 4 and self.cont != 1:
            self.caiu = False
            if self.caiuescada4:
                self.posDescida += 10
            self.caiuescada4 = False
            self.caiuescada5 = False
            self.cont = 1 
            self.levelCaiu = 0
            self.vet = [[3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3]]
            self.vet[1][self.posDescida] += 1
            self.posDescida = 0
        if (self.Barril.getAnchor().getX() + self.raio < 600 or self.caiuescada4 or self.caiuescada5) and self.level == 3 and self.cont != 1:
            print("entrei")
            self.Barril.move(0,-3)
            self.caiu = False
            self.cont = 1
            self.caiuescada5 = False
            self.caiuescada4 = False
            self.levelCaiu = 0
            self.vet = [[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [8, 8, 8, 8, 3, 3, 3, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]]
            self.vet[1][self.posDescida] += 1
            self.posDescida = 0        
        if (self.Barril.getAnchor().getX() + self.raio < 40 or self.caiuescada4 or self.caiuescada5) and self.level == 2 and self.cont != 1:
            self.Barril.move(0,-5)
            self.caiu = False
            self.cont = 1 
            self.caiuescada4 = False
            self.caiuescada5 = False
            self.levelCaiu = 0
            self.vet = [[3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 3, 3, 3, 3, 8, 8, 8]]
            self.vet[1][self.posDescida] += 1
            self.posDescida = 0
        if (self.Barril.getAnchor().getX() + self.raio < 600 or self.caiuescada4 or self.caiuescada5) and self.level == 1 and self.cont != 1:
                print("entrei")
                self.Barril.move(0,-5)
                self.caiu = False
                self.cont = 1
                self.caiuescada5 = False
                self.caiuescada4 = False
                self.levelCaiu = 0
                self.vet = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]]
    def move(self):
        center = self.Barril.getAnchor()
        self.Barril.undraw()
        self.Barril = Image(center,f"./assets/barril/barrilrodando{self.controdadas}.png").draw(self.win)
        posicaoDoUm = self.vet[1].index(1)
        if self.controdadas == 4:
            self.controdadas = 1
        self.controdadas += 1
        if self.level == 6 and not self.caiu:
            if self.vet[2][posicaoDoUm] in [3]:
                self.Barril.move(10,0.7)    
            else:
                self.Barril.move(10,0)
            self.vet[1][posicaoDoUm] -= 1
            self.vet[1][posicaoDoUm+1] += 1
        if self.level == 5 and not self.caiu:
            if self.vet[2][posicaoDoUm] in [3,5]:
                self.Barril.move(-10,0.7)
            elif self.vet[2][posicaoDoUm] in [4]:
                nivel = random.randint(1,20)
                if nivel <= 10:
                    self.caiuescada4 = True
                    print("Cai no 4")
                else:
                    self.caiuescada4 = False
                    self.Barril.move(-10,0.7)            
            else:
                self.Barril.move(-10,0)
            self.vet[1][posicaoDoUm] -= 1
            self.vet[1][posicaoDoUm-1] += 1
        if self.level == 4 and not self.caiu:
            print(self.posDescida)
            if self.vet[2][posicaoDoUm] in [3]:
                self.Barril.move(10,0.7)
            elif self.vet[2][posicaoDoUm] in [4]:
                nivel = random.randint(1,40)
                if nivel <= 10:
                    self.caiuescada4 = True
                    print("Cai no 4")
                    self.Barril.move(0,5)
                else:
                    self.caiuescada4 = False
                    self.Barril.move(10,0.7)
            elif self.vet[2][posicaoDoUm+1] in [5]:
                nivel = random.randint(1,60)
                if nivel <= 10:
                    self.caiuescada5 = True
                    print("Cai no 5")
                    self.Barril.move(0,15)
                else:
                    self.caiuescada5 = False
                    self.Barril.move(10,0.7)
            else:
                self.Barril.move(10,0)
            self.vet[1][posicaoDoUm] -= 1
            try:
                self.vet[1][posicaoDoUm+1] += 1
            except:
                self.vet[1][posicaoDoUm-1] += 1
        if self.level == 3 and not self.caiu:
            if self.vet[2][posicaoDoUm-1] in [3]:
                self.Barril.move(-10,0.7)
            else:
                self.Barril.move(-10,0)
            self.vet[1][posicaoDoUm] -= 1
            self.vet[1][posicaoDoUm-1] += 1
        if self.level == 2 and not self.caiu:
            if self.vet[2][posicaoDoUm-1] in [3]:
                self.Barril.move(10,0.7)
            else:
                self.Barril.move(10,0)
            self.vet[1][posicaoDoUm] -= 1
            self.vet[1][posicaoDoUm-1] += 1
        if self.level == 1 and not self.caiu:
            if self.vet[2][posicaoDoUm-1] in [3]:
                self.Barril.move(-10,0.7)
            
            else:
                self.Barril.move(-10,0)
            self.vet[1][posicaoDoUm] -= 1
            self.vet[1][posicaoDoUm-1] += 1

    def undraw(self):
        self.Barril.undraw()

    def getCenter(self):
        return self.Barril.getAnchor()

    def getRadius(self):
        return 20
    
class BarrilAzul:
    def __init__(self,x,y,win):
        self.barril = Image(Point(x,y),"./assets/barril/barrilblue1.png")
        self.win = win
        self.contadorDeRodadas = 0

    def jogarBarrilAzul(self,num, numerodejogadas):
        vet =[Image(self.barril.getAnchor(),"./assets/barril/barrilazulrodando.png"),
          Image(self.barril.getAnchor(),"./assets/barril/barrilazulrodando2.png"),
          Image(self.barril.getAnchor(),"./assets/barril/barrilazulrodando3.png"),
          Image(self.barril.getAnchor(),"./assets/barril/barrilazulrodando4.png"),]
        stomp_sound = pygame.mixer.Sound("./sounds/stomps.wav")
        if numerodejogadas != 1:
            if num == 100:
                self.barril.draw(self.win)
            if num in [105,115]:
                self.barril.move(0,110)
                stomp_sound.play()
            if num in [110,120]:
                self.barril.move(0,68)
                stomp_sound.play()
            if num == 125:
                self.barril.move(0,100)
                stomp_sound.play()
            if num >= 130 and num <= 160:
                cont = 130 - num
                if self.contadorDeRodadas == 4:
                    self.contadorDeRodadas = 0
                self.barril.undraw()
                self.barril = vet[self.contadorDeRodadas].draw(self.win)
                update(100)
                self.barril.move(2*cont,0)
                self.contadorDeRodadas += 1
    def getCenter(self):
        return self.barril.getAnchor()

    def getRadius(self):
        return 20