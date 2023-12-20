import pygame
from random import randint as rnd


prefix = "./Assets/"


def load_obj_rects_details(name):
    with open(prefix+name[:-3]+"txt") as file:
        content = file.readlines()
        content = [i.strip() for i in content]
        content = [i.split(",") for i in content]
        content = [[int(j) for j in i] for i in content]
    return content


class Obstacles:
    def __init__(self, y, min_gap, speed):
        self.obs_list = []
        self.y = y
        self.gap = min_gap
        self.speed = speed
        self.init_obs()

    def add(self, rect):
        self.obs_list.append(rect)

    def remove(self):
        self.obs_list.pop(0)

    def check(self):
        if self.obs_list[0].x_loc+self.obs_list[0].width<0:
            self.remove()
        if self.obs_list[-1].x_loc+self.obs_list[-1].width+self.gap<2000:
            self.gen_obs()
    
    def update(self, Surface):
        for obs in self.obs_list:
            obs.update(Surface)

    def gen_obs(self):
        self.obs_list.append(Obstacle((rnd(2000,2200), self.y), self.speed))

    def init_obs(self):
        self.obs_list.append(Obstacle((rnd(700,1000),  self.y), self.speed))
        self.obs_list.append(Obstacle((rnd(1450,1600), self.y), self.speed))
        self.obs_list.append(Obstacle((rnd(2000,2100), self.y), self.speed))

class Obstacle:
    img_list = [
        ["tree1s3.png", load_obj_rects_details("tree1s3.png")],
        ["tree2s3.png", load_obj_rects_details("tree2s3.png")],
        ["tree4s3.png", load_obj_rects_details("tree4s3.png")],
    ]
    def __init__(self, location, speed):
        self.location = location
        self.x_loc, self.y_loc = location
        self.speed = speed
        self.type = rnd(0,len(self.img_list)-1)
        self.img = pygame.image.load(prefix+self.img_list[self.type][0])
        self.width = self.img.get_width()
        self.rects = self.generate_rects()

    def generate_rects(self):
        rects = []
        for rect_details in self.img_list[self.type][1:]:
            for each_rec in range(len(rect_details)):
                rects.append(pygame.Rect(rect_details[each_rec][0]+self.x_loc,
                                        rect_details[each_rec][1]+self.y_loc,
                                        *rect_details[each_rec][2:]))
        return rects
    
    def update(self, Surface):
        self.x_loc-=self.speed
        Surface.blit(self.img, (self.x_loc,self.y_loc))
        for i in range(len(self.rects)):
            self.rects[i].x -= self.speed
            # pygame.draw.rect(Surface, (255,0,0), self.rects[i],2)


