def PrintingCosts(Line):
    line = list(Line)
    summ = 0
    for i in range(len(line)):
        if line[i] == ' ':
            summ += 0
        elif line[i] == '\'' or line[i] == '`':
            summ += 3
        elif line[i] == '.':
            summ += 4
        elif line[i] == '\"':
            summ += 6
        elif line[i] == ',' or line[i] == '-' or line[i] == '^':
            summ += 7
        elif line[i] == ':' or line[i] == '_':
            summ += 8
        elif line[i] == '!' or line[i] == '~':
            summ += 9
        elif line[i] == '>' or line[i] == '\\' or line[i] == '/' or line[i] == '<':
            summ += 10
        elif line[i] == ';':
            summ += 11
        elif line[i] == '(' or line[i] == '|' or line[i] == ')':
            summ += 12
        elif line[i] == 'v' or line[i] == 'r' or line[i] == 'x' or line[i] == '+':
            summ += 13
        elif line[i] == 'Y' or line[i] == '=':
            summ += 14
        elif line[i] == '?' or line[i] == 'i':
            summ += 15
        elif line[i] == 'L' or line[i] == 'T' or line[i] == 'l' or line[i] == '7':
            summ += 16
        elif line[i] == 't' or line[i] == 'c' or line[i] == 'u' or line[i] == '*':
            summ += 17
        elif line[i] == 'J' or line[i] == 'n' or line[i] == ']' or line[i] == '{' or line[i] == 'X' or line[i] == '}' or line[i] == 'f' or line[i] == 'I' or line[i] == '[':
            summ += 18
        elif line[i] == 'V' or line[i] == 'z' or line[i] == 'w' or line[i] == '1':
            summ += 19
        elif line[i] == 'o' or line[i] == 'F' or line[i] == 'j' or line[i] == 'C':
            summ += 20
        elif line[i] == 'h' or line[i] == 'K' or line[i] == '4' or line[i] == 'k' or line[i] == 's':
            summ += 21
        elif line[i] == '2' or line[i] == 'Z' or line[i] == '%' or line[i] == 'm' or line[i] == '0':
            summ += 22
        elif line[i] == '8' or line[i] == 'P' or line[i] == '3' or line[i] == 'e' or line[i] == 'U' or line[i] == 'a':
            summ += 23
        elif line[i] == '&' or line[i] == '#' or line[i] == 'A' or line[i] == 'y':
            summ += 24
        elif line[i] == 'b' or line[i] == 'd' or line[i] == 'p' or line[i] == 'G' or line[i] == 'S' or line[i] == 'q' or line[i] == 'H' or line[i] == 'N':
            summ += 25
        elif line[i] == 'D' or line[i] == '9' or line[i] == 'E' or line[i] == 'W' or line[i] == '6' or line[i] == 'O':
            summ += 26
        elif line[i] == '5':
            summ += 27
        elif line[i] == 'R' or line[i] == 'M':
            summ += 28
        elif line[i] == '$' or line[i] == 'B':
            summ += 29
        elif line[i] == 'g':
            summ += 30
        elif line[i] == 'Q':
            summ += 31
        elif line[i] == '@':
            summ += 32
        else:
            summ += 23
    return summ


# Line = input()
# print(PrintingCosts(Line))