"""
Testing how to draw stuff
"""
import arcade

# Open a window
arcade.open_window(600, 600, "Drawing Example")
# Sets color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# Getting ready to draw
arcade.start_render()

arcade.draw_lrtb_rectangle_filled(0, 600, 300, 0, arcade.csscolor.GREEN)

arcade.draw_rectangle_filled(100, 320, 20, 60, arcade.csscolor.SIENNA)

# Drawing circle- where and radius
arcade.draw_circle_filled(100, 350, 30, arcade.csscolor.DARK_GREEN)

# Drawing eclipse: center, width, and height
arcade.draw_rectangle_filled(200, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(200, 350, 60, 80, arcade.csscolor.DARK_GREEN)

# Drawing arc
arcade.draw_rectangle_filled(300, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_arc_filled(300, 340, 60, 100, arcade.csscolor.DARK_GREEN, 0, 180)

# Drawing triangle
arcade.draw_rectangle_filled(400, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(400, 400, 370, 320, 430, 320, arcade.csscolor.DARK_GREEN)

# Draw a tree using a polygon with a list of points
arcade.draw_rectangle_filled(500, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_polygon_filled(((500, 400),
                            (480, 360),
                            (470, 320),
                            (530, 320),
                            (520, 360)
                            ),
                           arcade.csscolor.DARK_GREEN)
# Bring paper to make coord map
# Draw a sun
arcade.draw_circle_filled(500, 550, 40, arcade.color.YELLOW)

# Rays to the left, right, up, and down
arcade.draw_line(500, 550, 400, 550, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 600, 550, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 500, 450, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 500, 650, arcade.color.YELLOW, 3)

# Diagonal rays
arcade.draw_line(500, 550, 550, 600, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 550, 500, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 450, 600, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 450, 500, arcade.color.YELLOW, 3)

# Draw text at (150, 230) with a font size of 24 pts.
arcade.draw_text("Arbor Day - Plant a Tree!",
                 150, 230,
                 arcade.color.BLACK, 24)

# Finish drawing
arcade.finish_render()

# Keeps window open
arcade.run()