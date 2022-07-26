# print formatting 
from email import message


mystring = "Your name is : {}".format('Jeevan')
print(mystring)

#multiple strings

myName= "FirstName : {} SecondName : {}".format('Jeevan', 'Sivanandan')
print(myName)

#multiple strings with variables

myName= "FirstName : {fn} SecondName : {sn}".format(fn='Jeevan', sn='Sivanandan')
print(myName)

# To split a string with some conditions
# split a sentence with $ sign in it

message = "This shoe costs $120"
splittedMessage = message.split('$')
price = message.split('$')[1]
price1 = splittedMessage[1]
print(price)
print(price1)