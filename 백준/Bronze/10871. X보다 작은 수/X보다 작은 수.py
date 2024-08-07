N, X = map(int, input().split())
if 1 <= N:
    A = list(map(int, input().split()))
    for i in range(N):
        if A[i] < X:
            print(A[i], end= " ")
else: 
    print("N value error")