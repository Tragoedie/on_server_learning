//47.4.1. �������� ������� ���������� f: int -> int, �� ��������� ��������, � ������� ������������ ������������.

let f n = 
 if n < 0 then failwith "incorrect n"
 let mutable result = 1 
 let mutable i = 1 
 while i <= n do 
  result <- result * i 
  i <- i + 1 
 result

(*let result = f 1
printf "%A" result*)

(*47.4.2. �������� ������� fibo: int -> int, ��� fibo(n) ��������� n-� ����� ��������� (n >= 0), �� ��������� ��������, � ������� ������������ ������������.
������������������ ��������� ���������� � ���� �������� 0,1, � n-� ������� ����� ����� n-1 - �� � n-2 - �� ���������: 0,1,1,2,3,5,8,13,...*)

let fibo n =
 if n < 0 then failwith "incorrect n"
 let mutable prev = 1
 let mutable result = 0
 let mutable i = 0
 while i < n do
  let next = result + prev
  prev <- result
  result <- next
  i <- i + 1
 result 

(*let result = fibo 6
printf "%A" result*)
