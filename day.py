import pygame

class DayOrNight:
    def __init__(self, fps, length):
        self.threshold = fps * length
        self.counter = 0
        self.state = True
        self.transition = False
        self.c = 0
        self.transition_speed = 2

    def update(self, Surface):
        _max = 255-self.transition_speed
        _min = 0-self.transition_speed
        if self.transition:
            self.c+=self.transition_speed
        if self.c>=_max or self.c<_min:
            self.transition_speed*=-1
            self.transition = False
        Surface.fill((self.c,self.c,self.c))
        self._update()
        return (255,255,255) if self.transition_speed>0 else (0,0,0)

    def _update(self):
        if not self.transition:
            if self.counter>=self.threshold:
                self.transition = True
                self.counter = 0
            else:
                self.counter += 1