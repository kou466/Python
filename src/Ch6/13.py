password = 0
while password != "pwpass":
    password = input("비밀번호:")
    if password == "pwpass":
        break
    else:
        continue
print("Login Pass!")