input_list = [int(ix) for ix in input().split()]
input_list.sort()
count = 0
if len(input_list) == 1:
  print('')
else:
  for ix in range(1, len(input_list)):
    if input_list[ix - 1] == input_list[ix]:
        count += 1
        if count == 1:
            print(input_list[ix - 1], end = ' ')
    else:
        count = 0