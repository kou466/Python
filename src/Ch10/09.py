def str2int(char):
    if char.isdigit():
        a = int(char)
    else:
        a = None
    return a


a = input("문자열: ")
print(str2int(a))
