class BinaryHeapPriorityQueue(object):

    def __init__(self, prefer, size=10):
        self.heapList = [None for i in range(0, size+1)]
        self.currentSize = 0
        self.prefer = prefer
        return

    def size(self):
        return self.currentSize

    def peek(self):
        result = self.heapList[1] if self.currentSize >=1 else None
        return result

    def pop(self):
        if self.currentSize < 1:
            return None
        result = self.heapList[1]
        self.__exch(1, self.currentSize)
        self.heapList[self.currentSize] = None
        self.currentSize -= 1
        self.__sink(1)
        return result

    def add(self, val):
        MAX_HEAPLIST_INDEX = len(self.heapList)-1
        VAL_INDEX = self.currentSize + 1

        if VAL_INDEX > MAX_HEAPLIST_INDEX:
            self.heapList.append(val)
        else:
            self.heapList[VAL_INDEX] = val

        self.currentSize += 1
        self.__swim(self.currentSize)
        return

    def __sink(self, n):
        k = n
        while 2*k <= self.currentSize:
            j = 2*k
            if j < self.currentSize\
            and self.heapList[j+1] == self.prefer(self.heapList[j], self.heapList[j+1]):
                j += 1
            if self.heapList[k] == self.prefer(self.heapList[j], self.heapList[k]):
                break
            self.__exch(j, k)
            k = j
        return

    def __swim(self, n):
        k = n
        while (k > 1)\
        and self.heapList[k] == self.prefer(self.heapList[k], self.heapList[int(k/2)]):
            self.__exch(k, int(k/2))
            k = int(k/2)
        return

    def __exch(self, i, j):
        temp =  self.heapList[i]
        self.heapList[i] = self.heapList[j]
        self.heapList[j] = temp
        return
