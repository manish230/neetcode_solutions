class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS= s.strip()
        joinS=re.sub(r'[^a-zA-Z0-9]', '', newS)
        return joinS.lower() == joinS[::-1].lower()
