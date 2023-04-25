(*23.4.1. � �������-��� ������� ��������� �������� �������: � ����� ������� 20 ����������, � � ����� 
���������� 12 �������. ����� � ����� ������� �������� �������� ����� ����� (�������, ����������, ������), 
�������� (1, 0, 128) ��� (32, 23, 5).
���������� ��������� �������� .+. , ������� ���������� ������, �������������� � ���� �����, 
� ��������� �������� .-. , ������� �������� ������. ��������� ��������� � �������, ����� ���������� ������� �� ��������� 11,
� ���������� ���������� �� ��������� 19.*)

let normalize_result (gold, silver, copper) =
 let result_coppers = gold * 20 * 12 + silver * 12 + copper
 let result_gold = result_coppers / (20 * 12)
 let result_silver = (result_coppers % (20 * 12)) / 12
 let result_copper = (result_coppers % (20 * 12)) % 12
 (result_gold, result_silver, result_copper)

let (.+.) x y =     
 let (gold_1, silver_1, copper_1) = x
 let (gold_2, silver_2, copper_2) = y
 normalize_result (gold_1 + gold_2, silver_1 + silver_2, copper_1 + copper_2)

let (.-.) x y = 
 let (a, b) = if x < y then (y, x) else (x, y)
 let (gold_1, silver_1, copper_1) = a
 let (gold_2, silver_2, copper_2) = b
 normalize_result (gold_1 - gold_2, silver_1 - silver_2, copper_1 - copper_2)

//let result_1 = (.+.) (1, 0, 128) (32, 23, 5)
//let result_2 = (.-.) (1, 0, 128) (32, 23, 5)
//printfn "%A" result_1
//printfn "%A" result_2

(*23.4.2. ���������� ������ ������ � ������������ �������. ����������� ����� ������� ����� ������������ ����� (x,y).
������� �������� � ���������:
(a, b) + (c, d) = (a + c, b + d)
(a, b) * (c, d) = (ac - bd, bc + ad)
��������� ����������� ��������� ����� ��������:
-(a, b) = (-a,-b),
������� ����������� ���������� ����� ��������:
1/(a, b) = (a/(a^2+b^2),-b/(a^2+b^2))
���������� ��������������� ��������� ��������� .+ , .- , .* � ./ .*)

let (.+) x y =
 let (a, b) = x
 let (c, d) = y
 (a + c, b + d)

let (.-) x y =
 let (a, b) = x
 let (c, d) = y
 (a - c, b - d)

let (.*) x y = 
 let (a, b) = x
 let (c, d) = y
 (a * c - b * d, b * c + a * d)

let (./) x y = 
 let (a, b) = x
 let (c, d) = y
 (a, b) .* (c / (c * c + d * d), -d / (c * c + d * d))
