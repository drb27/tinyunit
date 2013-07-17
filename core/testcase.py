"""
class: TestCase

This class provides a base for all test cases in your project. 
Deriving your test case class from TestCase informs tinyunit that your class holds
unit tests. The engine will then find methods decorated with @testmethod, and run
those tests automatically. 

In addition, the class provides base implementations for many assert methods. 

"""
from .decorators import testmethod

class TestCase(object):

    class AssertFailureException(Exception):
        def __init__(self):
                pass
    
    def __init__(self):
        pass

    def assertTrue(self,expr):
        if not expr:
            raise TestCase.AssertFailureException()

    def assertEquals(self,a,b):
        if not a==b:
            raise TestCase.AssertFailureException()

    def assertRaises(self,fn,exception):
        try:
            fn()
        except exception as e:
            pass
        else:
            raise TestCase.AssertFailureException()
