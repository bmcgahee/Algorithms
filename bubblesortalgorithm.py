#Bubble Sort
#Purpose:  The bubble sort algorithm starts at the first element of the list and compares its value to the next element of the list.
#If the pair of element are in the correct order, then go to next pair of elements.
#Otherwise, swap the pair of elements.
#The bubble sort does this until all of the elements are in the correct order.
#Note:  Bubble sort is a strong sorting algorithm for a small list of elements, but weak for a large list of elements.

def bubbleSort(List):
    length = len(List)
    for i in range(0, length - 1):
        for j in range(0, length - 1):
            if List[j + 1] < List[j]:
                temp = List[j + 1]
                List[j + 1] = List[j]
                List[j] = temp
    return List

#Test 1:  Sort all ten digits from 0 to 9.
numberList = [4, 2, 5, 7, 0, 1, 8, 9, 3, 6]
sortedNumberList = bubbleSort(numberList)
print sortedNumberList

#Test 2:  Sort all 26 letters in the English alphabet.
alphaList = ["b", "d", "c", "a", "g", "k", "i", "m", "p", "r", "v", "f", "z", "y", "x", "j", "h", "n", "q", "t", "o", "u", "w", "l", "e", "s"]
sortedAlphaList = bubbleSort(alphaList)
print alphaList
