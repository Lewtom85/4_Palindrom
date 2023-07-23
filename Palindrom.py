#Palindrom

text = ("Kobyla, ma maly bok.")

def palindrom(text):
    x = ''.join(c for c in text if c.isalnum())
    x = x.lower() #zmieniam litery na male w tekscie
    print(x)
    return x == x[::-1]

print(palindrom(text))
print(text)
