//17.4.1. �������� ������� pow: string * int -> string, ��� pow(s,n) ����� ������ s, ����������� n ���.

let rec pow = function
 | (s,0) -> ""
 | (s,1) -> s
 | (s,n) -> s + pow(s, n-1)

//17.4.2. �������� �������-�������� isIthChar: string * int * char -> bool, ��� isIthChar(s,n,c) ���������, ����� �� n-� (������� � ����) ������ ������ s ������� c.

let rec isIthChar(s:string, n:int, c:char) = s.[n] = c

//17.4.3. �������� ������� occFromIth: string * int * char -> int, ��� occFromIth(s,n,c) ���������� ���������� ��������� ������� � � ������ s, ������� � ������� n.

let rec occFromIth(s:string, n:int, c:char) = 
