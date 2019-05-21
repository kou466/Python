items = {"라면": 650, "우유": 1100, "콜라": 1200, "캔커피": 500, "과자": 700}
sum = 0
while(1):
    it = input("제품명: ")

    if it == "":
        print("총 급액: ", sum)
        break
    elif it in items:
        sum += items[it]
        print("[%s:%d] > %d" % (it, items[it], sum))
    else:
        print(it, "는 미등록 제품입니다.")