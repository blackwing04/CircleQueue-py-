class CircleQueue:
    def __init__(self , size):
        self._size = size
        self._data = [0] * size
        self._front = size-1
        self._rear = size - 1

    def enqueue(self,item):
        next_pos = (self._rear+1) % self._size
        if next_pos == self._front:
            return False

        self._rear = next_pos
        self._data[self._rear] = item
        return True

    def dequeue(self):
        if self._front == self._rear:
            return None
        else:
            self._front =(self._front+1) % self._size
            return  self._data[self._front]
