from math import sqrt, sin, pi
from .polydraw import draw_regular_polygon

sqrt3 = sqrt(3)

def cord_to_pixel(cord, radius):
    """Convert axial hex cords to pixel cords."""
    
    # unpack the axial cordinate
    (q, r) = cord

    # https://www.redblobgames.com/grids/hexagons/#hex-to-pixel-axial
    return (
        int(radius * (sqrt3 * q + sqrt3 / 2 * r)),
        int(radius * (                3 / 2 * r))
    )

def hex_round(cord, radius):
    """Round to the nearest whole hex."""

    # Convert from axial to cube cords.
    # https://www.redblobgames.com/grids/hexagons/#conversions-axial
    x = cord[0]
    z = cord[1]
    y = -x-z

    # Do the rounding.
    # https://www.redblobgames.com/grids/hexagons/#rounding
    rx = round(x)
    ry = round(y)
    rz = round(z)

    dx = abs(rx - x)
    dy = abs(ry - y)
    dz = abs(rz - z)

    if dx > dy and dx > dz:
        rx = -ry-rz
    elif dy > dz:
        ry = -rx-rz
    else:
        rz = -rx-ry

    return (int(rx), int(rz))

def pixel_to_cord(pixel, radius):
    """Convert pixel to axial cords."""

    (x, y) = pixel

    return hex_round((
        (sqrt3/3 * x - 1/3 * y) / radius,
        (              2/3 * y) / radius
    ), radius)

def draw_hex(cord, color, radius, batch):
    """Draw a hexagon centered at the given set of axial cordinates."""

    draw_regular_polygon(
        # Convert the hex cordinates to a pixel position.
        cord = cord_to_pixel(cord, radius),

        # Add 1 to the radius so that there isent a gap bettween the hexes.
        radius = radius + 1,

        # Pass on the color.
        color = color,

        # Pass on the batch.
        batch = batch,

        # A hexagon is a polygon of degree 6
        degree = 6
    )
    
def draw_entity(cord, color, radius, batch):
    draw_regular_polygon(cord_to_pixel(cord, 60), 4, color, radius, batch)
   
def axial_to_oddr(cord):
    (x, y) = cord

    return (
        int(x + (y - (y&1)) / 2),
        y
    )

def draw_hex_grid(area, map, radius, batch):
    """Draws a hex grid of given pixel size."""

    # The endpoints of the area.
    (a, b) = area

    # Convert endpoints to offr hex cords.
    (sx, sy) = axial_to_oddr(pixel_to_cord(a, radius))
    (ex, ey) = axial_to_oddr(pixel_to_cord(b, radius))
    
    # Draw the grid of hexes.
    for x in range(sx - 1, ex + 2):
        for y in range(sy - 1, ey + 2):
            # The iterator is in odd row cords, so we need to convert to cords.
            # https://www.redblobgames.com/grids/hexagons/#coordinates 
            cord = (
                int(x - (y - (y & 1)) / 2),
                int(y)
            )
            
            # Draw the hex
            draw_hex(cord, map.get_hex(cord).color, radius, batch)
            # print("Drawing cord " + str(cord) + " which is " + str(map.get_hex(cord)))
            if map.get_entity(cord) != None:
                # print("Drawing entity at " + str(cord))
                draw_entity(cord, map.get_entity(cord).color, 10, batch)
