class Player:
    def __init__(self, start_coords):
        self.coords = start_coords
        self.health = 1.00
        
    def reduce_health(self, amount):
        if self.health - amount > 0:
            self.health = self.health - amount
        else:
            self.health = 0
            # end_game() TODO: How do we want to end this?
            
class NPC:
    """ NPCs (esp. their lines) will likely be written in a file and read so 
    we don't have to hardcode them here.
    Lines is a list of strings that the NPC will say, in order.
    NPC should have an image that is displayed.
    """
    def __init__(self, lines, image, start_coords):
        self.lines, self.image = lines, image
        self.coords = start_coords
        self.curr_line = 0
        self.unlocked = False
    def interact(self, player):
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
