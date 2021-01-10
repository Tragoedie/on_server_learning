from on_server_learning.algorithms_1.stack_queue_deque.queue_linked_list import Queue


def rotation_against_the_clock(queue, N, change=False):
    if queue.size() <= 1:
        return
    N = N % queue.size()
    # while N > queue.size():
        # N = N - queue.size()
    if change is True:
        N = queue.size() - N
    while N > 0:
        queue.enqueue(queue.dequeue())
        N -= 1


def rotation_clockwise(queue, N):
    rotation_against_the_clock(queue, N, True)


qu = Queue()
qu.enqueue(1)
qu.enqueue(2)
qu.enqueue(3)
qu.enqueue(4)
qu.enqueue(5)
qu.enqueue(6)
qu.enqueue(7)
qu.enqueue(8)
rotation_against_the_clock(qu, 17)
print(qu.head.value)
print(qu.tail.value)
qu.print_all_nodes()

