//20.3.1. Напишите функцию vat: int -> float -> float, так что vat n x увеличивает x на n процентов (0 <= n <= 100).

let vat (n:int) (x:float) = x * ((float)1 + (float)n / (float)100)

//20.3.2. Напишите функцию unvat: int -> float -> float такую, что unvat n (vat n x) = x

let unvat (n:int) (x:float) = x / ((float)1 + (float)n / (float)100)

//20.3.3. Напишите функцию min: (int -> int) -> int, так что min(f) вычисляет минимальное целое положительное число n, когда f(n) = 0. Подразумевается, что такое натуральное число существует всегда.

let min f = 
 let rec min_rec n = 
  if f(n) = 0 then n 
  else min_rec(n + 1)
 min_rec 1
