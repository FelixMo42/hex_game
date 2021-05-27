# Stores the attributes of hex tiles as part of the logic of the game

class Hex:
    """ The superclass that all types of hex inherit from.
    This structure is somewhat reminiscent of the 61a ants project;
    the different types of Hex tile are comparable to different ants
    """

    color = (255, 255, 255)
    destroyable = False
    
    def __init__(self):
        self.walkable = True
        self.destroyed = False
        
        # What (NPC, player, or even object) is there. Impacts walkability
        self.occupant = None
        
    def is_walkable(self):
        return self.walkable and self.occupant == None

class WallHex(Hex):
    color = (110, 48, 48)
    destroyable = True
    
    def __init__(self, *args, **kwargs):
        """ Walls have some special properties: i.e. they are destroyable.
        Walkable is an instance attribute because it changes
        if wall is destroyed
        """

        super(*args, **kwargs)

        self.walkable = False
        self.destroyed = False

class FloorHex(Hex):
    color = (200, 200, 200) 
    destroyable = False
    
    def __init__(self, *args, **kwargs):
        """ A normal floor tile.
        """
        
        super(*args, **kwargs)
        
    
class LockedHex(Hex):
    """ A locked tile cannot be walked on or interacted with.
    """

    color = (100, 100, 100)
    destroyable = False

    def __init__(self, *args, **kwargs):
        super(*args, **kwargs)

        self.walkable = False
