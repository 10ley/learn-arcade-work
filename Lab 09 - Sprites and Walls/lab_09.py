"""
Lab 9
"""


import arcade

PLAYER_SCALING = .15
TRASH_SCALING = .05
WALL_SCALING = .2
BARRIER_SCALING = .2

DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600
SCREEN_TITLE = "LAB 9"

VIEW_POINT_MARGIN = 200
CAMERA_SPEED = .1
PLAYER_MOVEMENT_SPEED = 5

paper_sound = arcade.load_sound("Paper Crumple Crumpling Scrunch Crunch Sfx.wav")


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=True)

        # Sprite Lists
        self.player_list = None
        self.wall_list = None
        self.trash_list = None
        self.barrier_list = None

        self.score = 0

        # Set up player
        self.player_sprite = None

        # For not running through walls
        self.physics = None

        # Creates cameras
        self.camera_sprites = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

    def setup(self):

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.trash_list = arcade.SpriteList()
        self.barrier_list = arcade.SpriteList()

        # Player set up
        self.player_sprite = arcade.Sprite("janitor-clipart-md.png", PLAYER_SCALING)
        # SPRITE FROM CREAZILLA

        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 100
        self.player_list.append(self.player_sprite)

        # Wall placement
        for y in range(0, 800, 100):
            wall = arcade.Sprite("cubicle-wall-center-clipart-md.png", WALL_SCALING)
            wall.center_x = 0
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(0, 800, 100):
            wall = arcade.Sprite("cubicle-wall-center-clipart-md.png", WALL_SCALING)
            wall.center_x = 800
            wall.center_y = y
            self.wall_list.append(wall)

        for x in range(50, 850, 100):
            wall = arcade.Sprite("cubicle-wall-center-clipart-md.png", WALL_SCALING)
            wall.angle = 90
            wall.center_x = x
            wall.center_y = -20
            self.wall_list.append(wall)

        for x in range(50, 850, 100):
            wall = arcade.Sprite("cubicle-wall-center-clipart-md.png", WALL_SCALING)
            wall.angle = 90
            wall.center_x = x
            wall.center_y = 800
            self.wall_list.append(wall)

        # Barrier Placement
        for x in range(50, 850, 333):
            barrier = arcade.Sprite("file-cabinet-emoji-clipart-md.png", BARRIER_SCALING)
            # From Noto Color Emoji
            barrier.angle = 90
            barrier.center_x = x
            barrier.center_y = 200
            self.wall_list.append(barrier)

        for x in range(50, 650, 150):
            barrier = arcade.Sprite("file-cabinet-emoji-clipart-md.png", BARRIER_SCALING)
            barrier.angle = 90
            barrier.center_x = x
            barrier.center_y = 500
            self.wall_list.append(barrier)

        barrier = arcade.Sprite("file-cabinet-emoji-clipart-md.png", BARRIER_SCALING)
        barrier.center_x = 400
        barrier.center_y = 75
        self.wall_list.append(barrier)

        # Trash Placement
        for x in range(50, 400, 200):
            trash = arcade.Sprite("wastepaper-clipart-md.png", TRASH_SCALING)
            # Open Icons on Pixabay
            trash.center_x = x
            trash.center_y = 100
            self.trash_list.append(trash)

        trash = arcade.Sprite("wastepaper-clipart-md.png", TRASH_SCALING)
        trash.center_x = 700
        trash.center_y = 100
        self.trash_list.append(trash)

        for x in range(50, 800, 200):
            trash = arcade.Sprite("wastepaper-clipart-md.png", TRASH_SCALING)
            trash.center_x = x
            trash.center_y = 350
            self.trash_list.append(trash)

        for x in range(50, 800, 200):
            trash = arcade.Sprite("wastepaper-clipart-md.png", TRASH_SCALING)
            trash.center_x = x
            trash.center_y = 650
            self.trash_list.append(trash)

        self.physics = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):

        arcade.start_render()
        self.camera_sprites.use()

        self.wall_list.draw()
        self.player_list.draw()
        self.barrier_list.draw()
        self.trash_list.draw()

        self.camera_gui.use()

        arcade.draw_rectangle_filled(self.width // 2,
                                     20,
                                     self.width,
                                     40,
                                     arcade.color.GRAY)
        output = f"Score : {self.score}"
        arcade.draw_text(output, 10, 10, arcade.color.BLACK, 20)

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

        self.physics.update()
        self.scroll_to_player()
        hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.trash_list)
        for trash in hit_list:
            trash.remove_from_sprite_lists()
            arcade.play_sound(paper_sound)
            self.score += 1

    def scroll_to_player(self):

        position = (self.player_sprite.center_x - self.width / 2,
                    self.player_sprite.center_y - self.height / 2)
        self.camera_sprites.move_to(position, CAMERA_SPEED)

    def on_resize(self, width, height):

        self.camera_sprites.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))


def main():
    """ Main function """
    window = MyGame(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
