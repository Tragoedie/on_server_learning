// 40.1. �������� ������� sum(p, xs), ��� p -- �������� int -> bool, � xs -- ������ �����. ������� ���������� ����� ��� ��������� xs, ��� ������� �������� �������.

let rec sum (p, xs) = match xs with
 | [] -> 0
 | head :: tail when p(head) -> head + sum(p, tail)
 | head :: tail -> sum(p, tail)

(*let rec p x = 
 if x % 2 = 0 then true
 else false

let result = sum (p, [0; 1; 2; 3; 4])
printf "%A" result*)

(*40.2. ������ [x1; x2; ...; xn] ���������� ����� ����������, ���� ��� �������� ������������� ����������: x1 <= x2 <= ... <= xn
��������� ������� �������� �� ����� ����������� ��������. ��� �� ���������� ����������� ���������� ��� ���������, ����������� ����������.*)

//40.2.1. �������� ������� count: int list * int -> int, ������� ������������ ���������� ��������� ����� � ������.

let rec count (xs, n) = match xs with
 | [] -> 0
 | head :: _ when head > n -> 0
 | head :: tail when head = n -> 1 + count(tail, n)
 | head :: tail -> count(tail, n)

(*let result = count ([0; 1; 2; 2; 3; 3], 1)
printf "%A" result*)

//40.2.2. �������� ������� insert: int list * int -> int list, ������� ��������� ����� ������� � ������.

let rec insert (xs, n) = match xs with
 | [] -> [n]
 | head :: tail when head < n -> head :: insert(tail, n)
 | head :: _ -> n :: xs

(*let result = insert ([0; 1; 2; 3; 3], 5)
printf "%A" result*)

//40.2.3. �������� ������� intersect: int list * int list -> int list, ������� ������� ����� �������� � ����� �������, ������� �������������.

let rec intersect (xs1, xs2) = match (xs1, xs2) with
 | ([],[]) | ([],_) | (_,[]) -> []
 | (head_1 :: tail_1, head_2 :: tail_2) when head_1 = head_2 -> head_1 :: intersect(tail_1, tail_2)
 | (head_1 :: tail_1, head_2 :: tail_2) when head_1 < head_2 -> intersect(tail_1, xs2)
 | (head_1 :: tail_1, head_2 :: tail_2) -> intersect(xs1, tail_2)

(*let result = intersect ([1; 2; 3], [0; 1; 2; 3; 4])
printf "%A" result*)

//40.2.4. �������� ������� plus: int list * int list -> int list, ������� ��������� ������, ������������ ��� �������� ������� �������, ������� �������������.

let rec plus (xs1, xs2) = match (xs1, xs2) with
 | ([],[]) -> []
 | (xs1, []) -> xs1
 | ([], xs2) -> xs2
 | (head_1 :: tail_1, head_2 :: tail_2) when head_1 = head_2 -> head_1 :: head_2 :: plus(tail_1, tail_2)
 | (head_1 :: tail_1, head_2 :: tail_2) when head_1 < head_2 -> head_1 :: plus(tail_1, xs2)
 | (head_1 :: tail_1, head_2 :: tail_2) -> head_2 :: plus(xs1, tail_2)

(*let result = plus ([1; 2; 3], [0; 1; 2; 3; 4])
printf "%A" result*)

(*40.2.5. �������� ������� minus: int list * int list -> int list, ������� ���������� ������,
���������� �������� ������� ������ �� ����������� ��������� ������� ������ (��������, ���������� �� ��������, ��������� �������).*)

let rec minus (xs1, xs2) = match (xs1, xs2) with
 | ([],[]) -> []
 | (xs1, []) -> xs1
 | ([], xs2) -> []
 | (head_1 :: tail_1, head_2 :: tail_2) when head_1 = head_2 -> minus(tail_1, tail_2)
 | (head_1 :: tail_1, head_2 :: tail_2) when head_1 < head_2 -> head_1 :: minus(tail_1, xs2)
 | (head_1 :: tail_1, head_2 :: tail_2) -> minus(xs1, tail_2)

(*let result = minus ([1; 2; 3; 4; 5], [0; 1; 2; 3; 4])
printf "%A" result*)

//40.3. ������ ����������.

//40.3.1. �������� ������� smallest: int list -> int option, ������� ���������� ���������� ������� ��������� ������.

let rec smallest = function
 | [] -> None
 | [head] -> Some head
 | head_1::head_2::tail when head_1 <= head_2 -> smallest(head_1::tail)
 | head_1::head_2::tail when head_1 > head_2 -> smallest(head_2::tail)

(*let result = smallest ([0; 0; 1; 2; 3; 2; 4; -1])
printf "%A" result*)

//40.3.2. �������� ������� delete: int * int list -> int list, ������� ������� �� ������ ������ ��������� ��������� �������� (���� �� �������).

let rec delete (n, xs) = match xs with
 | [] -> []
 | head :: tail when head <> n -> head :: delete(n, tail)
 | head :: tail -> tail

(*let result = delete (2, [0; 1; 2; 3; 2; 4])
printf "%A" result*)

//40.3.3. �������� ������� ���������� � �������������� ���������� �������, ������� ��������� ������� ������ ���, ��� �� ������ ���������� ����� ���������� ������.

let rec sort = function
 | [] -> []
 | xs -> let head = Option.get (smallest xs)
         head :: sort(delete(head, xs))

(*let result = sort ([0; -1; 6; 2])
printf "%A" result*)

(*40.4. �������� ������� revrev, ������� �������� �� ���� ������ �������, � ������������ ��� ������� ��������� �������, ��� � ������� ��������� ������ ������� ���������� ������.
revrev [[1;2];[3;4;5]] = [[5;4;3];[2;1]]*)

let rec revrev = function
 | [] -> []
 | [head] -> [List.rev head]
 | head :: tail -> (revrev tail) @ [List.rev head]

(*let result = revrev ([[1;2];[3;4;5]])
printf "%A" result*)