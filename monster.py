import pygame
import random
import animation

class Monster(animation.AnimateSprite):
    
    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)
        self.game = game
        self.loot_amount = 10
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540 - offset
        self.start_animation()
    
    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.game.add_score(self.loot_amount)
            self.rect.x = 1080 + random.randint(0, 300)
            self.health = self.max_health
            self.speed = random.randint(1,2)
            if self.game.comet_fall.is_full_loaded():
                self.game.all_monster.remove(self)
                self.game.comet_fall.attemp_fall()
    
    def set_loot_amount(self, amount):
        self.loot_amount = amount            
    
    def update_animation(self):
        self.animate(loop=True)  
                  
    def update_health_bar(self, surface):
        pygame.draw.rect(surface, (247, 33, 8), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (119, 233, 50), [self.rect.x + 10, self.rect.y - 20, self.health, 5])
        
    def forward(self):
        if not self.game.check_collision(self, self.game.all_player):
            self.rect.x -= self.speed
        if self.game.check_collision(self, self.game.all_player):
            self.game.player.damage(self.attack)
            
    def set_speed(self, max_speed):
        self.default_speed = max_speed
        self.speed = random.randint(1,2)                  
    
class Mummy(Monster):
    
    def __init__(self, game):
        super().__init__(game, "mummy", (130,130))
        self.set_speed(3)
        self.set_loot_amount(20)
        
class Alien(Monster):
    
    def __init__(self, game):
        super().__init__(game, "alien", (300,300), 100)
        self.health = 250
        self.max_health = 250  
        self.attack = 0.8
        self.set_loot_amount(80)
        self.set_speed(1)      
        