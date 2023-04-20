import time
import numpy as np
import pygame


COLOR_BACKGROUND = (10, 10, 10)
COLOR_GRID = (40, 40, 40)
COLOR_ALIVE_NEXT = (255, 255, 255)
COLOR_DIE_NEXT = (170, 170, 170)


def update(screen, cells, size, with_progress=False):
    """
    screen <- pygame objet
    cells <- numpy matrix
    """

    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))

    for row, col in np.ndindex(cells.shape):
        alive = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col]
        color = COLOR_BACKGROUND if cells[row,col] == 0 else COLOR_ALIVE_NEXT

        if cells[row, col] == 1:
            if alive < 2 or alive >3:
                if with_progress:
                    color = COLOR_DIE_NEXT
            elif 2 <= alive <= 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = COLOR_ALIVE_NEXT
        else:
            if alive == 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = COLOR_ALIVE_NEXT
        
        pygame.draw.rect(screen, color, (col * size, row *size, size - 1, size -1))

    return updated_cells

def gun(board):
    pos = [(5, 1), (6, 1), (5, 11), (6, 11), (7, 11), (5, 2), (6, 2), (4, 12), (3, 13), (3, 14),
           (4, 16), (5, 17), (6, 17), (7, 17), (6, 18), (6, 15), (8, 16), (8, 15), (8, 14), (7, 13),
           (3, 21), (3, 22), (4, 22), (5, 22), (2, 23), (2, 25), (1, 25), (5, 23), (6, 25), (7, 25),
           (3, 35), (3, 36), (4, 35), (4, 36)]

    for y,x in pos:
        board[y][x] = 1

    return board

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    cells = np.zeros((60, 80))
    gun(cells)
    screen.fill(COLOR_GRID)
    update(screen, cells, 10)

    pygame.display.flip()
    pygame.display.update()

    running = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    update(screen, cells, 10)
                    pygame.display.update()
            
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1]//10, pos[0]//10] = 1
                update(screen, cells, size=10)
                pygame.display.update()
            
        screen.fill(COLOR_GRID)

        if running:
            cells = update(screen, cells, size=10, with_progress=True)
            pygame.display.update()

        time.sleep(0.1)


if __name__ == '__main__':
    main()
