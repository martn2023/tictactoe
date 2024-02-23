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

winner = 0
game_over = False

player_id = 1  #this will flip between the 2 players as 1 vs -1

x_marker_color = (0,255,0) #green for player 1
o_marker_color = (255,0,0) #red for player -1


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

def draw_markers():
    x_pos = 0
    for row in markers_board:
        y_pos = 0
        for column in row:
            if column == 1:
                pygame.draw.line(
                    screen,
                    x_marker_color,
            (x_pos * square_size +15, y_pos * square_size +15),
            (x_pos * square_size +85, y_pos * square_size +85),
                    line_width)

                #need 2 lines to make an X
                pygame.draw.line(
                    screen,
                    x_marker_color,
                    (x_pos * square_size + 85, y_pos * square_size + 15),
                    (x_pos * square_size + 15, y_pos * square_size + 85),
                    line_width)



            if column == -1:
                pygame.draw.circle(screen, o_marker_color, (x_pos*square_size+50, y_pos*square_size+50), 38,line_width)
            y_pos += 1
        x_pos += 1

def check_winner():
    global winner ##new lesson on global vars
    global game_over
    for index in range(3):
        if sum(markers_board[index]) == 3:
            winner = 1
            game_over = True

        if sum(markers_board[index]) == -3:
            winner = 2
            game_over = True

        if markers_board[0][index] + markers_board[1][index] + markers_board[2][index] == 3:
            winner = 1
            game_over = True

        if markers_board[0][index] + markers_board[1][index] + markers_board[2][index] == -3:
            winner = 2
            game_over = True

    if markers_board[0][0] + markers_board[1][1] + markers_board[2][2] == 3 or markers_board[2][0] + markers_board[1][1] + markers_board[0][2] == 3:
        winner = 1
        game_over = True

    if markers_board[0][0] + markers_board[1][1] + markers_board[2][2] == 3 or markers_board[2][0] + markers_board[1][1] + markers_board[0][2] == -3:
        winner = 2
        game_over = True


run = True
while run:
    draw_grid()
    draw_markers()

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
                player_id *= -1  #to flip players

                check_winner()

        if game_over:
            run = False

    pygame.display.update()

pygame.quit()