// 34.1. �������� ������� upto: int -> int list, ������� �������� ���: upto n = [1; 2; ...; n].

let rec upto = function
 | 1 -> [1]
 | n -> upto(n - 1) @ [n]

(*let upto = function
 | 1 -> [1]
 | n -> [1 .. n]
let result = upto 20
printf "%A" result*)

// 34.2. �������� ������� dnto: int -> int list, ������� �������� ���: downto n = [n; n-1; n-2; ...; 1].

let rec dnto =function
 | 1 -> [1]
 | n when n < 1 -> []
 | n -> n :: dnto(n - 1)

(*let result = dnto 20
printf "%A" result*)

// 34.3. �������� ������� evenn: int -> int list, ������� ���������� ������ �� ������ n ��������������� ������ �����.

let rec evenn = function
 | 1 -> [0]
 | n when n < 0 -> []
 | n -> evenn(n - 2) @ [n]

(*let result = evenn -5
printf "%A" result*)

