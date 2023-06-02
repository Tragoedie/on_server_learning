//49.5.1. Определите последовательность чётных положительных чисел.

let even_seq = Seq.initInfinite (function i -> (i + 1) * 2)

(*let result = even_seq
printf "%A" result*)

//49.5.2. Определите последовательность факториалов неотрицательных целых чисел 1,1,2,6,...,n!

let fac_seq = Seq.initInfinite (function i ->
 let rec factorial = function
  | 0 -> 1
  | n -> n * factorial (n - 1)
 factorial i
)

(*let result = fac_seq
printf "%A" result*)

//49.5.3. Определите последовательность 0, -1, 1, -2, 2, -3, 3, ...

let seq_seq = Seq.initInfinite (function i -> if i % 2 = 0 then i / 2 else -1 * (i + 1) / 2)

(*let result = seq_seq
printf "%A" result*)
