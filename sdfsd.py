set = [2, 3, 4, 1]
temp = 0
for num in range(len(set)):
  if set[num] > set[num + 1]:
    temp = set[num]
    set[num] = set[num + 1]
    set[num + 1] = set[num]

print(set)