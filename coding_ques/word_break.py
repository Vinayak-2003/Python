# Given a string s and a dictionary of strings wordDict, return true if s can be segmented 
# into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true

s = "leetcode"
wordDict = ["leet","cods"]

n = len(s)
temp_str = ""
temp_list = []
i = 0
for j in range(0,n):
    temp_str += s[j]
    if temp_str in wordDict:
        i = j+1
        temp_list.append(temp_str)
    if j==n-1:
        temp_list.append(temp_str)
        temp_str = ""
    j += 1
    
# print(temp_list)
for word in temp_list:
    if word in wordDict:
        # print(word)
        continue
    else:
        print("FALSE")

print("TRUE")