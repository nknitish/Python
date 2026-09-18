# EPAM

from typing import List
def two_sum(nums: List[int], target: int) -> List[int]:

    num_obj={}
    for index, num in enumerate(nums):
        complement= target-num
        if complement in num_obj:
            return [num_obj[complement], index]
        
        num_obj[num]=index




# nums = [3, 2, 4]
# target = 6
# print(two_sum(nums, target))


#-----------------------------------------------------------------------

def longest_substring(s: str) -> int:
    seen= set();
    maxlen=0
    left=0
    
    for right,char in enumerate(s):
        
        while char in seen:
            seen.remove(s[left])
            left+=1

        seen.add(char)
        maxlen= max(maxlen, right-left+1)
    
    return maxlen


print(longest_substring("abcabcbb"))    
