Solution:
def push(x):
    stack.append(x)

def pop():
    if stack:
        stack.pop()

def top():
    if stack:
        return stack[-1]
    return None

def get_min():
    if stack:
        return min(stack)
    return None


a = int(input())  
stack = []

for _ in range(a):
    c = list(map(int, input().split()))
    if c[0] == 0:         
        push(c[1])
    elif c[0] == 1:       
        pop()
    elif c[0] == 2:       
        x = top()
        if x is not None:
            print(x)
    elif c[0] == 3:       
        y = get_min()
        if y is not None:
            print(y)


Question:
Rar the Cat has developed a new data structure, the MinStack!

Rar's data structure supports the following operations:

push: pushing an integer X to the top of the stack. (0)
pop: removes the top integer from the stack. (1)
top: retrieves the value of the top integer on the stack. (2)
getMin: retrieves the value of the minimum integer in the stack. (3)
There will be a total of Q queries to the data structure. Help Rar implement it.

Implementation Details:

This is a function-call question. You are to implement the following functions:

void push(int X): push X into the stack.
void pop(): remove the top element from the stack.
int top(): returns (but not remove) the top element on the stack.
int getMin(): returns (but not remove) the minimum element on the stack.
It is guaranteed that pop, top and getMin will not be called when the stack is empty.

You may access the sample grader and solution template from the Attachments tab to test your solutions.

Sample Testcase 1

Input

6 0 5 0 9 2 3 0 1 3

Output

9 5 1

Input Format

NA

Constraints

NA

Output Format

NA

Sample Input 0

6
0 5
0 9
2
3
0 1
3
Sample Output 0

9
5
1
