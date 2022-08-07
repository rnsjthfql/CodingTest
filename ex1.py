n = int(input())
arr = list(map(int, input().split()))
arr2 = []

print(arr)


a = 1
for i in arr:
  if i == a:
    arr2.append(i)
    a += 1

print(arr2)

print(len(arr) - len(arr2))