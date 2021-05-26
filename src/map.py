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
                self.hexes[(x, y)] = None
                
    def get_hex(self, coords):
        if self.hexes[coords] == None:
            # Instead of None, loading from file was mentioned
            return None
        return self.hexes[coords]
