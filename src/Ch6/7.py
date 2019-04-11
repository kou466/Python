num_list = [8, 7, 3, 2, 9, 4, 1, 6, 5]

maxValue = num_list[0]
minValue = num_list[0]
for i in range(1, len(num_list)):
    if maxValue < num_list[i]:
        maxValue = num_list[i]
    if minValue > num_list[i]:
        minValue = num_list[i]
print("최댓값:", maxValue)
print("최솟값:", minValue)