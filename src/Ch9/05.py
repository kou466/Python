num1 = int(input("정수1: "))
num2 = int(input("정수2: "))


def div_qr(n1, n2):
    return n1 // n2, n1 % n2


quotient, remainder = div_qr(num1, num2)
print("몫: {0}, 나머지: {1}".format(quotient, remainder))
