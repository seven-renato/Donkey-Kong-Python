from graphics import *
from person import *
import time
from math import sin, cos, pi, sqrt
import pygame
pygame.init()

stomp_sound = pygame.mixer.Sound("./sounds/stomps.wav")
def urrar(win,num):
    if num == 1:
        dkInicio = Image(Point(300,343),"./assets/start/donkey2.png").draw(win)
        stomp_sound.play() # Som da pisada e batida no peito
        update(60)
    if num == 2:
        dkInicio = Image(Point(300,343),"./assets/start/donkey3.png").draw(win)
        stomp_sound.play()
        update(60)        
    return dkInicio

def verify_points_distance(p1, p2):
    return sqrt((p2.getX() - p1.getX()) ** 2 + (p2.getY() - p1.getY()) ** 2) # Pitágoras para achar a distância

def verify_colision_circles(circle, circle_2):
    centers_distance = verify_points_distance(circle.getCenter(), circle_2.getCenter())
    if centers_distance <= circle.getRadius() + circle_2.getRadius(): # Se a distância for <= a soma dos raios retorna True
        return True
    return False

    
def iniciar(win): # Animação de subindo a escada
    Rectangle(Point(-100,-100),Point(900,900)).draw(win).setFill("black")
    atual = Image(Point(300,343),f"./assets/start/frame-003.gif").draw(win)
    update(60)
    pygame.mixer.music.load("./sounds/animacaoinicial.wav")
    pygame.mixer.music.play() # Musica de subir escada
    for i in range(4,50):
        if i < 10 :
            atual.undraw()
            atual = Image(Point(300,343),f"./assets/start/frame-00{i}.gif").draw(win)
            update(60)
            time.sleep(0.1)
        else:
            atual.undraw()
            atual = Image(Point(300,343),f"./assets/start/frame-0{i}.gif").draw(win)
            update(60)
            time.sleep(0.1)
    for i in range(1,50):
        if i < 10 :
            atual.undraw()
            atual = Image(Point(300,343),f"./assets/start/frame-0{i}.gif").draw(win)
            update(60)
            time.sleep(0.1)
        else:
            atual.undraw()
            atual = Image(Point(300,343),f"./assets/start/frame-{i}.gif").draw(win)
            update(60)
            time.sleep(0.1)
    Image(Point(300,343),f"./assets/start/howhigh.png").draw(win) # Foto do nível
    pygame.mixer.music.load("./sounds/tuturururara.wav") # Musica da foto
    pygame.mixer.music.play()
    update(60)
    time.sleep(3.5)
testeDeMorte = False # Para ficar mais simples o ato de reiniciar o jogo quando morre
acabou = False
morreuMesmo = 0
while True:
    if acabou:
        break
    if not testeDeMorte: # Teste para a janel não abrir infinitas vezes, com base no numero de jogadas
        win = GraphWin("Donkey Kong",600,686, autoflush=False)
    testeDeMorte = False
    querJogar = False
    telaDeInicio = Image(Point(300,343),"./assets/start/start3.png").draw(win)
    marioInicio = Image(Point(130,535),"./assets/start/mariomartelo.png").draw(win)
    dkInicio = Image(Point(300,343),"./assets/start/donkey1.png")
    dkInicio.draw(win)
    ultimo = True
    cont = 0
    while True:
        if testeDeMorte:
            break
        tecla = win.checkKey()
        if cont % 300000 == 0 and cont != 0:
            dkInicio.undraw()
            x = urrar(win,1)
            update(24)
        if cont == 340000:
            x.undraw()
            x = urrar(win,2)
            update(24)
        if cont == 380000:
            x.undraw()
            update(24)
            try:
                dkInicio.draw(win)
            except:
                pass
            cont = 0
        if tecla == "Down":
            pygame.mixer.music.load("./sounds/bloop.wav")
            pygame.mixer.music.play()
            telaDeInicio.undraw()
            ultimo = False
            fechar = Image(Point(300,343),"./assets/start/start2.png").draw(win)
            marioInicio = Image(Point(170,600),"./assets/start/mariomartelo.png").draw(win)
            update(24)
            try:
                dkInicio = Image(Point(300,343),"./assets/start/donkey1.png").draw(win)
            except:
                pass
        if tecla == "Up":
            pygame.mixer.music.load("./sounds/bloop.wav") # Som de mover para cima ou para baixo
            pygame.mixer.music.play()
            try:
                fechar.undraw()
            except:
                pass
            telaDeInicio = Image(Point(300,343),"./assets/start/start3.png").draw(win)
            marioInicio = Image(Point(130,535),"./assets/start/mariomartelo.png").draw(win)
            try:
                dkInicio = Image(Point(300,343),"./assets/start/donkey1.png").draw(win)
            except:
                pass
            update(24)
            ultimo = True # Se tiver em exit = True, e novo jogo = fasle
        if ultimo and tecla == "Return": # Começa o jogo
            iniciar(win)
            cont2 = 0
            barril = BarrilAzul(115,198,win)
            cenario = Image(Point(300,343),"./assets/cenario.png")
            cenario.draw(win)
            frameRate = 1.0/60 # Taxa de quadros por segundos
            if morreuMesmo > -1:
                princesa = Princesa(255,128,win)
                p1 = Mario(6, 650, win, 25)
                Dk = Donkey(115,184,win)
            vet = []
            teste = False # Variável para fazer o inicio do Donkey Kong, para não precisar fazer mais de uma vez
            teste2 = False # Variável para fazer o inicio do Donkey Kong, para não precisar fazer mais de uma vez
            jogueiBarril = False
            cont = 0
            pygame.mixer.music.load("./sounds/musiquinhadefundo.wav")
            pygame.mixer.music.play(-1)
            while not win.isClosed():
                if verify_colision_circles(barril, p1) and cont < 150:
                    p1.morrer()
                start_time = time.time()
                if jogueiBarril:
                    for val in vet: # Para cada barril
                        val.getPosicao()
                        val.move()
                        if verify_colision_circles(val, p1) == True:
                            p1.morrer()
                            break
                    
                for val in vet:
                    if val.acabou == True: # Se chegou no final da tela
                        vet.pop(0)
                        val.undraw()
                        print("Foi",vet)
                p1.getPosicao() # Posição atual do mario na matriz
                p1.move() # Checkkey
                p1.gravidade() # Gravidade sempre atuando
                update(34) 
                if cont == 60 and teste == False:
                    Dk.inicia(1)
                    teste = True
                if cont == 100 and teste2 == False:
                    Dk.inicia(2)
                    print(cont)
                    teste2 = True
                if teste2:
                    barril.jogarBarrilAzul(cont, cont2)
                if cont % 120 == 0 and cont != 0: # Animação baseada no contador principal de jogar barril
                    Dk.jogarBarril(1)
                if cont % 140 == 0 and cont != 0:
                    Dk.jogarBarril(2)
                if cont % 160 == 0 and cont != 0:
                    Dk.jogarBarril(3)
                    NovoBarril = Barril(190,212,win)
                    vet.append(NovoBarril)
                    jogueiBarril = True 
                if cont % 180 == 0 and cont != 0:
                    Dk.jogarBarril(4) # Volta a foto normal do DK
                    cont = 0
                    cont2 = 1    
                if cont % 100 == 0 and cont != 0:
                    princesa.idle(True) # Animação da princesa
                if cont % 150 == 0 and cont != 0:
                    princesa.idle(False)
                if p1.ganhou:
                    sleep(2)
                    pygame.mixer.music.load("./sounds/musiquinhadefinalfeliz.wav")
                    pygame.mixer.music.play()
                    cenario = Image(Point(300,343),"./assets/teladefim.png").draw(win)
                    update(24)
                    win.getMouse()
                    win.close()

                if p1.die:
                    sleep(2)
                    cenario = Image(Point(300,343),"./assets/telademorte.png").draw(win)
                    update(24)
                    win.getMouse()
                    testeDeMorte = True
                    morreuMesmo += 1
                    break
                cont += 1
                end_time = time.time()
                frameTime = end_time - start_time
                if (frameTime) < (frameRate):
                    sleep((frameRate) - frameTime)
        elif ultimo == False and tecla == "Return":
            acabou = True
            break
        cont += 1
win.close()