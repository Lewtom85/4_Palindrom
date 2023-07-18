#Palindrom

text = ("Kobyla, ma maly bok.")

def palindrom(text):
    x = text.lower() #zmieniam litery na male w tekscie
    x = x.replace(" ", "") #usuwam spacje w tekscie
    x = x.replace(",", "") #usuwam przecinki i ponizej kropki
    x = x.replace(".", "")
    print(x)
    return x == x[::-1]

print(palindrom(text))
print(text)
