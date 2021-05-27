import pyglet
from src.hexdraw import draw_hex_grid, pixel_to_cord
from src.map import Map
from src.hex import FloorHex, LockedHex

class GameWindow(pyglet.window.Window) :
    """A window, with the game in it."""

    map = Map(100, 100)

    radius = 60

    def on_draw(self) :
        """Called whenever a new frame needs to get drawn."""
        
        # Make sure there is no trace of privous stuff left behind.
        self.clear()

        # Batchs are a group of opengl commands that will
        # be sent to the gpu to be rendered.
        batch = pyglet.graphics.Batch()

        # Draw the floor hex grid
        draw_hex_grid(
            # The size of the grid should just be the size of the screen.
            # The width and height are doubled for some reason.
            size = (
                self.width / 2,
                self.height / 2
            ),

            # Pass in the map we want to draw.
            map = self.map,

            # Radius of hexagon.
            radius = self.radius,

            # Pass in the batch so that the commands can be added to it.
            batch = batch
        )

        # Send the batch to the gpu to get rendered.
        batch.draw()
    
    def on_key_press(self, key, mod) :
        """Called whenever a key is pressed."""

        pass

    def on_mouse_press(self, x, y, button, mod) :
        """Called whenever the mouse is clicked."""

        # Get the hex that was clicked on.
        cord = pixel_to_cord((x, y), self.radius)

        # Make the clicked on tile a LockedHex.
        self.map.set_hex(cord, LockedHex())

        

if __name__ == '__main__' :
    # Initlize the game window.
    GameWindow(800, 600, resizable=True)

    # Start the actuall game.
    pyglet.app.run()
