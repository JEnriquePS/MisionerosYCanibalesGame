# encoding: utf-8
import pygame
import sys
from pygame.locals import *

SIZE = ancho, alto = 800, 500

class Text:

    hovered = False

    def __init__(self, text, posicion, screen, font, thover=(100, 100, 100), fhover= (255, 255, 255)):
        self.text = text
        self.posicion = posicion
        self.screen = screen
        self.font = font
        self.thover = thover
        self.fhover = fhover
        self.set_rect()
        self.draw()

    def draw(self):
        self.set_rend()
        self.screen.blit(self.rend, self.rect)

    def set_rend(self):
        self.rend = self.font.render(self.text, True, self.get_color())

    def get_color(self):
        if self.hovered:
            return self.thover
        else:
            return self.fhover

    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.posicion


class Barco(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("myc/bote1.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = 245
        self.rect.centery = 430
        self.velocidad = 1

    def mover_derecha(self):
        self.rect.right += self.velocidad
        self.__movimiento()

    def mover_izquierda(self):
        self.rect.left -= self.velocidad
        self.__movimiento()

    def __movimiento(self):
        if self.rect.left <= 200:
            self.rect.left = 200
        elif self.rect.right > 640:
            self.rect.right = 640

    def dibujar(self, superficie):
        superficie.blit(self.image, self.rect)


class Boton(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("myc/home.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = 30
        self.rect.centery = 30

    def dibujar(self, superficie):
        superficie.blit(self.image, self.rect)


class Actor(pygame.sprite.Sprite):
    hovered = False

    def __init__(self, pos_ini, pos_fin, imagen, imagen_hover, personaje):
        self.x, self.y = pos_ini
        self.lx, self.ly = pos_fin
        self.image = pygame.image.load(imagen)
        self.rect = self.image.get_rect()
        self.imageHover = pygame.image.load(imagen_hover)
        self.rect = self.imageHover.get_rect()
        self.personaje = personaje
        self.rect.centerx, self.rect.centery = self.x, self.y
        self.velocidad_personaje_barco = 1
        self.velocidad = 2
        self.llevar_personaje = True
        self.dejar_personaje = False
        self.l_llevar_personaje = False
        self.l_dejar_personaje = True

    def mover_derecha(self):
        self.rect.right += self.velocidad
        self.__movimiento(subir=True)

    def mover_derecha_barco(self):
        self.rect.right += self.velocidad_personaje_barco
        self.__movimiento(barco=True)

    def mover_derecha_l(self):
        self.rect.right += self.velocidad
        self.__movimiento(bajar=True)

    def mover_izquierda(self):
        self.rect.left -= self.velocidad
        self.__movimiento(subir=True)

    def mover_izquierda_barco(self):
        self.rect.right -= self.velocidad_personaje_barco
        self.__movimiento(barco=True)

    def mover_izquierda_l(self):
        self.rect.left -= self.velocidad
        self.__movimiento(bajar=True)

    def __movimiento(self, subir=False, barco=False, bajar=False):
        if subir:
            if self.rect.centerx <= self.rect.centerx:
                self.rect.centerx = self.rect.centerx
            elif self.rect.right > 240:
                self.rect.right = 240
        elif barco:
            if self.rect.centerx <= self.rect.centerx:
                self.rect.centerx = self.rect.centerx
            elif self.rect.right > 650:
                self.rect.right = 650
        elif bajar:
            if self.rect.centerx <= self.rect.centerx:
                self.rect.centerx = self.rect.centerx
            elif self.rect.right > 600:
                self.rect.right = 600

    def mostrar_imagen(self):
        if self.hovered is True:
            return self.imageHover
        else:
            return self.image

    def dibujar(self, superficie):
        superficie.blit(self.mostrar_imagen(), self.rect)


def jugar():
    pygame.display.set_caption("misioneros y canibales")

    IMAGENFONDO = pygame.image.load("myc/night_sky.jpeg")
    PuertoInicio = pygame.image.load('myc/puerto_inicio.png')
    PuertoFinal = pygame.image.load('myc/puerto_final.png')
    OLAS = pygame.image.load('myc/olas.png')

    barco = Barco()
    boton = Boton()

    canibal_a = Actor((15, 400), (785, 400), "myc/canibal_.png", "myc/canibal_hover.png", "canibal")
    canibal_b = Actor((50, 400), (750, 400), "myc/canibal_.png", "myc/canibal_hover.png", "canibal")
    canibal_c = Actor((85, 400), (715, 400), "myc/canibal_.png", "myc/canibal_hover.png", "canibal")
    misionero_a = Actor((120, 400), (680, 400), "myc/cura.png", "myc/cura_hover.png", "misionero")
    misionero_b = Actor((155, 400), (645, 400), "myc/cura.png", "myc/cura_hover.png", "misionero")
    misionero_c = Actor((190, 400), (610, 400), "myc/cura.png", "myc/cura_hover.png", "misionero")

    actores_iniciales = [canibal_a, canibal_b, canibal_c, misionero_a, misionero_b, misionero_c]
    objetos_izquierda = []
    personajes_elegidos = []
    barco_adelante = False
    barco_atras = False
    personaje_seleccionado = None
    numero_pasajeros = 0

    while True:
        pygame.event.pump()
        screen.fill((0, 10, 100))
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if barco.rect.collidepoint(pygame.mouse.get_pos()):
                if evento.type == MOUSEBUTTONDOWN:
                    if barco_adelante is False:
                        barco_adelante = True
                    if barco.rect.right == 640:
                        if barco_atras is False:
                            barco_atras = True
            elif boton.rect.collidepoint(pygame.mouse.get_pos()):
                if evento.type == MOUSEBUTTONDOWN:
                    main()

            if barco.rect.right <= 342:
                for personaje in actores_iniciales:
                    if personaje.rect.collidepoint(pygame.mouse.get_pos()):
                        personaje.hovered = True
                        if evento.type == MOUSEBUTTONDOWN:
                            personaje_seleccionado = personaje
                            if personaje.llevar_personaje:
                                if numero_pasajeros < 2:
                                    personaje.dejar_personaje = True
                                    personajes_elegidos.append(personaje)
                                    actores_iniciales.remove(personaje)
                                    while personaje_seleccionado.rect.right < 300:
                                        personaje_seleccionado.mover_derecha()
                                    if pygame.sprite.collide_rect(personaje, personajes_elegidos[0]):
                                        while personaje_seleccionado.rect.right <= 301:
                                            personaje_seleccionado.rect.right = 249
                                            break
                                    numero_pasajeros += 1
                                    personaje.llevar_personaje = False
                    else:
                        personaje.hovered = False

            if numero_pasajeros == 2 or numero_pasajeros == 1:

                if barco_adelante is False and barco_atras is False:
                    for personaje in personajes_elegidos:
                        if personaje.rect.collidepoint(pygame.mouse.get_pos()):
                            personaje.hovered = True
                            if evento.type == MOUSEBUTTONDOWN:
                                personaje_seleccionado = personaje

                                if barco.rect.right < 640:
                                    if personaje.dejar_personaje:
                                        personaje.llevar_personaje = True
                                        actores_iniciales.append(personaje)
                                        personajes_elegidos.remove(personaje)
                                        while personaje_seleccionado.rect.centerx > personaje_seleccionado.x:
                                            personaje_seleccionado.mover_izquierda()
                                        numero_pasajeros -= 1
                                        personaje.dejar_personaje = False
                                if barco.rect.right == 640:
                                    if personaje.l_dejar_personaje:
                                        personaje.l_llevar_personaje = True
                                        objetos_izquierda.append(personaje)
                                        personajes_elegidos.remove(personaje)
                                        while personaje_seleccionado.rect.centerx < personaje_seleccionado.lx:
                                            personaje_seleccionado.mover_derecha_l()
                                        numero_pasajeros -= 1
                                        personaje.l_dejar_personaje = False
                        else:
                            personaje.hovered = False

            if barco.rect.right == 640:
                for personaje in objetos_izquierda:
                    if personaje.rect.collidepoint(pygame.mouse.get_pos()):
                        personaje.hovered = True
                        if evento.type == MOUSEBUTTONDOWN:
                            personaje_seleccionado = personaje
                            if personaje.l_llevar_personaje:
                                if numero_pasajeros < 2:
                                    personaje.l_dejar_personaje = True
                                    personajes_elegidos.append(personaje)
                                    objetos_izquierda.remove(personaje)
                                    while personaje_seleccionado.rect.right > 550:
                                        personaje_seleccionado.mover_izquierda_l()
                                    if pygame.sprite.collide_rect(personaje, personajes_elegidos[0]):
                                        while personaje_seleccionado.rect.right >= 549:
                                            personaje_seleccionado.rect.right = 600
                                            break
                                    numero_pasajeros += 1
                                    personaje.llevar_personaje = False
                    else:
                        personaje.hovered = False

        if len(personajes_elegidos) > 0:
            if barco_adelante is True:
                if barco.rect.right < 640:
                    barco.mover_derecha()
                    mover_actores(personajes_elegidos, direccion="derecha")
                    if barco.rect.left > 200:
                        num_actores_elegidos(actores_iniciales)
                else:
                    barco_adelante = False
                    num_actores(objetos_izquierda, personajes_elegidos)
            elif barco_atras is True:

                if barco.rect.left > 200:
                    barco.mover_izquierda()
                    mover_actores(personajes_elegidos, direccion="izquierda")
                    if barco.rect.right < 640:
                        num_actores_elegidos(objetos_izquierda)
                else:
                    barco_atras = False
                    num_actores(actores_iniciales, personajes_elegidos)
        else:
            barco_adelante = False
            barco_atras = False

        if len(objetos_izquierda) == 6:
            template_ganador()

        screen.blit(IMAGENFONDO, (0, 0))
        screen.blit(OLAS, (0, 375))
        mostrar_actores(personajes_elegidos)
        barco.dibujar(screen)
        boton.dibujar(screen)
        screen.blit(OLAS, (0, 400))
        screen.blit(PuertoInicio, (-10, 400))
        screen.blit(PuertoFinal, (565, 400))
        mostrar_actores(actores_iniciales)
        mostrar_actores(objetos_izquierda)
        pygame.display.update()


def mover_actores(personajes_elegidos, direccion):
    if direccion is "izquierda":
        if len(personajes_elegidos) == 2:
            personajes_elegidos[0].mover_izquierda_barco()
            personajes_elegidos[1].mover_izquierda_barco()
        if len(personajes_elegidos) == 1:
            personajes_elegidos[0].mover_izquierda_barco()
    elif direccion is "derecha":
        if len(personajes_elegidos) == 2:
            personajes_elegidos[0].mover_derecha_barco()
            personajes_elegidos[1].mover_derecha_barco()
        if len(personajes_elegidos) == 1:
            personajes_elegidos[0].mover_derecha_barco()


def num_actores_elegidos(personajes):
    canibales = 0
    misioneros = 0
    for personaje in personajes:
        if personaje.personaje == "canibal":
            canibales += 1
        elif personaje.personaje == "misionero":
            misioneros += 1
    if misioneros > 0 and canibales > 0:
        if misioneros < canibales:
            template_perdedor()


def num_actores(personajes, personajes_elegidos):
    canibales = 0
    misioneros = 0
    for personaje in personajes:
        if personaje.personaje == "canibal":
            canibales += 1
        elif personaje.personaje == "misionero":
            misioneros += 1
    for personaje in personajes_elegidos:
        if personaje.personaje == "canibal":
            canibales += 1
        elif personaje.personaje == "misionero":
            misioneros += 1
    if misioneros > 0 and canibales > 0:
        if misioneros < canibales:
            template_perdedor()


def mostrar_actores(actores):
        if actores:
            for actor in actores:
                actor.dibujar(screen)


def template_perdedor():
    opciones = [Text("Jugar de Nuevo", (260, 405), screen, font, (239, 111, 84), (239, 111, 66))]
    boton = Boton()
    IMAGENFONDO = pygame.image.load("myc/gameover-myc.png")
    opciones_elegidas = {"jugar de nuevo": jugar}
    lista_opciones(IMAGENFONDO, opciones, opciones_elegidas, boton)


def template_integrantes():
    opciones = [Text("Autor", (300, 50), screen, font, (75, 60, 234), (60, 19, 137)),
                Text(u"Peña Siguas Jesus", (100, 110), screen, font, (75, 60, 234), (75, 60, 234)),
                Text("jenrique.ps@gmail.com", (100, 170), screen, font, (75, 60, 234), (75, 60, 234)),
                Text("https://github.com/JEnriquePS/MisionerosYCanibalesGame", (0, 230), screen, font_small, (75, 60, 234), (75, 60, 234))]

    IMAGENFONDO = pygame.image.load("myc/forest.jpg")
    boton = Boton()
    opciones_elegidas = []
    lista_opciones(IMAGENFONDO, opciones, opciones_elegidas, boton)


def template_ganador():
    opciones = [Text("Ganaste", (270, 250), screen, font, (255, 206, 54), (255, 159, 29))]
    boton = Boton()
    IMAGENFONDO = pygame.image.load("myc/forest.jpg")
    opciones_elegidas = {'Jugar de nuevo': jugar}
    lista_opciones(IMAGENFONDO, opciones, opciones_elegidas, boton)


def main():
    opciones = [Text("Jugar", (300, 105), screen, font, (60, 70, 89), (66, 95, 156)),
                Text("Integrantes", (300, 185), screen, font, (60, 70, 89), (66, 95, 156))]

    IMAGENFONDO = pygame.image.load("myc/forest.jpg")
    opciones_elegidas = {'Jugar': jugar, 'Integrantes': template_integrantes}
    lista_opciones(IMAGENFONDO, opciones, opciones_elegidas)


def lista_opciones(img_fondo, opciones, opciones_elegidas, *args):
    while True:
        pygame.event.pump()
        screen.blit(img_fondo, (0, 0))
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                sys.exit()
            if evento.type == MOUSEBUTTONDOWN:
                for opcion in opciones:
                    if opcion.rect.collidepoint(pygame.mouse.get_pos()):
                        if opciones_elegidas:
                            if opcion.text in opciones_elegidas.keys():
                                opciones_elegidas[opcion.text]()
                for objeto in args:
                    if objeto.rect.collidepoint(pygame.mouse.get_pos()):
                        main()
        for opcion in opciones:
            if opcion.rect.collidepoint(pygame.mouse.get_pos()):
                opcion.hovered = True
            else:
                opcion.hovered = False
            opcion.draw()
        for n in args:
            n.dibujar(screen)
        pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    font = pygame.font.SysFont('Arial', 40, True)
    font_small = pygame.font.SysFont('Arial', 28, True)
    pygame.display.set_mode()
    main()
