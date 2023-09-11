# Import the functions from the Draw 2-D library
# so that they can be used in this program.
import random
from turtle import width
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, scene_height / 3,
        scene_width, scene_height, width=0, fill="sky blue")
   ## Clouds
    half_height = round(scene_height)
    min_diam = 15
    max_diam = 50
    for i in range(200):
        x = random.randint(0, scene_width - max_diam)
        y = random.randint(0, half_height)
        diameter = random.randint(min_diam, max_diam)
        draw_oval(canvas, x, y, x + diameter, y + diameter,
                fill="white")
    ## Birds
#     draw_arc(canvas, scene_width, scene_height)
# def draw_arc(canvas, scene_width, scene_height):
#     draw_arc(canvas, 100, 100, 300, 200, start=180, extent=270)
def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="tan4")

    #pine tree
    tree_center_x = 290
    tree_bottom = 160
    tree_height = 160
    draw_pine_tree(canvas, tree_center_x,tree_bottom,tree_height)
    #pine tree
    tree_center_x = 230
    tree_bottom = 130
    tree_height = 180
    draw_pine_tree(canvas, tree_center_x,tree_bottom,tree_height)
    # Draw a pine tree.
    tree_center_x = 170
    tree_bottom = 100
    tree_height = 200
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)

    # Draw 2nd Pine Tree
    tree_center_x = 90
    tree_bottom = 70
    tree_height = 220
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    
    # Draw 3rd Pine Tree
    tree_center_x = 30
    tree_bottom = 40
    tree_height = 240
    draw_pine_tree(canvas, tree_center_x,tree_bottom,tree_height)
    # Draw rigth side pine tree
    tree_center_x= 710
    tree_bottom = 70
    tree_height= 220
    draw_pine_tree(canvas,tree_center_x,tree_bottom,tree_height)
    # Draw right side pine tree
    tree_center_x = 770
    tree_bottom = 40
    tree_height = 240
    draw_pine_tree(canvas,tree_center_x,tree_bottom,tree_height)

    # Draw Fence
    draw_fence(canvas, scene_width,scene_height)
    ## Draw Grass
    draw_grass(canvas, scene_width, scene_height)

def draw_pine_tree(canvas, center_x, bottom, height):
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    # Draw the trunk of the pine tree.
    draw_rectangle(canvas,
            trunk_left, trunk_top, trunk_right, bottom,
            outline="gray20", width=1, fill="tan3")

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    # Draw the crown (also called skirt) of the pine tree.
    draw_polygon(canvas, center_x, skirt_top,
            skirt_right, trunk_top,
            skirt_left, trunk_top,
            outline="gray20", width=1, fill="dark green")
def draw_fence(canvas, scene_width, scene_height):
    x_start = 0
    y_start = 0
    fence_width = 50
    fence_color = "black"
    for _ in range(20):
        draw_rectangle(canvas, x_start, y_start, x_start + fence_width, 100, fill = fence_color, outline = fence_color)
        x_start += fence_width +10
def draw_grass(canvas, scence_width, scene_height):
    x_start = 0
    y_start = 0
    grass_width = 15
    fence_color = "green1"
    for _ in range(50):
        grass_heigth = random.randint(10, 50)
        draw_rectangle(canvas, x_start, y_start, x_start + grass_width, grass_heigth, fill = fence_color, outline = fence_color)
        x_start += grass_width +2
# Call the main function so that
# this program will start executing.
main()