# functions in python

def getName(param='John Doe'):
    return 'Your name is : {}'.format(param)


name = getName('Jeevan')

print(name)

# type checking in python

def addNumbers(num1,num2):
     # compare the type of integer, say 1 
     if type(num1)==type(num2)==type(1):
         return num1+num2
     else:
         return 'need integers to add'

sum1 = addNumbers(20,30)
sum2 = addNumbers('20', '30')

print(sum1)
print(sum2)


# check if an item in a list 

myList2 = ['Jeevan', 37, 'John', 'Java', 'Python']

result = 'Jeevan' in myList2
print(result)

result1 = 100 in myList2
print(result1)