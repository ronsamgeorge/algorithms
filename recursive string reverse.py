# Recursive function are those function who call themselves in the same function
# this process of calling itself is called recursion 

# they use the call stack to keep track of the recursive function calls
# a recursive function needs to have a base case or stopping condition otherwise it will result in stack overflow 
# a recursive function should have two parts :
#	1. a base case part - stopping condition  
#	2. a recursive part 

### This program is going to implement string reverse using recursion and iterative method 

def RecursiveReverse(value):
	#print (value[len(value)-1])

	if len(value) == 1 :
		return value[0]
	else :s
		 return	value[len(value)-1] + RecursiveReverse(value[:-1])



#def IterativeReverse(value):

print(RecursiveReverse("hi asds"))
