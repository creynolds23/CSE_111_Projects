"""
Author: Conner Reynolds
Purpose: Alligator Game (Similar to the Snake game)
"""
import pygame
import time
import random

pygame.init()

distance_width = 700
distance_heigth = 500

dis=pygame.display.set_mode((distance_width,distance_heigth))  # Size of the game window
pygame.display.set_caption('Alligator game by Conner')



blue = (0,0,255)
red = (255,0,0)
white = (255,255,255)
black = (0,0,0)
yellow = (255, 255, 102)
green = (0, 255, 0)


alligator_block = 10
alligator_speed = 15
style_font = pygame.font.SysFont("bahnschrift", 20)
score_font = pygame.font.SysFont("comicsansms", 30)

clock = pygame.time.Clock()

def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, green)
    dis.blit(value, [0,0])

def our_alligator(alligator_block, alligator_list):
    for x in alligator_list:
        pygame.draw.rect(dis, white, [x[0], x[1], alligator_block, alligator_block])

def message(msg, color):
    mesg = style_font.render(msg, True, color)
    dis.blit(mesg, [distance_width/6, distance_heigth/3])

def gameLoop():
    game_over = False
    game_close = False

    x1 = distance_width/2
    y1 = distance_heigth/2

    x1_change = 0
    y1_change = 0

    alligtor_List = []
    length_alligator = 1

    xfood = round(random.randrange(0, distance_width - alligator_block) / 10.0) * 10.0
    yfood = round(random.randrange(0, distance_width - alligator_block) / 10.0) * 10.0

    while not game_over:
        
        while game_close == True: # Keeps the game window open until false
            dis.fill(black)
            message("You Lose! Press Q-Quit or C-Play", red)
            your_score(length_alligator - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -alligator_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = alligator_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -alligator_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = alligator_block
                    x1_change = 0
    
        if x1 >= distance_width or x1 < 0 or y1 >= distance_heigth or y1 <0:
            game_close = True
        
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, yellow, [xfood, yfood, alligator_block, alligator_block])
        alligator_head = []
        alligator_head.append(x1)
        alligator_head.append(y1)
        alligtor_List.append(alligator_head)
        if len(alligtor_List) > length_alligator:
            del alligtor_List[0]
        
        for x in alligtor_List[:-1]:
            if x == alligator_head:
                game_close = True

        our_alligator(alligator_block, alligtor_List)
        your_score(length_alligator - 1)
        pygame.display.update()

        if x1 == xfood and y1 == yfood:
            xfood = round(random.randrange(0, distance_width - alligator_block) / 10.0) * 10.0
            yfood = round(random.randrange(0, distance_heigth - alligator_block) / 10.0) * 10.0
            length_alligator += 1
        clock.tick(alligator_speed)

    pygame.quit()
    quit()

gameLoop()