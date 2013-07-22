from ..core.testcase import TestCase

class Inspector(object):
    """
    Returns a dictionary of module->list of test case classes
    """
    def __init__(self):
        pass

    def cases_per_method(self):

        # Start by generating a list of known subclasses from TestCase
        tc = TestCase.__subclasses__()

        # Create the blank dictionary
        d = {}

        # Add each class
        for sc in tc:
            if not sc.__module__ in d.keys():
                d[sc.__module__] = []
            d[sc.__module__].append(sc)

        # return the dictionary
        return d

    def cases(self):
        return TestCase.__subclasses__()

    def testmethods(self,case):
        
        # Get a list of callables on the given case
        m = [method for method in dir(case) if callable(getattr(case,method))]

        # return the list of methods decorated with @testmethod
        return [method for method in m if hasattr(getattr(case,method),'__testmethod__')]
