""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3

laser_sound = arcade.load_sound("laser.wav")
laser_button = arcade.load_sound("laserfire01.wav")


class Rocket:
    def __init__(self, position_x, position_y, change_x, change_y):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y

    def draw(self):
        arcade.draw_rectangle_filled(self.position_x, self.position_y, 110, 30, arcade.color.GREEN)
        arcade.draw_rectangle_filled(self.position_x, self.position_y + 20, 90, 10, arcade.color.GREEN)
        arcade.draw_rectangle_filled(self.position_x, self.position_y + 30, 30, 20, arcade.color.GREEN)
        arcade.draw_rectangle_filled(self.position_x, self.position_y + 40, 10, 15, arcade.color.GREEN)

    def update(self):
        self.position_x += self.change_x
        self.position_y += self.change_y

        if self.position_x + 55 > SCREEN_WIDTH:
            self.position_x = SCREEN_WIDTH - 55
            arcade.play_sound(laser_sound)

        if self.position_x - 55 < 0:
            self.position_x = 55
            arcade.play_sound(laser_sound)

        if self.position_y + 45 > SCREEN_HEIGHT:
            self.position_y = SCREEN_HEIGHT - 45
            arcade.play_sound(laser_sound)

        if self.position_y - 15 < 0:
            self.position_y = 15
            arcade.play_sound(laser_sound)


class Invader:
    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y

    def draw(self):
        arcade.draw_rectangle_filled(self.position_x, self.position_y, 110, 10, arcade.color.YELLOW)
        arcade.draw_rectangle_filled(self.position_x, self.position_y + 10, 90, 10, arcade.color.YELLOW)
        arcade.draw_rectangle_filled(self.position_x, self.position_y + 20, 70, 10, arcade.color.YELLOW)
        arcade.draw_rectangle_filled(self.position_x - 20, self.position_y + 30, 10, 10, arcade.color.YELLOW)
        arcade.draw_rectangle_filled(self.position_x + 20, self.position_y + 30, 10, 10, arcade.color.YELLOW)
        arcade.draw_rectangle_filled(self.position_x + 30, self.position_y + 40, 10, 10, arcade.color.YELLOW)
        arcade.draw_rectangle_filled(self.position_x - 30, self.position_y + 40, 10, 10, arcade.color.YELLOW)
        arcade.draw_rectangle_filled(self.position_x - 50, self.position_y - 10, 10, 30, arcade.color.YELLOW)
        arcade.draw_rectangle_filled(self.position_x + 50, self.position_y - 10, 10, 30, arcade.color.YELLOW)
        arcade.draw_rectangle_filled(self.position_x - 30, self.position_y - 10, 10, 30, arcade.color.YELLOW)
        arcade.draw_rectangle_filled(self.position_x + 30, self.position_y - 10, 10, 30, arcade.color.YELLOW)
        arcade.draw_rectangle_filled(self.position_x, self.position_y - 10, 50, 10, arcade.color.YELLOW)
        arcade.draw_rectangle_filled(self.position_x - 15, self.position_y - 30, 20, 10, arcade.color.YELLOW)
        arcade.draw_rectangle_filled(self.position_x + 15, self.position_y - 30, 20, 10, arcade.color.YELLOW)
        arcade.draw_rectangle_filled(self.position_x - 20, self.position_y + 10, 10, 10, arcade.color.BLACK)
        arcade.draw_rectangle_filled(self.position_x + 20, self.position_y + 10, 10, 10, arcade.color.BLACK)


class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")
        # Draw invader
        self.invader = Invader(100, 100)

        # Draw Rocket
        self.rocket = Rocket(300, 300, 0, 0)

        self.set_mouse_visible(False)

    def on_draw(self):
        arcade.start_render()

        arcade.set_background_color(arcade.color.BLACK)
        arcade.draw_circle_filled(125, 425, 325, (252, 251, 254))
        arcade.draw_ellipse_filled(60, 540, 70, 90, (232, 231, 234), 120)
        arcade.draw_ellipse_filled(100, 400, 100, 120, (232, 231, 234), 60)
        arcade.draw_ellipse_filled(10, 200, 120, 100, (232, 231, 234), 90)
        arcade.draw_ellipse_filled(300, 275, 100, 150, (232, 231, 234), 45)
        arcade.draw_ellipse_filled(330, 500, 120, 140, (232, 231, 234), 140)
        arcade.draw_ellipse_filled(200, 620, 150, 120, (232, 231, 234), 40)
        arcade.draw_circle_outline(125, 425, 330, (118, 73, 254), 10)

        self.invader.draw()
        self.rocket.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        self.invader.position_x = x
        self.invader.position_y = y

    def on_mouse_press(self, x, y, button, modifiers):

        if button == arcade.MOUSE_BUTTON_LEFT:
            arcade.play_sound(laser_button)

    def on_update(self, delta_time):
        self.rocket.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.A or key == arcade.key.LEFT:
            self.rocket.change_x = - MOVEMENT_SPEED
        elif key == arcade.key.D or key == arcade.key.RIGHT:
            self.rocket.change_x = MOVEMENT_SPEED
        elif key == arcade.key.W or key == arcade.key.UP:
            self.rocket.change_y = MOVEMENT_SPEED
        elif key == arcade.key.S or key == arcade.key.DOWN:
            self.rocket.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT or key == arcade.key.A or key == arcade.key.D:
            self.rocket.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN or key == arcade.key.W or key == arcade.key.S:
            self.rocket.change_y = 0


def main():
    window = MyGame()
    arcade.run()


main()
