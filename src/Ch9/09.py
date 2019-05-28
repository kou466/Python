data = [[21, 7, 43, 65], [2, 8, 72, 52]]

search = int(input("찾을 값: "))
flag = 0
for i in range(len(data)):
    for j in range(len(data[0])):
        if str(search) == str(data[i][j]):
            print("위치: ", i + 1, '행', j + 1, '열')
            flag = 1
            break

    if i + 1 == len(data) and flag == 0:
        print("찾지 못함")
