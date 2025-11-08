import pygame
import random

square1=pygame.Rect(50, 50, 100, 100)
square2=pygame.Rect(200, 50, 100, 100)

def add_custom_event(colors, event_type):
    color = random.choice(colors)
    pygame.event.post(pygame.event.Event(event_type, {'color': color}))
    return color

pygame.init()
screen = pygame.display.set_mode((400, 300))
CUSTOM_COLOR_EVENT = pygame.USEREVENT + 1
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == CUSTOM_COLOR_EVENT:
            if square1.collidepoint(pygame.mouse.get_pos()):
                square1_color = event.color
            if square2.collidepoint(pygame.mouse.get_pos()):
                square2_color = event.color

    if pygame.mouse.get_pressed()[0]:  # Left mouse button
        add_custom_event(colors, CUSTOM_COLOR_EVENT)

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, locals().get('square1_color', (0, 0, 0)), square1)
    pygame.draw.rect(screen, locals().get('square2_color', (0, 0, 0)), square2)
    pygame.display.flip()
pygame.quit()

