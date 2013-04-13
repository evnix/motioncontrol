import thread
import pygame
import threading
import random
import ubervar
import sys
import time
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((1024, 640))

player_img = pygame.image.load('sprites/x.png').convert_alpha()
stripe_img = pygame.image.load('sprites/stripe.png').convert_alpha()
stripe = stripe_img.get_rect()
player = player_img.get_rect()

def texts():
    font=pygame.font.Font(None,30)
    scoretext=font.render("Score:"+str(ubervar.score), 1,(255,255,255))
    screen.blit(scoretext, (500, 0))

def collide():
    font=pygame.font.Font(None,30)
    scoretext=font.render("COLLISION", 1,(255,0,0))
    screen.blit(scoretext, (200, 0))

def end_text():
    font=pygame.font.Font(None,30)
    scoretext=font.render("Game Over.", 1,(255,255,255))
    screen.blit(scoretext, (500, 200))


class  enemy():
    left = 0
    top = 0
    img_path = ""


    def __init__(self, img_path):
        self.left = random.randint(0, 800)
        self.top = -100
        self.speed = random.randint(30, 40)
        self.enemy_img = pygame.image.load(img_path).convert_alpha()
        self.enemy_rect = self.enemy_img.get_rect()

    def increment(self):
        if self.top > 550:
            self.init_left()
            self.top = -100
        else:
            self.top = self.top + self.speed
            self.enemy_rect.top=self.top

    def init_left(self):
        ubervar.score=ubervar.score+100
        self.speed = random.randint(30, 50)
        self.left = ubervar.car_left
        self.enemy_rect.left = self.left

    def draw(self):
        self.increment()
        screen.blit(self.enemy_img, (self.left, self.top, 100, 100))



def update_stripe():
        screen.blit(stripe_img, (500, ubervar.stripe_y, 100, 100))
        ubervar.stripe_y=ubervar.stripe_y + 20
        if ubervar.stripe_y>500:
            ubervar.stripe_y=0

def change_direction():
        if ubervar.current_direction == 1:
            if ubervar.car_left < 1024-100:
                ubervar.car_left = ubervar.car_left + 100
        else:
            if ubervar.car_left > 0:
                ubervar.car_left = ubervar.car_left - 100

        player.left = ubervar.car_left
        player.top = 500



def load_player():

        change_direction()
        screen.blit(player_img,(ubervar.car_left,500,100,100))#ubervar.player_top,100,100))

def show_end():
    screen.fill((0,0,0))
    end_text()
    pygame.display.update()
    pygame.display.flip()
    time.sleep(5)
    ubervar.out=True
    pygame.quit()
    sys.exit()
    print "end game"

class mgame(threading.Thread):

    def run(self):

          e = enemy("sprites/y1.png")
          e2 = enemy("sprites/y2.png")
          e3 = enemy("sprites/y2.png")

          while True:


            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        ubervar.current_direction = 0
                    if event.key == pygame.K_RIGHT:
                        ubervar.current_direction = 1

            #player=player.move(ubervar.player_left,ubervar.player_top)
            screen.fill((0,0,0))

            update_stripe()
            e.draw()
            e2.draw()
            e3.draw()
            load_player()
            texts()
            if ((player.colliderect(e.enemy_rect) == True) or (player.colliderect(e2.enemy_rect) == True)):
                ubervar.score=ubervar.score-200
                collide()
                print "collision"
            print str(e.enemy_rect.topleft)
            pygame.display.update()
            pygame.display.flip()

            if ubervar.score<-200:
                show_end()
                break
            pygame.time.delay(25)
