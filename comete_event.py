import pygame
from comet import Comet

class CometFALLEvent():
    
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 100
        self.all_comete = pygame.sprite.Group()
        self.game = game
        self.fall_mod = False
    
    def meteor_fall(self):
        for i in range(15):
            self.all_comete.add(Comet(self))
    
    def is_full_loaded(self):
        return self.percent >= 100
             
    def add_percent(self):
        self.percent += self.percent_speed/100
        
    def attemp_fall(self):    
        if self.is_full_loaded() and len(self.game.all_monster) == 0:
            self.meteor_fall()
            self.fall_mod = True 
        
    def update_comet_bar(self, surface):
        self.add_percent()
        pygame.draw.rect(surface, (0, 0, 0), [0, surface.get_height() - 20, surface.get_width(), 10])  
        pygame.draw.rect(surface, (187, 11, 11), [0, surface.get_height() - 20, (surface.get_width()/100)*self.percent, 10])       