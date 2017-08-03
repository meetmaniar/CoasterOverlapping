'''
Created on Aug 2, 2017

@author: Meet-69
'''
import unittest
from scratch import *
from inbuilt import *
import math
import inbuilt
import scratch


class testCases(unittest.TestCase):
    def test_scratch_sine(self):
        self.assertAlmostEqual(float(scratch_sine(0)), math.sin(0), 7, "Sin-Failed")
        self.assertAlmostEqual(float(scratch_sine(0.785)), math.sin(0.785), 7, "Sin-Failed")
        self.assertAlmostEqual(float(scratch_sine(1.57)), math.sin(1.57), 7, "Sin-Failed")
        self.assertAlmostEqual(float(scratch_sine(scratch_pi(20))), math.sin(scratch_pi(20)), 7, "Sin-Failed")
    
    def test_scratch_cosine(self):
        self.assertAlmostEqual(float(scratch_cosine(0)), math.cos(0), 7, "Cosine-Failed")
        self.assertAlmostEqual(float(scratch_cosine(0.785)), math.cos(0.785), 7, "Cosine-Failed")
        self.assertAlmostEqual(float(scratch_cosine(1.57)), math.cos(1.57), 7, "Cosine-Failed")
        self.assertAlmostEqual(float(scratch_cosine(scratch_pi(20))), math.cos(scratch_pi(20)), 7, "Cosine-Failed")
      
    def test_bisection(self):
        def f(a):  # Initiating the function
            a = Decimal(a)
            return a - 2
        
        self.assertEqual(scratch.bisection(f,0,3), 2, "scratchBisection Failed")
    
    def test_inbuilt_bisection(self):
        def f(a):  # Initiating the function
            a = Decimal(a)
            return a - 3
        
        self.assertEqual(inbuilt.bisection(f, 0, 4), 3, "inbuiltBisection Failed")
    
    def test_factorial(self):
        self.assertEqual(factorial(3), 6, "Failed")
        self.assertEqual(factorial(1), 1, "Failed")
        self.assertEqual(factorial(0), 1, "Failed")
    
    def test_scratch_pi(self):
        self.assertAlmostEqual(float(scratch_pi(20)),math.pi,7,"Pi failed")
     
    if __name__=='__main__':
        unittest.main()
