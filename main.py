import pygame
import os

pygame.init()

#constants
WIDTH , HEIGHT = 800,600
FPS = 60  #Frames Per second
SPACESHIP_WIDTH=SPACESHIP_HEIGHT=70
SPACESHIP_CHANGE_X=4
SPACESHIP_CHANGE_Y=5

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




def draw_screen(blue,red):
    screen.blit(background,(0,0))
    screen.blit(blue_spaceship,(blue.x,blue.y))
    screen.blit(red_spaceship,(red.x,red.y))
    pygame.display.update()
def blue_move(key_pressed,blue):
    if key_pressed[pygame.K_a]:
        if blue.x-SPACESHIP_CHANGE_X<0:
            blue.x=0
        else:
            blue.x -= SPACESHIP_CHANGE_X
    if key_pressed[pygame.K_d]:
        if blue.x+SPACESHIP_CHANGE_X>(WIDTH//2-SPACESHIP_WIDTH):
            blue.x=(WIDTH//2-SPACESHIP_WIDTH)
        else:
            blue.x += SPACESHIP_CHANGE_X
    if key_pressed[pygame.K_w]:
        if blue.y-SPACESHIP_CHANGE_Y<0:
            blue.y=0
        else:
            blue.y -= SPACESHIP_CHANGE_Y
    if key_pressed[pygame.K_s]:
        if blue.y + SPACESHIP_CHANGE_Y > (HEIGHT-SPACESHIP_HEIGHT):
            blue.y = HEIGHT-SPACESHIP_HEIGHT
        else:
            blue.y += SPACESHIP_CHANGE_Y

def red_move(key_pressed,red):
    if key_pressed[pygame.K_UP]:
        if red.y - SPACESHIP_CHANGE_Y < 0:
            red.y = 0
        else:
            red.y -= SPACESHIP_CHANGE_Y
    if key_pressed[pygame.K_DOWN]:
        if red.y + SPACESHIP_CHANGE_Y > (HEIGHT - SPACESHIP_HEIGHT):
            red.y = HEIGHT - SPACESHIP_HEIGHT
        else:
            red.y += SPACESHIP_CHANGE_Y
    if key_pressed[pygame.K_LEFT]:
        if red.x-SPACESHIP_CHANGE_X<(WIDTH//2):
            red.x=(WIDTH//2)
        else:
            red.x -= SPACESHIP_CHANGE_X
    if key_pressed[pygame.K_RIGHT]:
        if red.x+SPACESHIP_CHANGE_X>WIDTH-SPACESHIP_WIDTH:
            red.x=WIDTH-SPACESHIP_WIDTH
        else:
            red.x += SPACESHIP_CHANGE_X

def main():
    blue=pygame.Rect(100,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    red=pygame.Rect(600,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    clock=pygame.time.Clock()
    running=True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        key_pressed=pygame.key.get_pressed()
        blue_move(key_pressed,blue)
        red_move(key_pressed,red)







        draw_screen(blue,red)
    pygame.quit()







if __name__=="__main__":
    main()


