# -*- coding: UTF-8 -*-
import pygame
import time
from pygame.locals import *
from sys import exit


class HeroPlan(object):
    def __init__(self,screenTemp):
        self.LEFT = 200
        self.TOP = 500
        self.screen = screenTemp
        # 载入飞机图片
        self.plane = pygame.image.load("resources/image/hero1.png")
        self.bullet_list = []

    def display(self):
        # 绘制飞机plane
        self.screen.blit(self.plane, (self.LEFT, self.TOP))

        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge(): # 判断子弹是否越界
                self.bullet_list.remove(bullet)

    def move_left(self):
        self.LEFT -= 10

    def move_right(self):
        self.LEFT += 10

    def move_top(self):
        self.TOP -= 20

    def move_down(self):
        self.TOP += 10

    def fire(self):
        self.bullet_list.append(Bullet(self.screen,self.LEFT,self.TOP))

class EnemyPanel0(object):
    def __init__(self,screen):
        self.x = 0
        self.y = 0
        self.screen = screen
        self.image = pygame.image.load("resources/image/enemy0.png")
        self.direction = "right" # 控制敌机飞行方向

    def display(self):
        self.screen.blit(self.image,(self.x,self.y))

    def move(self):
        if self.direction is "right":
            self.x += 1
        else:
            self.x -= 1

        if self.x > 430:
            self.direction = "left"
        elif self.x < 0:
            self.direction = "right"

class Bullet(object):
    def __init__(self,screen,x,y):
        self.x = x + 7
        self.y = y + 15
        self.screen = screen
        self.image = pygame.image.load("resources/image/bullet.png")

    def display(self):
        # 绘制子弹
        self.screen.blit(self.image,(self.x,self.y))

    def move(self):
        self.y -= 10

    def judge(self):
        if self.y < 0:
            return True
        else:
            return False

def key_controller(hero):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                hero.move_left()
                print ('left')
            if event.key == K_d or event.key == K_RIGHT:
                hero.move_right()
                print ('right')
            if event.key == K_w or event.key == K_UP:
                hero.move_top()
                print ('up')
            if event.key == K_s or event.key == K_DOWN:
                hero.move_down()
                print ('down')
            if event.key == K_SPACE:
                hero.fire()
                print ('space')

def main():

    # 定义窗口分辨率
    SCREEN_WIDTH = 480
    SCREEN_HEIGHT = 640

    # 初始化游戏
    pygame.init()
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    pygame.display.set_caption('This is my first pygame-program')

    # 载入背景图
    background = pygame.image.load('resources/image/background.png')
    hero = HeroPlan(screen)
    enemy = EnemyPanel0(screen)

    # 事件循环
    while True:

        # 绘制背景
        screen.blit(background,(0,0))

        hero.display()

        enemy.display()
        enemy.move()

        # 更新屏幕
        pygame.display.update()
        key_controller(hero)
        time.sleep(0.01)



if __name__ == '__main__':
    main()