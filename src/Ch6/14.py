sum = 0
while(1):
    num = int(input("정수: "))
    if num > 0:
        sum += num
        continue
    elif num == 0:
        break
    else:
        continue
print(sum)