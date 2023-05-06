import pygame
from projectile import Projectile
import animation

# class joueur
class Player(animation.AnimateSprite):
    
    def __init__(self, game):
        super().__init__('player')
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 15
        self.speed = 10
        self.all_projectile = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500
    
    def damage(self, amount):
        if self.health - amount > amount :
            self.health -= amount
        else:
            self.game.game_over()    

    def update_animation(self):
        self.animate()   
             
    def update_health_bar(self, surface):
        pygame.draw.rect(surface, (46, 84, 37), [self.rect.x + 50, self.rect.y + 20, self.max_health, 5])
        pygame.draw.rect(surface, (50, 255, 0), [self.rect.x + 50, self.rect.y + 20, self.health, 5])
        
    def launch_projectile(self):
        self.start_animation()
        self.game.sound_manager.play('tir')
        self.all_projectile.add(Projectile(self))
         
    def move_right(self):
        if not self.game.check_collision(self, self.game.all_monster):
            self.rect.x += self.speed 
        
    def move_left(self):
        self.rect.x -= self.speed       