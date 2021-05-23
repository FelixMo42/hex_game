import pyglet

# initlize a new window
window = pyglet.window.Window(800, 600,resizable=True)

@window.event
def on_draw():
    # make sure there is no trace of privous stuff left behing
    window.clear()


if __name__ == '__main__':
    pyglet.app.run()
