from on_server_learning.algorithms_1.stack.queue_linked_list import Queue


def rotation_against_the_clock(queue, N):
    if queue.size() <= 1:
        return
    while N > 0:
        val = queue.dequeue()
        queue.enqueue(val)
        N -= 1


def rotation_clockwise(queue, N):
    if queue.size() <= 1:
        return
    while N > queue.size():
        N = N - queue.size()
    result = queue.size() - N
    rotation_against_the_clock(queue, result)


qu = Queue()
qu.enqueue(1)
qu.enqueue(2)
qu.enqueue(3)
qu.enqueue(4)
qu.enqueue(5)
qu.enqueue(6)
qu.enqueue(7)
qu.enqueue(8)
rotation_clockwise(qu, 5)
print(qu.head.value)
print(qu.tail.value)
qu.print_all_nodes()

