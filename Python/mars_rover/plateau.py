"""
Contains Plateau class
"""

class Plateau(object):
    """
    Represents the plateau
    This maybe extended so rovers do not occupy the same space
    
    Attributes:
        Lower left corner: x, y
        Upper left corner: x, y   
    """
    
    def __init__(self, x, y):
        self.lower_x = 0
        self.lower_y = 0
        self.upper_x = int(x)
        self.upper_y = int(y)


    def isLegal(self, x, y):
        """
        Whether coordinate is on plateau
        """
        if not self.lower_x <= x <= self.upper_x or not self.lower_y <= y <= self.upper_y:
            return False
        return True

        
    
