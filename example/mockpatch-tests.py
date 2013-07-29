#!/usr/bin/env python3
import argparse

from tinyunit.client import *
import mockpatch
from mockpatch import make_polite_conversation

class MockUserInput(Mock):

    def __init__(self):
        super(MockUserInput,self).__init__()

    def getline(self):
        return "FRED\n"

class MockPatchTests(TestCase):
        
        @testmethod
        @patch('mockpatch.UserInput','__main__.MockUserInput')
        def testMakePoliteConversation(self):

                # Create the ui
                ui = mockpatch.UserInput()

                # Check the output
                self.assertEquals('Well hello there, FRED',make_polite_conversation(ui))                

                # Check that UserInput.getline was called just once
                self.assertEquals(1,ui.calls())

if __name__=='__main__':

        # Check to see if XML output is enabled
        parser = argparse.ArgumentParser()
        parser.add_argument("-x","--xml",help="Output XML report", action="store_true")
        args = parser.parse_args()

        # Create an inspector to retrieve test cases automatically
        i=Inspector()
        
        # Run a set of test cases
        runset(i.cases(), enable_xml=args.xml)
