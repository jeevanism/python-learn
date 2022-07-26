# some excercises
# check if a given list, a sequence of 1,2,3 is exist or not 

#arrayCheck([1,1,2,3,1]) -> True

#arrayCheck([1,1,2,4,1]) -> False

#arrayCheck([1,1,2,1,2,3]) -> True


def arrayCheck(numList):
    # need to check before last two items to check if the sequence end, not to the very last element
    # we can use range helper with length of the list
     
    for i in range( len(numList) -1 ):
         
        # check if first,second,third are in the sequenece we need
        if numList[i]==1 and numList[i+1]==2 and numList[i+2]==3:
            return True
    return False
 
print(arrayCheck([1,1,2,3,1]) ) 

print(arrayCheck([1,1,2,4,1]) ) 

print(arrayCheck([1,1,2,1,2,3]) ) 
 