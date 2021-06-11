1)MassVote.py

percent = Votes[j] / summ_votes * 100

->

if summ_votes == 0:
    return
percent = Votes[j] / summ_votes * 100

2) QuickSort.py

if len(M) <= 1:
    return 0

->

if len(M) <= 1 or left < 0 or right < 0:
    return 0

3) BalancedParentheses.py

')', '('

->

CLOSE_BRACKET = ')'
OPEN_BRACKET = '('

4) BastShoe.py

'1' -> CMD_PUSH_BACK = '1'
'2' -> CMD_ERASE_BACK = '2'
'3' -> CMD_GET_SYMBOL = '3'
'4' -> CMD_UNDO = '4'
'5' -> CMD_REDO = '5'

5) if int(command[0]) < 1 or int(command[0]) > 5

->

IsCommandCorrect = int(command[0]) < 1 or int(command[0]) > 5
if IsCommandCorrect

6) (input[i] < input[j] and index_j == -1) or (input[i] < input[j] and input[j] < input[index_j])

->

IsFirstSuitablePair = input[i] < input[j] and index_j == -1
IsBetterThenExsisting = input[i] < input[j] and input[j] < input[index_j]
if IsFirstSuitablePair or IsBetterThenExsisting

7) BigMinus.py

if int(list_2[j]) > int(list_1[j])

->

IsSecondBumBigger = int(list_2[j]) > int(list_1[j])
if IsSecondBumBigger:

8) if int(max_number[len(max_number) - 1 - i]) >= int(min_number[len(min_number) - 1 - i]):

->

IsMaxnumNdigitBigger = int(max_number[len(max_number) - 1 - i]) >= int(min_number[len(min_number) - 1 - i])
if IsMaxnumNdigitBigger:

9) Football.py

if counter < 3 and index_x != -1 and index_y != -1:

->

IsExchangeNeeded = counter < 3 and index_x != -1 and index_y != -1
if (IsExchangeNeeded):

10) LineAnalysis.py

'*'

->

STAR_SYMBOL = '*'

11) MisterRobot.py

if data[i] > data[i+1] or data[i+1] > data[i+2]

->

NeedToReposTriple = data[i] > data[i+1] or data[i+1] > data[i+2]
if NeedToReposTriple:

12) odometr.py

if len(oksana) % 2 != 0 or len(oksana) < 2 or oksana[0] < 0 or oksana[1] <= 0:

->

IsArrayValid = len(oksana) % 2 != 0 or len(oksana) < 2 or oksana[0] < 0 or oksana[1] <= 0
if IsArrayValid: