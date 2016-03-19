import pygame
from pygame.locals import  *
import sys
import numpy
import random
import time
pygame.init()
global lives
lives=3
global score
score=0

class Player(pygame.sprite.Sprite):
    def __init__(self,name,image,color):
        pygame.sprite.Sprite.__init__(self)
        self.name=name
        self.color=color
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
           bck=pygame.image.load("bg-1040x670.png")
           main_screen.blit(bck,(240,0))

        elif where=="right":
         if (self.rect.x+80) >=1280:
             self.rect.x+=0
         else:
            self.rect.x+=80
            bck=pygame.image.load("bg-1040x670.png")
            main_screen.blit(bck,(240,0))
    def update(self):
        player_group.draw(main_screen)

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
    def update(self):
        self.rect.y+=7
        bck=pygame.image.load("bg-1040x670.png")
        main_screen.blit(bck,(240,0))
        traps_group.draw(main_screen)
    def is_out_of_bound(object):
        pygame.init()
        if object.rect.y>600:
            traps_group.remove(object)

class Advance_level (pygame.sprite.Sprite):
    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.image_name=image
        self.image=pygame.image.load(self.image).convert()
        self.rect=self.image.get_rect()
        group_for_level.add(self)

    def set_pos(self,x,y):
        self.rect.x=x
        self.rect.y=y

    def have_i_been_collided(object):
        pygame.init()
        if pygame.sprite.groupcollide(group_for_level,player_group,False,False,collided=None):
         pass

class Box_color(pygame.sprite.Sprite):
    def __init__(self,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.width=width
        self.height=height
    def set_color(self,color):
        self.color=color

    def position(self,x,y):
        self.x=x
        self.y=y
    def draw(self):
        pygame.draw.rect(surface_for_color_boxes,self.color,(self.x,self.y,self.width,self.height))



def draw_on_color_surface():
    surface_for_color_boxes.fill((0,0,0))
    font_to_render=pygame.font.Font(None,30)
    livesa=font_to_render.render("lives"+" "+str(lives),False,(190,190,0))
    surface_for_color_boxes.blit(livesa,(0,20))
    main_screen.blit(surface_for_color_boxes,(1040,630))#column,row
def drow_on_UI():
    global score
    surface_for_UI.fill((0,0,0))
    font_to_render=pygame.font.Font(None,30)
    score=font_to_render.render("score "+" "+str(score),False,(190,190,0))
    surface_for_UI.blit(score,(0,40))



"======================create a new trap every frame================"
"--------------------------global variables-------------------"
size_of_main_screen=(1280,720) #latime,inaltime
main_screen=pygame.display.set_mode((size_of_main_screen))
surface_for_UI=pygame.Surface((240,720))
surface_for_UI.fill((20,20,20))
surface_for_color_boxes=pygame.Surface((1040,90))
surface_for_color_boxes.fill((0,0,0))
background=pygame.image.load("bg-1040x670.png").convert()
player_group=pygame.sprite.Group()
traps_group=pygame.sprite.Group()
power_ups_group=pygame.sprite.Group()
group_for_level=pygame.sprite.Group()
group_of_colored_boxes=pygame.sprite.Group()


"------displaying general things on the screen---------"
player=Player("player1","images/tile-80px.png",(255,200,70))
main_screen.blit(background,(240,0))
player.set_position_on_grid(640,580)


player_group.add(player)
player_group.draw(main_screen)
main_screen.blit(surface_for_UI,(0,0))
list_of_possible_colors=[[255,43,54],[212,121,221],[45,54,32]]
color_box=Box_color(130,80)
color_box.position(520,630)
color_box.set_color(list_of_possible_colors[random.randint(0,len(list_of_possible_colors)-1)])
color_box.draw()
main_screen.blit(surface_for_color_boxes,(1040,630))
pygame.display.flip()


list_of_traps=[]
for i in range(5):
    trap=Traps("trap"+str(i),"images/bear-trap1.bmp")
    trap.set_pos(random.randint(240,1240),random.randint(0,600))
    traps_group.add(trap)


clock=pygame.time.Clock()

while True:
   clock.tick(30)
   main_screen.blit(surface_for_color_boxes,(240,630))

   draw_on_color_surface()
   drow_on_UI()

   sprites_list_for_traps=traps_group.sprites()
   sprites_list_for_colored_boxes=group_of_colored_boxes.sprites()

   for sprite in sprites_list_for_traps:
     Traps.is_out_of_bound(sprite)
     sprite.update()
     player.update()
   for box in sprites_list_for_colored_boxes:
       box.color=list_of_possible_colors[random.randint(0,len(list_of_possible_colors)-1)]
       box.draw()


   for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                player.move("left")

            if event.key==pygame.K_RIGHT:
                player.move("right")
            if pygame.sprite.groupcollide(player_group,traps_group,False,True,collided=None):
                global lives
                lives-=1
                print(lives)


   pygame.display.flip()



