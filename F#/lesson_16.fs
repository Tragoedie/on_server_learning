//�������� ������� allSubsets, ���������� ������������� ��������� n � k, � �������� ��������� ���� ����������� ��������� {1, 2, ..., n}, � ������� ����� k ��������� (0 <= k <= n).

let allSubsets n k =
 let rec loop = function
  | (i, 0) -> set [set[]]
  | (i, k) when k = n - i + 1 -> set [set [i .. n]]
  | (i, k) -> Set.union(loop(i + 1, k)) (Set.map (function m -> Set.add i m) (loop(i + 1, k - 1)))
 loop (1, k)

(*let result = allSubsets 5 1
printf "%A" result*)
