import pyglet

class GameWindow(pyglet.window.Window) :
    def on_draw(self) :
        # make sure there is no trace of privous stuff left behing
        window.clear()

    def on_key_press(self, key, mod) :
        pass

    def on_mouse_press(self, x, y, button, mod) :
        pass

if __name__ == '__main__' :
    # initlize a new window
    pyglet.window.Window(800, 600,resizable=True)

    # start the actuall game
    pyglet.app.run()
