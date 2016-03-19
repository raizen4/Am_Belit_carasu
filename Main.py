import pygame
from pygame.locals import  *
import sys
import numpy
import random
class Player(pygame.sprite.Sprite):
    def __init__(self,name,image):
        pygame.sprite.Sprite.__init__(self)
        self.name=name
        self.image_name=image
        self.image=pygame.image.load(self.image_name).convert()
        self.rect=self.image.get_rect()

    def set_position_on_grid(self,x_pos,y_pos):
        self.rect.x=x_pos
        self.rect.y=y_pos


    def move(self,where):
        pygame.init()
        if where=="left":
         if (self.rect.x-80) <240:
            self.rect.x-=0
         else:
           self.rect.x-=80
           bck=pygame.image.load("Background1.0g.png")
           main_screen.blit(bck,(0,0))
           surface_for_UI.fill((20,20,20))
           player_group.draw(main_screen)
           pygame.display.update(player_group.sprites())
        elif where=="right":
         if (self.rect.x+80) >=1280:
             self.rect.x+=0
         else:
            self.rect.x+=80
            bck=pygame.image.load("Background1.0g.png")
            main_screen.blit(bck,(0,0))
            player_group.draw(main_screen)
            surface_for_UI.fill((20,20,20))
            surface_for_UI.blit(main_screen,(0,0))
            pygame.display.flip()

class Traps(pygame.sprite.Sprite):
    def __init__(self,name,image,effect=None):
        pygame.sprite.Sprite.__init__(self)
        self.name=name
        self.image_name=image
        self.image=pygame.image.load(self.image_name).convert_alpha()
        self.rect=self.image.get_rect()
    def set_pos(self,x_pos,y_pos):
        self.rect.x=x_pos
        self.rect.y=y_pos


"--------------------------global variables-------------------"
size_of_main_screen=(1280,720) #latime,inaltime
main_screen=pygame.display.set_mode((size_of_main_screen))
surface_for_UI=pygame.Surface((240,720))
surface_for_UI.fill((20,20,20))
background=pygame.image.load("Background1.0g.png").convert()
player_group=pygame.sprite.Group()
traps_group=pygame.sprite.Group()
power_ups_group=pygame.sprite.Group()

"------displaying general things on the screen---------"
player=Player("player1","images/tile-80px.png")
main_screen.blit(background,(0,0))
player.set_position_on_grid(640,650)


player_group.add(player)
player_group.draw(main_screen)
main_screen.blit(surface_for_UI,(0,0))
pygame.display.flip()

trap=Traps("trap","images/bear-trap1.bmp")
trap.set_pos(0,0)
traps_group.add(trap)

while True:
    traps_group.draw(main_screen)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                player.move("left")

            if event.key==pygame.K_RIGHT:
                player.move("right")




