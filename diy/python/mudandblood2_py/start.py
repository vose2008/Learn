#!/usr/bin/env python
#coding:utf-8
import pygame
from sys import exit

pygame.init()
width,height = 400,600
screen = pygame.display.set_mode((width,height))

background = pygame.image.load("bg1.png")

pygame.display.set_caption("Py_MNB")

# start
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(background,(0,0))
    pygame.display.update()
