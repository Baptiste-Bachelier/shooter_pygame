import pygame
from player import Player
from monster import Monster
from comete_event import CometFALLEvent

class Game:
    
    def __init__(self):
        self.is_running = False
        self.comet_fall = CometFALLEvent()
        self.all_player = pygame.sprite.Group()
        self.player = Player(self)
        self.all_player.add(self.player)
        self.all_monster = pygame.sprite.Group()
        self.pressed = {}
    
    def start(self):
        self.is_running = True
        for i in range(3):
            self.spawn_monster()
    
    def game_over(self):
        self.all_monster = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_running = False
        
    def update(self, screen):
        screen.blit(self.player.image, self.player.rect)
        self.player.update_health_bar(screen)
        self.comet_fall.update_comet_bar(screen)
    
        for projectile in self.player.all_projectile:
            projectile.move()
            
        for monster in self.all_monster:
            monster.forward()
            monster.update_health_bar(screen)
        
        self.player.all_projectile.draw(screen)
        
        self.all_monster.draw(screen)
        
        pygame.display.flip()
        
        if self.pressed.get(pygame.K_d) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_q) and self.player.rect.x > 0:
            self.player.move_left()              
        
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
    
    def spawn_monster(self):
        self.all_monster.add(Monster(self))    