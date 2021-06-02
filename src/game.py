import pyglet
import pickle

from pyglet.gl import *

from src.hexdraw import draw_hex_grid, pixel_to_cord
from src.map import Map, load_or_new
from src.hex import FloorHex, LockedHex
from src.gui.camera import Camera
from src.gui.mouse import Mouse
from src.gui.gui import Gui

class Game():
    # If a save already exists, load it, otherwise return new 100x100 map
    map = load_or_new()

    # Radius of hexagons.
    radius = 60

    camera = Camera()
    mouse  = Mouse() 
    gui    = Gui()

    ##################
    # User Interface #
    ##################
    
    @gui.button("save")
    def save(self):
        self.map.pickle_map()

    #################
    # Window Events #
    #################

    def on_draw(self):
        # Apply the camera offset.
        with self.camera:
            # Batchs are a group of opengl commands
            batch = pyglet.graphics.Batch()

            # Draw the floor hex grid
            draw_hex_grid(self.camera.area(), self.map, self.radius, batch)

            # Send the batch to the gpu to get rendered.
            batch.draw()

    def on_resize(self):
        # Update the size of components that needs the size of the screen.
        self.camera.size = self.size 

    ################
    # Mouse Events #
    ################

    def on_mouse_release(self, x, y, button, mod):
        # Get the hex that was clicked on.
        cord = pixel_to_cord( self.camera.screen_to_world_position(x, y), self.radius )

        # Destroy the clicked tile >:)
        self.map.get_hex(cord).destroy()

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        self.camera.shift(dx, dy)

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        self.camera.zoom(scroll_y)

    ###################
    # Keyboard Events #
    ###################

    def on_key_release(self, key, mod):
        if key == pyglet.window.key.S:
            self.save()
        elif key == pyglet.window.key.N:
            self.map = Map(100, 100)
        elif key == pyglet.window.key.D:
            self.map.move_entity_right(self.map.player)
        elif key == pyglet.window.key.A:
            self.map.move_entity_left(self.map.player)
