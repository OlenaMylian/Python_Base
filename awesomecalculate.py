def error_b(last, vvod):
    while True:
        y = input(vvod)    
        print('last=', last)
        try:
            return number_into_underscore(y, last)
        except ValueError:
            pass
        
        
def number_into_underscore(y, last):
    
        if y == "_":
            y = last
            return y     
        else:
            return int(y)
           

            
    
        
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
