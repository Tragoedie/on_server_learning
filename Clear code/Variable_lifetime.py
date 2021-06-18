1) BigMinus.py

def BigMinus(s1, s2):
    list_1 = list(s1)
    list_2 = list(s2)
    ...

->

def SetMinMax(first_num, second_num, max_num, min_num):
    list_1 = list(first_num)
    list_2 = list(second_num)
    ...

def BigMinus(s1, s2):
    max_number = []
    min_number = []
    SetMinMax(s1, s2, max_number, min_number)
    ...

2) MadMax.py

def MadMax(N, Tele):
    x_change = True
    ...

->

def MixTele(N, Tele):
    x_change = True
    ...

def MadMax(N, Tele):
    MixTele(N, Tele)
    ...

3) MassVote.py

def MassVote(N, Votes):
    summ_votes = 0
    ...

->

def CalcPercentage(N, Votes, percent_votes):
    summ_votes = 0
    ...

def MassVote(N, Votes):
    percent_votes = []
    CalcPercentage(N, Votes, percent_votes)
    ...

4) MaximumDiscount.py

def MaximumDiscount(N, price):
    x_change = True
    ...

->

def RemixPrices(N, price):
    x_change = True
    ...

def MaximumDiscount(N, price):
    RemixPrices(N, price)
    ...

5) PatternUnlock.py

def PatternUnlock(N, hits):
    s_line = 0
    ...

->

def GetCode(N, hits):
    s_line = 0
    ...

def PatternUnlock(N, hits):
    code = GetCode(N, hits)
    ...

6) SherlockValidString.py

def SherlockValidString(s):
    s = list(s)
    change = True
    ...

->

def SortArray(s):
    change = True
    ...

def SherlockValidString(s):
    s = list(s)
    SortArray(s)
    ...

7) ...

def SherlockValidString(s):
    ...
    work_massive = []
    ...

->

def SherlockValidString(s):
    ...
    work_massive = []
    FillArray(s, work_massive)
    ...

def FillArray(s, work_massive):
    ...

8) ShopOLAP.py

def ShopOLAP(N, items):
    ...
    change = False
    ...

->

def CountNumOfIdentProducts(item_s, amount_s):
    change = False
    ...

def ShopOLAP(N, items):
    ...
    CountNumOfIdentProducts(item_s, amount_s)
    ...

9) ...

def ShopOLAP(N, items):
    ...
    change = False
    ...

->

def sort_quantity_asc(item_s, amount_s):
    change = False
    ...

def ShopOLAP(N, items):
    ...
    sort_quantity_asc(item_s, amount_s)
    ...

10) ...

def ShopOLAP(N, items):
    ...
    begin = 0
    end = 0
    ...

->

def sort_products_lexic_asc(item_s, amount_s):
    begin = 0
    end = 0
    ...

def ShopOLAP(N, items):
    ...
    sort_products_lexic_asc(item_s, amount_s)
    ...

11) SynchronizingTables.py

def SynchronizingTables(N, ids, salary):
    ...
    x_change = True
    ...

->

def ReplaceIDs(ids_copy, N):
    change = True
    ...

def SynchronizingTables(N, ids, salary):
    ...
    ReplaceIDs(ids_copy, N)
    ...

12) ...

def SynchronizingTables(N, ids, salary):
    ...
    y_change = True
    ...

->

def ReplaceSalaries(salary_copy, N):
    change = True
    ...

def SynchronizingTables(N, ids, salary):
    ...
    ReplaceSalaries(salary_copy, N)
    ...

13) TankRush.py

def TankRush(H1, W1, S1, H2, W2, S2):
    massive = []
    ...

->

def SplitMap(S1, map):
    massive = []
    ...

def TankRush(H1, W1, S1, H2, W2, S2):
    map = []
    SplitMap(S1, map)
    ...

14) TankRush.py

def TankRush(H1, W1, S1, H2, W2, S2):
    ...
    massive = []
    ...

->

def SplitTank(S2, tank):
    massive = []
    ...

def TankRush(H1, W1, S1, H2, W2, S2):
    ...
    tank = []
    SplitTank(S2, tank)
    ...

15) WordSearch.py

def WordSearch(ilen, s, subs):
    work_massive = []
    FillArray(ilen, s, work_massive)
    ...

->

def FillArray(ilen, s, work_massive):
    line = list(s)
    work_line = []
    ...

def WordSearch(ilen, s, subs):
    work_massive = []
    FillArray(ilen, s, work_massive)
    ...