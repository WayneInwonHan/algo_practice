def isPalindrome(self, s):
    new_string= [i.lower() for i in s if i.isalnum()]
    return new_string == new_string[::-1]