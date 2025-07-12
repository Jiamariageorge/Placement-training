solution:
n = int(input())
arr = list(map(int, input().split()))

minp = arr[0]   
maxp = 0       

for i in range(1, n):
    if arr[i] < minp:
        minp = arr[i]
    profit = arr[i] - minp
    maxp = max(maxp, profit)

print(maxp)

Question:
Write a program that takes an array that denotes the daily closing prices of a stock to determine the maximum profit by buying and selling one share of the stock.

Input Format

9
310 315 275 260 270 290 230 255 250

Constraints

NA

Output Format

30

Sample Input 0

9
310 315 275 260 270 290 230 255 250
Sample Output 0

30
