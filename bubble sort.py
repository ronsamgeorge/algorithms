"""
this program implements bubble sort. Which has an average and worst case complexity of O(n^2)

In this sorting algorithm we compare the adjacent elements and swap if the condition is met as we move through the array

This process is repeated for n-1 iteration
"""

def BubbleSort(arr):

	for i in arr:
		for j in range (len(arr)-1):
			if arr[j]>arr[j+1]:
				temp = arr[j]
				arr[j] = arr[j+1]
				arr[j+1] = temp

	print(arr)


arr = [1,0,5,2,22,3,35,77]
BubbleSort(arr)