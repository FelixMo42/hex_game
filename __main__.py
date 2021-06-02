import pyglet
from src.gui.window import GameWindowWithGui

if __name__ == '__main__' :
    # Initlize the game window.
    GameWindowWithGui(800, 600, resizable=True)

    # Start the actuall game.
    pyglet.app.run()
    
