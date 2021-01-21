"""
This program implements insertion sort which has a worst case  time complexity of O(n^2) and space complexity of O(1)

 In this algorithm , the array has two part , the sorted part and the unsorted part.
 
 The sorted part starts at the index 0 for the first iteration, in the subsequent iterations , the element right after the sorted 
part is taken and compared with the elements in the sorted part of the array

When the relevant criteria is met, the item is inserted into the sorted half of the array at the appropriate index. all the other 
elements in the sorted array are moved one space to the right to make the insertion 

NOTE : beneficial when the data is close to sorted 
"""

def InsertionSort(arr):

	for i in range(1,len(arr)):
		# i signifies the beginning of the unsorted part of the array and hence starts from 1 as the 0 index element is singular and is sorted as it is 
		temp = arr[i] # saves the arr[i] element to shift later.
		j = i-1       # i-1 is the end point of the sorted parted of the array. this is where we have to start the comparison
		while (temp< arr[j] and j>=0): # run the loop until we find the position where the temp variable is less than the element at index j
			#print(j)
			arr[j+1] = arr[j]  	# shift the position as we go on finding the position
			j-=1 			   	# reduce j 

		arr[j+1] = temp 		# once the index is found for temp , insert the value there 

	return array 				# returns the sorted arr 

arr = [4,1,5,2,89,0,97,55,23,44] # declaring an array 
print (InsertionSort(arr))		 # calling and then printing the returned sorted aray 

