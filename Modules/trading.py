import threading

class trade_VBOS(threading.Thread):
    """def __init__(self, name):
        super().__init__()
        self.name = name            # thread 이름 지정
"""
    def run(self):
        trade_by_VBOS()




def trade_by_VBOS():
    print("thr test")
    return None


thr1= trade_VBOS()
thr1.start()
