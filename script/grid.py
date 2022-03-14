from config import *


class Grid:

    def __init__(self):
        grid_size = WINDOW_SIZE // CELL_SIZE + 2 * PADDING
        self.table = [[False for _ in range(int(grid_size.x))] for _ in range(int(grid_size.y))]

        self.cell_value = True
        self.is_running = False

    def display(self):
        surface = pygame.display.get_surface()

        for y, line in enumerate(self.table):
            for x, element in enumerate(line):
                position = (Vector2(x, y) - PADDING) * CELL_SIZE
                size = Vector2(CELL_SIZE)

                width = 0 if element else 1
                color = CELL_COLOR if element else GRID_COLOR

                pygame.draw.rect(surface, color, (*position, *size), width)

    def get_adjacent(self, position):
        result = 0
        for y in (-1, 0, 1):
            for x in (-1, 0, 1):
                if (x != 0 or y != 0) and self.table[int(position.y + y)][int(position.x + x)]:
                    result += 1
        return result

    def update(self):
        table = [list(line) for line in self.table]
        for y, line in enumerate(self.table[1:-1]):
            for x, element in enumerate(line[1:-1]):
                position = Vector2(x+1, y+1)
                if element and self.get_adjacent(position) not in (2, 3):
                    self.update_cell(position, table)
                elif not element and self.get_adjacent(position) == 3:
                    self.update_cell(position, table)
        self.table = [list(line) for line in table]

    def set_cell_value(self, position):
        coords = position // CELL_SIZE + PADDING
        self.cell_value = not self.table[int(coords.y)][int(coords.x)]

    def click(self, position):
        coords = position // CELL_SIZE + PADDING
        self.table[int(coords.y)][int(coords.x)] = self.cell_value

    @staticmethod
    def update_cell(position, table):
        table[int(position.y)][int(position.x)] = not table[int(position.y)][int(position.x)]