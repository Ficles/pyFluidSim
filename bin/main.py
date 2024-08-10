# Copyright (c) Ficles 2024
import pygame

WIDTH = 1280
HEIGHT = 720
FPS = 60

# Define Colors
BACKGROUND = (0, 0, 0)
DOT = (0, 64, 255)

# Initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fluid Sim")
icon = pygame.image.load("../assets/icon.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

# Game loop
running = True
while running:

    # Process input/events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND)

    pygame.display.flip()     
    clock.tick(FPS)

pygame.quit()