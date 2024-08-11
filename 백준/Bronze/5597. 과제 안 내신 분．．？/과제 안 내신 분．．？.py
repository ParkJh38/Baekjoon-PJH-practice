#stdNumber = list(map(int, input().split()))
stdNumber = []
for i in range(28):
    n = int(input())
    stdNumber.append(n)
stdNumber.sort()
notInList = []

for i in range(1,31):
    if i not in stdNumber:
        notInList.append(i)
print(min(notInList))
print(max(notInList))
