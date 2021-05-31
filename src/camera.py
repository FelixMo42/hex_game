import pyglet
from .hexdraw import draw_hex_grid, pixel_to_cord

class Camera:
    radius = 60

    offset_x = 0
    offset_y = 0

    def shift(self, dx, dy) :
        self.offset_x -= dx
        self.offset_y -= dy

    def area(self, size):
        return (
            (self.offset_x, self.offset_y),
            (
                size[0] + self.offset_x,
                size[1] + self.offset_y
            )
        )

    def screen_to_world_position(self, x, y) :
        return (
            x + self.offset_x,
            y + self.offset_y
        )

    def __enter__(self):
        pyglet.gl.glPushMatrix()
        pyglet.gl.glLoadIdentity()
        pyglet.gl.glTranslatef(-self.offset_x, -self.offset_y, 0.0)

    def __exit__(self, exception_type, exception_value, traceback):
        pyglet.gl.glPopMatrix()

