import pyglet
from math import cos, sin, pi

def regular_polygon_vertices(cord, degree, radius=60) :
    """An iterator for the vertices in a regular polygon centered at cord."""
    
    for i in range(degree) :
        yield (
            int(radius * cos((pi/degree) * (1 + 2 * i))) + cord[0],
            int(radius * sin((pi/degree) * (1 + 2 * i))) + cord[1]
        )

def vertices_mesh(vertices) :
    """An iterator for the pixel cords of the vertices
    in a triangle mesh of the given polygon."""

    # Yield the cordinates for each triangle.
    for i in range(1, len(vertices) - 1) : 
        yield from vertices[0]
        yield from vertices[i + 0]
        yield from vertices[i + 1]

def draw_polygon(vertices, color, batch):
    # Number of vertices is the number of vertices in the triangles needed to make a the shape.
    num_vertices = (len(vertices) - 2) * 3

    return batch.add(
        # Tell the batch how many vertices we want to add.
        num_vertices,

        # Tell openGl to use polygon mode to draw the vertices.
        pyglet.gl.GL_TRIANGLES,

        # The Group of the vertices, idk read docs for more info.
        None,

        # The position of the vertices of the polygon.
        ('v2i', list(vertices_mesh(vertices))),

        # The color of each vertex.
        ('c3B', color * num_vertices) 
    )

def draw_regular_polygon(cord, degree, color, radius, batch) :
    """Draw a regular polygon centered at cord of given color and radius."""
    
    return draw_polygon(
        list(regular_polygon_vertices(cord, degree, radius)),
        color, batch
    )
