import sys

input = lambda: sys.stdin.readline().rstrip()
T = int(input())
if T <= 1000000:
    for i in range(1, T+1):
        A, B = map(int, input().split())
        if 1 <= A <= 1000 and 1 <= B <= 1000:
            print(A+B)
        else:
            print("Error")
else: 
    print("Error")