#lists
"""
    Lists are python forms of arrays

"""

myList = ['Jeevan', 37, True,['106,Kenpas Highway', 'CV36BQ']]
print (myList)
print(len(myList))
print(myList[0])
print(myList[-1])
print(myList[:3])
print(myList[3:])

#assing new value
myList[0]='Sunija'
print(myList)
myList[0]='Jeevan'

#append item
myList.append('currently living here')
print(myList)

#extend an item inside the list
meenuList=['Sunija', 32, True,'Same Address']
myList.extend(meenuList)
print(myList)

# reverse
myList.reverse()
print(myList)

#sort
simpleList=[4,19,3,45]
simpleList.sort()
print(simpleList)


#List nested level
print(myList[5][0])


#matrix

aMatrix=[['Jeevan',37,'male'],['Sunija',31,'female'],['Appu',12,'Male']]
print(aMatrix[0][0])
print(aMatrix[1][0])
print(aMatrix[2][2])

#matrix - list comprehension 

firstRow=[row[0] for row in aMatrix]
ageRow=[row[1] for row in aMatrix]

print(firstRow)
print(ageRow)