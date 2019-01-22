# We create an empty list
emptyList = list()

# We create a list with all the characters available in base 10 (Decimal)
numberList = list([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

# We create a list with all the characters available in base 2 (Binary)
otherNumbers = list([1, 0])

# Function that prints the contents of a list with their indexes
def printList( list ):
    # Print a line
    print("------------")

    # Create a counter that keeps track of the index
    counter = 0

    # Loop over the items in the list
    for item in list:
        # Print the index with it's corresponding value
        print( "[{0}] => {1}".format(counter, item) )

    # Print another line
    print("------------")

# We print all decimal numbers with the printList function
printList(numberList)

# Function that doubles all the numbers in a list
def numbersTimesTwo( numbers ):
    # Create a new list
    newList = list()
    
    # Loop over the numbers in the list
    for number in numbers:
        # Add the doubled number to the new list
        newList.append( number * 2 )

    # Return the new list
    return newList

# Try the function by calling it, and printing the result using the printList function
printList( numbersTimesTwo( otherNumbers ) )

# We define a function that returns a number multiplied by two
def singleNumberTimesTwo( number ):
    # Return the number multiplied by two
    return number * 2

# We define a lambda that returns a number multiplied by two
lambdaDoubler = lambda number: number * 2

# Using print, we show that the lambda and the function have the exact same behaviour
print ( singleNumberTimesTwo( 5 ) )
print ( lambdaDoubler( 5 ) )

# We define a map function
# The map function loops over all the items in a list, performs a function
# and returns the result in a new list
def Map( someList, action ):
    # Create a list that will store the manipulated values
    resultList = list()

    # Loop over alll the items in the list
    for item in someList:
        # Perform the function and store the item to the new list
        resultList.append( action( item ) )
    
    # Return the new list
    return resultList

# Define some lambda functions to test out the map function
multiplication = lambda number: number * 2
division = lambda number: number / 2

# Call the map function using two different lambdas
printList( Map( numberList, multiplication ) )
printList( Map( numberList, division ) )

# Define a fold func
def Fold( function, *items, startValue = 0):
    result = startValue

    for item in items:
        result = function( result, item )

    return result

# Create the fold function
# The fold function combines all the items in a list into a single value
def fold( function, *items, startValue = 0 ):
    # Create a variable that will store the result
    result = startValue

    # Loop over the items in the list
    for item in items:
        # Change the result using the provided function
        result = function( result, item )

    # Return the result
    return result

# Try oyut the fold function using some nice lambdas
print( Fold( lambda result, item: result + item, 2, 4, 6, 8 ) )
print( Fold( lambda result, item: result - item, 2, 4, 6, 8, startValue = 100 ) )

# Create the fold function in a recursive manner
def recursiveFold( function, startValue, *items, startIndex = 0 ):
    # Check whether we reached the final item in the list
    if len( items ) <= startIndex:
        # Return the base value
        return startValue
    # Return the execution of the function, with a recursive call and items
    return function( recursiveFold( function, startValue, *items, startIndex = startIndex + 1), items[startIndex] )

# The recursiveFold is called and the result is printed
print( recursiveFold( lambda result, item: result * item, 20, 1, 3, 5, 7, 9) )
