from multiprocessing import Value
class ThreadCoordinator():
    def __init__(self):
        self.shared_exit_flag = Value("i",0)
        self.running_thread_counter = 0