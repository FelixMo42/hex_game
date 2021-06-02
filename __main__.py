import pyglet
from pyglet.gl import *

from src.gui.camera import Camera 
from src.gui.mouse import Mouse
from src.gui.gui import Gui

from src.hexdraw import draw_hex_grid, pixel_to_cord
from src.map import Map, load_or_new
from src.hex import FloorHex, LockedHex
import pickle

import sys

# Make so that all files can import from src
sys.path.insert(1, './')

class GameWindow(pyglet.window.Window) :
    """A window, with the game in it."""

    # If a save already exists, load it, otherwise return new 100x100 map
    map = load_or_new()

    # Radius of hexagons.
    radius = 60

    # Create a camera.
    camera = Camera()

    # Create a gui.
    gui = Gui([
        ("testing", lambda self: print("hellya!")),
        ("bla", lambda self: self.do_this_thing_when_clicked())
    ])

    # Keeps track of mouse information
    mouse = Mouse()

    def do_this_thing_when_clicked(self):
        print("bla")

    def on_draw(self):
        """Called whenever a new frame needs to get drawn."""
        
        # Make sure there is no trace of privous stuff left behind.
        self.clear()

        self.camera.size = self.get_size()

        # Apply the camera offset.
        with self.camera:
            # Batchs are a group of opengl commands
            batch = pyglet.graphics.Batch()

            # Draw the floor hex grid
            draw_hex_grid(self.camera.area(), self.map, self.radius, batch)

            # Send the batch to the gpu to get rendered.
            batch.draw()

        # Draw the gui on top of the game.
        self.gui.draw(self.mouse.position)

    def on_key_press(self, key, mod):
        """Called whenever a key is pressed."""

        if key == pyglet.window.key.S:
            self.map.pickle_map()
        elif key == pyglet.window.key.N:
            self.map = Map(100, 100)
        elif key == pyglet.window.key.D:
            self.map.move_entity_right(self.map.player)
        elif key == pyglet.window.key.A:
            self.map.move_entity_left(self.map.player)

        print("Player cord: " + str(self.map.player.cord))

    def on_mouse_press(self, x, y, button, mod):
        """Called whenever the mouse is pressed."""

        # Only register a drag start if mouse is not over the gui. 
        # Used to see if click is drag or a simple press.
        if not self.gui.is_over((x, y)):
            self.mouse.drag_start(x, y)

    def on_mouse_release(self, x, y, button, mod):
        """Called whenever the mouse is released."""

        # If this is the end of a drag, then dont do anything.
        if self.mouse.drag_end(x, y):
            return

        if self.gui.is_over((x, y)):
            self.gui.click(self)

        else:
            # Get the hex that was clicked on.
            cord = pixel_to_cord( self.camera.screen_to_world_position(x, y), self.radius )

            # Destroy the clicked tile >:)
            self.map.get_hex(cord).destroy()

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        """Called when mouse is dragged."""

        # We still want to update the mouse position when dragging.
        self.mouse.set_mouse_pos(x, y)

        # If the drag was never triggered using mouse.start_drag, then we should bail.
        if not self.mouse.is_drag():
            return

        # Camera go weeeeeee!
        self.camera.shift(dx, dy)

    def on_mouse_motion(self, x, y, dx, dy):
        """Called when the mouse is moved, but not pressed."""

        self.mouse.set_mouse_pos(x, y)

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        """Called when scroll."""

        self.camera.zoom(scroll_y)

    def on_resize(self, width, height):
        """Called when window is resized."""

        # Update the size of components that needs the size of the screen.
        self.camera.size = self.get_size()
        self.gui.size = self.get_size()

        # Pyglet requires we call the default resize method.
        return super().on_resize(width, height)
        
if __name__ == '__main__' :
    # Initlize the game window.
    GameWindow(800, 600, resizable=True)

    # Start the actuall game.
    pyglet.app.run()
    
