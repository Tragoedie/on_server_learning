(*50.2.1-2. Определите последовательности из пп. 49.5.2 и 49.5.4 с помощью выражений последовательностей.
49.5.2. Определите последовательность факториалов неотрицательных целых чисел 1,1,2,6,...,n!
49.5.4. Определите последовательность 0, -1, 1, -2, 2, -3, 3, ...*)

let fac_seq = seq {
 yield 1
 let mutable i = 1
 let mutable x = 1
 while true do
  x <- x * i
  i <- i + 1
  yield x
}

(*let result = fac_seq
printf "%A" result*)

let seq_seq = seq {
 yield 0
 let mutable x = 1
 while true do
  yield -x
  yield x
  x <- x + 1
}

(*let result = seq_seq
printf "%A" result*)

  
















