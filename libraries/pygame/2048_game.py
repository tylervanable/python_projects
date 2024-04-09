"""
    Tyler's attempt at 2048

    Tyler
    adapted from @Tech With Tim from YouTube
    started 4/9/24
"""


# Import necessary modules. 
import pygame
import random
import math

# Initialize pygame features.
pygame.init()

# Define the constants.
FPS = 60
WIDTH, HEIGHT = 800, 800
ROWS = 4
COLUMNS = 4
RECT_HEIGHT = HEIGHT // ROWS
RECT_WIDTH = WIDTH // COLUMNS
OUTLINE_COLOR = (187, 173, 160)
OUTLINE_THICKNESS = 10
BACKGROUND_COLOR = (205, 192, 180)
FONT_COLOR = (119, 110, 101) 

# Create a pygame window and set pygame constants.
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")
FONT = pygame.font.SysFont("comicsans", 60, bold=True)
MOVE_VELOCITY = 20

# Set the event loop as a main function.
def main(window):
    """ asdasd """

    # Set the clock.
    clock = pygame.time.Clock()
    run = True

    # Run the clock based off the user's frames per second.
    while run:
        clock.tick(FPS)

        # Run an event loop that will register the user's keystrokes and events.
        for event in pygame.event.get():

            # Quit the game loop if the run is set to False. 
            if event.type == pygame.QUIT:
                run = False
                break

# Run the game loop if we are running this file.
if __name__ == "__main__":
    main(WINDOW)


