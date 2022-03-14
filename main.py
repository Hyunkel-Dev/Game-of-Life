import sys

from config import *
from script.grid import Grid


def set_title(is_running=False):
    game_state = "RUNNING" if is_running else "IDLE"
    title = f"Conway's Game of Life - {game_state}"
    pygame.display.set_caption(title)


pygame.init()
window = pygame.display.set_mode(WINDOW_SIZE)
set_title()

icon = pygame.image.load("assets/icon.png")
pygame.display.set_icon(icon)


grid = Grid()

i = 0
click = False

while True:

    window.fill(WINDOW_COLOR)

    if grid.is_running:
        if i == SPEED * FPS:
            grid.update()
            i = 0
        i += 1
    grid.display()

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT and not grid.is_running:
            grid.set_cell_value(Vector2(event.pos))
            grid.click(Vector2(event.pos))
            click = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == pygame.BUTTON_LEFT and click:
            click = False
        elif event.type == pygame.MOUSEMOTION and click:
            grid.click(Vector2(event.pos))
        elif event.type == pygame.KEYDOWN and event.key == START_KEY and not click:
            grid.is_running = not grid.is_running
            set_title(grid.is_running)

    pygame.time.wait(1000 // FPS)