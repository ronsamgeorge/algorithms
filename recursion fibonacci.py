# Recursive function are those function who call themselves in the same function
# this process of calling itself is called recursion 

# they use the call stack to keep track of the recursive function calls
# a recursive function needs to have a base case or stopping condition otherwise it will result in stack overflow 
# a recursive function should have two parts :
#	1. a base case part - stopping condition  
#	2. a recursive part 

# This program will implement the fibonacci series recursively and iteratively 

def RecursiveFibo(value):

	if value <= 0 :
		return 0

	elif value == 1 :
		return 1

	else :
		return RecursiveFibo(value-1) + RecursiveFibo(value-2)


def IterativeFibo(value):
	a = 0 
	b = 1 

	for i in range(value-1):
		c = a + b
		a = b
		b = c

	print (c)



print(RecursiveFibo(8))

IterativeFibo(8)