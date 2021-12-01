"""
Final lab
"""

import arcade

PLAYER_SCALING = .4
MISSLE_SCALING = 1
ENEMY_SCALING = .25

DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 800
SCREEN_TITLE = "FINAL LAB"

PLAYER_MOVEMENT_SPEED = 5
MISSLE_MOVEMENT_SPEED = 6
ENEMY_MOVEMENT_SPEED = 4


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # Sprite Lists
        self.player_list = None
        self.missle_list = None
        self.enemy_list = None

        self.lives = 3

        self.score = 0

        self.player_sprite = None

    def setup(self):

        # Sprite Lists
        self.player_list = arcade.SpriteList()
        self.missle_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.shield_list = arcade.SpriteList()

        # Player setup
        self.player_sprite = arcade.Sprite("pngkit_space-ship-png_328881.png", PLAYER_SCALING)
        # Sprite from PNGKIT 
        
        self.player_sprite.center_x = 400
        self.player_sprite.center_y = 100
        self.player_list.append(self.player_sprite)

        # Enemy setup
        self.enemy = arcade.Sprite("alien.png", ENEMY_SCALING)
        # Sprite from PIXELARTMAKER

        self.enemy.center_x = 400
        self.enemy.center_y = 700
        self.enemy_list.append(self.enemy)

        arcade.set_background_color(arcade.color.OUTER_SPACE)
        
    def on_draw(self):
        arcade.start_render()
        
        self.player_list.draw()
        self.missle_list.draw()
        self.enemy_list.draw()
        self.shield_list.draw()

    def on_key_press(self, key, modifiers):

        if key == arcade.key.UP:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0



    def on_update(self, delta_time):
        self.player_list.update()
        self.enemy_list.update()

        hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.missle_list)
        for missle in hit_list:
            missle.remove_from_sprite_lists()
            self.lives -= 1
            if self.lives == 0:
                arcade.draw_text("Game Over", 400, 300, arcade.color.WHITE, 50)


def main():
    """ Main function """
    window = MyGame(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
