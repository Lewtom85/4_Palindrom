#Palindrom
# 1. Wersja z Rafalem. Dziala poprawnie
text = ("kajak")

def palindrom(text):
    text = text.lower()
    return text == text[::-1]

print(palindrom(text))
print(text)

#2. Wersja z internetu z bledem.
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

# 3. Wersja internet.
a_string = ("potop")

def palindrome(a_string):
    a_string = a_string.lower().replace(' ', '')
    reversed_string = ''
    for i in range(len(a_string), 0, -1):
        reversed_string += a_string[i-1]
    return a_string == reversed_string
print(palindrome(a_string))
