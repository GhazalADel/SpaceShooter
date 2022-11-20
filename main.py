import pygame
import os

pygame.init()

#constants
WIDTH , HEIGHT = 800,600
FPS = 60  #Frames Per second
SPACESHIP_WIDTH=SPACESHIP_HEIGHT=70

#images
background=pygame.image.load(os.path.join("images", "background.jpg"))
icon=pygame.image.load(os.path.join("images", "icon.png"))
blue_spaceship_image=pygame.image.load(os.path.join("images","blue_spaceship.png"))
blue_spaceship=pygame.transform.rotate(pygame.transform.scale(blue_spaceship_image, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), -90)
red_spaceship_image=pygame.image.load(os.path.join("images","red_spaceship.png"))
red_spaceship=pygame.transform.rotate(pygame.transform.scale(red_spaceship_image, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)





screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space Shooter")
pygame.display.set_icon(icon)




def draw_screen():
    screen.blit(background,(0,0))
    screen.blit(blue_spaceship,(50,50))
    screen.blit(red_spaceship,(650,500))
    pygame.display.update()


def main():
    clock=pygame.time.Clock()
    running=True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False

        draw_screen()
    pygame.quit()







if __name__=="__main__":
    main()


