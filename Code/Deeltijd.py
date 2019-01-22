# Function that prints the contents of a list with their indexes
def printList( list ):
    # Print a line
    print("------------")

    # Create a counter that keeps track of the index
    counter = 0

    # Loop over the items in the list
    for item in list:
        # Print the index with it's corresponding value
        print( str( counter ) + " => " + str( item ) )

    # Print another line
    print("------------")

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

# Create a lambda function that returns a given number times two
lambdaNumberTimesTwo = lambda number: number * 2

# Create the fold function
# The fold function combines all the items in a list into a single value
def fold( list, startValue, function ):
    # Create a variable that will store the result
    result = startValue

    # Loop over the items in the list
    for item in list:
        # Change the result using the provided function
        result = function( result, item )

    # Return the result
    return result

# Create the factorial function
def factorial( number ):
    # Check whether the number has reached the lowest possible boundery
    if number <= 1:
        # Return 1
        return 1
    # Make a recursive call multiplying the current number
    # with the result of another call to this function
    return number * factorial( number - 1 )

# Create the fold function in a recursive manner
def recursiveFold( function, startValue, *items, startIndex = 0 ):
    # Check whether we reached the final item in the list
    if len( items ) <= startIndex:
        # Return the base value
        return startValue
    # Return the execution of the function, with a recursive call and items
    return function( recursiveFold( function, startValue, *items, startIndex = startIndex + 1), items[startIndex] )

# Test the printList function by providing a list and watching the outcome
printList( [9, 8, 7, 6 ] )

# The printList function can also be used for function that return a list
printList( numbersTimesTwo( [9, 8, 7, 6 ] ) )

# We start by the normal fold function, we want to add up all the numbers
print( 
    fold( 
        [2, 4, 6, 8], 
        0, 
        lambda result, number: result + number
    )
)

# Now we use the recursive fold function, we wanna subtract all the numbers
print(
    recursiveFold (
        lambda result, number: result - number,
        0,
        1, 3, 5, 7, 9
    )
)