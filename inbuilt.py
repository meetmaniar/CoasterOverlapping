import math


def checkSign(a, b):  # This function is to check weather the two numbers have the same polarity
    return a * b > 0


def bisection(function, negative, positive):
    # This function calculates the midpoint by performing number of iterations of getting the midpoints of the two numbers
    # with when substituted in the function, returns opposite polarity.
    assert not checkSign(function(negative), function(positive))

    for i in range(100):  # For 100 iterations
        midpoint = (negative + positive) / 2.0  # Getting the midpoint
        if checkSign(function(negative), function(midpoint)):  # Checking the polarity
            negative = midpoint  # setting the arguments for next iterations.
        else:
            positive = midpoint  # setting the arguments for next iterations.

    return midpoint  # Returning the midpoint which is most precise answer.


def UserInput():  # funtion for getting input from the user.
    try:
        r = float(input("Enter Radius: "))  # Getting float input from the user
        if(r < 0):  # Filtering out the negative number by raising the exception
            raise ValueError
        return float(r)
    except ValueError:  # Filtering the string and special characters out
        print("Invalid Input")
        UserInput()  # Recursively calling the same function
