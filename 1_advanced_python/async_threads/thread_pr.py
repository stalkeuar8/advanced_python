import threading
import time


class MyThread(threading.Thread):
    def __init__(self, name: int):
        threading.Thread.__init__(self)
        self.name = name

        def run(self) -> None:
            time.sleep(3)
