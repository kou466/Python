def issn_check(issn):
    weight = 8
    s = 0
    for i in range(len(issn) - 1):
        s = s + (int(issn[i]) * weight)
        weight -= 1
    print("ISSN 1~7자리의 가중치 반영 합계: %d" % s)
    t = s % 11
    chk = 11 - t

    if chk == 10:
        print("ISSN 1~7자리의 체크기호 값: X")
    elif chk == 11:
        print("ISSN 1~7자리의 체크기호 값: 0")
    else:
        print("ISSN 1~7자리의 체크기호 값: %d" % chk)

    if chk == int(issn[7]):
        rst = 1
    else:
        rst = 0
    return rst


issn = input("ISSN 8자리(- 제외): ")

if len(issn) == 8:
    rst = issn_check(issn)
    if rst == 1:
        print("ISSN 코드: %s는 검증되었습니다." % issn)
    else:
        print("ISSN 코드: %s는 검증되지 않았습니다." % issn)
