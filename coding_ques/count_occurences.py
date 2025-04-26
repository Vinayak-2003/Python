str1 = "aabbbcccccaa"
ans = ""
i,j = 0,0
cnt = 0

while i<=j and i<len(str1) and j<len(str1):
    if str1[i] == str1[j]:
        j += 1
        cnt += 1
        if j == len(str1):
            ans += str1[i]
            ans += str(cnt)
    else:
        ans += str1[i]
        ans += str(cnt)
        cnt = 0
        i = j
        
        

# for i in range(len(str1)):
#     if str1[i] == str1[j]:
#         cnt += 1
#     else:
#         ans += str1[j]
#         ans += str(cnt)
#         cnt = 0
#         j = i
        
print(ans)