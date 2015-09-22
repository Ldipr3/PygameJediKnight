############################################################################
###Trabalho de Programao 1                                             ###
###Nome: Lucas Dipr Pereira / Alvaro Rocha Jardim                       ###
###Data 19/11/2010                                                       ###   
###Prof: Hilário Seibel Junior                                           ### 
###Instituição: Ifes/Serra                                               ###
###Proposta: Desenvolver um jogo em python, usando a biblioteca pygame   ###
###com base em dois jogos dados exemplos ou criar um jogo a partir de    ###
###uma idéia original.                                                   ###
###                                                                      ###
###                                                                      ### 
############################################################################


# -*- coding: cp1252 -*-
import sys, pygame, os
pygame.init()

size = width, height = 800, 648
screen = pygame.display.set_mode(size)
pygame.mouse.set_visible(False)


class Sabre(pygame.sprite.Sprite):
# Classe Para o Sabre de Luz #
        def __init__(self, startpos, img):
                pygame.sprite.Sprite.__init__(self)
                self.image = img
                self.rect = self.image.get_rect()
                self.rect.centerx = startpos[0] 
                self.rect.centery = startpos[1]

# Função Update que verifica se o tiro colidiu com o Sabre de Luz #
        def update(self, b):
                if s.rect.colliderect(p):
                        if s.speed[1] > 0:
                                s.speed = [-s.speed[0], -s.speed[1]]

class Trooper(pygame.sprite.Sprite):
# Classe para o Objeto dos soldados que atiram # 

        def __init__(self, startpos, img):
                pygame.sprite.Sprite.__init__(self)
                self.image = img
                self.rect = self.image.get_rect()
                self.rect.centerx = startpos[0]
                self.rect.centery = startpos[1]
        
# Funo Update para verificar se o tiro refletido atinge o soldado, se sim ele morre #

        def update(self, l, b, kills):
                if t.rect.colliderect(s):
                        if t in Objetos: Objetos.remove(t)
                        if s in Objetos: Objetos.remove(s)
                        return kills + 1	
                else: return kills
		
                
class Tiro(pygame.sprite.Sprite):
# Classe para o Tiro que sai da arma do Soldado # 
        
        def __init__(self, startpos, img, spd):
                pygame.sprite.Sprite.__init__(self)
                self.image = img
                self.rect = self.image.get_rect()
                self.rect.centerx = startpos[0]
                self.rect.centery = startpos[1]
                self.speed = spd
                self.startpos = startpos
        
# Função Update para verificar se o jogador recebeu o tiro e que atualiza o medidor de HP #
        
        def update(self, Objetos, contador, r):
                self.rect.move_ip(self.speed)
                if self.rect.bottom > height:
                    if contador < 4:
                        Objetos[0] = r[contador+1]
                        Objetos.remove (self)
                        self.rect.centerx = self.startpos[0]
                        self.rect.centery = self.startpos[1]
                        return (contador + 1)
                    else: return (contador+1)
                else: return contador
                

class HP(pygame.sprite.Sprite):
# Classe para o medidor de HP # 
        
        def __init__(self, startpos, img):
                pygame.sprite.Sprite.__init__(self)
                self.image = img
                self.rect = self.image.get_rect()
                self.rect.centerx = startpos[0]
                self.rect.centery = startpos[1]



                          
# Declaração das imagens de cada objeto #
img1 = pygame.image.load('Images/Light_Saber_Central.gif')
img2 = pygame.image.load('Images/Light_Saber_Up_Right.gif')
img3 = pygame.image.load('Images/Light_Saber_Up_Left.gif')
img4 = pygame.image.load('Images/Trooper_1_1.gif')
img5 = pygame.image.load('Images/Trooper_2_1.gif')
img6 = pygame.image.load('Images/Trooper_3_1.gif')
img7 = pygame.image.load('Images/Trooper_4_1.gif')
img8 = pygame.image.load('Images/Tiro_Trooper_1_1.gif')
img9 = pygame.image.load('Images/Tiro_Trooper_2_1.gif')
img10 = pygame.image.load('Images/Tiro_Trooper_3_1.gif')
img11 = pygame.image.load('Images/Tiro_Trooper_4_1.gif')
img12 = pygame.image.load('Images/HP_Full.gif')
img13 = pygame.image.load('Images/HP_3_4.gif')
img14 = pygame.image.load('Images/HP_1_2.gif')
img15 = pygame.image.load('Images/HP_1_4.gif')
img16 = pygame.image.load('Images/HP_Empty.gif')

# Posições iniciais de cada objeto #
pos_inicial_Sabre = [width/2, height-120]
pos_inicial_Trooper1 = [50,380]
pos_inicial_Trooper2 = [750,380]
pos_inicial_Trooper3 = [320,450]
pos_inicial_Trooper4 = [550,420]
pos_inicial_Tiro1 = [105,390]
pos_inicial_Tiro2 = [695,390]
pos_inicial_Tiro3 = [374,480]
pos_inicial_Tiro4 = [495,455]
pos_inicial_HP = [60, 200]

# Criação do Objeto Sabre #
p = Sabre(pos_inicial_Sabre, img1)

t1 = Trooper(pos_inicial_Trooper1, img4)
t2 = Trooper(pos_inicial_Trooper2, img5)
t3 = Trooper(pos_inicial_Trooper3, img6)
t4 = Trooper(pos_inicial_Trooper4, img7)
# lista contendo os Soldaos #
l = [t1, t2, t3, t4]

# As velocidades de Cada Tiro #
spd_s1 = [10,10]
spd_s2 = [-10,10]
spd_s3 = [9,9]
spd_s4 = [-9,9]

# Criação dos Tiros #
s1 = Tiro(pos_inicial_Tiro1, img10, spd_s1)
s2 = Tiro(pos_inicial_Tiro2, img11, spd_s2)
s3 = Tiro(pos_inicial_Tiro3, img8, spd_s3)
s4 = Tiro(pos_inicial_Tiro4, img9, spd_s4)

# Lista contendo os Tiros #
b = [s1, s2, s3, s4]

# Criação de cada Objeto do Medidos de HP #
h1 = HP(pos_inicial_HP, img12)
h2 = HP(pos_inicial_HP, img13)
h3 = HP(pos_inicial_HP, img14)
h4 = HP(pos_inicial_HP, img15)
h5 = HP(pos_inicial_HP, img16)

# Lista contendo os objetos q compõem o medidor de HP #
r = [h1, h2, h3, h4, h5]

contador = 0
kills = 0

# Lista para os objetos a serem renderizados #
Objetos = [r[contador], p]

wallpaper = pygame.image.load('Images/Fundo.gif').convert()
Game_Over = pygame.image.load('Images/Game_Over.jpg').convert()
You_Win = pygame.image.load('Images/You_Win.jpg').convert()
MENU = pygame.image.load('Images/MENU.jpg').convert()
pygame.key.set_repeat(1,1)
pygame.display.set_caption('Jedi Knight') 
clock = pygame.time.Clock()
tempo = 0
# set up music
pygame.mixer.music.load('Sounds/sw-theme.wav')
pygame.mixer.music.play(-1, 0.0)
i = 0

# Primeiro Loop para o Menu #
while i == 0:

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        print 'Bye'
                        sys.exit()
		
                elif event.type == pygame.KEYDOWN:
			
                        if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                                print 'Bye'
                                sys.exit()
                        if event.key == pygame.K_i:
                                i = i + 1

        screen.blit(MENU, (0, 0))
        pygame.display.flip()


        

        

# Loop principal para o decorrer do jogo #
while True:

        clock.tick(120)
        
        tempo = (tempo + 1)%121

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        print 'Bye'
                        sys.exit()
		
                elif event.type == pygame.KEYDOWN:
			
                        if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                                print 'Bye'
                                sys.exit()
                        if event.key == pygame.K_a:
                                if p.rect.left >= 0:
                                        p.rect.move_ip([-10,0])
                        if event.key == pygame.K_d:
                                if p.rect.right <= width:
                                        p.rect.move_ip([10,0])
                        if event.key == pygame.K_RIGHT:
                                if p.rect.right <= width:
                                        p.image = img2
                        if event.key == pygame.K_LEFT:
                                if p.rect.left <= width:
                                        p.image = img3
                        if event.key == pygame.K_UP:
                                if p.rect.left <= width:
                                        p.image = img1


        
        if tempo == 120:

                soldado = l[0]
                tiro = b[0]
                Objetos.append(soldado)
                l.remove(soldado)
                l.append(soldado)
                Objetos.append(tiro)
                b.remove(tiro)
                b.append(tiro)

            
                        
        for s in b:
                
                if s in Objetos:
                        
                        contador = s.update(Objetos, contador, r)
                        p.update(b)

                        for t in l:
                                
                                if t in Objetos:
                                        
                                        kills = t.update(l, b, kills)
                                
                                kills = t.update(l, b, kills)
                        
        
                                
			
                                
                                
        screen.blit(wallpaper, (0, 0))
        for objeto in Objetos[::-1]: 
        	screen.blit(objeto.image, objeto.rect)

# Tela no caso de o Jogador vencer o Jogo #
        if kills >= 8:
                screen.blit(You_Win, (0,0))

# Tela no caso do Jogador morrer #
        if contador > 5:
                screen.blit(Game_Over, (0, 0))

        pygame.display.flip()
        
        	



