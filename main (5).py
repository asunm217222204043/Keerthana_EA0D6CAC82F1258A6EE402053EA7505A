def isLeapyear(year):
  if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    print("{} is a Leap Year.".format(year))
  else:
    print("{} is not a Leap Year.".format(year))

# Main Progam
year = int(input("Enter a year :"))
res = isLeapyear(year)
