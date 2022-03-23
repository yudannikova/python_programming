number_of_programmists = int(input())

if number_of_programmists % 10 == 1 and number_of_programmists % 100 != 11:
  print (int(number_of_programmists), 'программист')
elif (2 <= number_of_programmists % 10 <= 4) and not (12 <= number_of_programmists % 100 <= 14):
  print (int(number_of_programmists), 'программиста')
else: 
  print (int(number_of_programmists), 'программистов')