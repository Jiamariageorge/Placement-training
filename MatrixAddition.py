a, b = map(int, input().split())
matrix1 = []
matrix2 = []
for i in range(a):
    row = list(map(int, input().split()))
    matrix1.append(row)
print("First Matrix:")
for row in matrix1:
    print(' '.join(map(str, row)))
for i in range(a):
    row = list(map(int, input().split()))
    matrix2.append(row)
print("Second Matrix:")
for row in matrix2:
    print(' '.join(map(str, row)))
summatrix = []
for i in range(a):
    row = []
    for j in range(b):
        row.append(matrix1[i][j] + matrix2[i][j])
    summatrix.append(row)
print("Sum of the two matrices is:")
for row in summatrix:
    print(' '.join(map(str, row)))

Question:
Imagine you are helping a student with their mathematics homework which involves a lot of problems based on matrix addition. You decide to write a program to automate the task of adding two matrices, which would make the homework a breeze!

Write a program to add two matrices. The program should:

Prompt the user to enter the dimensions of the matrices (assume both matrices have the same dimensions).

Accept the elements of the two matrices from the user.

Display the two matrices.

Add the two matrices.

Print the resultant matrix.

Kindly check the sample test case for input and output format.

Input Format

2 2
1 2
3 4
5 6
7 8

Constraints

NA

Output Format

First Matrix:
1 2
3 4
Second Matrix:
5 6
7 8
Sum of the two matrices is:
6 8
10 12
