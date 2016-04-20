#Nearest Multiple Algorithm
#Purpose: Nearest Multiple Algorithm takes in a positive number called value and a specific multiple of a number called number,
#and finds the closest multiple to that value.  If there is more than one multiple that is closest to the value, then it will find the largest multiple.
#For example, if you have a value of 25 and a number of 4, then find the positive multiples of 4 such as 4, 8, 16, 24, 28,...
#We see that 24 is the closest to 25, so nearestMultiple(25, 4) = 24.  
def nearestMultiple(value, number):
    multipleDict = {}
    lastMultiple = value + number
    for i in range(0, lastMultiple):
        multiple = number * i
        distance = abs(value - multiple) #find the distances between the multiples and the given value and add them to the dictionary.
        multipleDict[distance] = multiple
    minDistance = min(multipleDict.keys()) #find the smallest distance, which is the smallest key in the dictionary.
    return multipleDict[minDistance] #return the value, which is the value of the smallest key in the dictionary.

#Test 1: value = 48, number = 11
firstMultiple = nearestMultiple(48, 11)
print "Nearest Multiple: " + str(firstMultiple)

#Test 2: value = 79, number = 6
secondMultiple = nearestMultiple(79, 6)
print "Nearest Multiple: " + str(secondMultiple)

#Test 3: value = 21, number = 21
thirdMultiple = nearestMultiple(21, 21)
print "Nearest Multiple: " + str(thirdMultiple)



    
        
        
        
        
