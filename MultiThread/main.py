#!python3

from queue import Queue
from time import time
from util import getData
from util import ThreadWorker
from multiprocessing import cpu_count

CPU_COUNT = cpu_count()

def main():
    ts = time()

    taskQueue = Queue()
    for i in range(CPU_COUNT):
        worker = ThreadWorker(taskQueue)
        worker.daemon = True
        worker.start()

    output1 = {}
    taskQueue.put(('getData', {'get_url' : 'http://google.com', 'output' : output1}))
    output2 = {}
    taskQueue.put(('getData', {'get_url' : 'http://example.com','output' : output2}))
    output3 = {}
    taskQueue.put(('getData', {'get_url' : 'http://example.com','output' : output3}))
    output4 = {}
    taskQueue.put(('getData', {'get_url' : 'http://example.com','output' : output4}))
    output5 = {}
    taskQueue.put(('getData', {'get_url' : 'http://example.com','output' : output5}))
    output6 = {}
    taskQueue.put(('getData', {'get_url' : 'http://example.com','output' : output6}))

    taskQueue.join()

    print('main takes time={}s'.format(time() -ts))

    serial_time = output1['time_taken'] + output2['time_taken']\
    + output3['time_taken'] + output4['time_taken']  + output5['time_taken']\
    + output6['time_taken']

    print('serial exec time would be time={}s'.format(serial_time))

# ==============================================================================
if __name__ == '__main__':
    main()
