from multiprocessing import Process

class Consumer():
    def __init__(self, queue, worker, collector, fixed_args={}):
        
        # queue of tasks, each task is a tuple (idx, ${input_for_worker})
        # it also contains stop signal tuple ("STOP CONSUMER",)
        self.queue = queue
        self.p = Process(target=self.wrapper)
        
        # worker function do the task received from queue
        # the first argument is the thing received from the task queue
        # all others are task-specific argument unpackaed from ${fixed_args}
        self.worker = worker
        self.collector = collector
        self.fixed_args = fixed_args
        

    def wrapper(self):
        #print('calling wrapper\n')
        while True:
            args = self.queue.get()   ###!!! This will NOT raise error and will NOT stop when the queue is empty
            if "STOP CONSUMER" in args:   ###!!! args is a tuple! Do NOT use "==" here!
                print("STOP CONSUMER")
                self.queue.task_done()
                break
            else:
                index, t = args
                ret = self.worker(t, **self.fixed_args)
                self.collector((index,ret))
                self.queue.task_done()

    def start(self):
        #print('consumer start!\n')
        self.p.start()

    def join(self):
        self.p.join()