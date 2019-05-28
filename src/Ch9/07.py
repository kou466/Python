data = [21, 7, 43, 65, 2, 8, 72, 52, 9]

search = int(input("찾을 값: "))

if search in data:
    print("위치: ", data.index(search))
else:
    print("찾지 못함")
