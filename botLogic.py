import random

# def --> definition --> tanımlama
def sifreOlusturucu(uzunluk):
    sifre = ""
    karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    for i in range(uzunluk):
        sifre += random.choice(karakterler)

    return sifre

def yaziTura():
    rastgeleSayi = random.randint(1, 2)

    if rastgeleSayi == 1:
        return("Yazı")
    elif rastgeleSayi == 2:
        return("Tura")
    
def emoji():
    emojiler = [
        ":smiley:", ":smile:", ":flag_tr:", ":face_with_monocle:", ":face_with_open_eyes_and_hand_over_mouth:",
        ":face_with_spiral_eyes:", ":factory:", ":fairy:", ":factory_worker:", ":falafel:", ":family:",
        ":flag_ps:", ":face_with_symbols_over_mouth:", ":family_mwg:",
        ":family_mwbb:", ":man:", ":woman:", ":older_adult:",
    ]

    emojimiz = random.choice(emojiler)

    return(emojimiz)

def komutCikar():
    komutlar =("Her komut dolar ile başlamak üzere;\n\n    merhaba\n    görüşürüz\n    şifre oluştur\n    yazı tura\n    emoji\n\nolmak üzere,\nbüyük-küçük harflerin yazılımına dikkat edin.")

    return(komutlar)

def temizle():
    temizleyici = "ㅤ\n"

    return(temizleyici*51)