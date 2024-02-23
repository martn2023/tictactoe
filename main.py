import pygame
from pygame.locals import *

pygame.init()

screen_width = 300
screen_height = 300

screen = pygame.display.set_mode((screen_width,screen_height))  # initialize the screen: looking for size, flags, depth, display, vsync
pygame.display.set_caption("TicTacToe - By Martin, using PyGame")

def draw_grid():
    background_color = (255,255,200)
    grid_color = (50,50,50)
    screen.fill(background_color)

    for line_index in range(1,3):  #can resuse this variable on 2 dimension bc its a square
        pygame.draw.line(screen, grid_color,(0,line_index*100),(screen_width, line_index*100))  #expecting parameters in terms of surface, surface type, color, start and end, width
        pygame.draw.line(screen, grid_color, (line_index * 100, 0),(line_index * 100,screen_height))

run = True
while run:
    draw_grid()

    #add event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()