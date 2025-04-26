# Product of Array Except Self

# Return an array where each element is the product of all elements except itself.
# Example: Input: [1,2,3,4] → Output: [24,12,8,6]

list1 = [1,2,3,4]
n = len(list1)
# ans = [1]*n
product = 1

ans = []
# for i in list1:
#     product *= i
    
# for i in list1:
#     ans.append(product//i)
    
# for i in range(0,n):                    # ----- O(n^2)
#     for j in range(0,n):
#         if i==j:
#             product *= 1
#         else:
#             product *= list1[j]
#     ans.append(product)
#     product=1
    
# increased space complexity
# pre = [1]*n
# suf = [1]*n

# for i in range(1,n):
#     pre[i] = pre[i-1]*list1[i-1]
    
# for i in range(n-2, -1, -1):
#     suf[i] = suf[i+1]*list1[i+1]
    
# for i in range(0,n):
#     ans[i] = pre[i] * suf[i]


# optimized
for i in range(1,n):
    ans[i] = ans[i-1]*list1[i-1]

suf = 1
for i in range(n-2,-1,-1):
    suf *= list1[i+1]
    ans[i] *= suf

print(ans)