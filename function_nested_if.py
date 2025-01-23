# This scrip demonstrates how to nest if statements in a function
# Given a year it determines if it is a leap year or not

def is_leap(year):
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

if __name__ == '__main__':
    year = int(input("Enter a year: "))
    print(is_leap(year))
