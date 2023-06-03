(*50.2.1-2. ���������� ������������������ �� ��. 49.5.2 � 49.5.4 � ������� ��������� �������������������.
49.5.2. ���������� ������������������ ����������� ��������������� ����� ����� 1,1,2,6,...,n!
49.5.4. ���������� ������������������ 0, -1, 1, -2, 2, -3, 3, ...*)

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

  
















