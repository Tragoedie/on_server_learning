from on_server_learning.algorithms_1.stack.queue_linked_list import Queue


def rotation_against_the_clock(queue, N):
    while N > 0 and queue.size() > 1:
        node = queue.head
        queue.head = queue.head.next
        node.next = None
        queue.tail.next = node
        queue.tail = node
        N -= 1


def rotation_clockwise(queue, N):
    while N > 0 and queue.size() > 1:
        node = queue.head
        while node.next != queue.tail:
            node = node.next
        node.next = None
        queue.tail.next = queue.head
        queue.head = queue.tail
        queue.tail = node
        N -= 1


def print_all_nodes(queue):
    node = queue.head
    while node is not None:
        print(node.value)
        node = node.next


qu = Queue()
qu.enqueue(1)
qu.enqueue(2)
qu.enqueue(3)
qu.enqueue(4)
qu.enqueue(5)
qu.enqueue(6)
qu.enqueue(7)
qu.enqueue(8)
rotation_against_the_clock(qu, 5)
print(qu.head.value)
print(qu.tail.value)
print_all_nodes(qu)

