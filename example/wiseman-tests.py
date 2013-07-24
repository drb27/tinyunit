#!/usr/bin/env python3
import argparse

from tinyunit.client import *
from wiseman import meaning_of_life

class WiseTests(TestCase):
        
        @testmethod
        def testMeaningOfLife(self):
                self.assertEquals(42,meaning_of_life())                

if __name__=='__main__':

        # Check to see if XML output is enabled
        parser = argparse.ArgumentParser()
        parser.add_argument("-x","--xml",help="Output XML report", action="store_true")
        args = parser.parse_args()

        # Create an inspector to retrieve test cases automatically
        i=Inspector()
        
        # Run a set of test cases
        runset(i.cases(), enable_xml=args.xml)
