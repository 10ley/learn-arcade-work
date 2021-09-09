"""
Drawing a picture
"""

# importing the arcade library
import arcade

# opening a window
arcade.open_window(600, 600, "Drawing in Python")

# setting a background color
arcade.set_background_color((29, 17, 53))

# getting ready to draw
arcade.start_render()

# creating moon
arcade.draw_circle_filled(125, 425, 325, (252, 251, 254))
arcade.draw_ellipse_filled(60, 540, 70, 90, (232, 231, 234), 120)
arcade.draw_ellipse_filled(100, 400, 100, 120, (232, 231, 234), 60)
arcade.draw_ellipse_filled(10, 200, 120, 100, (232, 231, 234), 90)
arcade.draw_ellipse_filled(300, 275, 100, 150, (232, 231, 234), 45)
arcade.draw_ellipse_filled(330, 500, 120, 140, (232, 231, 234), 140)
arcade.draw_ellipse_filled(200, 620, 150, 120, (232, 231, 234), 40)
arcade.draw_circle_outline(125, 425, 330, (118, 73, 254), 10)

# Shooting star
arcade.draw_arc_filled(550, 400, 300, 300, (255, 200, 102), 130, 170, 80, 180)
arcade.draw_circle_outline(550, 400, 25, (243, 237, 255), 2)
arcade.draw_rectangle_filled(550, 400, 50, 8, (255, 237, 97), 60)
arcade.draw_rectangle_filled(550, 400, 50, 8, (255, 237, 97), 120)
arcade.draw_rectangle_filled(550, 400, 50, 8, (255, 237, 97), 180)

# UFO
arcade.draw_arc_filled(500, 100, 500, 400, (188, 255, 140), 60, 80, 70, 300)
arcade.draw_ellipse_filled(512, 88, 60, 50, (150, 150, 150), 130)
arcade.draw_ellipse_filled(500, 100, 100, 30, (240, 240, 240), 130)

# Finish drawing
arcade.finish_render()

# Keep the window
arcade.run()
