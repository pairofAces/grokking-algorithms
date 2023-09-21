# include summary here

'''
Here is an example of a countdown function, written recursively, but this
specific function will run forever in an infinite loop. 

def countdown(i):
    print i
    countdown(i-1)

'''

# When writing a recursive function, it must be told when to stop. 

'''
Therefore, every recursive function has two parts. 
- the base case
- the recursive case

The recursive case is when the function calls itself.

The base case is when the function (doesn't) call itself. 
'''

# Example of countdown, recursively, with the base case and recursive case.

def countdown(i):
    print(i)
    if i <= 1:
        return
    else:
        countdown(i - 1)

countdown(5)