import pyglet
from src.camera import Camera 
from src.hexdraw import draw_hex_grid, pixel_to_cord
from src.map import Map, load_or_new
from src.hex import FloorHex, LockedHex
import pickle

class GameWindow(pyglet.window.Window) :
    """A window, with the game in it."""

    # If a save already exists, load it, otherwise return new 100x100 map
    map = load_or_new()

    # Radius of hexagons.
    radius = 60

    # Create a camera.
    camera = Camera()

    def on_draw(self):
        """Called whenever a new frame needs to get drawn."""
        
        # Make sure there is no trace of privous stuff left behind.
        self.clear()

        # Make the camera fill up the screen.
        self.camera.size = self.get_size()

        # Apply the camera offset.
        with self.camera:
            # Batchs are a group of opengl commands
            batch = pyglet.graphics.Batch()

            # Draw the floor hex grid
            draw_hex_grid(self.camera.area(), self.map, self.radius, batch)

            # Send the batch to the gpu to get rendered.
            batch.draw()


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

        # Keep track of where the drag started.
        # Used to see if click is drag or a simple press.
        self.drag_start = (x, y)

    def on_mouse_release(self, x, y, button, mod):
        """Called whenever the mouse is released."""

        # If this is the end of a drag, then dont do anything.
        if self.drag_start != (x, y):
            return
        
        # Get the hex that was clicked on.
        cord = pixel_to_cord( self.camera.screen_to_world_position(x, y), self.radius )

        # Destroy the clicked tile >:)
        self.map.get_hex(cord).destroy()

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        """Called when mouse is dragged."""

        self.camera.shift(dx, dy)

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        """Called when scroll."""

        self.camera.zoom(scroll_y)


if __name__ == '__main__' :
    # Initlize the game window.
    GameWindow(800, 600, resizable=True)

    # Start the actuall game.
    pyglet.app.run()
    
