n = 0
len = 1
while len <= 100000:
    n += 1
    len = len * 2
    print(n, "번 접으면", len, "mm")
print("횟수:", n, "두께:", len)