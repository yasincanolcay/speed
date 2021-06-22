#wordlist oluşturucu denemesi

import random
import time
from time import sleep

banner = """ 
                                         █████
                                        ░░███ 
  █████  ████████   ██████   ██████   ███████ 
 ███░░  ░░███░░███ ███░░███ ███░░███ ███░░███ 
░░█████  ░███ ░███░███████ ░███████ ░███ ░███ 
 ░░░░███ ░███ ░███░███░░░  ░███░░░  ░███ ░███ 
 ██████  ░███████ ░░██████ ░░██████ ░░████████
░░░░░░   ░███░░░   ░░░░░░   ░░░░░░   ░░░░░░░░ 
         ░███                                 
         █████                        
        ░░░░░                                 
"""
print(banner)
print("[SPEED WORDLİST CREATER]")
print("    [OlcaySoftware]")
print("------------------------------------------------------------------")
print(">>YOUTUBE: https://www.youtube.com/channel/UCJ8uEcZIP_sSKhZJ2NTjflg")
print(">>INSTAGRAM: https://www.instagram.com/olcaysoftware/")
print(">>FACEBOOK: https://tr-tr.facebook.com/olcaysoftware")
print(">>TWITTER: https://twitter.com/OlcayYasincan")

print("------------------------------------------------------------------")

while True:


    isim = input(">>[+]FİRSNAME (compulsory): ")
    soyisim = input(">>[+]SURNAME (compulsory): ")
    dogum_gunu = input(">>[*]BİRTHDAY (optional): ")
    partner = input(">>[*]PARTNER (optional): ")
    cocuklar = input(">>[*]CHİLDRENS (optional): ")
    kelime = input(">>[*]WORD  (optional): ")
    print("--------------------------------------------")
    wordlist_name = input(">>[+]WORDLİST NAME (compulsory): ")
    wordlist = wordlist_name+".txt"
    Alfabe = "abcçdefgğhiıjklmnoöprsştuüvyz"
    Buyuk_harf = "ABCÇDEFGĞHİIJKLMNOÖPRSŞTUÜVYZ"
    char = "@!#$%&^+?*.£"


    if isim == "" or soyisim == "":
        print("    warning>>[! isim ve soyisim boş bırakılamaz !]<<")
        print("    warning>>[! first and last name cannot be left blank !]<<")
        print("    warning>>[! Vor- und Nachname dürfen nicht leer bleiben !]<<")
        sleep(1)
        continue

    else:
    
        ilk1 = isim+dogum_gunu
        print(ilk1)


        ilk2 = isim+soyisim+dogum_gunu
        print(ilk2)


        ilk3 = isim+dogum_gunu+soyisim
        print(ilk3)


        ilk4 = soyisim+isim+dogum_gunu
        print(ilk4)


        ilk5 = soyisim+dogum_gunu+isim
        print(ilk5)


        ilk6 = isim+partner
        print(ilk6)

        ilk7 = isim+cocuklar
        print(ilk7)

        
        ilk8 = cocuklar + isim
        print(ilk8)

        dosya = open(wordlist,"a")
        yazdir = dosya.write(ilk1+"\n"+ilk2+"\n"+ilk3+"\n"+ilk4+"\n"+ilk5+ "\n" + ilk6 +"\n" + ilk7 + "\n" + ilk8 + "\n")
        dosya.close()



        print(">>>SPEED>> PLEASE WAİT , PASSWORD LİST CREATİNG...")
        sleep(1)
        print("[==============speed]%50")
        sleep(1)
        print("[===========================speed ;-)]%100")
        sleep(1)



        for i in Alfabe:
            for k in char:
                yaz = isim+i+k+"\n"
                print(yaz)

                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz)
                dosya.close()


        for c in Alfabe:
            for c1 in char:
                yaz = isim+cocuklar+c+c1+"\n"
                print(yaz)

                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz)
                dosya.close()

        for i1 in Alfabe:
            for k in char:
                yaz = isim+i1+k+kelime+"\n"
                print(yaz)

                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz)
                dosya.close()

        for c2 in Alfabe:
            for c3 in char:
                yaz = isim+c2+c3+cocuklar+"\n"
                print(yaz)
                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz)
                dosya.close()

        for c4 in Alfabe:
            for c5 in char:
                yaz = cocuklar+c4+c5+isim+"\n"
                print(yaz)
                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz)
                dosya.close()


        for i2 in Alfabe:
            for k in char:
                yaz = isim+i2+kelime+k+"\n"
                print(yaz)

                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz) 
                dosya.close()


        for chld in Alfabe:
            for chlds in char:
                yaz = isim+chld+kelime+chlds+cocuklar+"\n"
                print(yaz)

                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz) 
                dosya.close()

        for chld1 in Alfabe:
            for chlds1 in char:
                yaz = partner+chld1+kelime+chlds1+cocuklar+"\n"
                print(yaz)

                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz) 
                dosya.close()


        for chld2 in Alfabe:
            for chlds2 in char:
                yaz = cocuklar+chld2+kelime+chlds2+cocuklar+"\n"
                print(yaz)

                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz) 
                dosya.close()


        for chld3 in Alfabe:
            for chlds3 in char:
                yaz = partner+chlds3+kelime+chld3+cocuklar+"\n"
                print(yaz)

                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz) 
                dosya.close()





        for i3 in Alfabe:
            for k in char:
                yaz = isim+i3+k+soyisim+"\n"
                print(yaz)

                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz)
                dosya.close()

        for chld4 in Alfabe:
            for chlds4 in char:
                yaz = kelime+chld4+chlds4+cocuklar+"\n"
                print(yaz)
                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz)
                dosya.close()

        for i4 in Alfabe:
            for k in char:
                yaz = isim+soyisim+i4+k+"\n"  
                print(yaz)

                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz)
                dosya.close()


        for chld4 in Alfabe:
            for chlds4 in char:
                yaz = isim+cocuklar+soyisim+chld4+chlds4+"\n"  
                print(yaz)

                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz)
                dosya.close()


        for i5 in Alfabe:
            for k1 in char:
                yaz = soyisim+isim+i5+k1+"\n"
                print(yaz)

                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz)
                dosya.close()

        for i6 in Alfabe:
            for k2 in char:
                yaz = k2+isim+i6+"\n"
                print(yaz)

                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz)
                dosya.close()

        for i7 in Alfabe:
            for k3 in char:
                yaz = k3+isim+i7+soyisim+"\n"
                print(yaz)

                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz)
                dosya.close()


        for i8 in Alfabe:
            for k4 in char:
                yaz = k4+isim+soyisim+i8+"\n"
                print(yaz)

                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz)
                dosya.close()


        for i9 in Alfabe:
            for k5 in char:
                yaz = soyisim+k5+isim+i9+"\n"
                print(yaz)

                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz)
                dosya.close()

        for iz1 in Alfabe:
            for k6 in char:
                yaz = iz1+k6+isim+"\n"
                print(yaz)


                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz)
                dosya.close()

        for iz2 in Alfabe:
            for k7 in char:
                yaz = iz2+k7+isim+soyisim+"\n"
                print(yaz)


                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz)
                dosya.close()


        for b in Buyuk_harf:
            for k8 in char:
                yaz = isim+b+k8+"\n"
                print(yaz)

                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz)
                dosya.close()


        for b1 in Buyuk_harf:
            for k9 in char:
                yaz = isim+b1+k9+soyisim+"\n"
                print(yaz)

                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz)
                dosya.close()



        for b2 in Buyuk_harf:
            for kz1 in char:
                yaz = isim+b2+soyisim+kz1+"\n"
                print(yaz)

                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz)
                dosya.close()


        for b3 in Buyuk_harf:
            for kz2 in char:
                yaz = isim+soyisim+b3+kz2+"\n"
                print(yaz)

                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz)
                dosya.close()



        for b4 in Buyuk_harf:
            for kz3 in char:
                yaz = soyisim+isim+b4+kz3+"\n"
                print(yaz)

                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz)
                dosya.close()

        for b5 in Buyuk_harf:
            for kz4 in char:
                yaz = kz4+isim+b5+"\n"
                print(yaz)


                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz)
                dosya.close()


        for b6 in Buyuk_harf:
            for kz5 in char:
                yaz = kz5+isim+b6+dogum_gunu+"\n"
                print(yaz)

                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz)
                dosya.close()


        for b7 in Buyuk_harf:
            for kz6 in char:
                yaz = kz6+isim+dogum_gunu+b7+"\n"
                print(yaz)

                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz)
                dosya.close()

        for b8 in Buyuk_harf:
            for kz7 in char:
                yaz = kz7+dogum_gunu+isim+b8+"\n"
                print(yaz)

                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz)
                dosya.close()


        for b9 in Buyuk_harf:
            for kz8 in char:
                yaz = dogum_gunu+kz8+isim+b9+"\n"
                print(yaz)

                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz)
                dosya.close()


        for e in Buyuk_harf:
            for kz9 in char:
                yaz = e+kz9+isim+"\n"
                print(yaz)

                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz)
                dosya.close()


        for e1 in Buyuk_harf:
            for z1 in char:
                yaz = isim+e1+z1+isim+"\n"
                print(yaz)

                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz)
                dosya.close()


        for e2 in Buyuk_harf:
            for z2 in char:
                yaz = e+isim+z2+isim+"\n"
                print(yaz)

                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz)
                dosya.close()

        for e3 in Buyuk_harf:
            for z3 in char:
                yaz = isim+dogum_gunu+e3+z3+isim+"\n"
                print(yaz)

                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz)
                dosya.close()
    

        for yil in Alfabe:

            yaz = isim + dogum_gunu + yil+"\n"
            print(yaz)

            dosya = open(wordlist,"a")
            yazdir = dosya.write(yaz)
            dosya.close()

        for yil1 in Alfabe:

            yaz = isim + dogum_gunu + yil1 + soyisim+"\n"
            print(yaz)
            dosya = open(wordlist,"a")
            yazdir = dosya.write(yaz)
            dosya.close()


        for yil2 in Alfabe:

            yaz = isim + soyisim + dogum_gunu + yil2 +"\n"
            print(yaz)
            dosya = open(wordlist,"a")
            yazdir = dosya.write(yaz)
            dosya.close()


        for yil3 in Alfabe:

            yaz = soyisim + isim + dogum_gunu + yil3 +"\n"
            print(yaz)
            dosya = open(wordlist,"a")
            yazdir = dosya.write(yaz)
            dosya.close()
    
    
    

        for yil4 in Alfabe:

            yaz = isim + yil4 + dogum_gunu+"\n"
            print(yaz)
            dosya = open(wordlist,"a")
            yazdir = dosya.write(yaz)
            dosya.close()

        for yil5 in Alfabe:

            yaz =  dogum_gunu+ yil5 + isim +"\n"
            print(yaz)
            dosya = open(wordlist,"a")
            yazdir = dosya.write(yaz)
            dosya.close()

        for yil6 in Alfabe:

            yaz =  dogum_gunu+ yil6 + isim + soyisim+"\n"
            print(yaz)
            dosya = open(wordlist,"a")
            yazdir = dosya.write(yaz)
            dosya.close()
    

        for yil7 in Alfabe:

            yaz =  dogum_gunu+ yil7 + isim + soyisim+ partner +"\n"
            print(yaz)
            dosya = open(wordlist,"a")
            yazdir = dosya.write(yaz)
            dosya.close()
    
    
        for yil8 in Alfabe:

            yaz =  dogum_gunu+ yil8 + isim + partner +soyisim+"\n"
            print(yaz)
            dosya = open(wordlist,"a")
            yazdir = dosya.write(yaz)
            dosya.close()
    

        for yil9 in Alfabe:

            yaz =  dogum_gunu+ yil9 + partner +isim + soyisim+"\n"
            print(yaz)
            dosya = open(wordlist,"a")
            yazdir = dosya.write(yaz)
            dosya.close()
    
        for yilz1 in Alfabe:

            yaz =  dogum_gunu+ partner +yilz1 + isim + soyisim+ partner +"\n"
            print(yaz)
            dosya = open(wordlist,"a")
            yazdir = dosya.write(yaz)
            dosya.close()
    

        for yilz2 in Alfabe:

            yaz = partner + dogum_gunu+ yilz2 + isim + soyisim+ partner +"\n"
            print(yaz)
            dosya = open(wordlist,"a")
            yazdir = dosya.write(yaz)
            dosya.close()
    


        for yilz3 in Alfabe:

            yaz = partner + dogum_gunu+ yilz3 + isim + soyisim+ kelime +"\n"
            print(yaz)
            dosya = open(wordlist,"a")
            yazdir = dosya.write(yaz)
            dosya.close()
    

        for yilz4 in Alfabe:

            yaz = partner + dogum_gunu+ yilz4 + isim + kelime + soyisim+"\n"
            print(yaz)
            dosya = open(wordlist,"a")
            yazdir = dosya.write(yaz)
            dosya.close()

        for yilz5 in Alfabe:

            yaz = partner + dogum_gunu+ yilz5 + kelime + isim + soyisim+"\n"
            print(yaz)
            dosya = open(wordlist,"a")
            yazdir = dosya.write(yaz)
            dosya.close()
    
        for yilz6 in Alfabe:

            yaz = partner + dogum_gunu+ kelime + yilz6 + isim + soyisim+"\n"
            print(yaz)
            dosya = open(wordlist,"a")
            yazdir = dosya.write(yaz)
            dosya.close()
    
        for yilz7 in Alfabe:

            yaz = partner + kelime + dogum_gunu+ yilz7 + isim + soyisim+"\n"
            print(yaz)
            dosya = open(wordlist,"a")
            yazdir = dosya.write(yaz)
            dosya.close()

        for yilz8 in Alfabe:

            yaz = kelime + partner + dogum_gunu+yilz8 + isim + soyisim+"\n"
            print(yaz)
            dosya = open(wordlist,"a")
            yazdir = dosya.write(yaz)
            dosya.close()
    

        for isimAlfabe in Alfabe:

            yaz = isim + isimAlfabe + "\n"
            print(yaz)
            dosya = open(wordlist,"a")
            yazdir = dosya.write(yaz)
            dosya.close()

        for Alfabeisim in Alfabe:

            yaz = Alfabeisim + isim + "\n"
            print(yaz)
            dosya = open(wordlist,"a")
            yazdir = dosya.write(yaz)
            dosya.close()


        for buyuk in Buyuk_harf:

            yaz = isim + buyuk + "\n"
            print(yaz)
            dosya = open(wordlist,"a")
            yazdir = dosya.write(yaz)
            dosya.close()


        for buyuk2 in Buyuk_harf:

            yaz = buyuk2 + isim + "\n"
            print(yaz)
            dosya = open(wordlist,"a")
            yazdir = dosya.write(yaz)
            dosya.close()

        sayi = range(1,2030)

        for sayilar in sayi:

            yaz = isim + str(sayilar) + "\n"
            print(yaz)
            dosya = open(wordlist,"a")
            yazdir = dosya.write(yaz)
            dosya.close()

        for sayilar2 in sayi:

            yaz = isim + soyisim + str(sayilar2) + "\n"
            print(yaz)
            dosya = open(wordlist,"a")
            yazdir = dosya.write(yaz)
            dosya.close()

        for sayilar3 in sayi:

            for karakter in char:

                yaz = isim + soyisim + karakter + str(sayilar3) + "\n"
                print(yaz)
                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz)
                dosya.close()



        for sayilar4 in sayi:

            for karakter2 in char:

                yaz = isim + karakter2 +soyisim + str(sayilar4) + "\n"
                print(yaz)
                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz)
                dosya.close()


        for sayilar5 in sayi:

            for karakter3 in char:

                yaz = partner + karakter3 + str(sayilar5) + "\n"
                print(yaz)
                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz)
                dosya.close()


        for sayilar6 in sayi:

            for karakter4 in char:

                yaz = kelime + karakter4 + str(sayilar6) + "\n"
                print(yaz)
                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz)
                dosya.close()


        for sayilar7 in sayi:

            for karakter5 in char:

                yaz = cocuklar + karakter5 + str(sayilar7) + "\n"
                print(yaz)
                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz)
                dosya.close()


        for children in char:

            yaz = cocuklar + children + "\n"
            print(yaz)
            dosya = open(wordlist,"a")
            yazdir = dosya.write(yaz)
            dosya.close()

        for children2 in char:

            yaz = children2 + cocuklar + "\n"
            print(yaz)
            dosya = open(wordlist,"a")
            yazdir = dosya.write(yaz)
            dosya.close()


        for children3 in Alfabe:

            yaz = children3 + cocuklar + "\n"
            print(yaz)
            dosya = open(wordlist,"a")
            yazdir = dosya.write(yaz)
            dosya.close()


        for children4 in Alfabe:

            yaz = cocuklar + children4 + "\n"
            print(yaz)
            dosya = open(wordlist,"a")
            yazdir = dosya.write(yaz)
            dosya.close()

        for children5 in char:
            for children6 in Alfabe:

                yaz = cocuklar + children5 + children6 + "\n"
                print(yaz)
                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz)
                dosya.close()

        for children7 in char:
            for children8 in Alfabe:

                yaz = cocuklar + children8 + children7 + "\n"
                print(yaz)
                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz)
                dosya.close()



        for children9 in char:
            for childrenz1 in Alfabe:

                yaz = children9 + cocuklar + childrenz1 + "\n"
                print(yaz)
                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz)
                dosya.close()



        for childrenz2 in char:
            for childrenz3 in Alfabe:

                yaz = childrenz3 + cocuklar + childrenz2 + "\n"
                print(yaz)
                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz)
                dosya.close()


        for childrenz4 in char:
            for childrenz5 in Alfabe:

                yaz = childrenz4 + childrenz5 + cocuklar + "\n"
                print(yaz)
                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz)
                dosya.close()



        for childrenz6 in char:
            for childrenz7 in Alfabe:

                yaz = childrenz7 + childrenz6 + cocuklar + "\n"
                print(yaz)
                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz)
                dosya.close()


        for childBuyuk in Buyuk_harf:

            yaz = childBuyuk + cocuklar + "\n"
            print(yaz)
            dosya = open(wordlist,"a")
            yazdir = dosya.write(yaz)
            dosya.close()


        for childBuyuk2 in Buyuk_harf:

            for childChar in char:

                yaz = childBuyuk2 + cocuklar + childChar + "\n"
                print(yaz)
                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz)
                dosya.close()


        for childBuyuk3 in Buyuk_harf:

            for childChar2 in char:

                yaz = childChar2  + cocuklar + childBuyuk3 + "\n"
                print(yaz)
                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz)
                dosya.close()



        for childSayi in sayi:

            yaz = cocuklar + str(childSayi) + "\n"
            print(yaz)
            dosya = open(wordlist,"a")
            yazdir = dosya.write(yaz)
            dosya.close()

        for childSayi2 in sayi:

            yaz = str(childSayi2) + cocuklar + "\n"
            print(yaz)
            dosya = open(wordlist,"a")
            yazdir = dosya.write(yaz)
            dosya.close()


        for kelimeSayi in sayi:

            yaz = kelime + str(kelimeSayi) + "\n"
            print(yaz)
            dosya = open(wordlist,"a")
            yazdir = dosya.write(yaz)
            dosya.close()

        for kelimeSayi2 in sayi:
            for kelimeChar in char:

                yaz = kelime + str(kelimeSayi2) + kelimeChar + "\n"
                print(yaz)
                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz)
                dosya.close()


        for kelimeSayi3 in sayi:
            for kelimeChar1 in char:

                yaz = kelime + kelimeChar1 + str(kelimeSayi3) + "\n"
                print(yaz)
                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz)
                dosya.close()


        for kelimeSayi4 in sayi:
            for kelimeChar2 in char:

                yaz = kelimeChar2 + kelime + str(kelimeSayi4) + "\n"
                print(yaz)
                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz)
                dosya.close()

        for kelimeSayi5 in sayi:
            for kelimeChar3 in char:

                yaz = str(kelimeSayi5)  + kelime + kelimeChar3 + "\n"
                print(yaz)
                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz)
                dosya.close()


        for extra in sayi:
            for extraAlp in Alfabe:

                yaz = str(extra) + extraAlp + "\n"
                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz)
                dosya.close()


        for extra2 in sayi:
            for extraAlp2 in Alfabe:

                yaz = extraAlp2 + str(extra2) + "\n"
                dosya = open(wordlist,"a")
                yazdir = dosya.write(yaz)
                dosya.close()
        break


