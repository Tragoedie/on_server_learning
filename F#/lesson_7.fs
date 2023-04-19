//20.3.1. �������� ������� vat: int -> float -> float, ��� ��� vat n x ����������� x �� n ��������� (0 <= n <= 100).

let vat (n:int) (x:float) = x * ((float)1 + (float)n / (float)100)

//20.3.2. �������� ������� unvat: int -> float -> float �����, ��� unvat n (vat n x) = x

let unvat (n:int) (x:float) = x / ((float)1 + (float)n / (float)100)

//20.3.3. �������� ������� min: (int -> int) -> int, ��� ��� min(f) ��������� ����������� ����� ������������� ����� n, ����� f(n) = 0. ���������������, ��� ����� ����������� ����� ���������� ������.

let min f = 
 let rec min_rec n = 
  if f(n) = 0 then n 
  else min_rec(n + 1)
 min_rec 1
