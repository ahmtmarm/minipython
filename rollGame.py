import random

#Bu işlev, 1 ile 6 arasında rastgele bir sayı üretir ve
#bu sayıyı döndürür.
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)
    return roll

#Sonsuz bir döngü başlatılır ve oyuncu sayısını almak için kullanılır.
while True:
    players = input("Enter the number of players(1-4): ")
    if players.isdigit():
    #isdigit():Girilen değerin sayı olup olmadığını kontrol eder.
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        ("Invalid,try again")

max_score = 50
player_scores = [0 for _ in range(players)]
#Oyuncuların başlangıç skorlarını 0 değeri ile dolduruyor.

#Herhangi bir oyuncu maksimum skora ulaşıncaya kadar sürer.
#Her turda oyuncu zar atar ve puan kazanır
while max(player_scores) < max_score:
    
    #Oyuncuların sırayla zar atmalarını sağlar.
    for player_idx in range(players):
        print("\nPlayer number", player_idx + 1, "turn has just started!")
        print("Your total score is: ", player_scores[player_idx], "\n")
        current_score = 0
        #Oyuncun turunu temsil eden sonsuz bir döngü başlatır.
        #Oyuncu y girene kadar zar atmaya devam edebilir.
        while True:
            should_roll = input("Would you like to roll  (y)? ")
            if should_roll.lower() != "y":
                break
            #Bir zar atılır ve value değişkenine atanır.
            value = roll()
            #Eğer oyuncu 1 atarsaa oyunu kaybeder ve tur sona erer.
            #Oyuncunun puanı sıfırlanır ve döngüden çıkılır.
            if value == 1:
                print("You rolled a 1! Turn Done!")
                current_score = 0
                break
            #Eğer oyuncu 1 atmazsa,zarın değeri puana eklenir ve
            #oyuncunun puanı güncellenir.
            else:
                current_score += value
                print("You rolled a:", value)

            print("Your score is:", current_score)
        #Oyuncunun toplam skoru güncellenir.
        player_scores[player_idx] += current_score
        print("Your total score is:", player_scores[player_idx])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx + 1,
      "is the winner with a score of:", max_score)


