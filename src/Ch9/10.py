import copy

s7seg_num = [[1, 1, 1, 1, 1, 1, 0],  # 0
             [0, 1, 1, 0, 0, 0, 0],  # 1
             [1, 1, 0, 1, 1, 0, 1],  # 2
             [1, 1, 1, 1, 0, 0, 1],  # 3
             [0, 1, 1, 0, 0, 1, 1],  # 4
             [1, 0, 1, 1, 0, 1, 1],  # 5
             [1, 0, 1, 1, 1, 1, 1],  # 6
             [1, 1, 1, 0, 0, 0, 0],  # 7
             [1, 1, 1, 1, 1, 1, 1],  # 8
             [1, 1, 1, 1, 0, 1, 1]]  # 9
s7seg_num_anode = copy.deepcopy(s7seg_num)

for i in range(len(s7seg_num_anode)):
    for j in range(len(s7seg_num_anode[i])):
        if s7seg_num_anode[i][j] == 0:
            s7seg_num_anode[i][j] = 1
        else:
            s7seg_num_anode[i][j] = 0

print('s7seg_num', '\t       ', 's7seg_num_anode')
for i in range(len(s7seg_num)):
    for j in range(len(s7seg_num[i])):
        print(s7seg_num[i][j], end=' ')
    print('\t  \t', end='')
    for j in range(len(s7seg_num_anode[i])):
        print(s7seg_num_anode[i][j], end=' ')
    print()
