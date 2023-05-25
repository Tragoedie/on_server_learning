//Реализуйте стандартную функцию Map.tryFind самостоятельно в виде функции try_find.

let try_find key m =
 if Map.containsKey key m then Some(Map.find key m)
 else None
(*
let map_1 = Map.ofList [(128,"oksana"); (32,"oleg")]
let result = try_find 128 map_1
let result_false = try_find 256 map_1

printf "%A" result
printf "%A" result_false
*)

