//47.4.1. Напишите функцию факториала f: int -> int, не используя рекурсию, с помощью императивных возможностей.

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

(*47.4.2. Напишите функцию fibo: int -> int, где fibo(n) вычисляет n-е число Фибоначчи (n >= 0), не используя рекурсию, с помощью императивных возможностей.
Последовательность Фибоначчи начинается с двух значений 0,1, а n-й элемент равен сумме n-1 - го и n-2 - го элементов: 0,1,1,2,3,5,8,13,...*)

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
