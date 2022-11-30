import circlequeue as cq

queue = cq.CircleQueue(10)

for i in range(1,5):
    print(i)
    queue.enqueue(i)

for i in range(11):
    print(queue.dequeue())