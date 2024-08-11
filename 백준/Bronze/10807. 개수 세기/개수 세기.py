N = int(input())
numbers = list(map(int, input().split()))
target = int(input())

count = 0
for i in range(N):
    if numbers[i] == target:
        count += 1

print(count)