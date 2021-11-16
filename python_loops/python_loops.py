# Task
# Read an integer N. For all non-negative integers i < N, print i^2. See the sample for details.
# Input Format
# The first and only line contains the integer, N.
# Constraints
# i <= N <= 20
# Output Format
# Print N lines, one corresponding to each i.
# Sample Input 0
# 5
# Sample Output 0
# 0
# 1
# 4
# 9
# 16


def python_loops():
    limit = int(input())
    for n in range(0,limit):
        print(n*n)

if __name__ == '__main__':
    python_loops()