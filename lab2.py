def sort(a):
    wordlist = a.split()
    wordlist.sort()
    return wordlist

while True:
    a = str(input ("enter a word: "))
    choice = int(input("1 - count char\n2 - Sort the sentence\n"))
    if(choice == 1):
        symbol = str(input("enter a symbol: "))
        print(a.count(symbol))
    elif(choice == 2):
        for word in sort(a):
            print(word)

