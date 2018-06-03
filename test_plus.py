#!/usr/bin/env python

import unittest
from plus import plus

class TestPlus(unittest.TestCase):

   def test_int(self):
       self.assertTrue(plus(1,2), 3, "error on int")
       
   def test_float(self):
       self.assertTrue(3.299999 < plus(1.1,2.2) < 3.300001)
       
   def test_str(plus("ab","cd"), "abcd", "error on str")
   
unittest.main()
