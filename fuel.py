while True: #Sonsuz bir döngü başlatılır.
    num = input("Fraction: ")
    index = num.find("/")#Kullanıcının girdiği kesirin içindeki kesir çizgisini
    #bulmak için 'find' işlemini kullanır ve sonucu index değişkenine atanır.
    try:
        x = int(num[:index])#Kesirin pay kısmını almak için num'un başından index'e kadar
        #olan kısmı tamsayıya('int') dönüştürerek x değişkenine atar.
        y = int(num[index+1:])#Kesirin pay kısmını tamsayıya dönüştürerek y değişkenine atar.
        fraction = x / y
        if x > y:
            continue
        break
    except (ValueError, ZeroDivisionError):#Bu hatalar sağlanırsa expect bloguna girilir
        #ve continue ile döngü başa döner.
        continue

percentage = int(fraction * 100)

if fraction > 0.9:
    print("F")
elif fraction < 0.1:
    print("E")
else:
    print(str(percentage) + "%")