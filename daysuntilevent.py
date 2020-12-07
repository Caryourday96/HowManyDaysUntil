##How many days are there until?
# x event( Birthdays? and others)

#import b/c we are working with dates
import datetime


# define a number of methods

print("----------------")
print("Calculate Date Difference")
print("----------------")
print()


# getting user input for birthday , x , event

def get_birthday():
    print ("When were you born?", end="")
    year = int(input("What year were you born in?:"))
    month = int(input("What month were you born in?:"))
    day = int(input("What day were you born in?:"))


    birthdate = datetime.date(year,month,day)
    return birthdate 
#calculating 

# output to screen

#define a main method

def main():
    header()


main()
finaldate = get_birthday()
print(finaldate)