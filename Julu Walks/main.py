import pygame
from pygame import mixer
import os

pygame.init()

Width, Height = 900, 500
Win = pygame.display.set_mode((Width, Height))

mixer.music.load(os.path.join('Assets', 'Sia - Snowman.mp3'))
mixer.music.play(-1)

_Julu = pygame.image.load(os.path.join('Assets', 'Julu.png'))
Julu = pygame.transform.scale(_Julu, (175, 300))
Running = pygame.image.load(os.path.join('Assets', 'Running Julu.png'))
Running_Julu = pygame.transform.scale(Running, (175, 300))

Background = pygame.image.load(os.path.join('Assets', 'Background.jpg'))

Velocity = 10

def draw_window(julu):
    pygame.display.set_icon(pygame.image.load(os.path.join('Assets', 'Icon.jpg')))
    pygame.display.set_caption('Julu Walks')

    Win.blit(Background, (0, 0))

    Win.blit(Julu, (julu.x, julu.y))

    pygame.display.update()

# Ignore the errors with "quit" and "keys"
def Julu_Walks():
    julu = pygame.Rect(360, 90, 175, 300)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_d]: # Forwards
            julu.x += Velocity
        if key_pressed[pygame.K_a]: # Backwards
            julu.x -= Velocity
        if key_pressed[pygame.K_w]: # Upwards
            julu.y -= Velocity
        if key_pressed[pygame.K_s]: # Downwards
            julu.y += Velocity

        # Borders
        if julu.x <= -27:
            julu.x = -27
        elif julu.x >= 758:
            julu.x = 758

        if julu.y <= -10:
            julu.y = -10
        elif julu.y >= 212:
            julu.y = 212

        draw_window(julu)
    pygame.quit()

if __name__ == "__main__":
    Julu_Walks()