import types

class Mock(object):

        __instances = {}

        def __init__(self):
                
                # Init history
                self.history = []

                # Init Do Not Record list
                self.dnr = []

                # Add all of my callables to the Do Not Record list
                #for name in Mock.__dict__.keys():
                for name in dir(Mock): 
                        attr = object.__getattribute__(Mock,name)
                        if hasattr(attr,'__call__'):
                                self.dnr.append(name)
                
                # Record this mock object instance for later retrieval
                if not self.__class__ in self.__instances.keys():
                    self.__instances[self.__class__] = []

                # Add ourself to the list of instances
                self.__instances[self.__class__].append(self)

        def _record_call(self,name,args,kwargs,result=None):
                self.history.append((name,args,kwargs,result))

        def __getattribute__(self,name):
        
                # Ask the superclass to retrieve the attribute
                attr = object.__getattribute__(self,name)

                # Is it callable?
                if (name not in object.__getattribute__(self,'dnr')) and hasattr(attr,'__call__'):
                        def _instrumented_method(*args,**kwargs):
                                result = attr(*args,**kwargs)
                                self._record_call(name,args,kwargs,result)
                                return result

                        return _instrumented_method
                else:
                        return attr

        def calls(self):
                return len(self.history)


        def called(self,method):
            for call in self.history:
                if call[0] == method:
                    return True
            return False

        def callsbymethod(self,method):
            for call in self.history:
                if call[0] == method:
                    yield call
            

        @classmethod
        def reset_context(cls):
            cls.__instances = {}

        @classmethod
        def get_instances_of(cls,mocks):
            return cls.__instances[mocks]
