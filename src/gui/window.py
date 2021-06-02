import pyglet

from src.game import GameWindow
from src.gui.mouse import Mouse

class GameWindowWithGui(GameWindow, pyglet.window.Window):
    """ """

    # Manages mouse state
    mouse = Mouse()


