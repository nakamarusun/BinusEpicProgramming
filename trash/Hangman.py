def Hangman():
    word = input("Welcome to Hangman ! input your word: ")

    newWord = ""
    for i in word:
        newWord = newWord + "_ "
    
    attempts = 5
    while attempts > 0:

        print("Guess the word !")
        print(newWord)
        print("Attempts left: ", attempts)
        alph = input("Try alphabet: ")
        for i in range(len(word)):
            if word[i] == alph:
                newWord = list(newWord)         #rubah jadi list
                newWord[i*2] = alph
                newWord = ''.join(newWord)      #balikin jadi string

Hangman()