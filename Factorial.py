Solution:
def fact(n):
    if n==0:
        return 1
    else:
        return fact(n-1)*n
n=int(input())
f=fact(n)
print(f)

Question:
Write a program to find the factorial of a number using recursion.

Input Format

Read a number n from the console

Constraints

NA

Output Format

Print the factorial of the number n

Sample Input 0

6
Sample Output 0

720
