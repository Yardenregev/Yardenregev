
class ThreadCoordinator():
    def __init__(self):
        self.shared_exit_flag = False
        self.running_thread_counter = 0