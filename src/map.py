from .hex import FloorHex

class Map:
    """ A Map object stores all the hexes in it, as well
    as information about itself.
    """

    def __init__(self, width, height):
        """ Width and height are measured in hexes.
        This is the size of the rectangular hashmap of axial cord bounding it.
        Unique map shapes are achieved by having some of the cord be None
        We set them all to be None initially.
        """
    
        self.width, self.height = width, height
        self.hexes = {}
        self.entities = {}
        for x in range(width):
            for y in range(height):
                self.hexes[(x, y)] = FloorHex()
                
    def get_hex(self, cord) :
        if self.hexes[cord] == None:
            # Instead of None, loading from file was mentioned
            return None

        return self.hexes[cord]

    def set_hex(self, cord, hex_obj):
        self.hexes[cord] = hex_obj

    def move_entity(self, cord, entity):
        """ Move an entity from its previous location to cord
        """
        hex_obj = self.get_hex(cord)
        old_cord = entity.cord
        if hex_obj.is_walkable():
            self.entities[cord] = entity
            entity.cord = cord
            hex_obj.walkable = False
            self.entities[old_cord] = None
