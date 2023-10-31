import queue


class DataHolder():
    def __init__(self):
        self.data = queue.Queue()

    def get(self, timeout=None):
        self.data.get(timeout=timeout)

    def put(self, item):
        self.data.put(item)
    
    def task_done(self):
        self.data.task_done()