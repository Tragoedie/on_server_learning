//16.1. Напишите функцию-предикат notDivisible: int * int -> bool, где notDivisible(n,m) возвращает true, если число n -- делитель числа m

let notDivisible(n, m) = m % n = 0

//16.2. Напишите функцию-предикат prime: int -> bool, где prime(n) возвращает true, если n -- простое число.

let rec prime_rec (n, m) = 
 if m = 1 then true
 elif n % m = 0 then false
 else prime_rec(n, m-1)

let prime(n) = match n with 
 | 1 -> false
 | _ -> prime_rec(n, n/2)
