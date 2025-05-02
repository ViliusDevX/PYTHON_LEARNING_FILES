import pygame

pygame.init()

COLOR_WHITE = (255, 255, 255)
COLOR_GREEN = (0, 255, 0)

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tank Game")


def display_frame():
    screen.fill(COLOR_WHITE)

    tank_x, tank_y = 20, 30
    tank_width, tank_height = 50, 50

    pygame.draw.rect(screen, COLOR_GREEN,(tank_x, tank_y, tank_width, tank_height))

    pygame.display.flip()


display_frame()
e = input("Ivesk kazka jeigu nori baigti")

