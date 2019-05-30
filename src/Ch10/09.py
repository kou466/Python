def str2int():
    char = input("문자열: ")
    if char.isdigit():
        char = int(char)
    else:
        print("None")
        return 'None'
    print(char)


str2int()
