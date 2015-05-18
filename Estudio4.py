import pygame, Buttons, sys, time, os
from pygame.locals import *

if not pygame.font: print ('Advertencia, error de fuentes')
if not pygame.mixer: print ('Advertencia, error de sonido')

pygame.mixer.pre_init(44100, -16, 2, 2048)
#Initialize pygame
pygame.init()
pygame.mouse.set_visible(1)

try:
        # load graphic files from subfolder 'data'
        # ejemplo 1 background = pygame.image.load(os.path.join("data","wien.jpg"))
        # ejemplo 2 snake = pygame.image.load(os.path.join("data","snake.gif"))
        # ejemplo 3 bird = pygame.image.load(os.path.join("data","babytux.png"))
        
	# load sound files 
        sonido1 = pygame.mixer.Sound(os.path.join('data','bomb.wav'))
        #sonido2 = pygame.mixer.Sound(os.path.join('data', 'spring.wav'))
	#sonido3 = pygame.mixer.Sound(os.path.join('data', ''))
  
except:
        raise UserWarning, "Unable to find or play the files in the folder 'data' :-( "




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

                
    #Delete current screen
    def borrar(self):
        background = pygame.Surface(self.screen.get_size())
        background = background.convert()
        background.fill((0, 0, 0))
        self.screen.blit(background, [0,0])
        pygame.display.flip()
        

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

		pygame.display.flip()
		time0 = pygame.time.get_ticks()
		print "Inicio: %d" % time0
		if stim == "Ejemplo1":
			sonido1.play()
		
		answer = []	
		answer.append(self.responder(time0))
		print answer
		if answer == ans:
			print "correcto"
		else:
			print "incorrecto"
		self.borrar()
		
		
    def responder(self, tiempo):
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			elif event.type == KEYDOWN:
				if event.key == K_LSHIFT:
					time1 = pygame.time.get_ticks()
					print "Fin %d" % time1
					print "shift izquierdo"
					timeFinal = time1 - tiempo
					print timeFinal	
					return "left", timeFinal
				elif event.key == K_RSHIFT:
					time1 = pygame.time.get_ticks()
					print "Fin %d" % time1
					print "shift derecho"
					timeFinal = time1 - tiempo
					print timeFinal
					return "right", timeFinal
					
	

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


if __name__ == '__main__':
    obj = Button_Example()
