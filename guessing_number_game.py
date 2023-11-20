import random

def guessing_game():
    print(f"Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100")

    tutulan_sayi=random.randint(1,100) # Burada 1-100 arasinda rastgele tahmin etmemiz gereken sayiyi aliyoruz.
    zorluk_derecesi= input("Choose a diffuculty. Type 'easy' or 'hard':") # Burada zorluk derecesini seciyoruz.
    print(f"Psst, the correct answer is {tutulan_sayi}")
    tahmin_hak_sayisi = 0
    eslesme = False
    if zorluk_derecesi == "easy":
        tahmin_hak_sayisi+=10
        print(f"You have {tahmin_hak_sayisi} attemps remaining to guess the number.")
    else:
        tahmin_hak_sayisi+=5
        print(f"You have {tahmin_hak_sayisi} attemps remaining to guess the number.")
    while tahmin_hak_sayisi !=0 and eslesme!=True:
        tahmin_edilen_sayi=int(input("Make a guess:"))
        if tahmin_edilen_sayi > tutulan_sayi:
            print("Too high.")
            tahmin_hak_sayisi-=1
            print(f"You have {tahmin_hak_sayisi} attemps to remaining to guess the number")
        elif tahmin_edilen_sayi < tutulan_sayi:
            print("Too low.")
            tahmin_hak_sayisi-=1
            print(f"You have {tahmin_hak_sayisi} attemps to remaining to guess the number")
        elif tahmin_edilen_sayi == tutulan_sayi:
            eslesme=True
    if eslesme==True:
        print(f"You got it! The answer was {tutulan_sayi}.")
    else:
        print(f"You've run out of guesses, you lose. Number is {tutulan_sayi}")

guessing_game()