# Task
# Given an integer, n, perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

# Input Format

# A single line containing a positive integer, n.

# Constraints

# Output Format

# Print Weird if the number is weird. Otherwise, print Not Weird.

def if_else_func():
    n = int(input().strip())
    if (n%2) != 0:
        print('Weird')
        return 'Weird'
    elif (n%2) == 0:
        if n in range(2,5):
            print('Not Weird')
            return 'Not Weird'
        elif n in range(6,21):
            print('Weird')
            return 'Weird'
        else: print ('Not Weird')
        return 'Not Weird'

if __name__ == '__main__':
    if_else_func()









