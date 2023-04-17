//17.4.1. Напишите функцию pow: string * int -> string, где pow(s,n) выдаёт строку s, повторенную n раз.

let rec pow = function
 | (s,0) -> ""
 | (s,1) -> s
 | (s,n) -> s + pow(s, n-1)

//17.4.2. Напишите функцию-предикат isIthChar: string * int * char -> bool, где isIthChar(s,n,c) проверяет, равен ли n-й (начиная с нуля) символ строки s символу c.

let rec isIthChar(s:string, n:int, c:char) = s.[n] = c

//17.4.3. Напишите функцию occFromIth: string * int * char -> int, где occFromIth(s,n,c) возвращает количество вхождений символа с в строке s, начиная с позиции n.

let rec occFromIth(s:string, n:int, c:char) = 
