import pygame
import random

# Constants
CELL_SIZE = 60
MARGIN = 5
GRID_SIZE = 5
WIDTH = GRID_SIZE * CELL_SIZE + MARGIN * 2
HEIGHT = GRID_SIZE * CELL_SIZE + MARGIN * 2

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("N-Queens Problem Visualization")


class Chessboard:
    def __init__(self, size):
        self.size = size
        self.queens = []
        self.solutions = []

    def is_safe(self, row, col):
        for q_row, q_col in self.queens:
            if q_col == col or q_row - q_col == row - col or q_row + q_col == row + col:
                return False
        return True

    def solve_n_queens(self, row=0):
        if row == self.size:
            self.solutions.append(self.queens[:])
            return True

        for col in range(self.size):
            if self.is_safe(row, col):
                self.queens.append((row, col))
                self.solve_n_queens(row + 1)
                self.queens.pop()

    def draw(self):
        screen.fill(WHITE)

        # Draw board
        for row in range(self.size):
            for col in range(self.size):
                x = MARGIN + col * CELL_SIZE
                y = MARGIN + row * CELL_SIZE
                pygame.draw.rect(screen, BLACK, (x, y, CELL_SIZE, CELL_SIZE), 1)

        # Draw queens
        for row, col in self.queens:
            x = MARGIN + col * CELL_SIZE + CELL_SIZE // 2
            y = MARGIN + row * CELL_SIZE + CELL_SIZE // 2
            pygame.draw.circle(screen, RED, (x, y), CELL_SIZE // 4)

        pygame.display.flip()


def main():
    board = Chessboard(GRID_SIZE)
    board.solve_n_queens()

    running = True
    solution_index = 0
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if board.solutions:
            board.queens = board.solutions[solution_index]
            board.draw()
            pygame.time.wait(1000)
            solution_index = (solution_index + 1) % len(board.solutions)

        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()