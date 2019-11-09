alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghjklmnopqrstuvwxyzabcdefghjklmnopqrstuvwxyz01234567890123456789АБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯабвгдеєжзиіїклмнопрстуфхцчшщьюя"
step =1
text = input("Please write your text ").strip()
res = ''
for c in text:
    res += alphabet[(alphabet.index(c) + step)%len(alphabet)]
print("Result: " + res + "")

