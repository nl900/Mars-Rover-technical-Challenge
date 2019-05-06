import unittest
from mars_rover import Rover
from mars_rover import Plateau

class testRover(unittest.TestCase):
    
    def setUp(self):
        self.rover = Rover(1, 2, 'N')
    
    def test_rotate(self):
        inst1 = 'L'
        self.rover.rotate(inst1)
        self.assertEqual(self.rover.dir, 'W')
        
        inst2 = 'R'
        self.rover.rotate(inst2)
        self.assertEqual(self.rover.dir, 'N')
    
        
        
class testPlateau(unittest.TestCase):
    def setUp(self):
        self.plateau = Plateau(3, 3)
    
    def test_isLegal(self):
        case1 = self.plateau.isLegal(0, 0)
        self.assertTrue(case1)
        
        case2 = self.plateau.isLegal(5, 6)
        self.assertFalse(case2)
        
        case3 = self.plateau.isLegal(2, 6)
        self.assertFalse(case3)

    
if __name__ == '__main__':
    unittest.main()
