import pygame

prefix = "./Assets/"

class Dino:
    i_walk1 = pygame.image.load(prefix+"trex_run1.png")
    i_walk2 = pygame.image.load(prefix+"trex_run2.png")
    i_jump = pygame.image.load(prefix+"trex_jump.png")
    rects_vals = [[75,0,75,63],
            [105,61,16,13],
            [54,61,53,32],
            [0,71,56,12],
            [36,81,37,44],
            [72,93,21,51],
            [92,92,15,10],
            [92,101,9,7],
            [92,107,5,6],
            [57,127,16,6],
            [61,133,12,5],
            [67,138,6,4],
            [26,110,11,7],
            [30,116,6,10],
            [37,125,13,5],
            [41,130,8,4]]

    def __init__(self, location, fps):
        self.location = location
        self.x_loc, self.y_loc = location
        self.Y_LOC = location[1]
        self.fps = fps
        self.w_img = True
        self.w_slicer = 10
        self.w_counter = 0
        self.state = True  # True=Walk | False=Jump
        self.j_threshold = self.y_loc-250
        self.YD = 10
        self.yd = self.YD
        self.rect = self.i_walk1.get_rect(topleft=location)
        self.rects = self.create_rects()
        
    def create_rects(self):
        rects = []
        for rect in self.rects_vals:
            rects.append(pygame.Rect(rect[0]+self.x_loc,rect[1]+self.y_loc,rect[2],rect[3]))
        return rects
    
    def update_rects(self):
        for i in range(len(self.rects)):
            self.rects[i].y-=self.yd
    
    def update(self, Surface):
        # pygame.draw.rect(Surface, (255,0,0),self.rect)
        # for rect in self.rects:
        #     pygame.draw.rect(Surface, (255,0,0),rect,2)
        if self.state:
            if self.w_counter < self.fps:
                if self.w_counter % self.w_slicer == 0:
                    self.w_img = not self.w_img
                self.w_counter += 1
            else:
                self.w_counter = 0
            if self.w_img:
                Surface.blit(self.i_walk1, self.rect.topleft)
            else:
                Surface.blit(self.i_walk2, self.rect.topleft)
        else:
            if self.yd > 0:  # going up
                if self.y_loc < self.j_threshold:
                    self.yd *= -1
            else:  # going down
                if self.y_loc > self.Y_LOC:
                    self.state = True
                    self.yd = self.YD
            self.y_loc -= self.yd
            Surface.blit(self.i_jump, self.rect.topleft)
            self.rect.topleft = (self.x_loc, self.y_loc)
            self.update_rects()

    def jump(self):
        self.state = False
