#Author: Ben McGahee
#Title: String and Compression Algorithms
#Date: 4/18/2016
#Purpose: These two functions take an encoded string and expand to its decoded string,
#and finds the ratio of the length of the encoded string to the length of the decoded string.
#This is known as the compression ratio.

#expandString() takes a string in the form "c1n1c2n2...cknk",
#where c1, c2, c3, ..., ck are the characters and
#n1, n2, n3, ..., nk are the number of times each character is repeated
#and returns the expanded string.
#For example, expandString("a3b4") = aaabbbb.
def expandString(compString):
    fullString = ""
    size = len(compString)
    for i in range(0, size):
        evenIndex = 2 * i
        oddIndex = 2 * i + 1
        if evenIndex < size and oddIndex < size:
            char = compString[evenIndex]
            repeat = int(compString[oddIndex])
            charRepeat = char * repeat
            fullString += charRepeat
    return fullString

#compRatio() takes an encoded string in the form "c1n1c2n2...cknk" and
#uses expandString() to create the decoded string.
#Then the function finds the ratio of the length of the encoded string to the length of the decoded string
#and returns that ratio.
#For example, compRatio("a3b4") compares the lengths of "a3b4" and "aaabbbb",
#and will return a ratio of 0.57 rounded to two decimal places.
def compRatio(encodeString):
    decodeString = expandString(encodeString)
    encodeSize = len(encodeString) * 1.0
    decodeSize = len(decodeString) * 1.0
    ratio = round(encodeSize / decodeSize, 2)
    return ratio

#spaceSavings() uses compRatio() to determine how much space one can save after data compression.
#For example, if you have a string "aaa" and compress it to "a3" then the compression ratio is 2/3 or 0.67
#Thus, the amount of space you save with this compression is 1 - 0.67 = 0.33 or 33%.  
def spaceSavings(string):
    ratio = compRatio(string)
    savings = (1 - ratio) * 100.0
    return savings

#Test 1: "a1b2c3"
#Shows there is no savings in space because len("a1b2c3") = len("abbccc") = 6.
firstString = "a1b2c3"
firstStringRatio = compRatio(firstString)
firstSavings = spaceSavings(firstString)

print "Compression Ratio: " + str(firstStringRatio)
print "Space Savings: " + str(firstSavings) + "%"

#Test 2: "d4f5"
#Shows there is savings in space because len("d4f5") = 4 and len("ddddfffff") = 9 and 1 - 4/9 = 5/9 or about 56%.
secondString = "d4f5"
secondStringRatio = compRatio(secondString)
secondSavings = spaceSavings(secondString) 

print "Compression Ratio: " + str(secondStringRatio)
print "Space Savings: " + str(secondSavings) + "%"

#Test 3: "k1"
#Shows there is a loss of space because len("k1") = 2 and len("k") = 1 and 1 - 2/1 = -1 or -100%.  Negative sign means a loss.
thirdString = "k1"
thirdStringRatio = compRatio(thirdString)
thirdSavings = spaceSavings(thirdString)

print "Compression Ratio: " + str(thirdStringRatio)
print "Space Savings: " + str(thirdSavings) + "%"



    
