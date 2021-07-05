import threading

class Console_Control_Thread(threading.Thread):
  #  def __init__(self, name):
    #    super().__init__()
    #    self.name = name

    def run(self):
        print("console 관리 thread")

#console_thr = Console_Control_Thread()
#console_thr.start()
