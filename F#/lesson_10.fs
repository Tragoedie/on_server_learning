(*24.4. �������

����� ��� ����� ���� ������������ ������� (����, ������, �������� ���), 
��� ���� ��������� �������� � ��������� �� 0 �� 11, ������ -- �� 0 �� 59, 
� �������� ��� -- ��� ���� "AM" (������ 12 �����), ���� "PM" (������ 12 �����).

���������� ��������� �������� .>. , ������� ���������� ��� ���������� �������� ���� TimeOfDay..*)

type TimeOfDay = { hours: int; minutes: int; f: string }

let normalize_TimeOfDay (x: TimeOfDay) = 
    if x.f = "AM" then x.hours * 60 + x.minutes
    else (x.hours + 12) * 60 + x.minutes

let (.>.) x y = (normalize_TimeOfDay x) > (normalize_TimeOfDay y)
