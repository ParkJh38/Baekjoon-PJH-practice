N = int(input())
result = 1
if 0 < N <= 12:
    for i in range(1,N+1):
        result *= i
    print(result)
elif N == 0:
    print(1)
else:
    print("Error")