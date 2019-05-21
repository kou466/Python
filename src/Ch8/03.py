score = int(input("점수: "))

if 100 >= score >= 90:
    print(score, ": A")
elif 89 >= score >= 80:
    print(score, ": B")
elif 79 >= score >= 70:
    print(score, ": C")
elif 69 >= score >= 60:
    print(score, ": D")
elif 59 >= score >= 0:
    print(score, ": F")
else:
    print("입력 가능한 점수 범위는 0~100입니다.")