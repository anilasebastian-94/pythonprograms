# def is_leap(year):
#     leap = False
#     while year%100!=0:
#         if year%4==0 and year%400==0:
#             leap = True
#     return leap
# print(is_leap(2000))
year = int(input("Enter a year: "))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print(year,'is a leap year')
       else:
           print(year,'is not a leap year')
   else:
       print(year,'is a leap year')
else:
   print("{0} is not a leap year".format(year))