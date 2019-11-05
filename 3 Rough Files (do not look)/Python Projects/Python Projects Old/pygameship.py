import pygame

class Ship:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        
        self.image = pygame.image.load(r"C:\Users\Djagad P. Dwialam\Pictures\specialmemefresh.png")
        self.rect = self.image.get_rect()
        
        self.moving_right = False
        self.moving_left = False
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        if self.moving_right and self.rect.right <= self.screen_rect.right:
            self.rect.x += 10
        if self.moving_left and self.rect.left >= self.screen_rect.left:
            self.rect.x -= 10