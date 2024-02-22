# This function should provide a return; True is it is a leap year, False if it isn't

def is_leap(year):
  """Take a year as an input and determines if it is a leap year"""
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
  
# TODO: Add more code here 👇
def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if is_leap(year) and month == 2:
    return 29
  return month_days[month - 1]

  
#🚨 Do NOT change any of the code below 
year = int(input("enter")) # Enter a year
month = int(input("enter")) # Enter a month
days = days_in_month(year, month)
print(days)

is