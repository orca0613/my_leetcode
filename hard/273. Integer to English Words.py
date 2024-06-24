# Convert a non-negative integer num to its English words representation.

 

# Example 1:

# Input: num = 123
# Output: "One Hundred Twenty Three"
# Example 2:

# Input: num = 12345
# Output: "Twelve Thousand Three Hundred Forty Five"
# Example 3:

# Input: num = 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

class Solution:
    def numberToWords(self, num: int) -> str:
        if not num:
            return "Zero"
        z_nineteen = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine","Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        twenty_ninty = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        unit = ["", " Thousand ", " Million ", " Billion "]
        
        def convert_double(num):
            if num < 20:
                return z_nineteen[num]
            t = num // 10
            num %= 10
            if num:
                r = twenty_ninty[t - 2] + " " + z_nineteen[num]
            else:
                r = twenty_ninty[t - 2]
            return r
        
        def convert(num):
            if num < 100:
                return convert_double(num)
            h = num // 100
            num %= 100
            if num:
                r = z_nineteen[h] + " Hundred " + convert_double(num)
            else:
                r = z_nineteen[h] + " Hundred"
            return r
        
        u = 0
        result = ""
        while num:
            piece = num % 1000
            if piece:
                result = convert(piece) + unit[u] + result
            u += 1
            num //= 1000
        return result.rstrip()
        
        
        