import pyglet
from src.hexdraw import draw_hex_grid, pixel_to_cord

class Camera:
    zoom_factor = 1

    offset_x = 0
    offset_y = 0

    @property
    def scale(self):
        return 1.1 ** self.zoom_factor

    @property
    def ox(self):
        return self.offset_x + self.size[0] / 2

    @property
    def oy(self):
        return self.offset_y + self.size[1] / 2

    def zoom(self, dz):
        """Zoom in by a factor of delta z."""

        self.zoom_factor += dz

    def shift(self, dx, dy):
        """Shift the camera by the given amount."""

        self.offset_x -= dx / self.scale
        self.offset_y -= dy / self.scale

    def area(self):
        """Get the pixel area of the screen post conversions."""

        sx = self.offset_x - self.size[0] / 2 / self.scale
        sy = self.offset_y - self.size[1] / 2 / self.scale

        ex = self.offset_x + self.size[0] / 2 / self.scale
        ey = self.offset_y + self.size[1] / 2 / self.scale

        return ((sx, sy), (ex, ey))

    def screen_to_world_position(self, x, y):
        """Apply camera translation to (x, y) cordinates."""

        return (
            x / self.scale + self.offset_x - self.size[0] / 2 / self.scale,
            y / self.scale + self.offset_y - self.size[1] / 2 / self.scale
        )

    def __enter__(self):
        """Called on enter statment (with ____:)."""

        # Put the current translation matrix on the stack.
        pyglet.gl.glPushMatrix()

        # (0, 0) should be in the middle of the screen.
        pyglet.gl.glTranslatef(self.size[0] / 2, self.size[1] / 2, 0.0)

        # Scale the screen porpotionality.
        pyglet.gl.glScalef(self.scale, self.scale, 1.0)

        # Move to the offset.
        pyglet.gl.glTranslatef(-self.offset_x, -self.offset_y, 0.0)

    def __exit__(self, exception_type, exception_value, traceback):
        """Called on exit statment (with ____:)"""

        # Revert to the previus translation matrix.
        pyglet.gl.glPopMatrix()

