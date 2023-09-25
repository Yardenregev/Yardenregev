from datetime import time


class TimeStamps():
    
    def __init__(self):
        self.data = {}
        self.current_time = time(0,0,0)

    def __str__(self):
        return str(self.data)
    
    def items(self):
        return self.data.items()

    def increase_time(self, seconds_to_add):
        seconds = self.current_time.second + seconds_to_add
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes + self.current_time.minute, 60)

        # Update the current_time
        self.current_time = time(hours, minutes, seconds)

    def insert(self, value):
        self.data[str(self.current_time)] = value
