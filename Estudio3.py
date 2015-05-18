import pygame, Buttons, sys, time
from pygame.locals import *

if not pygame.font: print ('Advertencia, error de fuentes')
if not pygame.mixer: print ('Advertencia, error de sonido')

pygame.mixer.pre_init(44100, -16, 2, 2048)
#Initialize pygame
pygame.init()
pygame.mouse.set_visible(1)

class Button_Example:
    def __init__(self):
        self.main()
    
    #Create a display
    def display(self):
        self.screen = pygame.display.set_mode((800,480))
        pygame.display.set_caption("Estudio de respuestas")
        #Intro
        if pygame.font:
            font = pygame.font.Font(None, 36)
            text = font.render("Bievenido(a) al estudio. Gracias por su colaboracion", 1, (255, 255, 255))
            textpos = text.get_rect()
            textpos.center = (400, 45)
            self.screen.blit(text, textpos)

            font2 = pygame.font.Font(None, 22)
            introd = font2.render("A continuacion se le presentara una lista de palabras", 1, (255, 255, 255))
            introdpos = introd.get_rect()
            introdpos.center = (400, 120)
            self.screen.blit(introd, introdpos)

            introd1 = font2.render("a la izquierda y derecha de la pantalla junto con una imagen o sonido.", 1, (255, 255, 255))
            introdpos1 = introd1.get_rect()
            introdpos1.center = (400, 135)
            self.screen.blit(introd1, introdpos1)

            introd2 = font2.render("Usted debera presionar la tecla de direccion izquierda o derecha, segun", 1, (255, 255, 255))
            introdpos2 = introd2.get_rect()
            introdpos2.center = (400, 150)
            self.screen.blit(introd2, introdpos2)

            introd3 = font2.render("usted crea que la palabra represente mejor a esa imagen o sonido.", 1, (255, 255, 255))
            introdpos3 = introd3.get_rect()
            introdpos3.center = (400, 165)
            self.screen.blit(introd3, introdpos3)

            introd4 = font2.render("Para comenzar con el estudio, haga click en el boton SIGUIENTE.", 1, (255, 255, 255))
            introdpos4 = introd4.get_rect()
            introdpos4.center = (400, 270)
            self.screen.blit(introd4, introdpos4)

    #Update the display and show the button
    def update_display(self, presscheck):
        #Parameters:               surface,      color,       x,   y,   length, height, width,    text,      text_color
        if presscheck == True:
            self.Button1.create_button(self.screen, (255,255,255), 350, 300, 100,    50,    0,        "SIGUIENTE", (0,0,0))
        pygame.display.flip()

    #Question1
    """def pregunta1(self):
        print "entra al loop pregunta 1"
        font3 = pygame.font.Font(None, 22)
        
        izqA1 = font3.render("Palabra IZQ A1", 1, (255, 255, 255))
        izqposA1 = izqA1.get_rect()
        izqposA1.center = (300, 50)
        self.screen.blit(izqA1, izqposA1)

        derA1 = font3.render("Palabra DER A1", 1, (255, 255, 255))
        derposA1 = derA1.get_rect()
        derposA1.center = (500, 50)
        self.screen.blit(derA1, derposA1)

        izqA2 = font3.render("Palabra IZQ A2", 1, (255, 255, 255))
        izqposA2 = izqA2.get_rect()
        izqposA2.center = (300, 70)
        self.screen.blit(izqA2, izqposA2)

        derA2 = font3.render("Palabra DER A2", 1, (255, 255, 255))
        derposA2 = derA2.get_rect()
        derposA2.center = (500, 70)
        self.screen.blit(derA2, derposA2)
        
        print "termina creacion de elementos de pantalla P1"


    #Question2
    def pregunta2(self):
        self.borrar()
        print "entra al loop pregunta 2"
        font3 = pygame.font.Font(None, 22)
        
        izqB1 = font3.render("Palabra IZQ B1", 1, (255, 255, 255))
        izqposB1 = izqB1.get_rect()
        izqposB1.center = (300, 50)
        self.screen.blit(izqB1, izqposB1)

        derB1 = font3.render("Palabra DER B1", 1, (255, 255, 255))
        derposB1 = derB1.get_rect()
        derposB1.center = (500, 50)
        self.screen.blit(derB1, derposB1)

        izqB2 = font3.render("Palabra IZQ B2", 1, (255, 255, 255))
        izqposB2 = izqB2.get_rect()
        izqposB2.center = (300, 70)
        self.screen.blit(izqB2, izqposB2)

        derB2 = font3.render("Palabra DER B2", 1, (255, 255, 255))
        derposB2 = derB2.get_rect()
        derposB2.center = (500, 70)
        self.screen.blit(derB2, derposB2)

        print "termina creacion de elementos de pantalla P2"

        
    #Question3
    def pregunta3(self):
        self.borrar()
        print "entra al loop pregunta 3"
        font3 = pygame.font.Font(None, 22)
        
        izqC1 = font3.render("Palabra IZQ C1", 1, (255, 255, 255))
        izqposC1 = izqC1.get_rect()
        izqposC1.center = (300, 50)
        self.screen.blit(izqC1, izqposC1)

        derC1 = font3.render("Palabra DER C1", 1, (255, 255, 255))
        derposC1 = derC1.get_rect()
        derposC1.center = (500, 50)
        self.screen.blit(derC1, derposC1)

        izqC2 = font3.render("Palabra IZQ C2", 1, (255, 255, 255))
        izqposC2 = izqC2.get_rect()
        izqposC2.center = (300, 70)
        self.screen.blit(izqC2, izqposC2)

        derC2 = font3.render("Palabra DER C2", 1, (255, 255, 255))
        derposC2 = derC2.get_rect()
        derposC2.center = (500, 70)
        self.screen.blit(derC2, derposC2)

        print "termina creacion de elementos de pantalla P3""""
                
    #Delete current screen
    def borrar(self):
        background = pygame.Surface(self.screen.get_size())
        background = background.convert()
        background.fill((0, 0, 0))
        self.screen.blit(background, [0,0])
        pygame.display.flip()
        
    """def sigpreg(self, current):
        if(current == 2):
            self.pregunta2()
        elif(current == 3):
            self.pregunta3()
        else:
            print "fin del ciclo""""

    #Creates a new screen and overwrites the previous, then starts asking
    def encuestar(self):
        self.borrar()
        #self.pregunta1()
	Estimulo = [["agradable", "victima", "desagradable", "excombatiente", "Ejemplo1", "left"],
["agradable", "victima", "desagradable", "excombatiente", "Ejemplo2", "right"],
["agradable", "victima", "desagradable", "excombatiente", "Ejemplo3", "left"]]
	font3 = pygame.font.Font(None, 22)
	for left1, left2, right1, right2, stim, ans in Estimulo:
		izq1 = font3.render(left1, 1, (255, 255, 255))
		izqpos1 = izq1.get_rect()
		izqpos1.center = (300, 50)
		self.screen.blit(izq1, izqpos1)

		der1 = font3.render(right1, 1, (255, 255, 255))
		derpos1 = der1.get_rect()
		derpos1.center = (500, 50)
		self.screen.blit(der1, derpos1)

		izq2 = font3.render(left2, 1, (255, 255, 255))
		izqpos2 = izq2.get_rect()
		izqpos2.center = (300, 70)
		self.screen.blit(izq2, izqpos2)

		der2 = font3.render(right2, 1, (255, 255, 255))
		derpos2 = der2.get_rect()
		derpos2.center = (500, 70)
		self.screen.blit(der2, derpos2)
		
		mid = font3.render(stim, 1, (255, 255, 255))
		midpos = mid.get_rect()
		midpos.center = (400, 350)
		self.screen.blit(mid, midpos)
	
		

    #Run the loop
    def main(self):
        self.Button1 = Buttons.Button()
        self.display()
        pressed = True
        currentquestion = 0
        while True:
            self.update_display(pressed)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == MOUSEBUTTONDOWN:
                    if self.Button1.pressed(pygame.mouse.get_pos()):
                        pressed = False
                        self.encuestar()
                        currentquestion += 1
                        print "Give me a command!"
                elif event.type == KEYDOWN:
                    """font3 = pygame.font.Font(None, 22)
		    
                    if event.key == K_LEFT and currentquestion == 1:
                        print "tecla izq pregunta 1"
                        print "Incorrecto"
                        wrong1 = font3.render("Incorrecto", 1, (255, 255, 255))
                        wrongpos1 = wrong1.get_rect()
                        wrongpos1.center = (400, 300)
                        self.screen.blit(wrong1, wrongpos1)
                        currentquestion += 1
                        pygame.event.clear(KEYDOWN)
                        self.sigpreg(currentquestion)
                    if event.key == K_RIGHT and currentquestion == 1:
                        print "tecla der pregunta 1"
                        print "Correcto"
                        correct1 = font3.render("Correcto", 1, (255, 255, 255))
                        correctpos1 = correct1.get_rect()
                        correctpos1.center = (400, 300)
                        self.screen.blit(correct1, correctpos1)
                        currentquestion += 1
                        pygame.event.clear(KEYDOWN)
                        self.sigpreg(currentquestion)
                    if event.key == K_LEFT and currentquestion == 2:
                        print "tecla izq pregunta 2"
                        print "Correcto"
                        wrong1 = font3.render("Correcto", 1, (255, 255, 255))
                        wrongpos1 = wrong1.get_rect()
                        wrongpos1.center = (400, 300)
                        self.screen.blit(wrong1, wrongpos1)
                        currentquestion += 1
                        pygame.event.clear(KEYDOWN)
                        self.sigpreg(currentquestion)
                    if event.key == K_RIGHT and currentquestion == 2:
                        print "tecla der pregunta 2"
                        print "Incorrecto"
                        correct1 = font3.render("Incorrecto", 1, (255, 255, 255))
                        correctpos1 = correct1.get_rect()
                        correctpos1.center = (400, 300)
                        self.screen.blit(correct1, correctpos1)
                        currentquestion += 1
                        pygame.event.clear(KEYDOWN)
                        self.sigpreg(currentquestion)
                    if event.key == K_LEFT and currentquestion == 3:
                        pygame.event.clear(KEYDOWN)
                        print "tecla izq pregunta 3"
                        print "Correcto"
                        wrong1 = font3.render("Correcto", 1, (255, 255, 255))
                        wrongpos1 = wrong1.get_rect()
                        wrongpos1.center = (400, 300)
                        self.screen.blit(wrong1, wrongpos1)
                        currentquestion += 1
                        self.sigpreg(currentquestion)
                    if event.key == K_RIGHT and currentquestion == 3:
                        pygame.event.clear(KEYDOWN)
                        print "tecla der pregunta 3"
                        print "Incorrecto"
                        correct1 = font3.render("Incorrecto", 1, (255, 255, 255))
                        correctpos1 = correct1.get_rect()
                        correctpos1.center = (400, 300)
                        self.screen.blit(correct1, correctpos1)
                        currentquestion += 1
                        self.sigpreg(currentquestion)"""

if __name__ == '__main__':
    obj = Button_Example()
