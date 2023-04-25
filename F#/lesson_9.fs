(*23.4.1. В фэнтези-РПГ принята следующая денежная система: в одном золотом 20 серебряных, а в одном 
серебряном 12 медяков. Суммы в такой системе задаются тройками целых чисел (золотые, серебряные, медяки), 
например (1, 0, 128) или (32, 23, 5).
Реализуйте инфиксный оператор .+. , который складывает деньги, представленные в виде троек, 
и инфиксный оператор .-. , который вычитает деньги. Результат приводите к формату, когда количество медяков не превышает 11,
а количество серебряных не превышает 19.*)

let normalize_result (gold, silver, copper) =
 let result_coppers = gold * 20 * 12 + silver * 12 + copper
 let result_gold = result_coppers / (20 * 12)
 let result_silver = (result_coppers % (20 * 12)) / 12
 let result_copper = (result_coppers % (20 * 12)) % 12
 (result_gold, result_silver, result_copper)

let (.+.) x y =     
 let (gold_1, silver_1, copper_1) = x
 let (gold_2, silver_2, copper_2) = y
 normalize_result (gold_1 + gold_2, silver_1 + silver_2, copper_1 + copper_2)

let (.-.) x y = 
 let (a, b) = if x < y then (y, x) else (x, y)
 let (gold_1, silver_1, copper_1) = a
 let (gold_2, silver_2, copper_2) = b
 normalize_result (gold_1 - gold_2, silver_1 - silver_2, copper_1 - copper_2)

//let result_1 = (.+.) (1, 0, 128) (32, 23, 5)
//let result_2 = (.-.) (1, 0, 128) (32, 23, 5)
//printfn "%A" result_1
//printfn "%A" result_2

(*23.4.2. Реализуйте логику работы с комплексными числами. Комплексное число задаётся парой вещественных чисел (x,y).
Правила сложения и умножения:
(a, b) + (c, d) = (a + c, b + d)
(a, b) * (c, d) = (ac - bd, bc + ad)
Вычитание реализуется сложением через инверсию:
-(a, b) = (-a,-b),
Деление реализуется умножением через инверсию:
1/(a, b) = (a/(a^2+b^2),-b/(a^2+b^2))
Реализуйте соответствующие инфиксные операторы .+ , .- , .* и ./ .*)

let (.+) x y =
 let (a, b) = x
 let (c, d) = y
 (a + c, b + d)

let (.-) x y =
 let (a, b) = x
 let (c, d) = y
 (a - c, b - d)

let (.*) x y = 
 let (a, b) = x
 let (c, d) = y
 (a * c - b * d, b * c + a * d)

let (./) x y = 
 let (a, b) = x
 let (c, d) = y
 (a, b) .* (c / (c * c + d * d), -d / (c * c + d * d))
