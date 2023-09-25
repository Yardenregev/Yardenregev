import queue


class DataHolder():
    # def __init__(self, data = [], chunk_size = 130):
    #     self.data = data
    #     self.chunk_size = chunk_size

    def __init__(self):
        self.data = queue.Queue()


    # def append(self, data):
    #     self.data.append(data)

    def get(self, timeout=None):
        self.data.get(timeout=timeout)

    def put(self, item):
        self.data.put(item)
    
    def task_done(self):
        self.data.task_done()
    
    # def get_data(self, chunk_index):
    #     start = self.chunk_size * chunk_index
    #     end = (start + self.chunk_size) - 1
        
    #     return self.data[start:end]
    
    # def get_number_of_chunks(self):
    #     return int(len(self.data) / self.chunk_size) # TODO retreive info left out because of rounding
    
