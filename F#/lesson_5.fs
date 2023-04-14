//16.1. �������� �������-�������� notDivisible: int * int -> bool, ��� notDivisible(n,m) ���������� true, ���� ����� n -- �������� ����� m

let notDivisible(n, m) = m % n = 0

//16.2. �������� �������-�������� prime: int -> bool, ��� prime(n) ���������� true, ���� n -- ������� �����.

let rec prime_rec (n, m) = 
 if m = 1 then true
 elif n % m = 0 then false
 else prime_rec(n, m-1)

let prime(n) = match n with 
 | 1 -> false
 | _ -> prime_rec(n, n/2)
