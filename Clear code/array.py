1) BigMinus.py

min_number = []
max_number = []
<---code--->
for i in range(0, len(min_number)):
    if int(max_number[len(max_number) - 1 - i]) >= int(min_number[len(min_number) - 1 - i]):

-------->

min_number = LinkedList()
max_number = LinkedList()
<---code--->
min_item = min_number.head
max_item = max_number.head
for i in range(0, len(min_number)):
    if int(max_item.value) >= int(min_item.value):
    <---code--->
    min_item = min_item.next
    max_item = max_item.next

2) MadMax.py

Tele = []
<---code--->
for i in range(N - 1):
    if Tele[i] > Tele[i + 1]:
        Tele[i], Tele[i + 1] = Tele[i + 1], Tele[i]

-------->

Tele = LinkedList()
<---code--->
item_prev = Tele.head
item_next = item_prev.next
while item_prev != Tele.tail:
    if item_prev.value > item_next.value
        item_prev.value, item_next.value = item_next.value, item_prev.value

3) MassVote.py

Votes = []
<---code--->
summ_votes = 0
for i in range(N):
    summ_votes += Votes[i]

-------->

Votes = Stack()
<---code--->
summ_votes = 0
item = Votes.pop()
while item is not none:
    summ_votes += item.value
    item = Votes.pop()

4) MaximumDscount.py

price = []
<--code--->
for j in range(N):
    if (j + 1) % 3 == 0:
        sum_discount += price[j]

-------->

price = Queue()
<--code--->
item = price.pop()
cnt = 1
while item is not null:
    if cnt % 3 == 0:
        sum_discount += item.value
    cnt += 1
    item = price.pop()

5) MisterRobot.py
data = []
<--code--->
for i in range(N - 2):
    counter = 0
    while data[i] > data[i + 1] or data[i + 1] > data[i + 2]:
        number = data[i]
        data[i] = data[i + 1]
        data[i + 1] = data[i + 2]
        data[i + 2] = number
        counter += 1
<---code--->

-------->

data = OrderedList()
<---code--->
if (data.len() > 2):
    item = data.head
    item_next = item.next
    item_dblnext = item_next.next
    while (item_dblnext is not null):
        counter = 0
        while item.value > item_next.value or item_next.value > item_dblnext.value:
            number = item.value
            item.value = item_next.value
            item_next.value = item_dblnext.value
            item_dblnext.value = number
            counter += 1