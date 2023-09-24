
class DataHolder():
    def __init__(self, data = [], chunk_size = 130):
        self.data = data
        self.chunk_size = chunk_size
    
    def append(self, data):
        self.data.append(data)
    
    def get_data(self, chunk_index):
        start = self.chunk_size * chunk_index
        end = (start + self.chunk_size) - 1

        return self.data[start:end]
    