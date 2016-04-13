def Calculate(a):
    x = 0

    while True:
        try:
            sign1 = input("sign")
            b = int(input("next"))
        except ValueError:
            print("No number")

        else:
            if sign1 == "-":
                x = a - b
            elif sign1 == "+":
                x = a + b
            elif sign1 == "/":
                x = a / b
            elif sign1 == "*":
                x = a * b
            elif sign1 == "=":
                print(x)
            else:
                print("Invalid sign")
                continue
        print(x)

        return(x)


a = int(input("first?"))
while True:
    a = Calculate(a)
