class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

class result(object):
    success=0
    failure=1
    error=2
    unimplemented=3
    unknown=4

    @staticmethod
    def toString(r,color=False):

        if color:
            if r==result.success:
                return bcolors.OKGREEN + "ok" + bcolors.ENDC
            elif r==result.failure:
                return bcolors.FAIL + "fail" + bcolors.ENDC
            elif r==result.error:
                return bcolors.WARNING + "error" + bcolors.ENDC
            elif r==result.unimplemented:
                return bcolors.HEADER + "not implemented" + bcolors.ENDC
            else:
                return bcolors.WARNING + "???" + bcolors.ENDC
        else:
            if r==result.success:
                return "ok"
            elif r==result.failure:
                return "fail"
            elif r==result.error:
                return "error"
            elif r==result.unimplemented:
                return "not implemented"
            else:
                return "???"
