# QueueはFIFO, パケットの処理で使う
#popleft()はQueueと同じ挙動
#pop()はStackと同じ挙動

class My_Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, data):
        self.queue.append(data)
    
    def dequeue(self):
        if self.queue:
            # 先頭の要素を取り出す
            return self.queue.pop(0)

if __name__ == '__main__':
    q = My_Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.dequeue()
    print(q.queue)
    print("revert test")

