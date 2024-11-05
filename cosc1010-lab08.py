# RJ Tardoni
# UWYO COSC 1010
# Submission Date 11/04/2024
# Lab 08
# Lab Section: 14
# Sources, people worked with, help given to:
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 



def check_float_or_int (string_to_check):
    """A function to check for int or float"""
    returnValue = False
    try:
        returnValue = float (string_to_check)
        returnValue = int(string_to_check)
    except:
        pass
    return returnValue

print(check_float_or_int("12.5") )
print(check_float_or_int("-12"))


print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def slope_intercept(m,b,a,an):
    """parameters for a slope intercept"""
    m_number = check_float_or_int(m)
    b_number = check_float_or_int(b)
    a_number = check_float_or_int(a) 
    an_number = check_float_or_int(an)
    y_array= []
    if (m_number and b_number and a_number and an_number):

        for x in range(a_number,an_number):
            y = m_number * x + b_number
            y_array.append(y)
        return y_array
    
    else:
        print("Invalid number")
    
while True:
    m=input("Type a value for m")
    if (m=="exit"):
        break
    b=input("Type a value for b")
    if (b=="exit"):
        break
    a=input("Type a value for a")
    if (a=="exit"):
        break
    an=input("Type a value for an") 
    if (an=="exit"):
        break
    print(slope_intercept(m,b,a,an))

print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null
#use function from the first part to write in the third part, and only break the loop when exit from the user

def sqrt (a,b,c):
    """square root"""
    a_number = check_float_or_int(a)
    b_number = check_float_or_int(b)
    c_number = check_float_or_int(c) 
    discriminant = []
    if (a_number and b_number and c_number):
        discrim = (b_number*b_number-4*a_number*c_number)
        discriminant.append(discrim)
        return discriminant
    else:
        print("Invalid number")

def quadratic(a,b,c):
    """parameters the quadratic formula"""
    a_number = check_float_or_int(a)
    b_number = check_float_or_int(b)
    c_number = check_float_or_int(c) 
    x_array= []
    if (a_number and b_number and c_number):
    
         
            x= (-b_number +-  (discriminant))/(2*a_number)
            x_array.append(x)
            return x_array
    
    else:
        print("Invalid number")



while True:
    a=input("Type a value for a")
    if (a=="exit"):
        break
    b=input("Type a value for b")
    if (b=="exit"):
        break
    c=input("Type a value for c")
    if (c=="exit"):
        break
   
    print(quadratic(a,b,c))
