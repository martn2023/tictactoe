import pygame
from pygame.locals import *

pygame.init()

screen_width = 300
screen_height = 300

square_size = 100
line_width = 6
markers_board =[]
clicked_status = False
clicked_position = []

player_id = 1  #this will flip between the 2 players as 1 vs -1

screen = pygame.display.set_mode((screen_width,screen_height))  # initialize the screen: looking for size, flags, depth, display, vsync
pygame.display.set_caption("TicTacToe - By Martin, using PyGame")

def draw_grid():
    background_color = (255,255,200)
    grid_color = (50,50,50)
    screen.fill(background_color)

    for line_index in range(1,3):  #can resuse this variable on 2 dimension bc its a square
        pygame.draw.line(screen, grid_color,(0,line_index*100),(screen_width, line_index*100), line_width)  #expecting parameters in terms of surface, surface type, color, start and end, width
        pygame.draw.line(screen, grid_color, (line_index * 100, 0),(line_index * 100,screen_height), line_width)


for row_count in range(3):
    new_row = [0] * 3
    markers_board.append(new_row)

print("markers", markers_board)
run = True
while run:
    draw_grid()

    #add event handler
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:  #click detection
            clicked_status = True

        if event.type == pygame.MOUSEBUTTONUP and clicked_status: #this doesn't bug out bc you initialize it as False before loop starts
            clicked_status = False
            clicked_position = pygame.mouse.get_pos()  #caution on naming
            x_coordinate = clicked_position[0]
            y_coordinate = clicked_position[1]

            if markers_board[x_coordinate//square_size][y_coordinate//square_size] == 0:  #checking if this is fresh territory
                markers_board[x_coordinate // square_size][y_coordinate // square_size] = player_id
                player_id -= -1  #to flip players

    pygame.display.update()

pygame.quit()