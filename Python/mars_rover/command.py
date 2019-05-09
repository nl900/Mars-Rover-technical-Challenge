from .plateau import Plateau
from .rover import Rover, Squad

"""
The Command Centre that is responsible for executing instructions
"""

class Command(object):
    """
    Responsible for execution of instructions
    """
    
    squad = Squad()
    
    def extractInstructions(upper_x, upper_y, instructions):
        mars_plateau = Plateau(upper_x, upper_y)
        
        for r in instructions:
            rover = Rover(instructions[r]['start'][0], 
                      instructions[r]['start'][2], 
                      instructions[r]['start'][4])
            
            Command.squad.add_rover(rover)
            Command.execute(rover, instructions[r]['path'], mars_plateau)
        
        return Command.squad
    
    def execute(rover, commands, plateau):
        for c in commands:
            command = c.upper()
            if command == 'L' or command == 'R':
                rover.rotate(command)
            elif command == 'M':
                if not rover.move(plateau):   
                    break
   
    
   
