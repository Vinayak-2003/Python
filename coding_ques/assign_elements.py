groups = [8,4,3,2,4]
elements = [4,2]

n = len(elements)
m = len(groups)

assigned = [-1]*m

for i in range(0,n):
    for j in range(0,m):
        if assigned[j] == -1 and groups[j]>=elements[i] and groups[j]%elements[i] == 0:
            assigned[j] = i
        
print(assigned)