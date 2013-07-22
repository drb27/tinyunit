#!/usr/bin/env python3
from tinyunit.engine.inspector import Inspector
from tinyunit.core.testcase import TestCase
from tinyunit.core.decorators import testmethod
from tinyunit.engine.testrunner import runset

from wiseman import meaning_of_life

class WiseTests(TestCase):
        
        @testmethod
        def testMeaningOfLife(self):
                self.assertEquals(42,meaning_of_life())                

if __name__=='__main__':
        i=Inspector()
        runset(i.cases())
