s_list = LinkedList2()
s_list.add_in_tail(Node(55))
s_list.add_in_tail(Node(55))
s_list.add_in_tail(Node(12))
s_list.add_in_tail(Node(55))
s_list.add_in_tail(Node(128))
s_list.add_in_tail(Node(1))
s_list.add_in_tail(Node(876))
s_list.add_in_tail(Node(45))
s_list.add_in_tail(Node(89))
s_list.add_in_tail(Node(789))
s_list.add_in_tail(Node(4))
s_list.add_in_tail(Node(88))
s_list.add_in_tail(Node(55))
s_list.add_in_tail(Node(128))
s_list.add_in_tail(Node(55))
index = 4
node = s_list.head
while index > 0 and node is not None and node.next is not None:
    node = node.next
    index -= 1
s_list.insert(node, Node(454879854578))
s_list.print_all_nodes()
print('~~~~~~~~~~~1~~~~~~~~~~~')
s_list = LinkedList2()
s_list.add_in_tail(Node(55))
s_list.add_in_tail(Node(55))
s_list.add_in_tail(Node(12))
s_list.add_in_tail(Node(55))
s_list.add_in_tail(Node(128))
s_list.add_in_tail(Node(1))
s_list.add_in_tail(Node(876))
s_list.add_in_tail(Node(45))
s_list.add_in_tail(Node(89))
s_list.add_in_tail(Node(789))
s_list.add_in_tail(Node(4))
s_list.add_in_tail(Node(88))
s_list.add_in_tail(Node(55))
s_list.add_in_tail(Node(128))
s_list.add_in_tail(Node(55))
s_list.delete(55, False)
s_list.print_all_nodes()
print('~~~~~~~~~~~2~~~~~~~~~~~')
s_list = LinkedList2()
s_list.add_in_tail(Node(55))
s_list.add_in_tail(Node(55))
s_list.add_in_tail(Node(12))
s_list.add_in_tail(Node(55))
s_list.add_in_tail(Node(128))
s_list.add_in_tail(Node(1))
s_list.add_in_tail(Node(876))
s_list.add_in_tail(Node(12))
s_list.add_in_tail(Node(45))
s_list.add_in_tail(Node(89))
s_list.add_in_tail(Node(789))
s_list.add_in_tail(Node(4))
s_list.add_in_tail(Node(88))
s_list.add_in_tail(Node(55))
s_list.add_in_tail(Node(128))
s_list.add_in_tail(Node(55))
s_list.delete(12, False)
s_list.print_all_nodes()
print('~~~~~~~~~~~3~~~~~~~~~~~')
s_list = LinkedList2()
s_list.add_in_tail(Node(55))
s_list.add_in_tail(Node(55))
s_list.add_in_tail(Node(12))
s_list.add_in_tail(Node(55))
s_list.add_in_tail(Node(128))
s_list.add_in_tail(Node(1))
s_list.add_in_tail(Node(876))
s_list.add_in_tail(Node(12))
s_list.add_in_tail(Node(45))
s_list.add_in_tail(Node(89))
s_list.add_in_tail(Node(789))
s_list.add_in_tail(Node(4))
s_list.add_in_tail(Node(88))
s_list.add_in_tail(Node(55))
s_list.add_in_tail(Node(128))
s_list.add_in_tail(Node(55))
s_list.delete(12, True)
s_list.print_all_nodes()
print('~~~~~~~~~~~4~~~~~~~~~~~')
s_list = LinkedList2()
s_list.delete(55, True)
s_list.print_all_nodes()
print('~~~~~~~~~~~5~~~~~~~~~~~')
s_list = LinkedList2()
s_list.delete(55, False)
s_list.print_all_nodes()
print('~~~~~~~~~~~6~~~~~~~~~~~')
s_list = LinkedList2()
s_list.add_in_tail(Node(55))
s_list.add_in_tail(Node(55))
s_list.add_in_tail(Node(55))
s_list.delete(55, True)
s_list.print_all_nodes()
print('~~~~~~~~~~~7~~~~~~~~~~~')
s_list = LinkedList2()
s_list.add_in_tail(Node(55))
s_list.add_in_tail(Node(55))
s_list.add_in_tail(Node(55))
s_list.delete(55, False)
s_list.print_all_nodes()
print('~~~~~~~~~~~8~~~~~~~~~~~')
s_list = LinkedList2()
s_list.add_in_tail(Node(55))
s_list.delete(55, True)
s_list.print_all_nodes()
print('~~~~~~~~~~~9~~~~~~~~~~~')
s_list = LinkedList2()
s_list.add_in_tail(Node(55))
s_list.delete(55, False)
s_list.print_all_nodes()
print('~~~~~~~~~~~10~~~~~~~~~~~')
s_list = LinkedList2()
s_list.add_in_tail(Node(1))
s_list.delete(55, True)
s_list.print_all_nodes()
print('~~~~~~~~~~~11~~~~~~~~~~~')
s_list = LinkedList2()
s_list.add_in_tail(Node(1))
s_list.delete(55, False)
s_list.print_all_nodes()


s_list = LinkedList2()
s_list.add_in_tail(Node(55))
s_list.add_in_tail(Node(55))
s_list.add_in_tail(Node(12))
s_list.add_in_tail(Node(55))
s_list.add_in_tail(Node(128))
s_list.add_in_tail(Node(1))
s_list.add_in_tail(Node(876))
s_list.add_in_tail(Node(45))
s_list.add_in_tail(Node(89))
s_list.add_in_tail(Node(789))
s_list.add_in_tail(Node(4))
s_list.add_in_tail(Node(88))
s_list.add_in_tail(Node(55))
s_list.add_in_tail(Node(128))
s_list.add_in_tail(Node(55))
index = 15
node = s_list.head
while index > 0 and node is not None and node.next is not None:
    node = node.next
    index -= 1
s_list.insert(node, Node(454879854578))
s_list.print_all_nodes()
print(s_list.tail.value)
node = s_list.tail
while node.prev is not None:
    print(node.value)
    node = node.prev

