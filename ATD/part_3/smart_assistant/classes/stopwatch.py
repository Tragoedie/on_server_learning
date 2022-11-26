import time


class StopWatch:
    def __init__(self):
        self.start = time.time()

    def print(self):
        tm = time.time() - self.start
        hours = tm / 3600
        minutes = tm % 3600 / 60
        seconds = tm % 60
        milliseconds = int(tm * 10) % 10
        return "{0:02d}:{1:02d}:{2:02d}:{3}".format(int(hours), int(minutes), int(seconds), int(milliseconds))
