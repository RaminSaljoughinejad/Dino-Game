import pygame
import sys
from constants import *
from dino import Dino
from ground import GND
from day import DayOrNight
from obstacles import Obstacle, Obstacles

class Game:
    fps = 60
    def __init__(self):
        pygame.init()
        self.game_dsiplay = pygame.display.set_mode((1000,600))
        pygame.display.set_caption("Dino")
        self.font = pygame.font.Font(None, 22)
        self.hscore = self.load_hscore()
        self.score = 0
        self.day = DayOrNight(self.fps, 10)
        self.ground = GND((0,450),7)
        self.player1 = Dino(dino_init_location,self.fps)

        self.obstacles = Obstacles(440, 450, 7)

        self.clock = pygame.time.Clock()
        self.run()


    def load_hscore(self):
        with open("save.txt", "r") as file:
            hscore = file.read()
            return hscore
    
    def show_score(self, color):
        score = str(self.score)
        _score = self.font.render((6-len(score))*"0"+score, True, color)
        _hscore = self.font.render("Hi "+self.hscore, True, color)
        self.game_dsiplay.blit(_score, (910,20))
        self.game_dsiplay.blit(_hscore,(820,20))

    def new_score(self):
        if int(self.load_hscore)<self.new_score:
            with open("save.txt", "w") as file:
                file.write((6-len(str(self.score)))*"0"+str(self.score))

    def run(self):
        color = None
        while True:
            color = self.day.update(self.game_dsiplay)
            self.show_score(color)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player1.jump()
            
            
            self.ground.update(self.game_dsiplay)
            self.obstacles.update(self.game_dsiplay)
            self.player1.update(self.game_dsiplay)
            self.obstacles.check()
            pygame.display.update()
            self.score+=1
            self.clock.tick(self.fps)

new_game = Game()