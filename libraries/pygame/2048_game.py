"""
    Tyler's attempt at 2048

    Tyler
    adapted from @Tech With Tim from YouTube, time stamp 3:40
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

# Define the tiles.
class Tile:
    
    # Set the colors for the different tiles.
    COLORS = [
        (237, 229, 218),
        (238, 225, 201),
        (243, 178, 122),
        (246, 150, 101),
        (247, 124, 95),
        (247, 95, 59),
        (237, 208, 115),
        (237, 204, 99),
        (236, 202, 80),
    ]

    # Define the initialization for the tiles.
    def __init__(self, value, row, column):
        """Initialize tile values."""
        self.value = value
        self.row = row
        self.column = column
        self.x = column * RECT_WIDTH
        self.y = row * RECT_HEIGHT

    # Define how which color fits each tile.
    def get_color(self):
        """Define the color values."""

        # Find the log and assign it to our color_index variable.
        color_index = int(math.log2(self.value)) - 1

        # Assign the appropriate color_index value to the color variable. 
        color = self.COLORS[color_index]
        
        # Return the color variable
        return color

    # Define the draw function again.
    def draw(self, window):
        """Define another draw function."""

        # Obtain the color.
        color = self.get_color()

        # Draw the rectangles.
        pygame.draw.rect(window, color, (self.x, self.y, RECT_WIDTH, RECT_HEIGHT))

        # Generate text that will be written in middle of the rectangle.
        text = FONT.render(str(self.value), 1, FONT_COLOR)
        window.blit(
            text,
            (
            # Center the text.
                self.x + (RECT_WIDTH / 2 - text.get_width() / 2),
                self.y + (RECT_HEIGHT / 2 - text.get_height() / 2),
            ),
        )

    # Define the set position function.
    def set_position(self):
        """Define the set position function."""
        pass

    # Define the movement function.
    def move(self,delta):
        """Define our movement function."""
        pass


# Draw the horizontal and vertical lines, as a grid, for the game.
def draw_grid(window):
    """Draw the grid for the game."""

    # Draw the grid with 4 rows with a loop. 
    for row in range(1, ROWS):

        # Update the y value. 
        y = row * RECT_HEIGHT

        # Draw the rows. 
        pygame.draw.line(window, OUTLINE_COLOR, (0, y), (WIDTH, y), OUTLINE_THICKNESS)

    # Draw the grid with 4 columns with a loop. 
    for column in range(1, COLUMNS):

        # Update the y value. 
        x = column * RECT_HEIGHT

        # Draw the columns. 
        pygame.draw.line(window, OUTLINE_COLOR, (x, 0), (x, HEIGHT), OUTLINE_THICKNESS)

        
    # Draw the outline with the appropriate thickness and color. 
    pygame.draw.rect(window, OUTLINE_COLOR, (0, 0, WIDTH, HEIGHT), OUTLINE_THICKNESS)

# Draw the borders and boxes for the game.
def draw(window, tiles):
    """Draw the background color and grid in pygame."""

    # Set the background color.
    window.fill(BACKGROUND_COLOR)

    # Draw all the tiles, so gridlines are separated.
    for tile in tiles.values():
        tile.draw(window)
        
    # Invoke the draw function to draw the grid.
    draw_grid(window)

    # Update the screen.
    pygame.display.update()
    

# Set the event loop as a main function
def main(window):
    """Handle the event loop that controls the game."""

    # Set the clock.
    clock = pygame.time.Clock()
    run = True

    # Locate and store the tiles.
    tiles = {"00": Tile(4, 0, 0), "20": Tile(128, 2, 0)}

    # Run the clock based off the user's frames per second.
    while run:
        clock.tick(FPS)

        # Run an event loop that will register the user's keystrokes and events.
        for event in pygame.event.get():

            # Quit the game loop if the run is set to False. 
            if event.type == pygame.QUIT:
                run = False
                break

        # Invoke the draw_background function during gameplay.
        draw(window, tiles)

# Run the game loop if we are running this file.
if __name__ == "__main__":
    main(WINDOW)


