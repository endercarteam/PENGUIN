import os
import pygame
import button
WIDTH, HEIGHT = 900, 500
WHITE= (255,255,255)

Fondo = pygame.image.load(os.path.join('Images','fondo.png')) 

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) 
    
Penguin_Image = pygame.image.load(os.path.join('Images', 'Penguin_Idle.gif'))
Penguin = pygame.transform.scale(Penguin_Image, (300,100))
def draw_window():
    WIN.fill(WHITE) 
    WIN.blit(Penguin,(300, 100))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run: 
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()    
    pygame.quit()

if __name__ == "__main__":
    main()


