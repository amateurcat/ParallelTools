from multiprocessing import JoinableQueue, Process

class Producer():
    def __init__(self, iterable, queue=None, add_stop_signal=0):
        self.iterable = iterable
        if queue==None:
            self.queue = JoinableQueue()
        else:
            self.queue = queue
            
        self.p = Process(target=self.wrapper)
        self.add_stop_signal = add_stop_signal
        
    def wrapper(self):
        for i,t in enumerate(self.iterable):
            self.queue.put((i,t))
        for j in range(self.add_stop_signal):
            self.queue.put(("STOP CONSUMER",))
                
    def start(self):
        self.p.start()

    def join(self):
        self.p.join()
