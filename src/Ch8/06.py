engkor_dict = dict()

while(1):
    eng = input("영어 단어: ")
    kor = input("한글 단어: ")
    if eng == "":
        if kor == "":
            print(engkor_dict)
            break
    engkor_dict[eng] = kor
