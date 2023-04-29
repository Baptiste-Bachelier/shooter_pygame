import pygame
import random

class Monster(pygame.sprite.Sprite):
    
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 80
        self.max_health = 80
        self.attack = 0.3
        self.speed = random.randint(1,2)
        self.image = pygame.image.load('PygameAssets-main\mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540
    
    def damage(self, amount):
        self.health -= amount
        if self.health <= 0 :
            self.rect.x = 1080 + random.randint(0, 300)
            self.health = self.max_health
            self.speed = random.randint(1,2)
            
    
    def update_health_bar(self, surface):
        pygame.draw.rect(surface, (247, 33, 8), [self.rect.x + 20, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (119, 233, 50), [self.rect.x + 20, self.rect.y - 20, self.health, 5])
        
    def forward(self):
        if not self.game.check_collision(self, self.game.all_player):
            self.rect.x -= self.speed
        if self.game.check_collision(self, self.game.all_player):
            self.game.player.damage(self.attack)         
    