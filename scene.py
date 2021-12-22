"""
Author: Efrain Gomez Fajardo
TeacherL Comeau, Luc
Purpose: Getting use to creating and calling function by drawing an image using tkinter
Extra Mile:
1. Using random to select between two different images (Morning or night)
2. Using random to generate fixed amount of clouds and trees in random locations
"""

import tkinter as tk
from random import randint

def main():
    # The width and height of the scene window.
    width = 800
    height = 500

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right,scene_bottom):
    """Draw a scene in the canvas. scene_left, scene_top,
    scene_right, and scene_bottom contain the extent in
    pixels of the region where the scene should be drawn.

    Parameters
        scene_left: left side of the region; less than scene_right
        scene_top: top of the region; less than scene_bottom
        scene_right: right side of the region
        scene_bottom: bottom of the region
    Return: nothing

    If needed, the width and height of the
    region can be calculated like this:
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    """
    width = scene_right - scene_left + 1
    height = scene_bottom - scene_top + 1
    image_picker = randint(0, 1)
    if image_picker == 0:
        draw_sky(canvas, width - width, height - height, width , height / 2, 'light blue')
        draw_sun(canvas, scene_left + 10, scene_left + 10, scene_left + 100, scene_left + 100, 'yellow2', 'light blue')
        for _ in range(5):
            draw_cloud(canvas, randint(0, width), randint(0, height / 2), randint(0, width), randint(0, height / 2), 'white', 'white')
        draw_ground(canvas, width - width, height / 2, width, height, 'green3')
        for _ in range(20):
            tree_height = 150
            tree_center = scene_left + randint(scene_left + 50, scene_right - 50)
            tree_top = scene_top + randint(height / 2 - tree_height, height - tree_height)
            draw_pine_tree(canvas, tree_center, tree_top, tree_height)
    else:
        draw_sky(canvas, width - width, height - height, width, height, 'midnight blue')
        draw_sun(canvas, scene_left + 10, scene_left + 10, scene_left + 100, scene_left + 100, 'grey50', 'midnight blue')
        for _ in range(5):
            draw_cloud(canvas, randint(0, width), randint(0, height / 2), randint(0, width), randint(0, height / 2), 'white', 'white')
        draw_ground(canvas, width - width, height / 2, width, height, 'chartreuse4')
        for _ in range(20):
            tree_height = 150
            tree_center = scene_left + randint(scene_left + 50, scene_right - 50)
            tree_top = scene_top + randint(height / 2 - tree_height, height - tree_height)
            draw_pine_tree(canvas, tree_center, tree_top, tree_height)

    # draw_grid(canvas, scene_left, scene_top, scene_right, scene_bottom, 50)

def draw_grid(canvas, left, top, right, botton, grid_spacing):
    """
    Draw a grid useful for reference
    Parameters:
        canvas: 
            Required for drawing
        left, top, right, botton:
            The places where the lines will be drawn
        grid_spacing:
            The spacing in pixels between the lines
        return: nothing

    """
    text_horizontal_margin = 20
    text_vertical_margin = 10

    #Draw horizontal lines
    for i in range(top, botton, grid_spacing):
        canvas.create_line(left, i, right, i)
        canvas.create_text(left + text_horizontal_margin, i + text_vertical_margin, text=f'{i}')

    # Draw vertical lines
    for i in range(left, right, grid_spacing):
        canvas.create_line(i, top, i, botton)
        canvas.create_text(i, top + text_vertical_margin, text=f'{i}')

def draw_pine_tree(canvas, peak_x, peak_y, height):
    """Draw a single pine tree.
    Parameters
        canvas: The tkinter canvas where this
            function will draw a pine tree.
        peak_x, peak_y: The x and y location in pixels where
            this function will draw the top peak of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = peak_x - trunk_width / 2
    trunk_right = peak_x + trunk_width / 2
    trunk_bottom = peak_y + height

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = peak_x - skirt_width / 2
    skirt_right = peak_x + skirt_width / 2
    skirt_bottom = peak_y + skirt_height

    # Draw the trunk of the pine tree.
    canvas.create_rectangle(trunk_left, skirt_bottom,
            trunk_right, trunk_bottom,
            outline="gray20", width=1, fill="tan3")

    # Draw the crown (also called skirt) of the pine tree.
    canvas.create_polygon(peak_x, peak_y,
            skirt_right, skirt_bottom,
            skirt_left, skirt_bottom,
            outline="gray20", width=1, fill="dark green")

def draw_sky(canvas, x0, y0, x1, y2, color):
    canvas.create_rectangle(x0, y0, x1, y2, fill=color)

def draw_cloud(canvas, x0, y0, x1, y1, color, outline_color):
    canvas.create_oval(x0, y0, x1, y1, fill=color, outline=outline_color)

def draw_ground(canvas, x0, y0, x1, y2, color):
    canvas.create_rectangle(x0, y0, x1, y2, fill=color)

def draw_sun(canvas, x0, y0, x1, y2, color, outline_color):
    canvas.create_oval(x0, y0, x1, y2, fill=color, outline=outline_color)

main()