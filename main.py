import pygame
import math
from game import Game
pygame.init()

        
# generer la fenetre de notre jeu
pygame.display.set_caption("shooter_game")
screen = pygame.display.set_mode((1080, 720))

runnig = True

background = pygame.image.load('PygameAssets-main/bg.jpg', )

banner = pygame.image.load('PygameAssets-main/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width()/4)

play_button = pygame.image.load('PygameAssets-main/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width()/3.33)
play_button_rect.y = math.ceil(screen.get_height()/2)

game = Game()

while runnig:
        
    screen.blit(background, (0, -200))
    
    if game.is_running:
        game.update(screen)
    else:
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)
    
    pygame.display.flip()    
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            runnig = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            if event.key == pygame.K_z:
                game.player.launch_projectile()
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False  
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.is_running = True      
               