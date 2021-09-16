"""
Drawing With Functions
"""
import arcade
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500


def invader(x, y):
    arcade.draw_rectangle_filled(x, y, 110, 10, arcade.color.YELLOW)
    arcade.draw_rectangle_filled(x, y + 10, 90, 10, arcade.color.YELLOW)
    arcade.draw_rectangle_filled(x, y + 20, 70, 10, arcade.color.YELLOW)
    arcade.draw_rectangle_filled(x - 20, y + 30, 10, 10, arcade.color.YELLOW)
    arcade.draw_rectangle_filled(x + 20, y + 30, 10, 10, arcade.color.YELLOW)
    arcade.draw_rectangle_filled(x + 30, y + 40, 10, 10, arcade.color.YELLOW)
    arcade.draw_rectangle_filled(x - 30, y + 40, 10, 10, arcade.color.YELLOW)
    arcade.draw_rectangle_filled(x - 50, y - 10, 10, 30, arcade.color.YELLOW)
    arcade.draw_rectangle_filled(x + 50, y - 10, 10, 30, arcade.color.YELLOW)
    arcade.draw_rectangle_filled(x - 30, y - 10, 10, 30, arcade.color.YELLOW)
    arcade.draw_rectangle_filled(x + 30, y - 10, 10, 30, arcade.color.YELLOW)
    arcade.draw_rectangle_filled(x, y - 10, 50, 10, arcade.color.YELLOW)
    arcade.draw_rectangle_filled(x - 15, y - 30, 20, 10, arcade.color.YELLOW)
    arcade.draw_rectangle_filled(x + 15, y - 30, 20, 10, arcade.color.YELLOW)
    arcade.draw_rectangle_filled(x - 20, y + 10, 10, 10, arcade.color.BLACK)
    arcade.draw_rectangle_filled(x + 20, y + 10, 10, 10, arcade.color.BLACK)


def rocket(x, y):
    arcade.draw_rectangle_filled(x, y, 110, 30, arcade.color.GREEN)
    arcade.draw_rectangle_filled(x, y + 20, 90, 10, arcade.color.GREEN)
    arcade.draw_rectangle_filled(x, y + 30, 30, 20, arcade.color.GREEN)
    arcade.draw_rectangle_filled(x, y + 40, 10, 15, arcade.color.GREEN)


def laser(x, y):
    arcade.draw_rectangle_filled(x, y, 10, 30, arcade.color.LIGHT_GREEN)


def shield(x, y):
    arcade.draw_rectangle_filled(x, y, 150, 50, arcade.color.WHITE)
    arcade.draw_rectangle_filled(x, y + 30, 130, 10, arcade.color.WHITE)
    arcade.draw_rectangle_filled(x, y + 40, 110, 10, arcade.color.WHITE)
    arcade.draw_rectangle_filled(x - 60, y - 40, 30, 30, arcade.color.WHITE)
    arcade.draw_rectangle_filled(x + 60, y - 40, 30, 30, arcade.color.WHITE)
    arcade.draw_rectangle_filled(x + 40, y - 30, 10, 10, arcade.color.WHITE)
    arcade.draw_rectangle_filled(x - 40, y - 30, 10, 10, arcade.color.WHITE)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.BLACK)
    arcade.start_render()

    # Drawing
    invader(150, 420)
    invader(300, 370)
    invader(450, 420)
    rocket(300, 30)
    laser(300, 150)
    laser(300, 250)
    shield(150, 150)
    shield(450, 150)

    # Finish and run
    arcade.finish_render()
    arcade.run()


main()
