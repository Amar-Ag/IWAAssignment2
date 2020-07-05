"""
2.Write an if statement to determine whether a variable holding a year
is a leap year.
"""
try:
    inputYear = int(input("Enter a year:"))
except ValueError:
    inputYear = int(input("Invalid year. Enter a valid year:"))
if inputYear % 400 == 0:
    print(f"{inputYear} is leap year.")
elif inputYear % 100 == 0:
    print(f"{inputYear} is not a leap year.")
elif inputYear % 4 == 0:
    print(f"{inputYear} is leap year.")
else:
    print(f"{inputYear} is not a leap year.")
