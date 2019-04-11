a = 5
b = 3

opr = input("연산자: ")
if(opr == "+"):
    print("a", opr, "b", "=", a+b)
elif(opr == "-"):
    print("a", opr, "b", "=", a - b)
elif(opr == "*"):
    print("a", opr, "b", "=", a * b)
else:
    print("a", opr, "b", "=", a / b)