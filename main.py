import pygame
import os

pygame.init()
pygame.font.init()
pygame.mixer.init()

#constants
WIDTH , HEIGHT = 800,600
FPS = 60  #Frames Per second
SPACESHIP_WIDTH=SPACESHIP_HEIGHT=70
SPACESHIP_CHANGE_X=4
SPACESHIP_CHANGE_Y=5
BULLET_CHANGE_X=6
MAX_BULLET=8



#event code
RED_HIT=pygame.USEREVENT+1
BLUE_HIT=pygame.USEREVENT+2

#images
background=pygame.image.load(os.path.join("images", "background.jpg"))
icon=pygame.image.load(os.path.join("images", "icon.png"))
blue_spaceship_image=pygame.image.load(os.path.join("images","blue_spaceship.png"))
blue_spaceship=pygame.transform.rotate(pygame.transform.scale(blue_spaceship_image, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), -90)
red_spaceship_image=pygame.image.load(os.path.join("images","red_spaceship.png"))
red_spaceship=pygame.transform.rotate(pygame.transform.scale(red_spaceship_image, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
health_image=pygame.image.load(os.path.join("images","health.png"))
health=pygame.transform.scale(health_image,(50,50))


#fonts
health_font=pygame.font.Font(os.path.join("fonts","FruitDays.ttf"),25)
win_font=pygame.font.Font(os.path.join("fonts","FruitDays.ttf"),45)



screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space Shooter")
pygame.display.set_icon(icon)




def draw_screen(blue,red,red_health,blue_health):
    screen.blit(background,(0,0))
    red_health_text = health_font.render("x" + str(red_health), True, (255, 255, 255))
    blue_health_text = health_font.render("x" + str(blue_health), True, (255, 255, 255))
    screen.blit(red_health_text, (750, 38))
    screen.blit(blue_health_text, (75, 38))
    screen.blit(blue_spaceship,(blue.x,blue.y))
    screen.blit(red_spaceship,(red.x,red.y))
    pygame.draw.rect(screen,(0,0,255),pygame.Rect(WIDTH/2-2.25,0,7,HEIGHT))
    pygame.draw.rect(screen,(255,0,0),pygame.Rect(WIDTH/2+6,0,7,HEIGHT))
    pygame.draw.rect(screen,(8,12,21),pygame.Rect(WIDTH/2,0,10,HEIGHT))
    screen.blit(health,(700,20))
    screen.blit(health,(25, 20))

    pygame.display.update()

def blue_move(key_pressed,blue):
    if key_pressed[pygame.K_a]:
        if blue.x-SPACESHIP_CHANGE_X<0:
            blue.x=0
        else:
            blue.x -= SPACESHIP_CHANGE_X
    if key_pressed[pygame.K_d]:
        if blue.x+SPACESHIP_CHANGE_X>(WIDTH//2-SPACESHIP_WIDTH-7):
            blue.x=(WIDTH//2-SPACESHIP_WIDTH-7)
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
        if red.x-SPACESHIP_CHANGE_X<(WIDTH//2+14):
            red.x=(WIDTH//2+14)
        else:
            red.x -= SPACESHIP_CHANGE_X
    if key_pressed[pygame.K_RIGHT]:
        if red.x+SPACESHIP_CHANGE_X>WIDTH-SPACESHIP_WIDTH:
            red.x=WIDTH-SPACESHIP_WIDTH
        else:
            red.x += SPACESHIP_CHANGE_X
def handle_bullets(blue,red,blue_bullets,red_bullets):
    for bullet in blue_bullets:
        bullet.x+=BULLET_CHANGE_X
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            blue_bullets.remove(bullet)
        elif bullet.x>WIDTH:
            blue_bullets.remove(bullet)
        else:
            for redBullet in red_bullets:
                if redBullet.colliderect(bullet):
                    blue_bullets.remove(bullet)
                    red_bullets.remove(redBullet)

    for bullet in red_bullets:
        bullet.x-=BULLET_CHANGE_X
        if blue.colliderect(bullet):
            pygame.event.post(pygame.event.Event(BLUE_HIT))
            red_bullets.remove(bullet)
        elif bullet.x<0:
            red_bullets.remove(bullet)
        else:
            for blueBullet in blue_bullets:
                if blueBullet.colliderect(bullet):
                    blue_bullets.remove(blueBullet)
                    red_bullets.remove(bullet)



def draw_bullets(blue_bullet,red_bullet):
    for bullet in blue_bullet:
        pygame.draw.rect(screen,(0,0,255),bullet)
    for bullet in red_bullet:
        pygame.draw.rect(screen,(255,0,0),bullet)
    pygame.display.update()

def show_winner_text(text):
    win_text = win_font.render(text, 1, (255, 255, 255))
    screen.blit(win_text, (WIDTH//2-win_text.get_width()//2, HEIGHT//2-win_text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(5000)


def main():
    red_health = blue_health = 10
    blue=pygame.Rect(100,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    red=pygame.Rect(600,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    clock=pygame.time.Clock()
    running=True
    blue_bullets=[]
    red_bullets=[]
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
                pygame.quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LCTRL and len(blue_bullets)!=MAX_BULLET:
                    bullet=pygame.Rect(blue.x+SPACESHIP_WIDTH,blue.y+SPACESHIP_HEIGHT//2,10,5)
                    blue_bullets.append(bullet)
                if event.key==pygame.K_RCTRL and len(red_bullets)!=MAX_BULLET:
                    bullet=pygame.Rect(red.x,red.y+SPACESHIP_HEIGHT//2,10,5)
                    red_bullets.append(bullet)
            if event.type==RED_HIT:
                red_health-=1
            if event.type==BLUE_HIT:
                blue_health-=1
        wintext=""
        if red_health<=0:
            wintext="blue wins!"
        if blue_health<=0:
            wintext="red wins!"
        if wintext!="":
            show_winner_text(wintext)
            break
        key_pressed=pygame.key.get_pressed()
        blue_move(key_pressed,blue)
        red_move(key_pressed,red)
        handle_bullets(blue,red,blue_bullets,red_bullets)
        draw_screen(blue,red,red_health,blue_health)
        draw_bullets(blue_bullets,red_bullets)
    main()

if __name__=="__main__":
    main()


