from on_server_learning.algorithms_1.linked_list.work_linked_list import Node
from on_server_learning.algorithms_1.linked_list.work_linked_list import LinkedList


def massive_of_value(s_list):
    node = s_list.head
    massive = []
    while node is not None:
        massive.append(node.value)
        node = node.next
    return massive


def sum_of_linked_list(lin_list_1, lin_list_2):
    result_massive = []
    if lin_list_1.len() == lin_list_2.len():
        list_1 = massive_of_value(lin_list_1)
        list_2 = massive_of_value(lin_list_2)
        for i in range(len(list_1)):
            result_massive.append(list_1[i] + list_2[i])
    return result_massive


s_list_1 = LinkedList()
s_list_1.add_in_tail(Node(1))
s_list_1.add_in_tail(Node(1))
s_list_1.add_in_tail(Node(1))


s_list_2 = LinkedList()
s_list_2.add_in_tail(Node(1))
s_list_2.add_in_tail(Node(1))
s_list_2.add_in_tail(Node(1))


summ = sum_of_linked_list(s_list_1, s_list_2)
if summ is None:
    print('The lengths of linked lists are not equal')
else:
    print(summ)
