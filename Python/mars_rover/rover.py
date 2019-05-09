"""
Contains Rover and Squad classes
"""

class Rover(object):
    """
    Represent individual rovers
    Attributes:
        x coordinate
        y coordinate
        direction facing
        invalid_move: whether the move would push rover off plateau
    """
    
    rotation = {'L': {'N':'W', 'W':'S', 'S':'E','E':'N'},
                'R' : {'N':'E', 'W':'N', 'S':'W','E':'S'}}
    
    invalid_move = " *Move off plateau"
    
    def __init__(self, x, y, dir):
        self.x = int(x)
        self.y = int(y)
        self.dir = dir
        self.invalid_move = False
    
    def __repr__(self):
        output = "%d %d %s" %(self.x, self.y, self.dir)
        if self.invalid_move == True:
            output += Rover.invalid_move
        return output

    
    def rotate(self, c):
        self.dir = Rover.rotation[c][self.dir]
    
    def move(self, plateau):
        """
        Check first whether move is legal.
        If yes, make move
        else, no move
        """
        temp_x = self.x
        temp_y = self.y
        
        if self.dir == 'N':
            temp_y += 1
        elif self.dir == 'S':
            temp_y -=1
        elif self.dir == 'E':
            temp_x += 1
        elif self.dir == 'W':
            temp_x -= 1
            
        if plateau.isLegal(temp_x, temp_y):
            self.make_move(temp_x, temp_y)
            return True
        else: 
            self.invalid_move = True
            return False
   
    def make_move(self, x, y):
        self.y = y
        self.x = x

class Squad(object):
    """
    Represent a squad of rovers
    Attribute:
        rovers: list of Rover objects.
    """
    
    def __init__(self):
        self.rovers = []
    
    def add_rover(self, rover):
        self.rovers.append(rover)

    def __str__(self):
        s = ""
        for i in range(len(self.rovers)):
            s += str(self.rovers[i]) + "\n"
        return s
