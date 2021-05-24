from math import sqrt
from .polydraw import draw_regular_polygon

sqrt3 = sqrt(3)

def draw_hex(cord, color, radius=60, batch=None) :
    """Draw a hexagon centered at the given set of axial cordinates."""

    draw_regular_polygon(
        # Convert the axial cordinates to a pixel position.
        cord=axial_to_pixel(cord),

        # Add 1 to the radius so that there isent a gap bettween the hexs.
        radius=radius + 1,

        # Pass on the color.
        color=color,

        # Pass on the batch.
        batch=batch,

        # A hexagon is a polygon of degree 6
        degree=6
    )
    

def axial_to_pixel(cord, radius=60) :
    """Convert axial hex cords to pixel cords."""
    
    # unpack the axial cordinate
    (q, r) = cord

    # https://www.redblobgames.com/grids/hexagons/#hex-to-pixel-axial
    return (
        int(radius * (sqrt3 * q + sqrt3 / 2 * r)),
        int(radius * (                3 / 2 * r))
    )
