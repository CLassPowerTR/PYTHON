import threading
from tkinter import messagebox
from python_imagesearch.imagesearch import imagesearch
import pyautogui
import keyboard
import time
from tkinter import *
import tkinter as tk
from tkinter import ttk
import random
global stop
global secilenMetin

pencere = tk.Tk()
pencere.geometry("360x360")
pencere.title("Metin Botu")
version = tk.Label(pencere, text="METİN_BOTU_Version v0.1.6")
version.place(x=210, y=340)

def OtoAv():
    try:
        if z.get() == 1:
            bilgi = tk.Label(pencere, text="Oto Av Başladı")
            bilgi.place(x=100, y=100)
            a = int(t2.get())
            x_koor = int(t.get())
            y_koor = int(t1.get())
            time.sleep(a)

            while z.get() == 1:
                ################ BOT KONTROL İÇİ ##################
                metin7 = imagesearch("Uriel.PNG")
                if metin7[0] != -1:
                    metin7_x = metin7[0]
                    metin7_y = metin7[1]
                    metin7_x = metin7_x + 5
                    metin7_y = metin7_y + 5
                    pyautogui.moveTo(metin7_x, metin7_y, 0.2)
                    pyautogui.leftClick(metin7_x, metin7_y)
                    time.sleep(1)

                metin7 = imagesearch("Uriel1.PNG")
                if metin7[0] != -1:
                    metin7_x = metin7[0]
                    metin7_y = metin7[1]
                    metin7_x = metin7_x + 5
                    metin7_y = metin7_y + 5
                    pyautogui.moveTo(metin7_x, metin7_y, 0.2)
                    pyautogui.leftClick(metin7_x, metin7_y)
                    time.sleep(1)

                metin7 = imagesearch("Uriel2.PNG")
                if metin7[0] != -1:
                    metin7_x = metin7[0]
                    metin7_y = metin7[1]
                    metin7_x = metin7_x + 5
                    metin7_y = metin7_y + 5
                    pyautogui.moveTo(metin7_x, metin7_y, 0.2)
                    pyautogui.leftClick(metin7_x, metin7_y)
                    time.sleep(1)

                metin7 = imagesearch("Uriel3.PNG")
                if metin7[0] != -1:
                    metin7_x = metin7[0]
                    metin7_y = metin7[1]
                    metin7_x = metin7_x + 5
                    metin7_y = metin7_y + 5
                    pyautogui.moveTo(metin7_x, metin7_y, 0.2)
                    pyautogui.leftClick(metin7_x, metin7_y)
                    time.sleep(1)

                metin7 = imagesearch("Uriel4.PNG")
                if metin7[0] != -1:
                    metin7_x = metin7[0]
                    metin7_y = metin7[1]
                    metin7_x = metin7_x + 5
                    metin7_y = metin7_y + 5
                    pyautogui.moveTo(metin7_x, metin7_y, 0.2)
                    pyautogui.leftClick(metin7_x, metin7_y)
                    time.sleep(1)

                metin7 = imagesearch("Uriel5.PNG")
                if metin7[0] != -1:
                    metin7_x = metin7[0]
                    metin7_y = metin7[1]
                    metin7_x = metin7_x + 200
                    metin7_y = metin7_y + 120
                    pyautogui.moveTo(metin7_x, metin7_y, 0.2)
                    pyautogui.leftClick(metin7_x, metin7_y)
                    time.sleep(1)
                    continue
                    ################ SON ##################

                ################ 1.METİNi KESMEK İÇİN ##################
                metin5 = imagesearch(secilenMetin)
                if metin5[0] != -1:
                    metin5_x = metin5[0]
                    metin5_y = metin5[1]
                    metin5_x = metin5_x + x_koor
                    metin5_y = metin5_y + y_koor
                    print("1. Metin Bulundu")
                    print(metin5)
                    if metin5_y > 450 and metin5_x > 825:
                        if metin5_y > 720:
                            pyautogui.moveTo(metin5_x - 10, 720)
                            time.sleep(0.1)
                            pyautogui.click()
                            time.sleep(a)
                        else:
                            pyautogui.moveTo(metin5_x - 10, metin5_y)
                            time.sleep(0.1)
                            pyautogui.click()
                            time.sleep(a)

                    elif metin5_y > 450 and metin5_x < 400:
                        if metin5_y > 720:
                            pyautogui.moveTo(metin5_x + 10, 720)
                            time.sleep(0.1)
                            pyautogui.click()
                            time.sleep(a)
                        else:
                            pyautogui.moveTo(metin5_x + 10, metin5_y + 10)
                            time.sleep(0.1)
                            pyautogui.click()
                            time.sleep(a)

                    elif metin5_y < 300 and metin5_x > 825:
                        pyautogui.moveTo(metin5_x - 10, metin5_y - 10)
                        time.sleep(0.1)
                        pyautogui.click()
                        time.sleep(a)

                    elif metin5_y < 300 and metin5_x < 400:
                        pyautogui.moveTo(metin5_x + 10, metin5_y - 10)
                        time.sleep(0.1)
                        pyautogui.click()
                        time.sleep(a)

                    elif metin5_y > 720:
                        pyautogui.moveTo(metin5_x, 720)
                        time.sleep(0.1)
                        pyautogui.click()
                        time.sleep(a)

                    elif metin5_x > 1050:
                        pyautogui.moveTo(metin5_x - 10, metin5_y)
                        time.sleep(0.1)
                        pyautogui.click()
                        time.sleep(a)

                    elif metin5_x < 400:
                        pyautogui.moveTo(metin5_x + 10, metin5_y)
                        time.sleep(0.1)
                        pyautogui.click()
                        time.sleep(a)

                    elif metin5_y < 300:
                        pyautogui.moveTo(metin5_x, metin5_y - 10)
                        time.sleep(0.1)
                        pyautogui.click()
                        time.sleep(a)

                    elif metin5_y > 520:
                        pyautogui.moveTo(metin5_x, metin5_y + 10)
                        time.sleep(0.1)
                        pyautogui.click()
                        time.sleep(a)

                    else:
                        pyautogui.moveTo(metin5_x, metin5_y)
                        time.sleep(0.1)
                        pyautogui.click()
                        time.sleep(a)

                ################ 1. METİN KONTROL İÇİN ##################
                metin1 = imagesearch(secilenMetin)
                ################ METİN AYNI YERDE Mİ? ##################
                # Eğer metin bulunmaz ise random tıkla
                if metin1[0] == -1 and metin5[0] == -1:
                    x = random.randrange(450, 1000)
                    y = random.randrange(370, 500)
                    pyautogui.moveTo(x, y)
                    time.sleep(0.2)
                    pyautogui.click()
                    continue

                if metin1 == metin5:
                    keyboard.press("3")
                    time.sleep(0.1)
                    keyboard.release("3")
                    time.sleep(0.1)
                    x = random.randrange(350, 1200)
                    y = random.randrange(270, 600)
                    pyautogui.moveTo(x, y)
                    time.sleep(0.2)
                    pyautogui.click()
                    time.sleep(0.2)
                    pyautogui.click()
                    time.sleep(0.2)
                    pyautogui.click()
                    time.sleep(0.2)
                    pyautogui.click()
                    time.sleep(0.2)
                    pyautogui.click()
                    time.sleep(0.2)
                    pyautogui.click()
                    time.sleep(0.2)
                    pyautogui.click()
                    print("1. ve 2. Metin Aynı Yerde")
                    # time.sleep(0.5)

                if metin1 != metin5:
                    metin1_x = metin1[0]
                    metin1_y = metin1[1]
                    metin1_x = metin1_x + x_koor
                    metin1_y = metin1_y + y_koor
                    print("2. Metin Bulundu")
                    print(metin1)
                    if metin1_y > 450 and metin1_x > 825:
                        if metin1_y > 720:
                            pyautogui.moveTo(metin1_x - 10, 720)
                            time.sleep(0.1)
                            pyautogui.click()
                            time.sleep(a)
                        else:
                            pyautogui.moveTo(metin1_x - 10, metin1_y)
                            time.sleep(0.1)
                            pyautogui.click()
                            time.sleep(a)

                    elif metin1_y > 450 and metin1_x < 400:
                        if metin1_y > 720:
                            pyautogui.moveTo(metin1_x + 10, 720)
                            time.sleep(0.1)
                            pyautogui.click()
                            time.sleep(a)
                        else:
                            pyautogui.moveTo(metin1_x + 10, metin1_y + 10)
                            time.sleep(0.1)
                            pyautogui.click()
                            time.sleep(a)

                    elif metin1_y < 300 and metin1_x > 825:
                        pyautogui.moveTo(metin1_x - 10, metin1_y - 10)
                        time.sleep(0.1)
                        pyautogui.click()
                        time.sleep(a)

                    elif metin1_y < 300 and metin1_x < 400:
                        pyautogui.moveTo(metin1_x + 10, metin1_y - 10)
                        time.sleep(0.1)
                        pyautogui.click()
                        time.sleep(a)

                    elif metin1_y > 720:
                        pyautogui.moveTo(metin1_x, 720)
                        time.sleep(0.1)
                        pyautogui.click()
                        time.sleep(a)

                    elif metin1_x > 1050:
                        pyautogui.moveTo(metin1_x - 10, metin1_y)
                        time.sleep(0.1)
                        pyautogui.click()
                        time.sleep(a)

                    elif metin1_x < 400:
                        pyautogui.moveTo(metin1_x + 10, metin1_y)
                        time.sleep(0.1)
                        pyautogui.click()
                        time.sleep(a)

                    elif metin1_y < 300:
                        pyautogui.moveTo(metin1_x, metin1_y - 10)
                        time.sleep(0.1)
                        pyautogui.click()
                        time.sleep(a)

                    elif metin1_y > 520:
                        pyautogui.moveTo(metin1_x, metin1_y + 10)
                        time.sleep(0.1)
                        pyautogui.click()
                        time.sleep(a)

                    else:
                        pyautogui.moveTo(metin1_x, metin1_y)
                        time.sleep(0.1)
                        pyautogui.click()
                        time.sleep(a)

                if metin7[0] == -1 and metin5[0] == -1 and metin1[0] == -1:
                    ################ SUNUCUYA BAĞLANMAK İÇİN ##################
                    giris = imagesearch("tamam.PNG")
                    if giris[0] != -1:
                        giris_x = giris[0]
                        giris_y = giris[1]
                        giris_x = giris_x + 25
                        giris_y = giris_y + 15
                        print("Oyundan Atmış, Oyuna Giriliyor...")
                        time.sleep(1)
                        pyautogui.moveTo(giris_x, giris_y, 0.2)
                        time.sleep(0.1)
                        pyautogui.leftClick(giris_x, giris_y)
                        time.sleep(1)
                        keyboard.press("F1")
                        time.sleep(0.2)
                        keyboard.release("F1")
                        time.sleep(10)

                    ################ SUNUCUYA BAĞLANIRKEN SORUN OLURSA ##################
                    iptalet = imagesearch("iptal.PNG")
                    if iptalet[0] != -1:
                        iptalet_x = iptalet[0]
                        iptalet_y = iptalet[1]
                        iptalet_x = iptalet_x + 25
                        iptalet_y = iptalet_y + 15
                        print("Oyuna Girerken Hata")
                        pyautogui.moveTo(iptalet_x, iptalet_y, 0.2)
                        time.sleep(0.1)
                        pyautogui.leftClick(iptalet_x, iptalet_y)

                    ################ OYUNA GİRİŞ İÇİN ##################
                    karakter = imagesearch("Karakter.PNG")
                    if not karakter[0] == -1:
                        print("Karakter Ekranında, Oyuna Giriliyor...")
                        keyboard.press("enter")
                        time.sleep(0.2)
                        keyboard.release("enter")
                        time.sleep(15)
                        keyboard.press("f")
                        time.sleep(1)
                        keyboard.release("f")
                        time.sleep(0.1)
                        keyboard.press("F8")
                        time.sleep(0.1)
                        keyboard.release("F8")
                        time.sleep(0.1)

                    ################ PET PENCERESİ AÇILIRSA DİYE ##################
                    pet = imagesearch("pet.PNG")
                    if pet[0] != -1:
                        pet_x = pet[0]
                        pet_y = pet[1]
                        pet_x = pet_x + 70
                        pet_y = pet_y + 10
                        pyautogui.moveTo(pet_x, pet_y, 0.2)
                        # pyautogui.mouseDown(button='left')
                        pyautogui.drag(-150, 0, 0.2, button='left')
                        # pyautogui.mouseUp(button='left')


                    menu = imagesearch("Menu.PNG")
                    if menu[0] != -1:
                        print("Menü Açılmış, Kapatılıyor...")
                        keyboard.press("esc")
                        time.sleep(0.1)
                        keyboard.release("esc")

                    secenekler = imagesearch("Ayarlar.PNG")
                    if secenekler[0] != -1:
                        print("Seçenekler Açılmış, Kapatılıyor...")
                        keyboard.press("esc")
                        time.sleep(0.1)
                        keyboard.release("esc")

                    uyari = imagesearch("Uyari.PNG")
                    if uyari[0] != -1:
                        print("Uyarı Açılmış, Kapatılıyor...")
                        keyboard.press("esc")
                        time.sleep(0.1)
                        keyboard.release("esc")

                    ##### SAATİ YAZDIRMAK İÇİN ####
                    epoch = time.gmtime(time.time())
                    print("Saat: ", epoch.tm_hour, "Dakika: ", epoch.tm_min)
                    ###############################################################

                if stop == 1:
                    break

                if z.get() == 0:
                    break

            if z.get() == 0:
                bilgi["text"] = "Oto Av Durdu"
                pencere.update()
    except:
        print("Bir Sorun Oluştu.")
        epoch = time.gmtime(time.time())
        print("Saat: ", epoch.tm_hour, "Dakika: ", epoch.tm_min)


########################### Pencere Donmaması için ########################
def b():
    global stop
    global secilenMetin
    stop = 0
    if q.get() == "Deniz Kabukları Metini":
        secilenMetin = "DenizKabuklariMetini.PNG"
    elif q.get() == "Kurak Arazi Metini":
        secilenMetin = "KurakAraziMetini.PNG"
    elif q.get() == "Mağrurluğun Metini":
        secilenMetin = "Abc.PNG"
    elif q.get() == "Büyülü Orman Metini":
        secilenMetin = "BuyuluOrman.PNG"
    elif q.get() == "Buz Ormanı Metini":
        secilenMetin = "BuzOrmanMetini.PNG"
    elif q.get() == "Doyyumhwan Metini":
        secilenMetin = "doyyummetini.PNG"
    elif q.get() == "Gölge Metini":
        secilenMetin = "GolgeMetini.PNG"
    elif q.get() == "Işıksızlık Metini":
        secilenMetin = "Isiksizlik.PNG"
    elif q.get() == "Jeon-Un Metini":
        secilenMetin = "Jeon-UnMetini.PNG"
    elif q.get() == "Katil Metini":
        secilenMetin = "KatilMetini.PNG"
    elif q.get() == "Kızıl Orman Metini":
        secilenMetin = "kızılormanmetini.PNG"
    elif q.get() == "Korku Metini":
        secilenMetin = "KorkuMetni.PNG"
    elif q.get() == "Lanet Metini":
        secilenMetin = "Lanet.PNG"
    elif q.get() == "Natural Metin":
        secilenMetin = "Natural.PNG"
    elif q.get() == "Dayanıklılık Metini":
        secilenMetin = "New7.PNG"
    elif q.get() == "Metin Tu-Young":
        secilenMetin = "New17.PNG"
    elif q.get() == "Namertlik Metini":
        secilenMetin = "New18.PNG"
    elif q.get() == "Ağaç Yaratığı Metini":
        secilenMetin = "New20.PNG"
    elif q.get() == "Orman Metini":
        secilenMetin = "New23.PNG"
    elif q.get() == "Çöl Taşı":
        secilenMetin = "New33.PNG"
    elif q.get() == "Diken Taşı":
        secilenMetin = "New23.PNG"
    elif q.get() == "Yongbi Çölü Metini":
        secilenMetin = "New666.PNG"
    elif q.get() == "Dostluk Ormanı Metini":
        secilenMetin = "OrmanMetini.PNG"
    elif q.get() == "Yaz Adası Metini":
        secilenMetin = "YazAdasiMetini.PNG"

    t1 = threading.Thread(target=OtoAv)
    t1.start()
##############################################################################

z = tk.IntVar()
z.set(0)
check2 = tk.Checkbutton(pencere, text="Oto Metin Avı Başlat", fg="black", activebackground="red", variable=z, onvalue=1, offvalue=0, command=b)
check2.place(x=100, y=70)

########################## Pencereyi Kapatmak İçin #############################
def dur():
    global stop
    #stop = 1
    if messagebox.askokcancel("Çık", "Çıkmak İstiyor Musunuz?"):
        stop = 1
    pencere.destroy()

check = tk.Button(pencere, text="Pençereyi Kapat", fg="black", activebackground="red", command=dur)
check.place(x=140, y=310)
#########################################################################################

####################### Metin Kesme Süresi için########################################################
def only_numbers(char):
    return char.isdigit()
validation = pencere.register(only_numbers)
t2 = Entry(pencere, validate="key", validatecommand=(validation, '%S'))
t2.place(x=0, y=10)
zaman = tk.Label(pencere, text=" = Bekleme Süresini Giriniz!")
zaman.place(x=50, y=10)
#########################################################################################

################################## DENEME X ve Y KOORDİNATLARI İÇİN ########################
def only_numbers1(char):
    return char.isdigit()
def only_numbers2(char):
    return char.isdigit()
validation1 = pencere.register(only_numbers1)
validation2 = pencere.register(only_numbers2)
t = Entry(pencere, validate="key",width=3, validatecommand=(validation1, '%S'))
t.place(x=10, y=90)
t1 = Entry(pencere, validate="key",width=3, validatecommand=(validation2, '%S'))
t1.place(x=40, y=90)
x_koordinati = tk.Label(pencere, text="X")
x_koordinati.place(x=10, y=70)
y_koordinati = tk.Label(pencere, text="Y ")
y_koordinati.place(x=40, y=70)
############################################################################################

####################### Metin Seçmek için########################################################
q = tk.StringVar()
Metinler = ["Deniz Kabukları Metini",
            "Kurak Arazi Metini",
            "Mağrurluğun Metini",
            "Büyülü Orman Metini",
            "Buz Ormanı Metini",
            "Doyyumhwan Metini",
            "Gölge Metini",
            "Işıksızlık Metini",
            "Jeon-Un Metini",
            "Katil Metini",
            "Kızıl Orman Metini",
            "Korku Metini",
            "Lanet Metini",
            "Natural Metin",
            "Dayanıklılık Metini",
            "Metin Tu-Young",
            "Namertlik Metini",
            "Ağaç Yaratığı Metini",
            "Orman Metini",
            "Çöl Taşı",
            "Diken Taşı",
            "Yongbi Çölü Metini",
            "Dostluk Ormanı Metini",
            "Yaz Adası Metini",
            ]
kutu = ttk.Combobox(pencere, values=Metinler, textvariable=q).place(x=180,y=40)
metinsec = tk.Label(pencere, text="Keseceğiniz Metini Belirtiniz= ")
metinsec.place(x=0, y=40)
#################################################################################

pencere.protocol("WM_DELETE_WINDOW", dur)
pencere.mainloop()
