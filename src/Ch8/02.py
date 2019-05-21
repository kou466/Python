char = input("문자열: ")
result1 = ""
result2 = ""
for i in range(len(char)):
    result2 += char[i]
print("개별 문자 출력:", result2)
for j in range(len(char) - 1, -1, -1):
    result1 += char[j]
print("역순 개별 문자 출력:", result1)