num_devs = int(input())

if num_devs % 10 == 1 and num_devs % 100 != 11:
  print (num_devs, 'программист')
elif (2 <= num_devs % 10 <= 4) and not (12 <= num_devs % 100 <= 14):
  print (num_devs, 'программиста')
else: 
  print (num_devs, 'программистов')