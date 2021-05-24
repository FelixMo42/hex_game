import pyglet
from src.hexs import draw_hex, axial_to_pixel

class GameWindow(pyglet.window.Window) :
    """A window, with the game in it."""

    def on_draw(self) :
        """Called whenever a new frame needs to get drawn."""
        
        # Make sure there is no trace of privous stuff left behind.
        self.clear()

        # Batchs are a group of opengl commands that will
        # be sent to the gpu to be rendered.
        batch = pyglet.graphics.Batch()

        # Draw a grid of hexs.
        for q in range(3) :
            for r in range(3) :
                draw_hex((q, r), (q * 30 + 60, r * 30 + 60, 12), batch=batch)

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
