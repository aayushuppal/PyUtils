from threading import Thread
from util.data_util import getData

class ThreadWorker(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            action_type, args = self.queue.get()
            if action_type == 'getData':
                getData(args=args)

            self.queue.task_done()
