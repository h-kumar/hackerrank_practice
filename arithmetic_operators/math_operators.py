# Task
# The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.

# Example
#a=3
#b=5

# Print the following:
# 8
# -2
# 15

# Input Format
# The first line contains the first integer, a.
# The second line contains the second integer,b .

# Constraints
#1<a<10^10
#1<b<10^10

# Output Format

# Print the three lines as explained above.

# Sample Input 0
# 3
# 2

# Sample Output
# 5
# 1
# 6


def math_op():
    a = int(input())
    b = int(input())

    def add_num(a,b):
        sum = a+b;
        return sum;
    print(add_num(a,b))

    def sub_num(a,b):
        sub = a-b;
        return sub;
    print(sub_num(a,b))

    def prod_num(a,b):
        prod = a*b;
        return prod;
    print(prod_num(a,b))

if __name__ == '__main__':
    math_op()
