# s = "aaaabaaaa"
# k = 3

# s = "h"
# k = 1

s = "dii"
k = 1

def hasSpecialSubstring(s: str, k: int) -> bool:
    n = len(s)
    cnt = 1
    i = 0  # Start index of a possible k-length segment
    
    if n==1 and k==1:
        return True
    
    for j in range(1, n):  # Start loop from index 1
        if s[j] == s[j - 1]:  # Same as the previous character
            cnt += 1
        else:
            cnt = 1
            i = j  # Reset start index to the new character
        
        if cnt == k:  # We found a substring of length k
            before_valid = (i == 0 or s[i - 1] != s[i])  # Either at start or previous is different
            after_valid = (j == n - 1 or s[j + 1] != s[j])  # Either at end or next is different
            
            if before_valid and after_valid:
                return True
        
    return False


print(hasSpecialSubstring(s,k))