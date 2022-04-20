# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
from calendar import month


month = input("Enter the month of the year (Jan - Dec): ").lower()
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
day = input("Enter the day of the month: ")
# 3. Calculate what season it is based upon this chart:
if month in ('dec') and day >20:
    print(f"{month} {day} is in Winter")
elif month in("jan"):
    print(f"{month} {day} is in Winter")
elif month in('feb'):
    print(f"{month} {day} is in Winter")
elif month in("mar") and day <20:
    print(f"{month} {day} is in Winter")
elif month in("mar") and day>20:
    print(f"{month} {day} is in Spring")
elif month in("apr"):
    print(f"{month} {day} is in Spring")
elif month in("may"):
    print(f"{month} {day} is in Spring")
elif month in("jun") and day < 21:
    print(f"{month} {day} is in Spring")
elif month in ("jun") and day>20:
    print(f"{month} {day} is in Summer")
elif month in ("jul"):
    print(f"{month} {day} is in Summer")
elif month in ("aug"):
    print(f"{month} {day} is in Summer")
elif month in ("sep") and day<22:
    print(f"{month} {day} is in Fall")
elif month in ("oct") and day>20:
    print(f"{month} {day} is in Fall")
elif month in ("nov"):
    print(f"{month} {day} is in Fall")
elif month in ("dec") and day>21:
    print(f"{month} {day} is in Fall")

#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.