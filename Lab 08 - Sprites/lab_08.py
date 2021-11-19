"""
Lab 8
"""

import random
import arcade

# Constants
SPRITE_SCALING_PLAYER = .4
SPRITE_SCALING_FISH = .03
SPRITE_SCALING_WATER = .01
FISH_COUNT = 20
WATER_COUNT = 15

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Fish(arcade.Sprite):
    def reset_pos(self):
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        self.center_y -= random.randrange(1, 5)

        if self.top < 0:
            # Reset the coin to a random spot above the screen
            self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                             SCREEN_HEIGHT + 100)
            self.center_x = random.randrange(SCREEN_WIDTH)


class Water(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 8")

        self.player_list = None
        self.fish_list = None
        self.water_list = None

        self.player_sprite = None
        self.score = 0

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.fish_list = arcade.SpriteList()
        self.water_list = arcade.SpriteList()

        self.score = 0

        self.player_sprite = arcade.Sprite("flying-cat-png-21.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        for i in range(FISH_COUNT):
            fish = Fish("ornamental-fish-farming-7.png", SPRITE_SCALING_FISH)

            fish.center_x = random.randrange(SCREEN_WIDTH)
            fish.center_y = random.randrange(SCREEN_HEIGHT)

            self.fish_list.append(fish)

        for i in range(WATER_COUNT):
            water = Water("water-png-720.png", SPRITE_SCALING_WATER)

            water.center_x = random.randrange(SCREEN_WIDTH)
            water.center_y = random.randrange(SCREEN_HEIGHT)
            water.change_x = random.randrange(-3, 3)
            water.change_y = random.randrange(-3, 3)

            self.water_list.append(water)

    def on_draw(self):
        arcade.start_render()
        self.fish_list.draw()
        self.player_list.draw()
        self.water_list.draw()

        output = f"Score : {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):

        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):
        self.fish_list.update()
        self.water_list.update()

        hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.fish_list)
        for fish in hit_list:
            fish.remove_from_sprite_lists()
            self.score += 1
            if len(hit_list) >= 0:
                arcade.draw_text("Game Over", 350, 250, arcade.color.WHITE, 50)

        bad_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                            self.water_list)

        for water in bad_hit_list:
            water.remove_from_sprite_lists()
            self.score -= 1



def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
