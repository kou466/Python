num_odd = 0
num_even = 0

for i in range(1, 101, 1):
    if(i%2 == 1):
        num_odd += i
print("홀수의 합:", num_odd)

for j in range(0, 101, 2):
    num_even += j
print("짝수의 합:", num_even)