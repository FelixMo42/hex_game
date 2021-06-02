import pyglet
import sys
from src.gui.window import GameWindow

# Make so that all files can import from src
sys.path.insert(1, './')

if __name__ == '__main__' :
    # Initlize the game window.
    GameWindow(800, 600, resizable=True)

    # Start the actuall game.
    pyglet.app.run()
    
