#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1

class Solution:
    def mergeAlternately(self, word1, word2):
        result = []
        i, j = 0, 0

        while i < len(word1) and j < len(word2):
            result.append(word1[i])
            result.append(word2[j])
            i += 1
            j += 1

        # Append remaining characters from word1, if any
        while i < len(word1):
            result.append(word1[i])
            i += 1

        # Append remaining characters from word2, if any
        while j < len(word2):
            result.append(word2[j])
            j += 1

        return ''.join(result)


sol = Solution()
word1_example = "abc"
word2_example = "pqr"
result_example = sol.mergeAlternately(word1_example, word2_example)
print(result_example)  


# In[ ]:


#2

class Solution:
    def findTheDifference(self, s, t):
        result = 0

        # XOR all characters in both strings
        for char in s:
            result ^= ord(char)

        for char in t:
            result ^= ord(char)

        # Convert the XOR result back to a character
        return chr(result)

# Example usage:
sol = Solution()
param_1 = "abcd"
param_2 = "abcde"
ret = sol.findTheDifference(param_1, param_2)
print(ret)  


# In[ ]:


#3

class Solution(object):
    def strStr(self, haystack, needle):
        if not needle:
            return 0

        haystack_len, needle_len = len(haystack), len(needle)

        for i in range(haystack_len - needle_len + 1):
            if haystack[i:i + needle_len] == needle:
                return i

        return -1


haystack_example1 = "sadbutsad"
needle_example1 = "sad"
output_example1 = Solution().strStr(haystack_example1, needle_example1)
print(output_example1)

haystack_example2 = "leetcode"
needle_example2 = "leeto"
output_example2 = Solution().strStr(haystack_example2, needle_example2)
print(output_example2)


# In[ ]:


#4

class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)


s_e1, t_e1 = "anagram", "nagaram"
output_1 = Solution().isAnagram(s_e1, t_e1)
print(output_1) 

s_e2, t_e2 = "rat", "car"
output_2 = Solution().isAnagram(s_e2, t_e2)
print(output_2)  


# In[ ]:


#5

class Solution(object):
    def repeatedSubstringPattern(self, s):
        length = len(s)

        for substring_len in range(1, length // 2 + 1):
            if length % substring_len == 0:
                substr = s[:substring_len]
                repetitions = length // substring_len
                repeated_string = substr * repetitions

                if repeated_string == s:
                    return True

        return False

sol = Solution()

s_example1 = "abab"
output_example1 = sol.repeatedSubstringPattern(s_example1)
print(output_example1)

s_example2 = "aba"
output_example2 = sol.repeatedSubstringPattern(s_example2)
print(output_example2)

s_example3 = "abcabcabcabc"
output_example3 = sol.repeatedSubstringPattern(s_example3)
print(output_example3)


# In[ ]:


#6

class Solution(object):
    def moveZeroes(self, nums):
        non_zero_ptr = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[non_zero_ptr] = nums[non_zero_ptr], nums[i]
                non_zero_ptr += 1

                
sol = Solution()

nums_example1 = [0, 1, 0, 3, 12]
sol.moveZeroes(nums_example1)
print(nums_example1)

nums_example2 = [0]
sol.moveZeroes(nums_example2)
print(nums_example2)


# In[ ]:


#7

class Solution(object):
    def plusOne(self, digits):
        n = len(digits)
        carry = 1

        for i in range(n - 1, -1, -1):
            total = digits[i] + carry
            digits[i] = total % 10
            carry = total // 10

        if carry:
            digits.insert(0, carry)

        return digits

sol = Solution()

digits_example1 = [1, 2, 3]
output_example1 = sol.plusOne(digits_example1)
print(output_example1)  

digits_example2 = [4, 3, 2, 1]
output_example2 = sol.plusOne(digits_example2)
print(output_example2)  

digits_example3 = [9]
output_example3 = sol.plusOne(digits_example3)
print(output_example3)  


# In[ ]:


#8

class Solution(object):
    def arraySign(self, nums):
        negative_count = 0

        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                negative_count += 1

        return 1 if negative_count % 2 == 0 else -1

# Example usage:
sol = Solution()

nums_example1 = [-1, -2, -3, -4, 3, 2, 1]
output_example1 = sol.arraySign(nums_example1)
print(output_example1)


# In[ ]:


#9

class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        arr.sort()
        common_diff = arr[1] - arr[0]

        for i in range(2, len(arr)):
            if arr[i] - arr[i-1] != common_diff:
                return False

        return True


sol = Solution()

arr_example1 = [3, 5, 1]
output_example1 = sol.canMakeArithmeticProgression(arr_example1)
print(output_example1)  

arr_example2 = [1, 2, 4]
output_example2 = sol.canMakeArithmeticProgression(arr_example2)
print(output_example2)  


# In[ ]:


#10

class Solution(object):
    def isMonotonic(self, nums):
        increasing = decreasing = True

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                decreasing = False
            elif nums[i] < nums[i-1]:
                increasing = False

        return increasing or decreasing


sol = Solution()

nums_example1 = [1, 2, 2, 3]
output_example1 = sol.isMonotonic(nums_example1)
print(output_example1)  

nums_example2 = [6, 5, 4, 4]
output_example2 = sol.isMonotonic(nums_example2)
print(output_example2) 

nums_example3 = [1, 3, 2]
output_example3 = sol.isMonotonic(nums_example3)
print(output_example3) 


# In[ ]:


#11

class Solution(object):
    def romanToInt(self, s):
        roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        prev_value = 0

        for numeral in s:
            value = roman_values[numeral]
            result += value

            # Check for subtractive pairs
            if value > prev_value:
                result -= 2 * prev_value

            prev_value = value

        return result

sol = Solution()

s_example1 = "III"
output_example1 = sol.romanToInt(s_example1)
print(output_example1)  

s_example2 = "LVIII"
output_example2 = sol.romanToInt(s_example2)
print(output_example2) 

s_example3 = "MCMXCIV"
output_example3 = sol.romanToInt(s_example3)
print(output_example3)

