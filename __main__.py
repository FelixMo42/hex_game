import pyglet
from src.hexs import draw_hex

class GameWindow(pyglet.window.Window) :
    """A window, with the game in it."""

    def on_draw(self) :
        """Called whenever a new frame needs to get drawn."""
        
        # make sure there is no trace of privous stuff left behing
        self.clear()

        # draw a hex cause I feel like it. What are you gonna do about it?
        draw_hex(300, 300, [100, 140, 12])

    def on_key_press(self, key, mod) :
        """Called whenever a key is pressed."""

        pass

    def on_mouse_press(self, x, y, button, mod) :
        """Called whenever the mouse is clicked."""

        pass

if __name__ == '__main__' :
    # initlize a new window
    GameWindow(800, 600, resizable=True)

    # start the actuall game
    pyglet.app.run()
