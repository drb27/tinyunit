#!/usr/bin/env python3
from tinyunit.client import *

from wiseman import meaning_of_life

class WiseTests(TestCase):
        
        @testmethod
        def testMeaningOfLife(self):
                self.assertEquals(42,meaning_of_life())                

if __name__=='__main__':
        i=Inspector()
        runset(i.cases())
