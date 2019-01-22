def printList( list ):
    print("----------")
    counter = 0
    for item in list:
        print( str( counter ) + " => " + str( item ) )
        counter = counter + 1
    print("----------")

def numbersTimesTwo( numbers ):
    newList = list()

    for number in numbers:
        newList.append( number * 2)

    return newList

lambdaNumberTimesTwo = lambda number: number * 2
def NumberTimesTwo( number ):
    return number * 2

def fold( list, startValue, function ):
    result = startValue

    for item in list:
        result = function( result, item )

    return result

def factorial( number ):
    if number <= 1:
        return 1
    return number * factorial( number - 1)

def recursiveFold( function, startValue, *items, startIndex = 0 ):
    if len( items ) <= startIndex:
        return startValue

    return function (  
        recursiveFold( function, startValue, *items, startIndex = startIndex + 1 ), 
        items[startIndex]
    )

# printList( [9, 8, 7, 6 ] )
printList( numbersTimesTwo( [9, 8, 7, 6 ] ) )

print( 
    fold( 
        [2, 4, 6, 8], 
        0, 
        lambda result, number: result + number
    )
)

print(
    recursiveFold (
        lambda result, number: result - number,
        0,
        1, 3, 5, 7, 9
    )
)