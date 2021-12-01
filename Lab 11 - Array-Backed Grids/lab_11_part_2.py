"""
Lab 11 part 2
"""

import arcade

ROW_COUNT = 10
COLUMN_COUNT = 10

WIDTH = 20
HEIGHT = 20

MARGIN = 5

SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN

class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):
        """
        Set up the application.
        """
        super().__init__(width, height)
        # Create a 2 dimensional array. A two dimensional
        # array is simply a list of lists.
        self.grid = []
        for row in range(ROW_COUNT):
            # Add an empty array that will hold each cell
            # in this row
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)  # Append a cell

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw the grid
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                # Figure out what color to draw the box
                if self.grid[row][column] == 1:
                    color = arcade.color.GREEN
                else:
                    color = arcade.color.WHITE

                # Do the math to figure out where the box is
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                # Draw the box
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)

    def on_mouse_press(self, x, y, button, modifiers):

        column = x // (WIDTH + MARGIN)
        row = y // (HEIGHT + MARGIN)

        if row < ROW_COUNT and column < COLUMN_COUNT:

            if self.grid[row][column] == 0:
                self.grid[row][column] = 1
            else:
                self.grid[row][column] = 0

        cells = 0
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                if self.grid[row][column] == 1:
                    cells += 1
        print("Total of", cells, "cells are selected.")

        for row in range(ROW_COUNT):
            row_total = 0
            continuous_count = 0
            for column in range(COLUMN_COUNT):
                if self.grid[row][column] == 1:
                    row_total += 1
                    continuous_count += 1
                if self.grid[row][column] == 0:
                    if continuous_count > 2:
                        print("There are", continuous_count, "continuous blocks selected on row", row)
                    continuous_count = 0
            if continuous_count > 2:
                print("There are", continuous_count, "continuous blocks selected on row", row)
            print("Row", row, "has", row_total, "cells are selected.")

        for column in range(COLUMN_COUNT):
            column_total = 0
            for row in range(ROW_COUNT):
                if self.grid[row][column] == 1:
                    column_total += 1
            print("Column", column, "has", column_total, "cells are selected.")


def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()