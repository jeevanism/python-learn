#lambda expression (amomymous function)
"""
    if there is a use case that a function is required only once, better us a lambda expression instead of a function
    lets create a normal function first then convert it into lambda
"""


# lets make a list

myList = ['Jeevan', 37, 'Male', 'India']

# lets make a function to filter only strings from a given list

def stringsOnly(param):
    return type(param)==type('String')

# filter is helper function in Python - takes two args - 1) another function 2) list or any other
filteredList = filter(stringsOnly,myList)

# this will get an error since we dont cast this into list - filter  helps outs a generic result
print(filteredList)

#cast the filter output into list
print(list(filteredList))


#lets apply lambda expression - no need of def, just use the arg : then return arg

#lambda param:type(param)==type('String')

filteredListWithLambdaEx= filter(lambda param:type(param)==type('String'), myList)
print(list(filteredListWithLambdaEx))
