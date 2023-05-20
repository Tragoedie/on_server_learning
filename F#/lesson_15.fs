//41.4.1. Напишите функцию list_filter, которая реализует стандартную функцию List.filter, с помощью List.foldBack.

let list_filter f xs = 
 List.foldBack (fun head tail -> if (f head) then head :: tail else tail) xs []

(*
let p x = 
if x % 2 = 0 then true
else false
 
let result = (list_filter p [1;2;3;4;5])
printf "%A" result

let list_filter f xs =
    let loop x acc =
        if f x then x::acc
        else acc
    List.foldBack loop xs []

let result = (list_filter p [1;2;3;4;5])
printf "%A" result
*)


(*41.4.2. Напишите функцию sum(p, xs), где p -- предикат int -> bool, и xs -- список целых.
Функция возвращает сумму тех элементов xs, для которых предикат истинен.
Реализуйте sum с помощью List.fold или List.foldBack.*)

let sum (p, xs) = 
 List.fold (fun acc i -> if p i then i + acc else acc) 0 xs 

(*
let sum (p, xs) = 
 List.foldBack (fun i acc -> if p i then acc + i else acc) xs 0

let result = sum (p, [1;2;3;4;5])
printf "%A" result*)


(*41.4.3. Напишите функцию revrev, которая получает на вход список списков, и перевёртывает как порядок вложенных списков, так и порядок элементов внутри каждого вложенного списка.
revrev [[1;2];[3;4;5]] = [[5;4;3];[2;1]]
Реализуйте revrev с помощью List.fold или List.foldBack.*)

let revrev = 
 List.fold (fun head tail -> (List.rev tail) :: head) []

(*let result = revrev ([[1;2];[3;4;5]])
printf "%A" result*)