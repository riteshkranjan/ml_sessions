import unittest 
from max_prime_no  import *
class SimpleTest(unittest.TestCase): 
  
    def test(self):         
        self.assertTrue(True) 
    
    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(5))
  
if __name__ == '__main__': 
    unittest.main() 