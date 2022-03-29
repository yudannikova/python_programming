genome = input()
prev_letter = [0]
count = 1
for letter in genome:
  if prev_letter == letter:
    count += 1
  else:
    print(str(prev_letter) + str(count), end = '')
    count = 1
    prev_letter = letter
print(str(prev_letter) + str(count))