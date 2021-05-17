import pygame
from pygame import mixer
import os

pygame.mixer.init()

Width, Height = 900, 500
Win = pygame.display.set_mode((Width, Height))

mixer.music.load(os.path.join('Assets', 'Sia - Snowman.mp3'))
mixer.music.play(-1)
mixer.music.set_volume(0.1)

_Julu = pygame.image.load(os.path.join('Assets', 'Julu.png'))
Julu = pygame.transform.scale(_Julu, (175, 300))

_Right_Julu = pygame.image.load(os.path.join('Assets', 'Right_Julu.png'))
Right_Julu = pygame.transform.scale(_Right_Julu, (175, 300))

_Left_Julu = pygame.image.load(os.path.join('Assets', 'Left_Julu.png'))
Left_Julu = pygame.transform.scale(_Left_Julu, (175, 300))

_Up_Julu = pygame.image.load(os.path.join('Assets', 'Up_Julu.png'))
Up_Julu = pygame.transform.scale(_Up_Julu, (175, 300))

Running = pygame.image.load(os.path.join('Assets', 'Running Julu.png'))
Running_Julu = pygame.transform.scale(Running, (175, 300))

Background = pygame.image.load(os.path.join('Assets', 'Background.jpg'))

Velocity = 7
Run_Velocity = 4 # This is actually 11 because the Velocity was combined with Run Velocity

# Ignore all of the "key" errors
def draw_window(julu):
    pygame.display.set_icon(pygame.image.load(os.path.join('Assets', 'Icon.jpg')))
    pygame.display.set_caption('Julu Walks')

    Win.blit(Background, (0, 0))

    # Changing Images (Not sprites)
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_a] and key_pressed[pygame.K_d]:
        Win.blit(Julu, (julu.x, julu.y))

    elif key_pressed[pygame.K_a] and key_pressed[pygame.K_w]:
        Win.blit(Up_Julu, (julu.x, julu.y))

    elif key_pressed[pygame.K_d] and key_pressed[pygame.K_w]:
        Win.blit(Up_Julu, (julu.x, julu.y))

    elif key_pressed[pygame.K_a] and key_pressed[pygame.K_LSHIFT]: # Run Frame
        Win.blit(pygame.transform.flip(Running_Julu, True, False), (julu.x, julu.y))

    elif key_pressed[pygame.K_a]: # Backwards - 1st
        Win.blit(Left_Julu, (julu.x, julu.y))

    elif key_pressed[pygame.K_d] and key_pressed[pygame.K_LSHIFT]: # Run Frame
        Win.blit(Running_Julu, (julu.x, julu.y))

    elif key_pressed[pygame.K_d]:
        Win.blit(Right_Julu, (julu.x, julu.y))
    
    elif key_pressed[pygame.K_s] and key_pressed[pygame.K_LSHIFT]: # Run Frame
        Win.blit(Running_Julu, (julu.x, julu.y))

    elif key_pressed[pygame.K_w]:
        Win.blit(Up_Julu, (julu.x, julu.y))

    else:
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
            if key_pressed[pygame.K_d] and key_pressed[pygame.K_LSHIFT]: # Running
                julu.x += Run_Velocity
            
            julu.x += Velocity
        if key_pressed[pygame.K_a]: # Backwards
            if key_pressed[pygame.K_a] and key_pressed[pygame.K_LSHIFT]: # Running
                julu.x -= Run_Velocity
            
            julu.x -= Velocity
        if key_pressed[pygame.K_w]: # Upwards
            if key_pressed[pygame.K_w] and key_pressed[pygame.K_LSHIFT]: # Running
                julu.y -= Run_Velocity
            
            julu.y -= Velocity
        if key_pressed[pygame.K_s]: # Downwards
            if key_pressed[pygame.K_s] and key_pressed[pygame.K_LSHIFT]: # Running
                julu.y += Run_Velocity
            
            julu.y += Velocity

        # Borders

        # Left
        if julu.x <= -35:
            julu.x = -35
        # Right
        elif julu.x >= 758:
            julu.x = 758

        # Top
        if julu.y <= -6:
            julu.y = -6
        # Bottom
        elif julu.y >= 218:
            julu.y = 218

        draw_window(julu)
    pygame.quit()

if __name__ == "__main__":
    Julu_Walks()