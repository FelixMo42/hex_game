from .hex import WallHex, FloorHex
from .player import *
import pickle

# Paramaters/constants we can tweak
mapsave_file = 'mapsave'
player_start = (-1, 4)

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
                self.hexes[(x, y)] = WallHex()
        
        # Create and place the player
        self.player = Player(player_start)
        self.place_entity(player_start, self.player)
        
    def get_hex(self, cord):
        if cord not in self.hexes:
            # Return a FloorHex for now, loading from file was mentioned
            self.set_hex(cord, FloorHex())

        return self.hexes[cord]

    def set_hex(self, cord, hex_obj):
        self.hexes[cord] = hex_obj

    def get_entity(self, cord):
        if cord not in self.entities:
            return None
        return self.entities[cord]
        
    def place_entity(self, cord, entity):
        """ Place entity at cord, updating entities map and entity's coords
        Returns TRUE if the entity was placed, FALSE if not walkable
        """
        hex_obj = self.get_hex(cord)
        if hex_obj.is_walkable():
            self.entities[cord] = entity
            entity.cord = cord
            hex_obj.walkable = False
            return True
        else:
            return False
        
    def move_entity(self, cord, entity):
        """ Move an entity from its previous location to cord
        """
        old_cord = entity.cord
        if self.place_entity(cord, entity):
            self.entities[old_cord] = None
            self.get_hex(old_cord).walkable = True
    
    def move_entity_right(self, entity):
        new_cord = (entity.cord[0] + 1, entity.cord[1])
        self.move_entity(new_cord, entity)
    def move_entity_left(self, entity):
        new_cord = (entity.cord[0] - 1, entity.cord[1])
        self.move_entity(new_cord, entity)
    
    def pickle_map(self):
        """ Serialize the entire game state by serializing the Map
        since it contains the tiles, entities, etc.
        """
        outfile = open(mapsave_file, 'wb')
        pickle.dump(self, outfile)
        outfile.close()
        
def load_or_new():
    """ If can't load mapsave file, return new map
    If it does, read the Map object from save file, and return it
    """
    try:
        infile = open(mapsave_file, 'rb')
        map_obj = pickle.load(infile)
        infile.close()
    except:
        map_obj = Map(100, 100)
    return map_obj
