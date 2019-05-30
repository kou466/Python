char = input("문자열: ")

while (1):
    char1 = input("문자: ")
    if char1 == "":
        break
    if char1 in char:
        print("문자", char1,"가 문자열", char,"에 존재함")
    else:
        print("문자", char1,"가 문자열", char,"에 존재하지 않음")
