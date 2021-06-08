import pyglet
from src.hexdraw import cord_to_pixel

class Entity:
    color = (100, 255, 100)
    
    def __init__(self, img_name, start_cord):
        
        # Images should be placed in ./static directory and referenced just by name
        self.image = img_name
        self.cord = start_cord
    

class Player(Entity):
    def __init__(self, start_cord):
        self.health = 1.00
        super().__init__('player.png', start_cord)
        
    def reduce_health(self, amount):
        if self.health - amount > 0:
            self.health = self.health - amount
        else:
            self.health = 0
            # end_game() TODO: How do we want to end this?
            
class NPC(Entity):
    """ NPCs (esp. their lines) will likely be written in a file and read so 
    we don't have to hardcode them here.
    Lines is a list of strings that the NPC will say, in order.
    NPC should have an image that is displayed.
    """
    
    def __init__(self, lines, img_name, start_cord):
        self.lines = lines
        self.curr_line = 0
        self.unlocked = False
        
        super().__init__(img_name, start_cord)
        
    def interact_with(self, player):
        """ Interact with the given player. NPCs can do stuff 
        to characters but usually just say lines. 
        Saying lines is done by returning the line, should be displayed
        by GUI
        """
        if self.unlocked:
            curr_line = self.curr_line
            self.curr_line += 1
            return self.lines[curr_line]
        else:
            return "Cannot interact with locked NPC"
    def unlock(self):
        self.unlocked = True

class Destroyer(NPC):
    """ Destroys the player"""
