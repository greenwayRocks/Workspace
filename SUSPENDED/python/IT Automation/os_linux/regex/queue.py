# QUEUE
queue = [0, 1, 2, 3, 4, 5, 6]  # 7 items

front = queue.index(0)
rear = len(queue) - 1  # MAXSIZE - 1
# Only dequeue if elements present
while(front >= 0):
    item = queue[front]

    if front == rear:
        front = -1
        rear = -1
    else:
        front += 1

    print(queue[item])

print('Queue is Empty!')
