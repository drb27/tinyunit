class result(object):
    success=0
    failure=1
    error=2
    unknown=3

    @staticmethod
    def toString(r):
        if r==result.success:
            return "ok"
        elif r==result.failure:
            return "fail"
        elif r==result.error:
            return "error"
        else:
            return "???"
