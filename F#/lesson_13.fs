(* 39.1. Напишите функцию rmodd, которая получает на вход список, и выдаёт список, в который входят значения входного списка на нечётных 
позициях (первая позиция в списке, с индексом 0, считается чётной).*)

let rec rmodd = function
 | head :: (head2 :: tail) -> head2 :: rmodd tail 
 | _ -> [] 

// 39.2. Напишите функцию del_even, которая получает на вход список, и выдаёт список, из которого удалены все чётные значения входного списка.

let rec del_even = function 
 | [] -> [] 
 | head :: tail when head % 2 = 0 -> del_even tail 
 | head :: tail -> head :: del_even tail

// 39.3. Напишите функцию multiplicity x xs, которая находит, сколько раз значение x встречается в списке xs.

let rec multiplicity x xs =  
 let rec loop (x, xs, i) = match xs with 
  | [] -> i 
  | head :: tail when head = x -> loop (x, tail, i+1) 
  | head :: tail -> loop(x, tail, i) 
 loop (x, xs, 0)

(*let rec multiplicity x xs = match xs with
 | [] -> 0
 | head::tail -> (if head = x then 1 else 0) + multiplicity x tail*)

//39.4. Напишите функцию split, которая разделяет входной список на два следующим образом: split [x1; x2; ...; xn-1; xn] = ([x1; x3; ...], [x2; x4; ...])

let rec rmodd_2 = function 
 | head :: (head2 :: tail) -> head :: rmodd_2 tail 
 | [x] -> [x] 
 | _ -> []

let rec split = function xs -> (rmodd xs, rmodd_2 xs) 

(*let result = split [-1; 0; 1; 2; 3; 7]
printf "%A" result*)

(*39.5. Напишите функцию zip, которая преобразует два входных списка в результирующий список следующим образом:
zip ([x1; x2; ...], [y1; y2; ...]) = [(x1,y1); (x2,y2); ...]
Если длины входных списков неодинаковы, генерируйте исключение.*)

let rec zip (xs1,xs2) = 
 if List.length xs1 <> List.length xs2 then failwith "Different lengths of lists"
 else match (xs1, xs2) with 
  | ([], []) -> [] 
  | (head1 :: tail1, head2 :: tail2) -> (head1, head2) :: zip (tail1, tail2)

(*let result = zip ([5; 2; 4], [0])
printf "%A" result*)