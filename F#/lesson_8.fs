(*���� ��� �������
curry: (int * int -> int) -> int -> int ->int � uncurry: (int -> int ->int) -> int * int -> int
curry f -- ��� ������� g, ��� g x -- ��� ������� h, ��� h y = f(x,y).
uncurry g -- ��� ������� f, ��� f(x,y) -- ��� �������� h y ��� ������� h = g x.
�������� �� ����������.
*)

let curry f = function x y -> f(x, y)

let uncurry f = function (x, y) -> f x y
