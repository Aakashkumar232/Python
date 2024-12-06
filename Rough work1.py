# # Tic-Tac-Toe Game in :-

# # Function to print the Tic-Tac-Toe board
# def print_board(board):
#     print(f"{board[0]} | {board[1]} | {board[2]}")
#     print("--+---+--")
#     print(f"{board[3]} | {board[4]} | {board[5]}")
#     print("--+---+--")
#     print(f"{board[6]} | {board[7]} | {board[8]}")
#     print("\n")

# # Function to check if a player has won
# def check_winner(board, player):
#     # Check rows, columns, and diagonals for a win
#     win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
#                       (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
#                       (0, 4, 8), (2, 4, 6)]  # Diagonals
    
#     for condition in win_conditions:
#         if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
#             return True
#     return False

# # Function to check if the board is full (a tie)
# def is_board_full(board):
#     return " " not in board

# # Main function to play the game
# def play_game():
#     # Initialize the game board (empty)
#     board = [" "] * 9  # 9 spaces for a 3x3 grid
#     current_player = "X"  # Player "X" starts
#     game_over = False

#     while not game_over:
#         # Print the current board
#         print_board(board)
        
#         # Ask the current player for their move
#         try:
#             move = int(input(f"Player {current_player}, enter a position (1-9): ")) - 1
#             if board[move] != " ":
#                 print("This spot is already taken! Try again.")
#                 continue
#         except (ValueError, IndexError):
#             print("Invalid input! Please enter a number between 1 and 9.")
#             continue

#         # Update the board with the player's move
#         board[move] = current_player

#         # Check if the current player has won
#         if check_winner(board, current_player):
#             print_board(board)
#             print(f"Player {current_player} wins!")
#             game_over = True
#         # Check if the game is a tie (board is full and no winner)
#         elif is_board_full(board):
#             print_board(board)
#             print("It's a tie!")
#             game_over = True
#         else:
#             # Switch players
#             current_player = "O" if current_player == "X" else "X"

# # Start the game
# if __name__ == "__main__":
#     play_game()
 







import pygame
import time
import random

# Initialize pygame
pygame.init()

# Define game colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Define display dimensions
dis_width = 800
dis_height = 600

# Create the display window
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Bike Game')

# Set game clock
clock = pygame.time.Clock()

# Set the bike block size and speed
block_size = 20
speed = 10

# Set the font for displaying text
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Function to display the current score
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, black)
    dis.blit(value, [0, 0])

# Function to draw the bike (snake)
def draw_bike(block_size, bike_list):
    for x in bike_list:
        pygame.draw.rect(dis, green, [x[0], x[1], block_size, block_size])

# Function to display a message in the center
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

# Main game function
def gameLoop():
    game_over = False
    game_close = False

    # Initial position of the bike
    x1 = dis_width / 2
    y1 = dis_height / 2

    # Initial movement direction
    x1_change = 0
    y1_change = 0

    # List for the bike body
    bike_List = []
    Length_of_bike = 1

    # Randomly place the food
    foodx = round(random.randrange(0, dis_width - block_size) / 20.0) * 20.0
    foody = round(random.randrange(0, dis_height - block_size) / 20.0) * 20.0

    while not game_over:

        while game_close:
            dis.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            Your_score(Length_of_bike - 1)
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
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        # Check if the bike hits the boundaries
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        # Update the bike's position
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)

        # Draw the food (red square)
        pygame.draw.rect(dis, red, [foodx, foody, block_size, block_size])

        # Add the head of the bike to the bike list
        bike_Head = []
        bike_Head.append(x1)
        bike_Head.append(y1)
        bike_List.append(bike_Head)

        if len(bike_List) > Length_of_bike:
            del bike_List[0]

        # Check if the bike collides with itself
        for x in bike_List[:-1]:
            if x == bike_Head:
                game_close = True

        # Draw the bike
        draw_bike(block_size, bike_List)

        # Display the score
        Your_score(Length_of_bike - 1)

        pygame.display.update()

        # Check if the bike eats the food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - block_size) / 20.0) * 20.0
            foody = round(random.randrange(0, dis_height - block_size) / 20.0) * 20.0
            Length_of_bike += 1

        clock.tick(speed)

    pygame.quit()
    quit()

# Start the game
gameLoop()
