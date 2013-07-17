from ..core.testcase import TestCase
from ..core.decorators import testmethod

class ExampleTests(TestCase):

    def __init__(self):
        pass

    @testmethod
    def testTrue(self):
        self.assertTrue(True)

class OtherTests(TestCase):

    def __init__(self):
        pass

    @testmethod
    def testFirst(self):
        pass

    @testmethod
    def testSecond(self):
        pass

    def notATest(self):
        pass
