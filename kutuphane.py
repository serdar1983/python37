import sqlite3
veritabanı = sqlite3.connect("kutuphane.sqlite")
imleç = veritabanı.cursor()
imleç.execute("CREATE TABLE IF NOT EXISTS Kitap(KitapAdi TEXT, YazarAdi TEXT, BasimYili INTEGER)")

def ekle():
    veritabanı = sqlite3.connect("kutuphane.sqlite")
    imleç = veritabanı.cursor()

    kitap_adı  =     input("Kitap Adı  : ")
    yazar_adı  =     input("Yazar Adı  : ")
    basım_yılı = int(input("Basım Yılı : "))

    kitaplar = []
    kitaplar.append((kitap_adı,yazar_adı,basım_yılı))

    for veri in kitaplar:
        imleç.execute("INSERT INTO Kitap VALUES (?,?,?)",veri)

    veritabanı.commit()
    veritabanı.close()
    print("Kayıt Eklendi !")
    print()
print()

def listele():
    veritabanı = sqlite3.connect("kutuphane.sqlite")
    imleç = veritabanı.cursor()

    satır = " Kitap Adı               Yazar Adı              Basım Yılı"
    #print(len(satır))
    print(satır)
    print()

    imleç.execute("SELECT * FROM Kitap")
    sonuç = imleç.fetchall()
    for s in sonuç:
        boşluk1 = 23 - len(s[0])
        boşluk2 = 23 - len(s[1])
        #boşluk3 = 23 - len(str(s[2]))

        print(" " + s[0] + boşluk1*" " + " " + s[1] + boşluk2*" "+ str(s[2]))

    veritabanı.close()
    print()
def exit():
    pass

# Ana Program
ana_menü = "[1] Tabloya Kayıt Ekleme\n" \
           "[2] Kayıtları Listeleme\n" \
           "[0] Çıkış"

print(ana_menü)
print()

while True:
    seçim = input("Seçiminiz --> ")
    print()

    if seçim == "1":
        ekle()

    elif seçim == "2":
        listele()

    elif seçim == "0":
        import time
        print("Program kapanıyor...")
        time.sleep(3)
        raise SystemExit
