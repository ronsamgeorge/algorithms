"""
This program will implement Selection sort. Which  has a time complexity of O(n^2) and a space complexity of O(1)

Algorithm :
 The number of iterations over the entire list will be n-1 iterations 
 which pick the smallest item in each iteration and then swap it with the ith element , which places the smallest element
 at the beginning of the list

"""

def SelectionSort(arr):

	print (arr)

	for i in range(len(arr)-1):
		
		smallestIndex=i
		for j in range(i+1,len(arr)):
			#smallestIndex = i
			if arr[smallestIndex] > arr[j]:
				smallestIndex = j

			temp = arr[smallestIndex]
			arr[smallestIndex]=arr[i]
			arr[i] = temp
		print (arr)
	return arr

arr = [20,1,4,2,67,9,90,1]

print(SelectionSort(arr))

