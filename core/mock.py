import sys

def containing_attribute(symbol):

    if symbol.count('.')==0:
        return __name__
    else:
        return symbol[0:symbol.rfind('.')]

def leaf(fqs):
    if fqs.count('.')==0:
        return fqs
    else:
        return fqs[1+fqs.rfind('.'):]

def lookup_symbol(symbol):
    
    module = containing_attribute(symbol)
    return vars(sys.modules[module])[leaf(symbol)]

def replace_symbol(symbol,newvalue):
    
    module = containing_attribute(symbol)
    vars(sys.modules[module])[leaf(symbol)] = newvalue

def patch(old,new):

    def _patched(f,*args,**kwargs):
        def __patched(self,*args,**kwargs):
                restore = lookup_symbol(old)
                try:
                        #patch
                        replace_symbol(old,lookup_symbol(new)) 

                        #call
                        return f(self,*args,**kwargs)
                finally:
                        #Unpatch
                        replace_symbol(old,restore)
        return __patched
    return _patched
