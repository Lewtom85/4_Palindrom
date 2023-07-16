#Palindrom
def isPalindrome(s):
    if len(s) <= 1 :
        return True
    if s(0) == s(len(s) - 1):
        return isPalindrome(s(1:len(s) - 1))
    else:
        return False

Palindrome_input = ('kajak')
print("Palindrom check program")
for i in Palindrome_input:
    ans = isPalindrome(i)
    if ans == 1:
        print("The given string ", "'", i, "'", "is a palindrome")
    else:
        print("The given string ", "'", i, "'", "is not a palindrome")