def maxFreqSum(s: str) -> int:
    vowelsDict = {}
    consonantsDict = {}

    for ch in s:
        if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
            vowelsDict[ch] = vowelsDict.get(ch, 0) + 1
        else:
            consonantsDict[ch] = consonantsDict.get(ch, 0) + 1

    max_vowel = 0
    max_consonant = 0

    if len(vowelsDict) != 0:
        max_vowel = max(vowelsDict.values())
    if len(consonantsDict) != 0:
        max_consonant = max(consonantsDict.values())
        
    return max_vowel + max_consonant

s = "aeiaeia"
ans = maxFreqSum(s)
print(ans)