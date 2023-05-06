import pygame
import random
from sound import SoundManager

class Comet(pygame.sprite.Sprite):
    
    def __init__(self, comet_event):
        super().__init__()
        self.image = pygame.image.load('PygameAssets-main\comet.png')
        self.rect = self.image.get_rect()
        self.speed = random.randint(1, 3)
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(0,800)
        self.comet_event = comet_event
        self.sound_manager = SoundManager()
    
    def remove(self):
        self.comet_event.all_comete.remove(self)
        self.sound_manager.play('meteorite')
        if len(self.comet_event.all_comete) == 0:
            self.comet_event.percent = 0
            self.comet_event.game.start()
        
    def fall(self):
        self.rect.y += self.speed   
        
        if self.rect.y >= 500:
            self.remove()
            if len(self.comet_event.all_comete) == 0:
                self.comet_event.percent = 0
                self.comet_event.game.start()
                
        if self.comet_event.game.check_collision(self, self.comet_event.game.all_player ):
            self.comet_event.all_comete.remove(self)
            self.comet_event.game.player.damage(30)   