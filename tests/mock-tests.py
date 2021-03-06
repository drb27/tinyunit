#!/usr/bin/env python3

from tinyunit.client import *

class MockDerivative(Mock):
    
    meaningoflife = 42

    def __init__(self):
        super(MockDerivative,self).__init__()

    @classmethod
    def simplecase(self):
        return self.meaningoflife

    def simplemethod(self):
        return self.__class__.meaningoflife

    def singleposparam(self,val):
        return self.__class__.meaningoflife + val

    def singleparamwithdefault(self,val=4):
        return self.__class__.meaningoflife + val

class MockTests(TestCase):

    def __init__(self):
        super(MockTests,self).__init__()


    @testmethod
    def testConstruction(self):

        # Reset the mock context
        Mock.reset_context()

        # Create a mock derivative and check type
        out = MockDerivative()
        self.assertTrue( isinstance(out,MockDerivative) )

        # Is history blank?
        self.assertTrue( hasattr(out,'history') )
        self.assertEquals( 0, len(out.history) )

        # Did the mock context recognise the object?
        mocks = Mock.get_instances_of(MockDerivative)
        
        self.assertEquals( 1, len(mocks) )
        self.assertTrue( mocks[0] is out)        


    @testmethod
    def testSimpleCase(self):

        # Attempt to create the mock derivative
        out = MockDerivative()
        
        # Call the simplecase method
        self.assertEquals(42,out.simplecase())

        # Check one item of history
        self.assertEquals(1, len(out.history))

        # Check no parameters
        history = out.history[0]
        methodname = history[0]
        posargs = history[1]
        namedargs = history[2]
       
        self.assertEquals(methodname,'simplecase')
        self.assertEquals(0,len(posargs))
        self.assertEquals(0,len(namedargs))
 

    @testmethod
    def testSimpleMethod(self):

        # Attempt to create the mock derivative
        out = MockDerivative()
        
        # Call the simplecase method
        self.assertEquals(42,out.simplemethod())

        # Check one item of history
        self.assertEquals(1, len(out.history))

        # Check no parameters
        history = out.history[0]
        methodname = history[0]
        posargs = history[1]
        namedargs = history[2]
       
        self.assertEquals(methodname,'simplemethod')
        self.assertEquals(0,len(posargs))
        self.assertEquals(0,len(namedargs))

    @testmethod
    def testSimplePosParam(self):

        # Attempt to create the mock derivative
        out = MockDerivative()
        
        # Call the simplecase method
        self.assertEquals(43,out.singleposparam(1))

        # Check one item of history
        self.assertEquals(1, len(out.history))

        # Check no parameters
        history = out.history[0]
        methodname = history[0]
        posargs = history[1]
        namedargs = history[2]
       
        self.assertEquals(methodname,'singleposparam')
        self.assertEquals(1,len(posargs))
        self.assertEquals(0,len(namedargs))
        self.assertEquals(1, posargs[0])

    @testmethod
    def testSimplePosParamMultiple(self):

        # Attempt to create the mock derivative
        out = MockDerivative()
        
        for x in range(5):
            # Call the simplecase method
            self.assertEquals(42+x,out.singleposparam(x))

        # Check history length
        self.assertEquals(5, len(out.history))

        for x in range(5):
            # Check no parameters
            history = out.history[x]
            methodname = history[0]
            posargs = history[1]
            namedargs = history[2]
           
            self.assertEquals(methodname,'singleposparam')
            self.assertEquals(1,len(posargs))
            self.assertEquals(0,len(namedargs))
            self.assertEquals(x, posargs[0])

    @testmethod
    def testSingleParamWithDefaultUnused(self):
        
        out = MockDerivative()
        self.assertEquals(43,out.singleparamwithdefault(1))
        
        history = out.history[0]
        posargs = history[1]
        namedargs = history[2]

        self.assertEquals(1,len(posargs))
        self.assertEquals(0,len(namedargs))
        self.assertEquals(1,posargs[0])

    @testmethod
    def testSingleParamWithDefaultUsed(self):

        out = MockDerivative()
        self.assertEquals(46,out.singleparamwithdefault())
        
        history = out.history[0]
        posargs = history[1]
        namedargs = history[2]

        self.assertEquals(0,len(posargs))
        self.assertEquals(0,len(namedargs))

    @testmethod
    def testSingleParamWithDefaultNamed(self):
        
        out = MockDerivative()
        self.assertEquals(50,out.singleparamwithdefault(val=8))
        
        history = out.history[0]
        posargs = history[1]
        namedargs = history[2]
    
        self.assertEquals(0,len(posargs))
        self.assertEquals(1,len(namedargs))

        self.assertTrue('val' in namedargs.keys())
        self.assertEquals(8, namedargs['val'])

    @testmethod
    def testCalled(self):
        out = MockDerivative()

        out.simplecase()
        out.singleposparam(4)

        self.assertTrue( out.called('simplecase') )
        self.assertTrue( out.called('singleposparam') )
        self.assertFalse( out.called('simplemethod') ) 
        self.assertFalse( out.called('nosuchmethod') )


    @testmethod
    def testByMethod(self):
    
        out = MockDerivative()

        out.simplecase()
        out.singleposparam(0)
        out.simplecase()
        out.singleposparam(1)
        out.simplecase()
        out.simplecase()
        out.singleposparam(2)

        # Use list comprehension to build a list of calls to singleposparam
        calllist = [x for x in out.callsbymethod('singleposparam')]
        self.assertEquals( len(calllist), 3 )
 
        expectedparamvalue = 0

        # Check each entry
        for call in calllist:
            self.assertEquals(call[0],'singleposparam')
            self.assertEquals(len(call[1]),1)
            self.assertEquals(call[1][0], expectedparamvalue )
            expectedparamvalue += 1

class MockRegressionTests(TestCase):

    def __init__(self):
        super(MockRegressionTests,self).__init__()

    @testmethod
    def testMultipleInstancesRetainDnr(self):
        
        out = MockDerivative()
        out2 = MockDerivative()

        for i in [out,out2]:
            self.assertTrue( i.dnr.count('_record_call') > 0 )

  
    @testmethod
    def testMethodReturnValueStored(self):

        out = MockDerivative()
        result = out.singleposparam(5)

        self.assertEquals(result, out.history[0][3])

if __name__=="__main__":
    run()
