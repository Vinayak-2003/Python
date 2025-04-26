s = "babab"

def smallestPalindrome(s: str) -> str:
    count = {}
    ans = []
    odd = ""
    odd_cnt = 0
    
    for c in s:
        count[c] = count.get(c, 0) + 1
         
    for key,val in count.items():
        if val%2 == 1:
            odd_cnt += 1
            odd = key
            
        ans.append(key * (val//2))      # appending if multiple count exists
        
    if odd_cnt > 1:
        return ""
    
    ans = ''.join(sorted(ans))
    return ans + odd + ans[::-1]

   
ans = smallestPalindrome(s)
print(ans)