(*27.5. �������
���������� ������� 24.4, � ������� �������� ��� ������������ �� �������, � ����������� ������������ F.*)

type F = 
  | AM
  | PM

type TimeOfDay = { hours : int; minutes : int; f: F }

let normalize_TimeOfDay (x: TimeOfDay) = 
    if x.f = AM then x.hours * 60 + x.minutes
    else (x.hours + 12) * 60 + x.minutes

let (.>.) x y = (normalize_TimeOfDay x) > (normalize_TimeOfDay y)
