from .hex import WallHex, FloorHex

class Map:
    """ A Map object stores all the hexes in it, as well
    as information about itself.
    """

    def __init__(self, width, height):
        """ Width and height are measured in hexes.
        This is the size of the rectangular hashmap of axial coords bounding it.
        Unique map shapes are achieved by having some of the coords be None
        We set them all to be None initially.
        """
    
        self.width, self.height = width, height
        self.hexes = {}
        for x in range(width):
            for y in range(height):
                self.hexes[(x, y)] = WallHex()
                
    def get_hex(self, coords) :
        if coords not in self.hexes:
            # Return a FloorHex for now, loading from file was mentioned
            self.set_hex(coords, FloorHex())

        return self.hexes[coords]

    def set_hex(self, cord, hex) :
        self.hexes[cord] = hex

