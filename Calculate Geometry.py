import math
from math import sqrt
def menü():
    print('')
    print('# GEOMETRİK ŞEKİL ALAN, ÇEVRE VE HACİM HESAPLAYICI #')
    print('')
    print('# ALAN HESAPLAMA BÖLÜMÜ #')
    print('1. Üçgenin Alanını Hesapla')
    print('2. Dikdörtgenin Alanını Hesapla')
    print('3. Karenin Alanını Hesapla')
    print('4. Dairenin Alanını Hesapla')
    print('5. Beşgenin Alanını Hesapla')
    print('6. Altıgenin Alanını Hesapla')
    print('7. Yamuğun Alanını Hesapla')
    print('')
    print('# ÇEVRE HESAPLAMA BÖLÜMÜ #')
    print('8. Üçgenin Çevresini Hesapla')
    print('9. Karenin Çevresini Hesapla')
    print('10. Dikdörtgenin Çevresini Hesapla')
    print('11. Dairenin Çevresini Hesapla')
    print('12. Beşgenin Çevresini Hesapla')
    print('13. Altıgenin Çevresini Hesapla')
    print('14. Yamuğun Çevresini Hesapla')
    print('')
    print('# 3 BOYUTLU ŞEKİLLER BÖLÜMÜ #')
    print('15. Piramitin Alanını Hesapla')
    print('16. Piramitin Hacmini Hesapla')
    print('17. Küpün Alanını Hesapla')
    print('18. Küpün Hacmini Hesapla')
    print('19. Dikdörtgenler Prizmasının Alanını Hesapla')
    print('20. Dikdörtgenler Prizmasının Hacmini Hesapla')
    print('21. Kürenin Alanını Hesapla')
    print('22. Kürenin Hacmini Hesapla')
    print('')


menü()

programsonlanmasin = 1
while programsonlanmasin == 1:
    print('-> Programı Sonlandırmak İsterseniz 0 Yazın.')
    menü_seçimi = int(input('-> Hesaplayacağınız Geometrik Şeklin Menüdeki Numarasını Girin: '))



    if menü_seçimi < 0 or menü_seçimi > 22:
        print('-----------------------')
        print('Geçersiz Menü Seçimi!')
        print('-----------------------')



    if menü_seçimi == 0:
        print('')
        print('Program Sonlanıyor...')
        programsonlanmasin = 0

# TÜM ÜÇGENLERİN ALANINI BUL #
    if menü_seçimi == 1:

        a = int(input('Üçgenin 1.Kenarını Girin:'))
        b = int(input('Üçgenin 2.Kenarını Girin:'))
        c = int(input('Üçgenin 3.Kenarını Girin:'))

        if (a < 0 or b < 0 or c < 0 or a + b <= c or a + c <= b or b + c <= a):
            print('Bu Geçersiz Üçgendir!')



        s = (a + b + c) / 2
        alan = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print('--------------------------------------------------------------')
        print('Üçgende S yi Bulma Formülü s = (a + b + c) / 2 dir.')
        print('Üçgende Alan Bulma Formülü √(s x (s-a) x (s-b) x (s-c)) dir.')
        print('Üçgenin Alanı: %f' %alan)
        print('--------------------------------------------------------------')

# DİKDÖRTGENİN ALANINI BUL #

    elif menü_seçimi == 2:
        Uzun_Kenar = int(input('Uzun Kenarı Girin: '))
        Kısa_Kenar = int(input('Kısa Kenarı Girin: '))
        Dikdörtgen_Alanı = Uzun_Kenar * Kısa_Kenar
        print('------------------------')
        print('Dikdörtgenin Alan Formülü a x b dir.')
        print('Dikdörtgenin Alanı : ', Dikdörtgen_Alanı)
        print('------------------------')

# KARENİN ALANINI BUL #

    elif menü_seçimi == 3:
        Karenin_Kenarı = int(input('Karenin Kenarını Girin:'))
        Kare_Alanı = Karenin_Kenarı * Karenin_Kenarı
        print('------------------')
        print('Karenin Alan Formülü a x a dır.')
        print('Karenin Alanı:',Kare_Alanı)
        print('------------------')
# DAİRENİN ALANINI BUL #
    elif menü_seçimi == 4:
        daireyarıçap = int(input('Dairenin Yarıçapını Girin:'))
        try:
            Pi = float(input('Pi(π) yi 3 Almak İstiyorsanız Buraya 3 Yazın. Pi(π) nin Küsüratlı Değeri 3.14159 dur.'))
            Daire_Alanı = (daireyarıçap * daireyarıçap) * Pi # 3.14159 = Pi (π)
            print('---------------------------')
            print('Dairenin Alan Formülü π x r2 dir.')
            print('Dairenin Alanı: ', Daire_Alanı)
            print('---------------------------')
        except ValueError:
            print('')
            print('Pi(π) nin Küsüratını Nokta(.) İle Yazmalısınız!')
# BEŞGENİN ALANINI BUL #
    elif menü_seçimi == 5:
        beşgenyükseklik = int(input('Beşgenin Merkezinden Bir Kenarına İnen Dikmenin Yüksekliğini Girin:'))
        beşgenkenarı = int(input('Beşgenin Bir Kenarını Girin:'))
        Beşgen_Alanı = (beşgenkenarı * 5 * beşgenyükseklik) / 2
        print('---------------------------')
        print('Beşgenin Alan Formülü 5a x h / 2 dir.')
        print('Beşgenin Alanı: ', Beşgen_Alanı)
        print('---------------------------')
# ALTIGENİN ALANINI BUL #
    elif menü_seçimi == 6:
        W = 3
        altıgenkenarı = int(input('Altıgenin Bir Kenarını Girin:'))
        Altıgen_Alanı = (altıgenkenarı * altıgenkenarı * (3*sqrt(W)) / 2)
        print('----------------------------------------------')
        print('Altıgenin Alan Formülü a x a x 3√3 / 2 dir.')
        print('Altıgenin Alanı: ', Altıgen_Alanı)
        print('----------------------------------------------')
# YAMUĞUN ALANINI BUL #
    elif menü_seçimi == 7:
        yamugunüsttabanı = int(input('Yamugun Üst Tabanını Girin:'))
        yamugunalttabanı = int(input('Yamugun Alt Tabanını Girin:'))
        yamugunyüksekligi = int(input('Yamugun Yüksekliğini Girin:'))
        Yamuk_Alanı = (yamugunalttabanı + yamugunüsttabanı) * yamugunyüksekligi / 2
        print('--------------------------------------------------------------')
        print('Yamuğun Alan Formülü (alttaban + üsttaban) x yükseklik / 2 dir.')
        print('Yamuğun Alanı: ', Yamuk_Alanı)
        print('--------------------------------------------------------------')
# ÜÇGENİN ÇEVRESİNİ BUL #
    elif menü_seçimi == 8:
        a = int(input('Üçgenin 1.Kenarını Girin:'))
        b = int(input('Üçgenin 2.Kenarını Girin:'))
        c = int(input('Üçgenin 3.Kenarını Girin:'))
        Ucgen_Cevresi = a + b + c
        print('---------------------------')
        print('Üçgenin Çevresi 3 Kenarının Toplamıyla Bulunur.')
        print('Üçgenin Çevresi: ',Ucgen_Cevresi)
        print('---------------------------')
# KARENİN ÇEVRESİNİ BUL #
    elif menü_seçimi == 9:
        karekenari = int(input('Karenin Bir Kenarını Girin:'))
        Kare_Cevresi = karekenari * 4
        print('-------------------------')
        print('Karenin Çevresi Bir Kenarın 4 İle Çarpılmasıyla Bulunur.')
        print('Karenin Çevresi: ', Kare_Cevresi)
        print('-------------------------')
# DİKDÖRTGENİN ÇEVRESİNİ BUL #
    elif menü_seçimi == 10:
        dikdortgenkisakenar = int(input('Dikdortgenin Bir Kisa Kenarının Uzunluğunu Girin:'))
        dikdortgenuzunkenar = int(input('Dikdortgenin Bir Uzun Kenarının Uzunluğunu Girin:'))
        Dikdortgen_Cevresi = 2 * (dikdortgenuzunkenar+dikdortgenkisakenar)
        print('---------------------------')
        print('Dikdörtgenin Çevre Formülü 2 x a x b dir.')
        print('Dikdörtgenin Çevresi: ', Dikdortgen_Cevresi)
        print('---------------------------')
# DAİRENİN ÇEVRESİNİ BUL #
    elif menü_seçimi == 11:
        daireyaricapi = int(input('Dairenin Yarıçapını Girin:'))
        try:
            Pi = float(input('Pi(π) yi 3 Almak İstiyorsanız Buraya 3 Yazın. Pi(π) nin Küsüratlı Değeri 3.14159 dur.'))
            Daire_Cevresi = 2 * Pi * daireyaricapi # 3.14159 = Pi (π)
            print('--------------------------------------')
            print('Dairenin Çevresinin Formülü 2π x r dir.')
            print('Dairenin Çevresi: ', Daire_Cevresi)
            print('--------------------------------------')
        except ValueError:
            print('')
            print('Pi(π) nin Küsüratını Nokta(.) İle Yazmalısınız!')
# BEŞGENİN ÇEVRESİNİ BUL #
    elif menü_seçimi == 12:
        besgenkenari = int(input('Beşgenin Bir Kenarının Uzunluğunu Girin:'))
        Besgen_Cevresi = besgenkenari * 5
        print('------------------------')
        print('Beşgenin Çevresi Tüm Kenarlarının Toplamıyla Bulunur.')
        print('Beşgenin Çevresi:', Besgen_Cevresi)
        print('------------------------')
# ALTIGENİN ÇEVRESİNİ BUL #
    elif menü_seçimi == 13:
        altigenkenari = int(input('Altıgenin Bir Kenarının Uzunluğunu Girin:'))
        Altigen_Cevresi = altigenkenari * 5
        print('------------------------')
        print('Altıgenin Çevresi Tüm Kenarlarının Toplamıyla Bulunur.')
        print('Altıgenin Çevresi:', Altigen_Cevresi)
        print('------------------------')
# YAMUĞUN ÇEVRESİNİ BUL #
    elif menü_seçimi == 14:
        a = int(input('Yamuğun 1.Kenarını Girin:'))
        b = int(input('Yamuğun 2.Kenarını Girin:'))
        c = int(input('Yamuğun 3.Kenarını Girin:'))
        d = int(input('Yamuğun 4.Kenarını Girin:'))
        Yamuk_Cevresi = a+b+c+d
        print('-----------------------')
        print('Yamuğun Çevresinin Formülü a+b+c+d dir.')
        print('Yamuğun Çevresi:', Yamuk_Cevresi)
        print('-----------------------')
# PİRAMİTİN ALANINI BUL #
    elif menü_seçimi == 15:
        a = int(input('Piramitin Taban Uzunluğunu Girin:'))
        h = int(input('Piramitin Yüksekliğinin Uzunluğunu Girin:'))
        print('-----------------------------------')
        Piramit_Alan = a * (a+sqrt(a*a + 4*h*h))
        print('Piramitin Alanı:', Piramit_Alan)
        print('-----------------------------------')
# PİRAMİTİN HACMİNİ BUL #
    elif menü_seçimi == 16:
        a = int(input('Piramitin 1.Taban Uzunluğunu Girin:'))
        b = int(input('Piramitin 2.Taban Uzunluğunu Girin:'))
        h = int(input('Piramitin Yüksekliğinin Uzunluğunu Girin:'))
        Piramit_Hacim = 1 / 3 * a * b * h
        print('------------------------------------------------------')
        print('Piramitin Hacim Hesaplama Formülü 1/3 x a x b x h dir.')
        print('Piramitin Hacmi:', Piramit_Hacim)
        print('------------------------------------------------------')
# KÜPÜN ALANINI BUL #
    elif menü_seçimi == 17:
        a = int(input('Küpün Bir Kenarını Giriniz:'))
        Küp_Alan = 6 * a * a
        print('-----------------------------------')
        print('Küpün Alanı 6 x a x a dır.')
        print('Küpün Alanı: ', Küp_Alan)
        print('-----------------------------------')
# KÜPÜN HACMİNİ BUL #
    elif menü_seçimi == 18:
        a = int(input('Küpün Bir Kenarını Giriniz:'))
        Küp_Hacmi = a * a * a
        print('-----------------------------------')
        print('Küpün Hacmi a x a x a Olarak Hesaplanır.')
        print('Küpün Hacmi: ', Küp_Hacmi)
        print('-----------------------------------')
# DİKDÖRTGENLER PRİZMASININ ALANINI BUL #
    elif menü_seçimi == 19:
        kisakenar = int(input('Dikdörtgenler Prizmasının Kısa Kenarını Girin:'))
        uzunkenar = int(input('Dikdörtgenler Prizmasının Uzun Kenarını Girin:'))
        yukseklik = int(input('Dikdörtgenler Prizmasının Yüksekliğini Girin:'))
        DikdortgenlerPrizması_Alan = 2 * (kisakenar*uzunkenar + uzunkenar*yukseklik + kisakenar*yukseklik)
        print('----------------------------------------------------------------')
        print('Dikdörtgenler Prizması Alanı Formülü 2 x (ab + bc + ac) dir.')
        print('Dikdörtgenler Prizmasının Alanı: ', DikdortgenlerPrizması_Alan)
        print('----------------------------------------------------------------')
# DİKDÖRTGENLER PRİZMASININ HACMİNİ BUL #
    elif menü_seçimi == 20:
        kisakenar = int(input('Dikdörtgenler Prizmasının Kısa Kenarını Girin:'))
        uzunkenar = int(input('Dikdörtgenler Prizmasının Uzun Kenarını Girin:'))
        yukseklik = int(input('Dikdörtgenler Prizmasının Yüksekliğini Girin:'))
        DikdortgenlerPrizması_Hacim = kisakenar * uzunkenar * yukseklik
        print('----------------------------------------------------------------')
        print('Dikdörtgenler Prizması Hacim Formülü a x b x c dir.')
        print('Dikdörtgenler Prizmasının Hacmi: ', DikdortgenlerPrizması_Hacim)
        print('----------------------------------------------------------------')
# KÜRENİN ALANINI BUL #
    elif menü_seçimi == 21:
        r = int(input('Kürenin Yarıçapını Girin:'))
        try:
            Pi = float(input('Pi(π) yi 3 Almak İstiyorsanız Buraya 3 Yazın. Pi(π) nin Küsüratlı Değeri 3.14159 dur.'))
            Kure_Alan = 4 * Pi * r * r # 3.14159 = Pi (π)
            print('---------------------------------------------')
            print('Kürenin Alan Formülü 4 x π x r x r dir.')
            print('Kürenin Alanı: ', Kure_Alan)
            print('---------------------------------------------')
        except ValueError:
            print('')
            print('Pi(π) nin Küsüratını Nokta(.) İle Yazmalısınız!')
# KÜRENİN HACMİNİ BUL #
    elif menü_seçimi == 22:
        r = int(input('Kürenin Yarıçapını Girin:'))
        try:
            Pi = float(input('Pi(π) yi 3 Almak İstiyorsanız Buraya 3 Yazın. Pi(π) nin Küsüratlı Değeri 3.14159 dur.'))
            Kure_Hacmi = 4 / 3 * Pi * r * r * r  # 3.14159 = Pi (π)
            print('---------------------------------------------')
            print('Kürenin Hacim Formülü 4/3 x π x r x r x r dir. ')
            print('Kürenin Hacmi: ', Kure_Hacmi)
            print('---------------------------------------------')
        except ValueError:
            print('')
            print('Pi(π) nin Küsüratını Nokta(.) İle Yazmalısınız!')