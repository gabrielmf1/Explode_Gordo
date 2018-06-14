# -*- coding: utf-8 -*-
"""
Created on Fri May 11 08:04:56 2018

@author: Gabriel Miras
"""

import pygame
#import random, os.path
from pygame.locals import *
from random import randrange
from random import randint
import random
#pygame.mouse.get_focused(False)
black = (0,0,0)

myDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Exploda o Gordo")

clock = pygame.time.Clock()
gordinhoexplode = True
background_position = [0, 0]

background_image = pygame.image.load("Restaurante2.jpg").convert()



def Tempo(t):
    font = pygame.font.SysFont(None, 50)
    text = font.render(str(t), True, black)
    myDisplay.blit(text,(20,20))

def reestar():
    font = pygame.font.SysFont(None, 70)
    text = font.render('Aperte espaço para reiniciar!', True, black)
    myDisplay.blit(text,(60,300))



class Gordinho(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.niveldegordura = 0

        self.listagordo = []

        for i in range(1,4):
            gordo_atual =  pygame.image.load("gordo" + str(i) + ".png")
            gordo_atual = pygame.transform.scale(gordo_atual, (150, 225))
            self.listagordo.append(gordo_atual)

        self.image = self.listagordo[0]
        self.rect  = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.explodindo = False
        self.frame = 3

        for i in range(1,25):
            explosion_frame =  pygame.image.load("e7fdd30386fe41b0e4318114a0f8f3af-" + str(i) +".png")
            self.listagordo.append(explosion_frame)

    def next(self):

        if self.niveldegordura == 0:
            self.image = self.listagordo[0]


        elif self.niveldegordura > 5 and self.niveldegordura <= 10:
            self.image = self.listagordo[1]


        elif self.niveldegordura <= 20 and self.niveldegordura > 15:
            self.image = self.listagordo[2]


        elif self.niveldegordura == 29:
            self.explodindo = True

            self.image = self.listagordo[self.frame]
            if self.frame <= 24:
                self.frame += 1


    def move(self, pixels):
        self.rect.x += pixels
        
#    def stop(self):
#        if 




class ComidaSaudavel(pygame.sprite.Sprite):
    def __init__(self, arquivo_imagem, pos_x, pos_y, vel_y, max_y):
        pygame.sprite.Sprite.__init__(self)
        self.vy = vel_y
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.max_y = max_y

    def move(self):
        self.rect.y += self.vy
        return self.rect.y <= self.max_y


class ComidaGorda(pygame.sprite.Sprite):
    def __init__(self, arquivo_imagem, pos_x, pos_y, vel_y, max_y):
        pygame.sprite.Sprite.__init__(self)
        self.vy = vel_y
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.max_y = max_y

    def move(self):
        self.rect.y += self.vy
        return self.rect.y <= self.max_y

pygame.init()

gordinho = Gordinho(300, 375)
gordinho_group = pygame.sprite.Group()
gordinho_group.add(gordinho)

comidasaudavel_group = pygame.sprite.Group()
comidagorda_group = pygame.sprite.Group()

myDisplay.fill(black)
myfont = pygame.font.SysFont("monospace", 16)
nivel_de_gordura_texto = myfont.render("Nível de Gordura = " +str(gordinho.niveldegordura), 1, (0,0,0))
#nivel_de_diabetes_texto = myfont.render("Nível de Diabétes = " +str(gordinho.niveldediabetes), 1, (0,0,0))


alimentos_saudaveis = ["abacaxi", "brocolis"]
alimentos_gordos = ['hamburger',' milkshake']

#def sorteialimentosbons(listaalibons):
#
alimentosSaudaveis = []
alimentosGordo = []
menu = True
while menu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                gordinhoexplode = False
                menu = False
            if event.key == pygame.K_ESCAPE:
                menu = False

    myDisplay.fill(black)
    pygame.display.update()
    tempo0 = pygame.time.get_ticks()


while not gordinhoexplode:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gordinhoexplode = True
            menu = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gordinhoexplode = True

    myDisplay.blit(background_image, background_position)

    clock.tick(60)
#    if pygame.sprite.spritecollide(gordinho, comidasaudavel_group, True):
#        if gordinho.niveldegordura >= 0:
#            gordinho.niveldegordura -= 1
#
#    if pygame.sprite.spritecollide(gordinho, comidagorda_group, True):
#        gordinho.niveldegordura += 1
    
    
    if pygame.sprite.spritecollide(gordinho, comidasaudavel_group, True):
        if gordinho.niveldegordura >= 0:
            nivel_de_gordura_texto = myfont.render("Nível de Gordura = " +str(gordinho.niveldegordura - 1), 1, (0,0,0))
            gordinho.niveldegordura -= 1

    if pygame.sprite.spritecollide(gordinho, comidagorda_group, True):
        gordinho.niveldegordura += 1
        nivel_de_gordura_texto = myfont.render("Nível de Gordura = " +str(gordinho.niveldegordura + 1), 1, (0,0,0))

#    if pygame.sprite.spritecollide(gordinho, comidasaudavel_group, True):
#        if gordinho.niveldegordura >= 0:
#            nivel_de_gordura_texto = myfont.render("Nível de Gordura = " +str(gordinho.niveldegordura - 1), 1, (0,0,0))
#            gordinho.niveldegordura -= 1
#
#    if pygame.sprite.spritecollide(gordinho, comidagorda_group, True):
#        gordinho.niveldegordura += 1
#        nivel_de_gordura_texto = myfont.render("Nível de Gordura = " +str(gordinho.niveldegordura + 1), 1, (0,0,0))
#      
#    
    #timer para cair alimento de tempos em tempos
    #dentro do timer, criar um objeto aleatorio(saudavel, gordo) atraves da funçao
    #como? aleatorizar pngs e os objetos
    #mata o objeto
    if not gordinho.explodindo:
        if random.random() < 0.02:
            print("Um alimento está prestes a cair.")
            novo_alimento = random.choice(alimentos_saudaveis)
            if novo_alimento == 'abacaxi':
                arquivo = "AbacaxiFinal.png"
            else:
                arquivo = "BrocolisFinal.png"
            comida = ComidaSaudavel(arquivo, randrange(0, 780), 0, 4, 600)
            comidasaudavel_group.add(comida)
            alimentosSaudaveis.append(comida)
        if random.random() < 0.02:
            novo_alimento = random.choice(alimentos_gordos)
            if novo_alimento == 'hamburger':
                arquivo = "HamburguerFinal.png"
            else:
                arquivo = "MilkshakeFinal.png"
            comida = ComidaGorda(arquivo, randrange(0, 780), 0, 4, 600)
            comidagorda_group.add(comida)
            alimentosGordo.append(comida)


        for each in alimentosSaudaveis:
            if not each.move():
                comidasaudavel_group.remove(each)
                alimentosSaudaveis.remove(each)

        for each in alimentosGordo:
            if not each.move():
                comidagorda_group.remove(each)
                alimentosGordo.remove(each)




    #    novo_alimento.move()
        background_image = pygame.image.load("Restaurante2.jpg").convert()
        pressed_keys = pygame.key.get_pressed() #pega teclas pressionadas
#        if gordinho.rect.x = 0 or gordinho.rect.x = 800:
#            gordinho.stop()
            
        if pressed_keys[pygame.K_LEFT]:
            gordinho.move(-20)
            background_image = pygame.image.load("Restaurante2.jpg").convert()
        elif pressed_keys[pygame.K_RIGHT]:
            gordinho.move(+20)
            background_image = pygame.image.load("Restaurante2.jpg").convert()

    if not gordinho.explodindo:
        segundos = int((pygame.time.get_ticks()-tempo0)/1000)

    if gordinho.explodindo:
        reestar()
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            tempo0 = pygame.time.get_ticks()
            gordinho.explodindo = False
            gordinho.niveldegordura = 0
            gordinho.frame = 0
            for comida in comidasaudavel_group:
                comidasaudavel_group.remove(comida)
            for comida in comidagorda_group:
                comidagorda_group.remove(comida)


    gordinho.next()
    Tempo(segundos)

    gordinho_group.draw(background_image)
    comidasaudavel_group.draw(background_image)
    comidagorda_group.draw(background_image)
    myDisplay.blit(nivel_de_gordura_texto, (570, 10))
    pygame.display.update()

#    novo_alimento.draw(background_image)

print(gordinho.niveldegordura)
pygame.quit()
