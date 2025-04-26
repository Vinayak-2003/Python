# Group Anagrams Together
# Input: A list of strings.
# Output: A list of groups of anagrams.
# Example: 
    # Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
    # Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

from collections import defaultdict

list1 = ["eat", "tea", "tan", "ate", "nat", "bat"]

ans = defaultdict(list)

# for word in list1:
#     sorted_word = "".join(sorted(word))
#     ans[sorted_word].append(word)
    
# print(ans.values())

for word in list1:
    freq_arr = [0]*26
    
    for i in word:
        freq_arr[ord(i)-ord("a")] += 1
        
    ans[tuple(freq_arr)].append(word)
    
# print(ans.values())

def check_anagram(str1, str2):
    count_str1 = {}

    for i in str1:
        if i in count_str1:
            count_str1[i] += 1
        else:
            count_str1[i] = 1
            
    for i in str2:
        if i in count_str1:
            count_str1[i] -= 1
            
    for i in count_str1.values():
        if i != 0:
            return False
    return True
    
ans = []
n = len(list1)
for i in range(0,n):
    temp_list = [list1[i]]
    for j in range(i+1, n):
        if check_anagram(list1[i], list1[j]):
            temp_list.append(list1[j])
    
    ans.append(temp_list)
    
print(ans)



str1 = "eat"
str2 = "ate"

count_str1 = {}

for i in str1:
    if i in count_str1:
        count_str1[i] += 1
    else:
        count_str1[i] = 1
        
for i in str2:
    if i in count_str1:
        count_str1[i] -= 1

flag = 1
for i in count_str1.values():
    if i != 0:
        flag = 0
        break
    
if flag == 1:
    print("anagram")
else:
    print("not anagram")