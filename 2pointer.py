Solution:
def num(arr, b):
    left = 0
    right = len(arr) - 1

    while left < right:
        s = arr[left] + arr[right]
        if s == b:
            return "Yes"
        elif s < b:
            left += 1
        else:
            right -= 1

    return "No"

a = int(input())
arr = list(map(int, input().split()))
b = int(input())

c = num(arr, b)
print(c)

question:

Given a sorted (in ascending order) integer array nums of n elements and a target value, find if there exists any pair of elements (nums[i], nums[j], i!=j) such that their sum is equal to target.

Solve this problem using the Two-pointers concept. The complexity should not be O(N-square) or more

Input Format

5
-3 -1 0 1 2
-2

Constraints

1 < nums.length <100

Output Format

Yes

Sample Input 0

5
-3 -1 0 1 2
-2
Sample Output 0

Yes
