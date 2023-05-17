// 40.1. Напишите функцию sum(p, xs), где p -- предикат int -> bool, и xs -- список целых. Функция возвращает сумму тех элементов xs, для которых предикат истинен.

let rec sum (p, xs) = match xs with
 | [] -> 0
 | head :: tail when p(head) -> head + sum(p, tail)
 | head :: tail -> sum(p, tail)

(*let rec p x = 
 if x % 2 = 0 then true
 else false

let result = sum (p, [0; 1; 2; 3; 4])
printf "%A" result*)

(*40.2. Список [x1; x2; ...; xn] называется слабо восходящим, если его элементы удовлетворяют требованию: x1 <= x2 <= ... <= xn
Следующие функции работают со слабо восходящими списками. При их реализации обязательно учитывайте эту специфику, оптимизируя вычисления.*)

//40.2.1. Напишите функцию count: int list * int -> int, которая подсчитывает количество вхождений числа в список.

let rec count (xs, n) = match xs with
 | [] -> 0
 | head :: _ when head > n -> 0
 | head :: tail when head = n -> 1 + count(tail, n)
 | head :: tail -> count(tail, n)

(*let result = count ([0; 1; 2; 2; 3; 3], 1)
printf "%A" result*)

//40.2.2. Напишите функцию insert: int list * int -> int list, которая добавляет новый элемент в список.

let rec insert (xs, n) = match xs with
 | [] -> [n]
 | head :: tail when head < n -> head :: insert(tail, n)
 | head :: _ -> n :: xs

(*let result = insert ([0; 1; 2; 3; 3], 5)
printf "%A" result*)

//40.2.3. Напишите функцию intersect: int list * int list -> int list, которая находит общие элементы в обоих списках, включая повторяющиеся.

let rec intersect (xs1, xs2) = match (xs1, xs2) with
 | ([],[]) | ([],_) | (_,[]) -> []
 | (head_1 :: tail_1, head_2 :: tail_2) when head_1 = head_2 -> head_1 :: intersect(tail_1, tail_2)
 | (head_1 :: tail_1, head_2 :: tail_2) when head_1 < head_2 -> intersect(tail_1, xs2)
 | (head_1 :: tail_1, head_2 :: tail_2) -> intersect(xs1, tail_2)

(*let result = intersect ([1; 2; 3], [0; 1; 2; 3; 4])
printf "%A" result*)

//40.2.4. Напишите функцию plus: int list * int list -> int list, которая формирует список, объединяющий все элементы входных списков, включая повторяющиеся.

let rec plus (xs1, xs2) = match (xs1, xs2) with
 | ([],[]) -> []
 | (xs1, []) -> xs1
 | ([], xs2) -> xs2
 | (head_1 :: tail_1, head_2 :: tail_2) when head_1 = head_2 -> head_1 :: head_2 :: plus(tail_1, tail_2)
 | (head_1 :: tail_1, head_2 :: tail_2) when head_1 < head_2 -> head_1 :: plus(tail_1, xs2)
 | (head_1 :: tail_1, head_2 :: tail_2) -> head_2 :: plus(xs1, tail_2)

(*let result = plus ([1; 2; 3], [0; 1; 2; 3; 4])
printf "%A" result*)

(*40.2.5. Напишите функцию minus: int list * int list -> int list, которая возвращает список,
содержащий элементы первого списка за исключением элементов второго списка (элементы, одинаковые по значению, считаются разными).*)

let rec minus (xs1, xs2) = match (xs1, xs2) with
 | ([],[]) -> []
 | (xs1, []) -> xs1
 | ([], xs2) -> []
 | (head_1 :: tail_1, head_2 :: tail_2) when head_1 = head_2 -> minus(tail_1, tail_2)
 | (head_1 :: tail_1, head_2 :: tail_2) when head_1 < head_2 -> head_1 :: minus(tail_1, xs2)
 | (head_1 :: tail_1, head_2 :: tail_2) -> minus(xs1, tail_2)

(*let result = minus ([1; 2; 3; 4; 5], [0; 1; 2; 3; 4])
printf "%A" result*)

//40.3. Делаем сортировку.

//40.3.1. Напишите функцию smallest: int list -> int option, которая возвращает наименьший элемент непустого списка.

let rec smallest = function
 | [] -> None
 | [head] -> Some head
 | head_1::head_2::tail when head_1 <= head_2 -> smallest(head_1::tail)
 | head_1::head_2::tail when head_1 > head_2 -> smallest(head_2::tail)

(*let result = smallest ([0; 0; 1; 2; 3; 2; 4; -1])
printf "%A" result*)

//40.3.2. Напишите функцию delete: int * int list -> int list, которая удаляет из списка первое вхождение заданного элемента (если он имеется).

let rec delete (n, xs) = match xs with
 | [] -> []
 | head :: tail when head <> n -> head :: delete(n, tail)
 | head :: tail -> tail

(*let result = delete (2, [0; 1; 2; 3; 2; 4])
printf "%A" result*)

//40.3.3. Напишите функцию сортировки с использованием предыдущих функций, которая сортирует входной список так, что на выходе получается слабо восходящий список.

let rec sort = function
 | [] -> []
 | xs -> let head = Option.get (smallest xs)
         head :: sort(delete(head, xs))

(*let result = sort ([0; -1; 6; 2])
printf "%A" result*)

(*40.4. Напишите функцию revrev, которая получает на вход список списков, и перевёртывает как порядок вложенных списков, так и порядок элементов внутри каждого вложенного списка.
revrev [[1;2];[3;4;5]] = [[5;4;3];[2;1]]*)

let rec revrev = function
 | [] -> []
 | [head] -> [List.rev head]
 | head :: tail -> (revrev tail) @ [List.rev head]

(*let result = revrev ([[1;2];[3;4;5]])
printf "%A" result*)