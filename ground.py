import pygame

prefix = "./Assets/"

class GND:
    img = pygame.image.load(prefix+"ground.png")
    def __init__(self, location, speed):
        self.speed = speed
        self.locs = [[0,location[1]],[2000,location[1]]]
        
    def update(self, Surface):
        self.locs = [[2000 if self.locs[i][0]-self.speed<-1999 else self.locs[i][0]-self.speed, self.locs[i][1]]
                      for i in range(len(self.locs))]
        Surface.blit(self.img, self.locs[0])
        Surface.blit(self.img, self.locs[1])
