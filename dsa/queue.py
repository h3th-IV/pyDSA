class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        return self.queue.pop(0)

    def print(self):
        if self.isEmpty():
            print("Queue is empty!")
            return None
        else:
            for i in self.queue:
                print(i, end=" ")



new_queue = Queue()

new_queue.enqueue(1998)
new_queue.enqueue(1998)
new_queue.enqueue(1998)
new_queue.enqueue(1998)
new_queue.enqueue(1998)

new_queue.print()
