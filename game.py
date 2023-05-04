import pygame
from player import Player
from monster import Mummy, Alien
from comete_event import CometFALLEvent
from sound import SoundManager

class Game:
    
    def __init__(self):
        self.is_running = False
        self.sound_manager = SoundManager()
        self.comet_fall = CometFALLEvent(self)
        self.all_player = pygame.sprite.Group()
        self.player = Player(self)
        self.all_player.add(self.player)
        self.all_monster = pygame.sprite.Group()
        self.pressed = {}
        self.score = 0
    
    def start(self):
        self.is_running = True
        for i in range(3):
            self.spawn_monster(Mummy)
        self.spawn_monster(Alien)    
    
    def game_over(self):
        self.all_monster = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_fall.all_comete = pygame.sprite.Group()
        self.comet_fall.percent = 0
        self.is_running = False
        self.score = 0
        self.sound_manager.play('game_over')
        
    def add_score(self, point):
        self.score += point
         
    def update(self, screen):
        
        font = pygame.font.Font("PygameAssets-main\Sigmar-Regular.ttf", 25)
        score_text = font.render(f"Score: {self.score}", 1, (0,0,0))
        screen.blit(score_text, (20, 20))
        
        screen.blit(self.player.image, self.player.rect)
        self.player.update_health_bar(screen)
        self.player.update_animation()
        self.comet_fall.update_comet_bar(screen)
        self.comet_fall.all_comete.draw(screen)
        

        for comete in self.comet_fall.all_comete:
            comete.fall()
            
        for projectile in self.player.all_projectile:
            projectile.move()
            
        for monster in self.all_monster:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()
        
        self.player.all_projectile.draw(screen)
        
        self.all_monster.draw(screen)
        
        pygame.display.flip()
        
        if self.pressed.get(pygame.K_d) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_q) and self.player.rect.x > 0:
            self.player.move_left()              
        
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
    
    def spawn_monster(self, monster_name):
        self.all_monster.add(monster_name.__call__(self))    