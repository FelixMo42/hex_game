import pyglet
from src.hexdraw import draw_hex_grid

class GameWindow(pyglet.window.Window) :
    """A window, with the game in it."""

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

        pass

if __name__ == '__main__' :
    # Initlize the game window.
    GameWindow(800, 600, resizable=True)

    # Start the actuall game.
    pyglet.app.run()
