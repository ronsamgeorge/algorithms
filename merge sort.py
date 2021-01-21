"""
Merge sort works on the principle of divide and conquer.

This constantly divides the array into halves until only one element is left in each part and it can't be broken down any further
Afer this merging and sorting of the array start until all the elements are merged and sorted into one 

Time complexity : O(n log n) -- better than the elementary sort algorithms(bubble,selection,insertion) which are O(n^2)
Space complexity : O(n)     --- worse than elementary sort algorithms since we have to maintain the data once we divide the array

"""

# the merge() method breaks down the arr into halves until there is only one element in each component 
def merge(arr):

	if len(arr) == 1 : # base case for the recursion to return arr when the len of each halve reaches 1
		return arr
	else:	
		half = len(arr)	// 2		# Finding the mid point of the arr to perform the separation on 

		#print (half)
		left = arr[0:half]				# left will be from 0 to half-1
		right = arr[half:len(arr)]	# right will be from half to (array length-1)

		#print (left)
		#print (right)
		return MergeSort(merge(left),merge(right)) # calls the MergeSort() function with each half as the arguments 



# MergeSort() function does the sorting between two halves (left and right part) of the array in a particular iteration  

def MergeSort(left,right):  		# takes two lists as an argument on which to perform the sorting 
	sortedArr = []					# declaring an empty list to insert the sorted items into

	counterLeft = 0					# keeps track of the elements in the left array , starts at the first index = 0
	counterRight = 0				# keeps track of the elements in the right array, starts at the first index = 0

	while (counterLeft < len(left) and counterRight < len(right)):  # runs till either of the side reaches the end of the array

		# the section below compares the elements in both the arrays provided and counters are updated accordingly

		if left[counterLeft] < right[counterRight]:			
			sortedArr.append(left[counterLeft])
			counterLeft+=1

		elif left[counterLeft] == right[counterRight] :
			sortedArr.append(left[counterLeft])
			sortedArr.append(right[counterRight])
			counterLeft+=1
			counterRight+=1

		else :
			sortedArr.append(right[counterRight])
			counterRight+=1

	# the additional + are for the remaining elments that might be present in the array whose counter didn't reach the end 
	return sortedArr + left[counterLeft:] + right[counterRight:]




# main driver code 
arr = [12,2,45,3,67,1,23,0,11,1]
print(arr)
print(merge(arr))