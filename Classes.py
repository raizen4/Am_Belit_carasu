import random
import pygame
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

color_list = [(255,255,255),(255,0,0),(0,255,0),(0,0,255),
              (0,0,0)] #white, red, green, blue, white

class Object:
    
    def __init__(self, position, size, image):
        '''position - tuple | size - tuple | image - image location string'''

        self.x = position[0]
        self.y = position[1]

        self.width = position[0]
        self.height = position[1]

        self.image = pygame.image.load(image)

        self.render()

    def render(self):
        self.n = 1
##        window.blit(self.i, (self.x, self.y))
##        pass

class Obstacle(Object):
    
    def __init__(self, position, size, image):

        Object.__init__(self, position, size, image) #inheriteaza initiate-ul de la objectul

    def render(self):
        window.blit(self.i, (self.x, self.y))
        if 
    


block1 = Obstacle((25,25),(50,50),"test.png")

print(block1.x, block1.y, block1.width, block1.height, block1.image)
print(block1.n)
