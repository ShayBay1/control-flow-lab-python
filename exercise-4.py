# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
a = input("enter length of side a from your triangle: ")
b= input("enter length of side b from your triangle: ")
c= input("enter length of side c from your triangle: ")
if (a==b and b==c):
    print(f"A triangle with sides of {a}, {b}, & {c} is a Equalateral Triangle")
elif (a== b or a==c) or (b==c):
    print(f"A triangle with sides of {a}, {b}, & {c} is a Isosceles Triangle") 
elif a != b and a !=c  and b != c:
    print(f"A triangle with sides of {a}, {b}, & {c} is a Scalene Triangle")
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle
