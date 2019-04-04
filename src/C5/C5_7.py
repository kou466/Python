a = int(input("a: "))
b = int(input("b: "))
tmp = a+b-b*b
if(tmp >= 0):
    print(tmp)
else:
    print("음수")