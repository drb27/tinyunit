import types

class Mock(object):

        def __init__(self):
                
                # Init history
                self.history = []

                # Init Do Not Record list
                self.dnr = []

                # Add all of my callables to the Do Not Record list
                for name in Mock.__dict__.keys():
                        attr = getattr(Mock,name)
                        if hasattr(attr,'__call__'):
                                self.dnr.append(name)
                
                self.__class__.__getattribute__ = types.MethodType(Mock.___getattribute__,self)

        def _record_call(self,name,args):
                self.history.append({ name : args } )

        def ___getattribute__(self,name):
        
                # Ask the superclass to retrieve the attribute
                attr = object.__getattribute__(self,name)

                # Is it callable?
                if (name not in object.__getattribute__(self,'dnr')) and hasattr(attr,'__call__'):
                        def _instrumented_method(*args,**kwargs):
                                self._record_call(name,args)
                                result = attr(*args,**kwargs)
                                return result

                        return _instrumented_method
                else:
                        return attr

        def calls(self):
                return len(self.history)

class TestMock(Mock):
        def __init__(self):
                super(TestMock,self).__init__()
        def doit(self):
                return 42
        def test(self,a,b,c=0,d=0):
            pass
