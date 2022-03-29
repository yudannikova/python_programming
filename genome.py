genome = input()
prev_letter = genome[0]
count = 1
for letter in genome[1:]:
  if prev_letter == letter:
    count += 1
  else:
    print(prev_letter + str(count), end = '')
    count = 1
    prev_letter = letter
print(prev_letter + str(count))