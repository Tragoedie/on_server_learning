// 34.1. Напишите функцию upto: int -> int list, которая работает так: upto n = [1; 2; ...; n].

let rec upto = function
 | 1 -> [1]
 | n -> upto(n - 1) @ [n]

(*let upto = function
 | 1 -> [1]
 | n -> [1 .. n]
let result = upto 20
printf "%A" result*)

// 34.2. Напишите функцию dnto: int -> int list, которая работает так: downto n = [n; n-1; n-2; ...; 1].

let rec dnto =function
 | 1 -> [1]
 | n when n < 1 -> []
 | n -> n :: dnto(n - 1)

(*let result = dnto 20
printf "%A" result*)

// 34.3. Напишите функцию evenn: int -> int list, которая генерирует список из первых n неотрицательных чётных чисел.

let rec evenn = function
 | 1 -> [0]
 | n when n < 0 -> []
 | n -> evenn(n - 2) @ [n]

(*let result = evenn -5
printf "%A" result*)

