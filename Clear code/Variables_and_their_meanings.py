1) LineAnalysis.py

work_line = []
//-- code
for ...
    work_line.append(pattern_l)

-->

//-- code
work_line = []
for ...
    work_line.append(pattern_l)

2) SynchronizingTables.py

salary_copy = salary.copy()
//-- code
for ...
    if salary_copy[j] > salary_copy[j + 1]:
        salary_copy[j], salary_copy[j + 1] = salary_copy[j + 1], salary_copy[j]

-->

//-- code
salary_copy = salary.copy()
for ...
    if salary_copy[j] > salary_copy[j + 1]:
        salary_copy[j], salary_copy[j + 1] = salary_copy[j + 1], salary_copy[j]

3) Unmanned.py

car_stop = track[0][0]
//-- code
for ...
    while car_stop >= traffic_light:
    ...

-->

//-- code
car_stop = track[0][0]
for ...
    while car_stop >= traffic_light:
    ...

4) TankRush.py

tank = []
//-- code
for ...
    tank.append(massive)

-->

//-- code
tank = []
for ...
    tank.append(massive)

5) MisterRobot.py

x_change = False
y_change = False
//-- code

-->

x_change = False
y_change = False
//-- code
x_change = False
y_change = False
//-- code

6) WordSearch.py

work_line =[]
work_massive =[]
//-- code
return ...

->

work_line =[]
work_massive =[]
//-- code
work_line.clear()
work_massive.clear()
return ...

7) BalancedParentheses.py

work_massive = []
//-- code
return ...

-->

work_massive = []
//-- code
work_massive.clear()
return ...

8) BigMinus.py

list_1 = list(s1)
list_2 = list(s2)
//-- code

-->

list_1 = list(s1)
list_2 = list(s2)
//-- code
list_1.clear()
list_2.clear()
//-- code

9) Football.py

index_x = -1
index_y = -1
counter = 0
//-- code

-->

index_x = -1
index_y = -1
counter = 0
//-- code
index_x = -1
index_y = -1
counter = 0
//-- code

10) MaximumDiscount.py

x_change = False
//-- code

-->

x_change = False
//-- code
x_change = False
//-- code

11) MassVote.py
summ_votes = 0
//-- code

-->

summ_votes = 0
//-- code
summ_votes = -1
//-- code

12) winner = 0
//-- code
result = "majority winner " + str(winner)

-->

winner = 0
//-- code
if (winner > 0)
    result = "majority winner " + str(winner)
else result = "Irregular Answer"

13) ShopOLAP.py

if N == 1:
    return items
//-- code

-->

if N == 1:
    return items
elif N < 1:
    print("Wrong num!")
    return items
//-- code



14) TheRabbitsFoot.py

line = list(s)
//-- code

-->

line = list(s)
//-- code
line.clear()
//-- code

15)SherlockValidString.py

s = list(s)
//-- code

-->

s = list(s)
//-- code
s.clear()
//-- code