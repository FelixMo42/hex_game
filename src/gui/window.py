from pyglet.window import Window
from src.game import Game
from src.gui.mouse import Mouse
from src.gui.gui import Gui

class GameWindow(Window):

    game = Game()

    #################
    # Window Events #
    #################

    def on_draw(self):
        # Draw the game first.
        self.game.on_draw()

        # Then draw the gui on top.
        self.game.gui.draw(self.mouse.position)

    def on_resize(self, width, height):
        self.game.size = (width, height)

        self.game.on_resize()

        # Pyglet requires we call the default on_resize callback.
        super().on_resize(width, height)

    ################
    # Mouse Events #
    ################

    def on_mouse_press(self, x, y, button, mod):
        # Only register a drag start if mouse is not over the gui. 
        # Used to see if click is drag or a simple press.
        if not self.game.gui.is_over((x, y)):
            self.game.mouse.drag_start()

    def on_mouse_release(self, x, y, button, mod):
        # If this is the end of a drag, then we shouldnt trigger a release event.
        if self.game.mouse.drag_end():
            return
        
        self.game.on_mouse_release(x, y, button, mod)

    def on_mouse_motion(self, x, y, dx, dy):
        self.game.mouse.position = (x, y)

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        # We still want to update the mouse position when dragging.
        self.game.mouse.position = (x, y)

        # If the drag was never triggered using mouse.start_drag, then we should bail.
        if not self.game.mouse.is_drag():
            return

        self.game.on_mouse_drag(x, y, dx, dy, buttons, modifiers)

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        self.game.on_mouse_scroll(x, y, scroll_x, scroll_y)

    ###################
    # Keyboard Events #
    ###################

    def on_key_release(self, key, mod):
        self.game.on_key_release(key, mod)
