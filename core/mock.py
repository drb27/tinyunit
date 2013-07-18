import sys

def patch(s):

    def _patched(f,*args,**kwargs):
        def __patched(self,*args,**kwargs):
                old = vars(sys.modules[__name__])['unpatched']
                try:
                        #patch
                        
                        vars(sys.modules[__name__])['unpatched'] = patched                        
                        #call
                        return f(self,*args,**kwargs)
                finally:
                        #Unpatch
                        vars(sys.modules[__name__])['unpatched'] = old                        
        return __patched
    return _patched

def unpatched():
    return 42

def patched():
    return 43

class patchtest(object):

    def __init__(self,base=0):
        self.base = base

    @patch('thing')
    def meaning(self):
        return self.base+unpatched()

    @patch('otherthing')
    def addmeaning(self,x):
        return self.base+x+unpatched()
