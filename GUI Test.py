import pygame

# Initialize Pygame
pygame.init()

# Set the window size
screen_size = (1280, 800)

# Create the window
screen = pygame.display.set_mode(screen_size)

# Set the window caption
pygame.display.set_caption("My Pygame Template")

# Define some colors
black = (0, 0, 0)
white = (255, 255, 255)

# Create a font for the text box
font = pygame.font.Font(None, 32)

# Create a surface for the text box
text_surface = font.render("Text Box", True, black)

# Set the size of the side bar
side_bar_size = (200, 800)

# Set the position of the side bar
side_bar_pos = (0, 0)

# Set the size of the text box
text_box_size = (1080, 100)

# Set the position of the text box
text_box_pos = (200, 700)

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(white)

    # Draw the side bar
    pygame.draw.rect(screen, black, side_bar_pos + side_bar_size)

    # Create a new text box surface with an alpha value of 128
    text_box_surface = pygame.Surface(text_box_size, pygame.SRCALPHA)
    text_box_surface.set_alpha(128)

    # Blit the text surface onto the text box surface
    text_box_surface.blit(text_surface, (0, 0))

    # Blit the text box surface onto the screen
    screen.blit(text_box_surface, text_box_pos)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()