import random

play = True
while play:

    print("가위, 바위, 보!")

    c = random.choice(["가위", "바위", "보"])
    m = input("당신: ")
    while (m != "가위" and m != "바위" and m != "보"):
        m = input("가위, 바위, 보 중에 하나를 입력해주세요: ")

    if c == "가위" and m == "가위":
        print("컴퓨터:", c, "\n당신:", m, "\n무승부")
    elif c == "가위" and m == "바위":
        print("컴퓨터:", c, "\n당신:", m, "\n승리")
    elif c == "가위" and m == "보":
        print("컴퓨터:", c, "\n당신:", m, "\n패배")
    elif c == "바위" and m == "가위":
        print("컴퓨터:", c, "\n당신:", m, "\n패배")
    elif c == "바위" and m == "바위":
        print("컴퓨터:", c, "\n당신:", m, "\n무승부")
    elif c == "바위" and m == "보":
        print("컴퓨터:", c, "\n당신:", m, "\n승리")
    elif c == "보" and m == "가위":
        print("컴퓨터:", c, "\n당신:", m, "\n승리")
    elif c == "보" and m == "바위":
        print("컴퓨터:", c, "\n당신:", m, "\n패배")
    elif c == "보" and m == "보":
        print("컴퓨터:", c, "\n당신:", m, "\n무승부")

    userInput = input("끝내시겠습니까? y/n: ")
    if (userInput == "y"):
        play = False
        print("수고하셨습니다.")
    else:
        play = True