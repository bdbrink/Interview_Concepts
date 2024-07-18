class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        prev_value = 0
        
        for char in s[::-1]:
            current_value = roman_values[char]
            
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value
            
            prev_value = current_value
        
        return total
    

class SolutioInt:
    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        
        roman = ""
        
        for i, value in enumerate(values):
            # While the number is greater than or equal to the current value
            while num >= value:
                # Add the corresponding symbol to the result
                roman += symbols[i]
                # Subtract the value from the number
                num -= value
        
        return roman