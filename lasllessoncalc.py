def error_b(last, vvod):
    while True:
        y = input(vvod)   1 функция 
        print('last=', last)
        if y == "_":
            y = last
            return y     2 функция
        else:   в елсе визвать след.ф-ю которая говорит всё что ниже в елс
            try:
                y = int(y)
                return y
            except ValueError:
                print("No number")
                continue
        
def error_sign():
    while True:
        sign = input("sign?")
        if sign == "-" or sign == "+" or sign == "/" or sign == "*" or sign == "=":
            return sign 
        else:
            print("Invalid sign")
            continue
        
def Calculate():
    x = 0
    b = 0
    last = 0
    a = error_b(last, "first?")
    while True:
        sign = error_sign()      
        b = error_b(last, "next?")
        print('b =  ', b)
        print('last=', last)
        if sign == "-":
            x = a - b 
        elif sign == "+":
            x = a + b
        elif sign == "/":
            x = a / b
        elif sign == "*":
            x = a * b
        else:
            print("Wrong operation")
        last = a = x
        print('x =  ', x)
        continue


Calculate()



