
def patch(s):

    def _patched(f,*args,**kwargs):
        return f

    return _patched

def unpatched():
    return 42

def patched():
    return 43

class patchtest(object):

    @patch('thing')
    def meaning(self):
        return unpatched()

    @patch('otherthing')
    def addmeaning(self,x):
        return x+unpatched()
