class Solution:
    def isPalindrome(self, x: int) -> bool:
        int_to_string = str(x)
        reverse_str = int_to_string[::-1]
        if int_to_string == reverse_str:
            return True
        else:
            return False
        return
        
