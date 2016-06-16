# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = 0
max_index_x = -1
max_index_y = -1

for i in range(0, n):
    if ((max_index_x == -1) or (a[i] > a[max_index_x])):
        max_index_x = i
        
for j in range(0, n):
    if ((j != max_index_x) and ((max_index_y == -1) or (a[j] > a[max_index_y]))):
        max_index_y = j

result = a[max_index_x] * a[max_index_y]
        
print(result)
