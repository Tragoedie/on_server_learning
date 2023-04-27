(*24.4. Задание

Время дня может быть представлено тройкой (часы, минуты, половина дня), 
где часы принимают значение в диапазоне от 0 до 11, минуты -- от 0 до 59, 
и половина дня -- это либо "AM" (первые 12 часов), либо "PM" (вторые 12 часов).

Реализуйте инфиксный оператор .>. , который сравнивает два корректных значения типа TimeOfDay..*)

type TimeOfDay = { hours: int; minutes: int; f: string }

let normalize_TimeOfDay (x: TimeOfDay) = 
    if x.f = "AM" then x.hours * 60 + x.minutes
    else (x.hours + 12) * 60 + x.minutes

let (.>.) x y = (normalize_TimeOfDay x) > (normalize_TimeOfDay y)
