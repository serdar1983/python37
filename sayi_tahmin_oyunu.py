import random
import time
sayaç = 5

sayı = random.randint(1, 100)
print(" ---------SAYI TAHMİN OYUNU----------", "\n", "----------------------------------")
print(" Oyundan çıkmak için 0 ")
print(" 6 tahmin hakkınız var!")
print(" ************************")

while True:
    try:
        print(" -------------------------------------------")
        tahmin = int(input(" Tutulan sayıyı tahmin edin (1-100) --> "))

        if tahmin == 0:
            print(" oyun kapanıyor...")
            time.sleep(5)
            break

        elif tahmin == sayı:
            print(" BRAVO... Bildiniz!")
            print(" oyun kapanıyor...")
            time.sleep(5)
            break

        elif tahmin < sayı:
            if sayaç == 0:
                print(" üzgünüm oyun kapanıyor...")
                print(" Tutulan sayı -->", sayı, "bilemediniz!")
                time.sleep(5)
                break
            print(" Kalan tahmin-->", sayaç, "---YUKARI !!!")
            sayaç = sayaç - 1


        elif tahmin > sayı:
            if sayaç == 0:
                print(" üzgünüm oyun kapanıyor...")
                print(" Tutulan sayı -->", sayı, "bilemediniz!")
                time.sleep(5)
                break
            print(" Kalan tahmin-->", sayaç ,"---AŞAĞI !!!")
            sayaç = sayaç - 1


    except ValueError:
        print(" Lütfen tamsayı girin!")
