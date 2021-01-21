# Recursive function are those function who call themselves in the same function
# this process of calling itself is called recursion 

# they use the call stack to keep track of the recursive function calls
# a recursive function needs to have a base case or stopping condition otherwise it will result in stack overflow 
# a recursive function should have two parts :
#	1. a base case part - stopping condition  
#	2. a recursive part 


# this program will implement factorial using recursion and iterative methods 

def RecursiveFactorial(value):

	if value <= 1:
		return 1

	else :
		return value * RecursiveFactorial(value-1)

def IterativeFactorial(value):

	val = value
	factorial = 1

	print (value)
	for i in range(value,1,-1):
		factorial = factorial * i 

	print (factorial)

IterativeFactorial(0)
print(RecursiveFactorial(0))