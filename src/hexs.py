import pyglet
import math

def regular_polygone_vertices(x, y, degree, radius=60) :
    """An iterator of the vertices in a regulat polygon centered at (x, y)."""

    for i in range(degree) :
        yield int(radius * math.cos((math.pi/degree) * (1 + 2 * i))) + x
        yield int(radius * math.sin((math.pi/degree) * (1 + 2 * i))) + y

def draw_hex(x, y, color) :
    """Draw a hexagon centered at (x, y) of given color."""

    # the degree of a hexagon
    degree = 6

    # batchs are a group of opengl commands that will
    # be sent to the gpu to be rendered
    batch = pyglet.graphics.Batch()

    # add the polygon to the batch
    polygon = batch.add(
        # number of vertices is the degree of polygone
        degree,

        # tell openGl to use polygon mode to draw the vertices
        pyglet.gl.GL_POLYGON,

        # the Group of the vertices, idk read docs for more info 
        None,

        # the position of the vertices of the polygon
        ('v2i', list(regular_polygone_vertices(x, y, degree))),

        # the color of each vertex
        ('c3B', color * degree) 
    )

    # send the batch of to the gpu to get rendered
    batch.draw()
