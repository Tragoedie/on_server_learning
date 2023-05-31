(*48.4.1. �������� ��� ������ ������� ���������� n-�� ����� ��������� Fn.

1. fibo1: int -> int -> int -> int, � ����� �����������-�������������� n1 � n2, ���
fibo1 n n1 n2 = Fn, n1 = ������ ��������� ������� ������������������, � n2 -- ����� ������ ���������.

��������, fibo1 6 1 0 = 8 , fibo1 6 5 3 = 55.*)

let rec fibo1 n n1 n2 = match n with
 | 0 -> n2
 | 1 -> n1
 | _ -> fibo1 (n - 1) (n1 + n2) n1

(*let result = fibo1 6 5 3 
printf "%A" result*)

//2. fibo2: int -> (int -> int) -> int , ��� ������ �������� -- n, � ��������� �������� -- �������-�����������.

let rec fibo2 n c = match n with
 | 0 -> c 0
 | 1 -> c 1
 | _ -> fibo2 (n - 1) (function x -> c x) + fibo2 (n - 2) (function y -> c y)

(*48.4.2. ������� ������� ��������� ������

let rec bigList n k =
  if n=0 then k []
  else bigList (n-1) (fun res -> 1::k(res))
��� ������� ��� ������

bigList 230000 id
���������� ���������� StackOverflow.

�������� ���������� ������ bigList.*)

let rec bigList n k = 
 let acc = k []
 match n with
  | 0 -> acc
  | _ -> bigList (n - 1) (function res -> 1::acc)

(*let result = bigList 230000 id
printf "%A" result*)

