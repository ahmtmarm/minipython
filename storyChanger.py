#story.txt adlı bir metin dosyasını okumak için bir with bloğu açılır.
#dosya f aldı bir değişkene atanır ve bu blok içinde otomatik olarak kapatılır.
with open("story.txt", "r") as f:
    #story adlı bir değişkene okunur ve atanır.
    story = f.read()

#Bu küme aynı kelimenin birden fazla kez eklenmesini engeller.
words = set()
#Kelimenin indeksini tutan bir değişken -1 olarak ayarlanır.
start_of_word = -1

#Kelimelerin başında ve sonunda o işaretlerin olup olmadığını anlamak için atandı.
target_start = "<"
target_end = ">"
#Hikayeyi döngüye alır ve her karakteri 'i' indeksi ile birlikte işler.
for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1

answers = {}

for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer

for word in words:
    #Hikaye içindeki özel kelimeler,
    # kullanıcı tarafından verilen yeni kelimelerle değiştirilir.
    story = story.replace(word, answers[word])

print(story)