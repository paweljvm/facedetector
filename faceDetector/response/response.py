class Response:
    def __init__(self,ok,message="",item=None):
        self.ok = ok
        self.message = message
        self.item = item

OK = Response(True)