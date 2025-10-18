from queue import Queue

q = Queue()

q.put(1)
q.put(2)
q.put(3)

print("Queue size:", q.qsize())
print("Queue empty:", q.empty())

print(q.get())
print(q.get())
print(q.get())

print("Queue size after gets:", q.qsize())
print("Queue empty:", q.empty())