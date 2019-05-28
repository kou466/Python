num1 = int(input("정수1: "))
num2 = int(input("정수2: "))
quotient, remainder = 0, 0


def div_qr():
    global quotient, remainder
    quotient = num1 // num2
    remainder = num1 % num2
    print("몫: {0}, 나머지: {1}".format(quotient, remainder))


div_qr()
