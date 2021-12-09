"""
Final lab
"""

import arcade
import math
import random
import os

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

laser_fire = arcade.load_sound("laserfire01.wav")
boom = arcade.load_sound("8bit_bomb_explosion.wav")
music2 = arcade.load_sound("spaceship.wav")
powerup_sound = arcade.load_sound("SFX_Powerup_01.wav")


PLAYER_SCALING = .4
BULLET_SCALING = .25
ENEMY_SCALING = .2
ASTROID_SCALING = .05
HEART_SCALING = .15

DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 800
SCREEN_TITLE = "FINAL LAB"

PLAYER_MOVEMENT_SPEED = 5
BULLET_SPEED = 8
ENEMY_MOVEMENT_SPEED = 4
ASTROID_MOVEMENT_SPEED = 7
HEART_MOVEMENT = 5

ASTROID_COUNT = 10


class MenuView(arcade.View):
    """
    First Menu
    """

    def on_show(self):
        arcade.set_background_color(arcade.color.OUTER_SPACE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("INVASION", DEFAULT_SCREEN_WIDTH / 2, DEFAULT_SCREEN_HEIGHT / 2,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Click to advance", DEFAULT_SCREEN_WIDTH / 2, DEFAULT_SCREEN_HEIGHT / 2 - 75,
                         arcade.color.LIGHT_GRAY, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        instructions_view = InstructionView()
        self.window.show_view(instructions_view)


class InstructionView(arcade.View):
    """
    Instructions
    """

    def on_show(self):
        arcade.set_background_color(arcade.color.SPACE_CADET)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Instructions Screen", 400, 700,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Attack the aliens"
                         , 400, 500,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Space to shoot"
                         , 400, 425,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Arrows to move"
                         , 400, 350,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("SURVIVE"
                         , 400, 275,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Click to advance", 400, 100,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView()
        self.window.show_view(game_view)


class Lifeup(arcade.Sprite):
    """
    Lifeup powerup sprite set up
    """
    def __init__(self, filename, scaling):

        super().__init__(filename, HEART_SCALING)

        self.change_x = 0
        self.change_y = 0

    def update(self):

        # Move the coin
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.change_x *= -1

        if self.right > DEFAULT_SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > DEFAULT_SCREEN_HEIGHT + 150:
            self.change_y *= -1


class Astroid(arcade.Sprite):
    """
    Astroid set up
    """

    def reset_pos(self):

        self.center_y = random.randrange(DEFAULT_SCREEN_HEIGHT + 20,
                                         DEFAULT_SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(DEFAULT_SCREEN_WIDTH)

    def update(self):

        self.center_y -= ASTROID_MOVEMENT_SPEED

        if self.top < 0:
            self.reset_pos()


class Enemy(arcade.Sprite):
    """
    Enemy logic
    """

    def __init__(self, image, scale, position_list):
        super().__init__(image, scale)
        self.position_list = position_list
        self.cur_position = 0
        self.speed = ENEMY_MOVEMENT_SPEED

    def update(self):
        """ Have a sprite follow a path """
        start_x = self.center_x
        start_y = self.center_y

        dest_x = self.position_list[self.cur_position][0]
        dest_y = self.position_list[self.cur_position][1]

        x_diff = dest_x - start_x
        y_diff = dest_y - start_y

        angle = math.atan2(y_diff, x_diff)

        distance = math.sqrt((self.center_x - dest_x) ** 2 + (self.center_y - dest_y) ** 2)

        speed = min(self.speed, distance)

        change_x = math.cos(angle) * speed
        change_y = math.sin(angle) * speed

        self.center_x += change_x
        self.center_y += change_y

        distance = math.sqrt((self.center_x - dest_x) ** 2 + (self.center_y - dest_y) ** 2)

        if distance <= self.speed:
            self.cur_position += 1

            if self.cur_position >= len(self.position_list):
                self.cur_position = 0


class GameView(arcade.View):
    """
    Main Game
    """

    def __init__(self):
        super().__init__()

        self.time_taken = 0

        # Sprite Lists
        self.player_list = None
        self.enemy_list = None
        self.player_bullet = None
        self.astroid_list = None
        self.enemy_bullet = None

        self.frame_count = 0
        self.score = 0
        self.player_sprite = None
        self.lives = 3
        self.done = False
        self.lifeup = None

        # Sprite Lists
        self.player_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.player_bullet = arcade.SpriteList()
        self.astroid_list = arcade.SpriteList()
        self.lifeup = arcade.SpriteList()
        self.enemy_bullet = arcade.SpriteList()

        # Player setup
        self.player_sprite = arcade.Sprite("pngkit_space-ship-png_328881.png", PLAYER_SCALING)
        # Sprite from PIXELARTMAKER
        
        self.player_sprite.center_x = 400
        self.player_sprite.center_y = 100
        self.player_list.append(self.player_sprite)

        position_list = [[700, 800],
                         [700, 700],
                         [100, 700],
                         [100, 650],
                         [700, 650],
                         [700, 600],
                         [100, 600],
                         [100, 550],
                         [700, 550],
                         [700, 500],
                         [100, 500],
                         [100, 450],
                         [700, 450],
                         [700, 400],
                         [100, 400],
                         [100, 350],
                         [700, 350],
                         [700, 300],
                         [100, 300],
                         [100, 250],
                         [700, 250],
                         [400, 200]]

        # Create the enemy
        ycoord = 0
        for i in range(10):
            enemy = Enemy("alien.png",
                          ENEMY_SCALING,
                          position_list)
            # Sprite from PNGKIT

            enemy.center_y = position_list[0][1] + ycoord
            enemy.center_x = position_list[1][1]
            ycoord += 500
            self.enemy_list.append(enemy)

        # Creating astroids
        for i in range(ASTROID_COUNT):
            astroid = Astroid("e1b72fdc59bc3b1.png", ASTROID_SCALING)
            # Art from nivannono

            astroid.center_x = random.randrange(DEFAULT_SCREEN_WIDTH)
            astroid.center_y = random.randrange(DEFAULT_SCREEN_HEIGHT) + 1000

            self.astroid_list.append(astroid)

        # Creating lifeup sprites
        for i in range(3):
            life = Lifeup("heart pixel art 254x254.png", HEART_SCALING)
            # Art from Dansevenstar

            life.center_x = random.randrange(DEFAULT_SCREEN_WIDTH)
            life.center_y = DEFAULT_SCREEN_HEIGHT + 50
            life.change_x = random.randrange(-3, 4)
            life.change_y = random.randrange(-3, 4)
            self.lifeup.append(life)

    def on_show(self):
        arcade.set_background_color(arcade.color.OUTER_SPACE)

    def on_draw(self):
        # Start drawing
        arcade.start_render()
        self.player_list.draw()
        self.enemy_list.draw()
        self.player_bullet.draw()
        self.astroid_list.draw()
        self.lifeup.draw()
        self.enemy_bullet.draw()

        output = f"Score : {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)
        output = f"Lives : {self.lives}"
        arcade.draw_text(output, 10, 40, arcade.color.WHITE, 14)

    def on_key_press(self, key, modifiers):
        # Player movement
        if key == arcade.key.LEFT:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
        # Bullets
        elif key == arcade.key.SPACE:
            bullet = arcade.Sprite("bullet.png", BULLET_SCALING)
            # Sprite from PIXELARTMAKER
            bullet.angle = 90
            bullet.change_y = BULLET_SPEED
            arcade.play_sound(laser_fire)

            bullet.center_x = self.player_sprite.center_x
            bullet.bottom = self.player_sprite.top

            self.player_bullet.append(bullet)

    def on_key_release(self, key, modifiers):

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):

        self.frame_count += 1
        self.time_taken += delta_time
        self.player_list.update()
        self.enemy_list.update()
        self.player_bullet.update()

        for bullet in self.player_bullet:
            hit_list = arcade.check_for_collision_with_list(bullet, self.enemy_list)
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()
                position_list = [[700, 800],
                                 [700, 700],
                                 [100, 700],
                                 [100, 650],
                                 [700, 650],
                                 [700, 600],
                                 [100, 600],
                                 [100, 550],
                                 [700, 550],
                                 [700, 500],
                                 [100, 500],
                                 [100, 450],
                                 [700, 450],
                                 [700, 400],
                                 [100, 400],
                                 [100, 350],
                                 [700, 350],
                                 [700, 300],
                                 [100, 300],
                                 [100, 250],
                                 [700, 250],
                                 [400, 200]]
                ycoord = 1000
                for i in range(2):
                    enemy = Enemy("alien.png",
                                  ENEMY_SCALING,
                                  position_list)
                    # Sprite from PNGKIT
                    enemy.center_y = position_list[0][1] + ycoord
                    enemy.center_x = position_list[1][1]
                    ycoord += 500
                    self.enemy_list.append(enemy)

            for enemy in hit_list:
                enemy.remove_from_sprite_lists()
                self.score += 1
                arcade.play_sound(boom)

                if bullet.bottom > DEFAULT_SCREEN_HEIGHT:
                    bullet.remove_from_sprite_lists()

        for enemy in self.enemy_list:
            if enemy.center_y <= 225:
                self.lives -= 1
                enemy.remove_from_sprite_lists()

        if self.lives <= 0:
            self.done = True
            game_over_view = GameOverView()
            game_over_view.time_taken = self.time_taken
            self.window.set_mouse_visible(True)
            self.window.show_view(game_over_view)

        bad_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.astroid_list)

        if self.score >= 10:
            self.astroid_list.update()
            for astroid in bad_hit_list:
                astroid.reset_pos()
                astroid.remove_from_sprite_lists()
                self.lives -= 1

        lifeup_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.lifeup)

        if self.score >= 30:
            self.lifeup.update()
            for life in lifeup_hit_list:
                arcade.play_sound(powerup_sound)
                life.remove_from_sprite_lists()
                self.lives += 1

        if self.time_taken >= 30:
            for enemy in self.enemy_list:
                if self.frame_count % 100 == 0:
                    bullet2 = arcade.Sprite("874fa0e5bf7b854.png", BULLET_SCALING)
                    # Sprite from PIXELARTMAKER
                    bullet2.angle = 0
                    bullet2.change_y = - BULLET_SPEED
                    arcade.play_sound(laser_fire)

                    bullet2.center_x = enemy.center_x
                    bullet2.bottom = enemy.bottom

                    self.enemy_bullet.append(bullet2)

        for bullet2 in self.enemy_bullet:
            if bullet2.top < 0:
                bullet2.remove_from_sprite_lists()

        self.enemy_bullet.update()

        bullet_hitlist = arcade.check_for_collision_with_list(self.player_sprite, self.enemy_bullet)

        for bullet2 in bullet_hitlist:
            arcade.play_sound(boom)
            bullet2.remove_from_sprite_lists()
            self.lives -= 1



class GameOverView(arcade.View):
    def __init__(self):
        super().__init__()
        self.time_taken = 0

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        """
        Draw "Game over" across the screen.
        """
        arcade.draw_text("Game Over", 230, 400, arcade.color.WHITE, 54)
        arcade.draw_text("Click to restart", 300, 325, arcade.color.WHITE, 24)

        time_taken_formatted = f"{round(self.time_taken, 2)} seconds"
        arcade.draw_text(f"Time taken: {time_taken_formatted}",
                         DEFAULT_SCREEN_WIDTH / 2,
                         200,
                         arcade.color.GRAY,
                         font_size=15,
                         anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView()
        self.window.show_view(game_view)


def main():
    """ Main function """
    window = arcade.Window(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE)
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()


if __name__ == "__main__":
    main()
