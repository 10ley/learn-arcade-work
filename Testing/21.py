""" Sprite Sample Program """

import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
COIN_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Coin(arcade.Sprite):

    def update(self):
        self.center_y -= 1

        if self.center_y < 0:
            self.center_y = SCREEN_HEIGHT

class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Variables that will hold sprite list
        self.player_list = None
        self.coin_list = None

        # Set up player info
        self.player_sprite = None
        self.score = 0

        # Don't show mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite("character.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create coins
        for i in range(COIN_COUNT):
            # Coin image from kenny.nl
            coin = Coin("coin_01.png", SPRITE_SCALING_COIN)

            # position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Add coin to the list
            self.coin_list.append(coin)

    def on_draw(self):
        arcade.start_render()

        self.coin_list.draw()
        self.player_list.draw()

        output = "Score: " + str(self.score)
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 28)

    def on_mouse_motion(self, x, y, dx, dy):
        """Handle Mouse Motion"""

        # Moves center of player sprite to match mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):
        """Movement and game logic"""

        # Call update on all sprites
        self.coin_list.update()

        # Generate a list of all sprites that collide with the player
        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                             self.coin_list)

        # Loop through each colliding sprite, remove it, and add to score
        for coin in coin_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1


def main():
    """ Main method """
    window = MyGame()
    # Need to call set up
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
