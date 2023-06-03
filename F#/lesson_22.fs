//51.3. �������: �������� � ������� hd � tl ������� nth, ������� ���������� n-� (n >= 0) ����������� ������� ������������ ������.

type 'a cell = Nil | Cons of 'a * Lazy<'a cell>

let hd (s : 'a cell) : 'a =
 match s with
   Nil -> failwith "hd"
 | Cons (x, _) -> x

let tl (s : 'a cell) : Lazy<'a cell> =
 match s with
   Nil -> failwith "tl"
 | Cons (_, g) -> g

let rec nth (s : 'a cell) (n : int) : 'a =
 if n = 0 then hd s
 else nth ((tl s).Force()) (n - 1)

(*let rec nat (n:int) : 'a cell = Cons (n, lazy(nat(n+1)))
let n0 = nat 0
let result = nth n0 30000
printf "%A" result*)