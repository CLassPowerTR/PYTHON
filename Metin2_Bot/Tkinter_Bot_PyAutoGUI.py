9import threading
from tkinter import messagebox
from python_imagesearch.imagesearch import imagesearch
import pyautogui
import keyboard
import time
from tkinter import *
import tkinter as tk
from tkinter import ttk
import random
import pyautogui
from PIL.Image import Image
import cv2
import numpy as np
from PIL import Image
import pytesseract
global bilgi
global pelerinText    
global resimSirasi
global time_sleep
global aktifKanal
global channels
global g
from tkinter import Tk,Menubutton

pencere = tk.Tk()
pencere.geometry("360x420")
version = Label(pencere, text="xxxx yyyy | METİN_BOTU_Version v0.4.0")
version.pack(side=BOTTOM)

menu = ttk.Notebook(pencere)
otoGiris = ttk.Frame(menu)
otoMetin = ttk.Frame(menu)
otoTus   = ttk.Frame(menu)
etkinlik = ttk.Frame(menu)

menu.add(otoGiris, text="Oto Giriş")
menu.add(otoMetin, text="Oto Metin")
menu.add(otoTus, text="Oto Tuş")
menu.add(etkinlik, text="Etkinlik")
menu.pack(side= TOP,expand=True, fill="both")

######################################## KOMUTLAR ################################################
def chlerArasiFarm():
    try:
        if otoTusButton4Baslat.get() == 1:
            for u in range(3,0,-1):
                otoFarm["text"] = f" = {u}"
                time.sleep(1)
            otoFarm["text"] = "Aktif"
            girilecekKanal=seciliKanal
            suankiKanal = girilecekKanal
            chlerArasiFarmBilgi6.config(text = "Aktif Edildi")
            tupple = [(1,"Kanal 1"),(2,"Kanal 2"),(3,"Kanal 3"),(4,"Kanal 4"),(5,"Kanal 5"),(6,"Kanal 6")]
            while otoTusButton4Baslat.get()==1: 
                oyundaMi = pyautogui.locateOnScreen("oyundaMi.PNG", confidence=0.8)
                if oyundaMi !=None:
                    chlerArasiFarmBilgi6.config(text = "Oyun Görüldü")
                    suankiKanal = girilecekKanal
                    chlerArasiFarmBilgi7.config(text = suankiKanal)
                    for a,b in tupple:
                        if str(girilecekKanal)==str(b):
                            if str(b) =="Kanal 6":
                                girilecekKanal = tupple[0]
                                girilecekKanal = girilecekKanal[1]
                                break
                            girilecekKanal = tupple[a]
                            girilecekKanal = girilecekKanal[1]
                            break
                    chlerArasiFarmBilgi8.config(text = girilecekKanal)
                    chlerArasiFarmBilgi6.config(text = "Saldırı Başlatıldı")
                    if otoTusButton4Baslat.get() == 1:
                        oyundaMi = pyautogui.locateOnScreen("oyundaMi.PNG", confidence=0.8)
                        if oyundaMi !=None:
                            keyboard.release("space")
                            time.sleep(1)
                            keyboard.press("space")
                            for i in range(10):
                                keyboard.press("F4")
                                time.sleep(0.2)
                                keyboard.release("F4")
                                time.sleep(0.5)
                            time.sleep(10)
                            keyboard.release("space")
                            chlerArasiFarmBilgi6.config(text = "Kanal Değiştiriliyor")
                            oyundaMi = pyautogui.locateOnScreen("oyundaMi.PNG", confidence=0.8)
                            if oyundaMi !=None:
                                time.sleep(0.2)
                                keyboard.press("enter")
                                time.sleep(0.2)
                                keyboard.release("enter")
                                pyautogui.write("/"+girilecekKanal, interval=0.05)
                                time.sleep(0.5)
                                keyboard.press("enter")
                                time.sleep(0.2)
                                keyboard.release("enter")
                                time.sleep(3)
                
                else:
                    yukleniyor = pyautogui.locateOnScreen("yukleniyor.PNG", confidence=0.7)
                    if yukleniyor != None:
                        chlerArasiFarmBilgi6.config(text = "Ekran Yükleniyor")
                        time.sleep(2)
                    else:
                        chlerArasiFarmBilgi6.config(text = "Görüntü Yok")
                        time.sleep(2)
                
        elif otoTusButton4Baslat.get() == 0:
            chlerArasiFarmBilgi6.config(text = "Durduruldur")
    except:
        print("Hata")


def donerekVur():
    try:
        if otoTusBasla2.get() == 1:
            for i in range(3,0,-1):
                otoTusLabel3["text"] = f" = {i}"
                time.sleep(1)
            otoTusLabel3["text"] = " Aktif "
            while otoTusBasla2.get() == 1:
                keyboard.press("space")
                time.sleep(0.5)
                keyboard.press("w")
                keyboard.press("e")
                time.sleep(5)
                keyboard.release("w")
                keyboard.release("e")
                keyboard.release("space")
                
        elif otoTusBasla2.get() == 0:
            otoTusLabel3["text"] = "Deaktif"
    except:
        print("Hata")


def Pelerin():
    try:
        bekle = time_sleep
        if otoTusBasla.get() == 1:
            a = otoTusEntryValue.get()
            for i in range(3,0,-1):
                otoTusDurum["text"] = f" = {i}"
                time.sleep(1)
            otoTusDurum["text"] = f"Aktif Tuş ({a})"
            while otoTusBasla.get() == 1:
                keyboard.press(f"{a}")
                time.sleep(0.001)
                keyboard.release(f"{a}")    
                time.sleep(bekle)
        if otoTusBasla.get() == 0:
            otoTusDurum["text"] = " Deaktif"
    except:
        print("Hata")


def Pelerin1():
    try:
        bekle = time_sleep1
        if otoTusBasla1.get() == 1:
            b = otoTusEntryValue1.get()
            for i in range(3,0,-1):
                otoTusDurum1["text"] = f" = {i}"
                pencere.update()
                time.sleep(1)
            otoTusDurum1["text"] = f"Aktif Tuş ({b})"
            pencere.update()
            while otoTusBasla1.get() == 1:
                keyboard.press(f"{b}")
                time.sleep(0.001)
                keyboard.release(f"{b}")    
                time.sleep(bekle)
        if otoTusBasla1.get() == 0:
            otoTusDurum1["text"] = " Deaktif"
            pencere.update()
    except:
        print("Hata")


def zamanlayici1():
    try:
        if o.get() ==1:
            
            k=1
            
            while k==1:
                epoch = time.gmtime(time.time())
                saat = epoch.tm_hour+3
                dakika = epoch.tm_min+2
                saniye = epoch.tm_sec+40
                if saniye>=60:
                    dakika = dakika +1
                    saniye = saniye-60
                if dakika>=60:
                    saat=saat+1
                    dakika=dakika-60
                if saat>=24:
                    saat=saat-24
                kalanDakika = 2
                kalanSaniye = 40
                cikacakSaat["text"] = "{}:{}:{}".format(saat,dakika,saniye)
                x = epoch.tm_sec
                g=1
                while g==1:
                    epoch = time.gmtime(time.time())
                    saat1 = epoch.tm_hour+3
                    if saat1>=24:
                        saat1=saat1-24
                    kalanSüre["text"] = "Kalan Süre: 00:0{}:{}".format(kalanDakika,kalanSaniye)
                    metinZamanlayici["text"] = "{}:{}:{}".format(saat1,epoch.tm_min,epoch.tm_sec)
                    if x != epoch.tm_sec:
                        if kalanSaniye==0:
                            kalanDakika = kalanDakika-1
                            kalanSaniye = 60
                        kalanSaniye=kalanSaniye-1
                    if o.get() ==0:
                        metinZamanlayici["text"] = "Durdu"
                        g=0
                        k=0
                    if epoch.tm_min==dakika and epoch.tm_sec==saniye:
                        g=0
                    x = epoch.tm_sec
                    time.sleep(0.1)
    except:
        print("Hata")


def metinKes():
    try:
        if l.get() == 1:
            bilgi = Label(pencere, text="Metin Botu Başladı")
            bilgi.place(x=240, y=370)
            
            metinAdi = metinValue.get()
            a = int(otoMetinEntryValue.get())
            time.sleep(2)
            kesilenMetinSayisi = 1

            while l.get() == 1:
                try:
                    metin = pyautogui.locateOnScreen(secilenMetin, confidence=0.6, region= (0,100,1920,980))
                    if metin != None:
                        metin_x = metin[0]+(metin[2]/2)
                        metin_y = metin[1]+ 60
                        epoch = time.gmtime(time.time())
                        saat = epoch.tm_hour+3
                        if saat>=24:
                            saat=saat-24
                        print("{} Bulundu Koordinat: x:{} y:{} -- Kesilen Metin Sayisi: {} -- Saat: {}:{}:{}".format(metinAdi, metin[0],metin[1], kesilenMetinSayisi,saat,epoch.tm_min,epoch.tm_sec))
                        pyautogui.moveTo(metin_x, metin_y)
                        time.sleep(0.3)
                        pyautogui.click()
                        kesilenMetinSayisi=kesilenMetinSayisi + 1
                        time.sleep(1)
                        for i in range(a+1):
                            if l.get() == 0:
                                bilgi["text"] = "Oto Av Durdu"
                                break
                            time.sleep(1)
                except:
                    time.sleep(1)
            if l.get() == 0:
                    bilgi["text"] = "Metin Botu Durdu"

    except:
        print("Bir Sorun Oluştu.")
        epoch = time.gmtime(time.time())
        print("Saat: ", epoch.tm_hour + 3, "Dakika: ", epoch.tm_min)


def otomatikGiris():
    try:
        if oG.get() == 1:
            kAdi = otoGirisEntryValue.get()
            bilgi1 = Label(pencere, text="Otomatik Giriş Başladı")
            bilgi1.place(x=0, y=350)
            while oG.get() == 1:
                try:
                    server = pyautogui.locateOnScreen("server.PNG", confidence=0.6)
                    if server != None:
                        x,y,w,h = pyautogui.locateOnScreen(kanal, confidence=0.99)
                        if x != None:
                            girilecekKanal = ch.get()
                            x = x + (w/2)
                            y = y + (h/2)
                            pyautogui.moveTo(x, y)
                            time.sleep(0.3)
                            pyautogui.click()
                            time.sleep(1)
                    giris = pyautogui.locateOnScreen("giris.PNG", confidence=0.8)
                    if giris != None:
                        giris_x = giris[0]+(giris[2]/2)
                        giris_y = giris[1]+(giris[3]/2)
                        pyautogui.moveTo(giris_x, giris_y)
                        time.sleep(0.3)
                        pyautogui.click()
                        time.sleep(5)
                        hata = pyautogui.locateOnScreen("ok.PNG", confidence=0.8)
                        if hata != None:
                            hata_x = hata[0]+(hata[2]/2)
                            hata_y = hata[1]+(hata[3]/2)
                            pyautogui.moveTo(hata_x, hata_y)
                            time.sleep(0.3)
                            pyautogui.click()
                            time.sleep(5)
                    hesap = pyautogui.locateOnScreen("hesap.PNG", confidence=0.8)
                    if hesap != None:
                        pyautogui.write(kAdi, interval=0.1)
                        pyautogui.press('enter') 
                        pyautogui.write("", interval=0.1)
                        pyautogui.press('enter')
                        time.sleep(0.1)
                        keyboard.release("enter")
                        time.sleep(5)
                    basla = pyautogui.locateOnScreen("basla.PNG", confidence=0.8)
                    if basla != None:
                        basla_x = basla[0]+(basla[2]/2)
                        basla_y = basla[1]+(basla[3]/2)
                        pyautogui.moveTo(basla_x, basla_y)
                        time.sleep(0.3)
                        pyautogui.click()
                        time.sleep(5) 
                except:
                    time.sleep(1)
            if oG.get() == 0:
                bilgi1["text"] = "Otomatik Giriş Durdu"
    except:
        time.sleep(1)
    
def yenidenBasla():
    try:
        if yB.get() == 1:
            
            
            bilgi2 = Label(pencere, text="Yeniden Başla Aktif")
            bilgi2.place(x=0, y=370)
            while yB.get() == 1:
                try:
                    yenidenBasla = pyautogui.locateOnScreen("yenidenBasla.PNG", confidence=0.8)
                    if yenidenBasla != None:
                        time.sleep(10)
                        yenidenBasla_x = yenidenBasla[0]+(yenidenBasla[2]/2)
                        yenidenBasla_y = yenidenBasla[1]+(yenidenBasla[3]/2)
                        pyautogui.moveTo(yenidenBasla_x, yenidenBasla_y)
                        time.sleep(0.3)
                        pyautogui.click()
                        time.sleep(2)
                        keyboard.press("F3")
                        time.sleep(0.1)
                        keyboard.release("F3")
                        time.sleep(2)
                        """
                        keyboard.press("ctrl")
                        keyboard.press("h")
                        time.sleep(0.1)
                        keyboard.release("ctrl")
                        keyboard.release("h")
                        """
                except:
                    time.sleep(1)
            if yB.get() == 0:
                bilgi2["text"] = "Yeniden Başla Deaktif"
    except:
        time.sleep(1)


def botKontrol():
    try:
        if t.get() == 1:
            while t.get() == 1:
                try:
                    left,top,width,height = pyautogui.locateOnScreen('BotVerify.PNG', confidence=0.5)
                    botDurum["text"] = "svside Bulundu"
                    ekran_goruntusu = pyautogui.screenshot(region=(left, top+10, width-70, height-155))
                    dosya_adi = f"ekran_goruntusu.jpg"
                    ekran_goruntusu.save(dosya_adi)

                    # Pytesseract yolumuzu belirtiyoruz
                    pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
                    # C:\\Users\\tunah\\PycharmProjects\\MetinBotu\\

                    custom_config = r'-c tessedit_char_whitelist=0123456789 --psm 6'  # Sadece beyaz listedekileri çıkar
                    sonuc = pytesseract.image_to_string(Image.open('EnTemizResimCaptcha1.png'), config=custom_config)
                    print(sonuc)
                    if t.get() == 1:
                        for i in sonuc:
                            if i == "0":
                                botDurum["text"] = "0"
                                loc = pyautogui.locateOnScreen("sifir.png")
                                pyautogui.moveTo(loc[0] + (loc[2]/2), loc[1] + (loc[3]/2), 0.2)
                                pyautogui.click()
                            elif i == "1":
                                botDurum["text"] = "1"
                                loc = pyautogui.locateOnScreen("bir.png")
                                pyautogui.moveTo(loc[0] + (loc[2]/2), loc[1] + (loc[3]/2), 0.2)
                                pyautogui.click()
                            elif i == "2":
                                botDurum["text"] = "2"
                                loc = pyautogui.locateOnScreen("iki.png")
                                pyautogui.moveTo(loc[0] + (loc[2]/2), loc[1] + (loc[3]/2), 0.2)
                                pyautogui.click()
                            elif i == "3":
                                botDurum["text"] = "3"
                                loc = pyautogui.locateOnScreen("uc.png")
                                pyautogui.moveTo(loc[0] + (loc[2]/2), loc[1] + (loc[3]/2), 0.2)
                                pyautogui.click()
                            elif i == "4":
                                botDurum["text"] = "4"
                                loc = pyautogui.locateOnScreen("dört.png", confidence=0.49)
                                pyautogui.moveTo(loc[0] + (loc[2]/2), loc[1] + (loc[3]/2), 0.2)
                                pyautogui.click()
                            elif i == "5":
                                botDurum["text"] = "5"
                                loc = pyautogui.locateOnScreen("bes.png")
                                pyautogui.moveTo(loc[0] + (loc[2]/2), loc[1] + (loc[3]/2), 0.2)
                                pyautogui.click()
                            elif i == "6":
                                botDurum["text"] = "6"
                                loc = pyautogui.locateOnScreen("alti.png")
                                pyautogui.moveTo(loc[0] + (loc[2]/2), loc[1] + (loc[3]/2), 0.2)
                                pyautogui.click()
                            elif i == "7":
                                botDurum["text"] = "7"
                                loc = pyautogui.locateOnScreen("yedi.png")
                                pyautogui.moveTo(loc[0] + (loc[2]/2), loc[1] + (loc[3]/2), 0.2)
                                pyautogui.click()
                            elif i == "8":
                                botDurum["text"] = "8"
                                loc = pyautogui.locateOnScreen("sekiz.png")
                                pyautogui.moveTo(loc[0] + (loc[2]/2), loc[1] + (loc[3]/2), 0.2)
                                pyautogui.click()
                            elif i == "9":
                                botDurum["text"] = "9"
                                loc = pyautogui.locateOnScreen("dokuz.png")
                                pyautogui.moveTo(loc[0] + (loc[2]/2), loc[1] + (loc[3]/2), 0.2)
                                pyautogui.click()
                        botDurum["text"] = sonuc
                        loc = pyautogui.locateOnScreen("ok.png", confidence=0.8)
                        pyautogui.moveTo(loc[0] + (loc[2]/2), loc[1] + (loc[3]/2), 0.2)

                except:
                    print("svside Bulunamadı")
                    botDurum["text"] = "svside Bulunamadı"
                    time.sleep(15)

        if t.get() == 0:
            botKontrolText["text"] = "Bot Kontrol: Deaktif"
            botDurum["text"] = "Bot Durdu"
    except:
        pass


def Captcha():
    botKontrol = pyautogui.locateOnScreen('BotKontrol.PNG', confidence=0.6)
    left=botKontrol[0]+5
    top=botKontrol[1]+7
    width=botKontrol[2]-100
    height=botKontrol[3]-155
    ekran_goruntusu = pyautogui.screenshot(region=(left,top,width,height))
    dosya_adi = f"ekran_goruntusu{resimSirasi}.jpg"
    ekran_goruntusu.save(dosya_adi)

    # Pytesseract yolumuzu belirtiyoruz
    pytesseract.pytesseract.tesseract_cmd="C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
    # C:\\Users\\tunah\\PycharmProjects\\MetinBotu\\


    def metinOku(resim_yolu):
        image = cv2.imread(resim_yolu)#Okuyacağımız resmin yolunu alıyoruz


        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Resmimimizi gri tona çeviriyoruz

        #Resimde Kirlilik varsa onları temizliyoruz
        kernel=np.ones((1,1),np.uint8)
        image=cv2.erode(image,kernel,iterations=1)
        image=cv2.dilate(image,kernel,iterations=1)



        #Resmimizde ki gri tonları siyah yapıyoruz
        image=cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,31,2)
        cv2.imwrite('temizlenmisResim.png',image)
        custom_config = r'-c tessedit_char_whitelist=0123456789 --psm 6' #Sadece beyaz listedekileri çıkar
        sonuc=pytesseract.image_to_string(Image.open('temizlenmisResim.png'),config=custom_config)
        print(sonuc)

    print('Okuma Başladı')
    print(' ')
    #Metin olarak görmek istediğimiz resmin yolunu belirtiyoruz
    metinOku(f'ekran_goruntusu{resimSirasi}.jpg')
    print(' ')
    print('Okuma Bitti')
    return     


def skillYak():
    try:
        if x.get() == 1:
            for i in range(3,0,-1):
                skillText["text"] = f" = {i}"
                time.sleep(1)
            while x.get() == 1:
                keyboard.press("space")
                time.sleep(95)
                keyboard.release("space")
                if x.get()==1:
                    time.sleep(0.2)
                    keyboard.press("ctrl")
                    keyboard.press("g")
                    time.sleep(0.1)
                    keyboard.release("ctrl")
                    keyboard.release("g")
                    time.sleep(0.5)
                    keyboard.press(f"4")
                    time.sleep(0.1)
                    keyboard.release(f"4")
                    time.sleep(1)
                    keyboard.press("ctrl")
                    keyboard.press("g")
                    time.sleep(0.1)
                    keyboard.release("ctrl")
                    keyboard.release("g")

        if x.get() == 0:
            skillText["text"] = "Deaktif"
    except:
        print("Hata")




######################################## OTO GİRİŞ ################################################
def otoGirisCommand():
    global kanal
    if ch.get() == "Kanal 1":
        kanal = "Kanal1.PNG"
    elif ch.get() == "Kanal 2":
        kanal = "Kanal2.PNG"
    elif ch.get() == "Kanal 3":
        kanal = "Kanal3.PNG"
    elif ch.get() == "Kanal 4":
        kanal = "Kanal4.PNG"
    elif ch.get() == "Kanal 5":
        kanal = "Kanal5.PNG"
    elif ch.get() == "Kanal 6":
        kanal = "Kanal6.PNG"
    t1 = threading.Thread(target=otomatikGiris)
    t1.start()
def yBasla():
    t2 = threading.Thread(target=yenidenBasla)
    t2.start()


ch = StringVar(pencere)
channels = [
"Kanal 1",
"Kanal 2",
"Kanal 3",
"Kanal 4",
"Kanal 5",
"Kanal 6",
]
otoGirisLabel = ttk.Combobox(otoGiris, values=channels, textvariable=ch).grid(row=1,column=1)
oG = tk.IntVar(pencere)
oG.set(0)
otoGirisButton = ttk.Checkbutton(otoGiris, text="Otomatik Giriş", variable=oG, onvalue=1, offvalue=0, command=otoGirisCommand).grid(row=3,column=1)
otoGirisEntryValue = StringVar()
otoGirisEntry = ttk.Entry(otoGiris, textvariable = otoGirisEntryValue).grid(row=0,column=1)
otoGirisLabel1 = ttk.Label(otoGiris, text="Kullanıcı Adı =").grid(row=0,column=0)
chLabel = ttk.Label(otoGiris, text="Kanal : ").grid(row=1,column=0)
yB = tk.IntVar(pencere)
yB.set(0)
otoGirisButton = ttk.Checkbutton(otoGiris, text="Yeniden Başla", variable=yB, onvalue=1, offvalue=0, command=yBasla).grid(row=3,column=0)
##################################################################################################

######################################## OTO METİN ################################################
def otoMetinCommand():
    global stop
    global secilenMetin
    stop = 0
    if metinValue.get() == "Kurtuluş Metini":
        secilenMetin = "KurtulusMetini.PNG"
    elif metinValue.get() == "Hainlik Metini":
        secilenMetin = "HainlikMetini.PNG"
    elif metinValue.get() == "Mutsuzluk Metini":
        secilenMetin = "MutsuzlukMetini.PNG"
    t3 = threading.Thread(target=metinKes)
    t3.start()

def zamanlayiciCommand():
    t4 = threading.Thread(target=zamanlayici1)
    t4.start()

metinValue = StringVar(pencere)
metinler = ["Kurtuluş Metini",
"Hainlik Metini",
"Mutsuzluk Metini",
]

otoMetinEntryValue = StringVar()
otoMetinEntry = ttk.Entry(otoMetin,textvariable=otoMetinEntryValue).grid(row=0, column=1)
otoMetinLabel = ttk.Label(otoMetin, text="Bekleme Süresi =").grid(row=0,column=0)
l = tk.IntVar(pencere)
l.set(0)
otoMetinButton = ttk.Checkbutton(otoMetin,text="Oto Metin Av Başlat",variable=l, onvalue=1, offvalue=0, command=otoMetinCommand).grid(row=2,column=1)
otoMetinLabel1 = ttk.Label(otoMetin, text="Kesilecek Metin =").grid(row=1,column=0)
otoMetinButton1 = ttk.Combobox(otoMetin, values=metinler, textvariable=metinValue).grid(row=1,column=1)

metinZamanlayici = ttk.Label(otoMetin, text="00.00.00")
metinZamanlayici.place(x=80,y=70)
cikacakSaat1 = ttk.Label(otoMetin, text="Metin Yenilenme Saati =")
cikacakSaat1.place(x=140, y=70)
cikacakSaat = ttk.Label(otoMetin, text="00.00.00")
cikacakSaat.place(x=270, y=70)
kalanSüre = ttk.Label(otoMetin, text="Kalan Süre =")
kalanSüre.place(x=20,y=90)



o = tk.IntVar(pencere)
o.set(0)
metinZamanlayiciButon = ttk.Checkbutton(otoMetin,text="Saat: ",variable=o, onvalue=1, offvalue=0, command=zamanlayiciCommand).grid(row=4,column=0)


##################################################################################################

########################################### OTO TUŞ #######################################################
def otoTusCommand():
    global time_sleep
    if tusHizValue.get() == "Çok Yavaş":
        time_sleep = 2
    elif tusHizValue.get() == "Yavaş":
        time_sleep = 1
    elif tusHizValue.get() == "Orta":
        time_sleep = 0.5
    elif tusHizValue.get() == "Hızlı":
        time_sleep = 0.1
    elif tusHizValue.get() == "Çok Hızlı":
        time_sleep = 0.01
    t5 = threading.Thread(target=Pelerin)
    t5.start()

def otoTusCommand1():
    global time_sleep1
    if tusHizValue1.get() == "Çok Yavaş":
        time_sleep1 = 2
    elif tusHizValue1.get() == "Yavaş":
        time_sleep1 = 1
    elif tusHizValue1.get() == "Orta":
        time_sleep1 = 0.5
    elif tusHizValue1.get() == "Hızlı":
        time_sleep1 = 0.1
    elif tusHizValue1.get() == "Çok Hızlı":
        time_sleep1 = 0.01
    t6 = threading.Thread(target=Pelerin1)
    t6.start()

def donerekVurCommand():
    t7 = threading.Thread(target=donerekVur)
    t7.start()


otoTusBasla = tk.IntVar(pencere)
otoTusBasla.set(0)
otoTusDurum = ttk.Label(otoTus, text="Deaktif")
otoTusDurum.grid(row=1,column=3)
otoTusEntryValue = tk.StringVar(pencere)
otoTusEntry = ttk.Entry(otoTus,textvariable=otoTusEntryValue,width=7).grid(row=1,column=0)
otoTusButton = ttk.Checkbutton(otoTus,text="Oto Tuşu Başlat",variable=otoTusBasla, onvalue=1, offvalue=0, command=otoTusCommand).grid(row=1,column=2)

otoTusBasla1 = tk.IntVar(pencere)
otoTusBasla1.set(0)
otoTusDurum1 = ttk.Label(otoTus, text="Deaktif")
otoTusDurum1.grid(row=2,column=3)
otoTusEntryValue1 = StringVar(pencere)
otoTusEntry1 = ttk.Entry(otoTus,textvariable=otoTusEntryValue1,width=7).grid(row=2,column=0)
otoTusButton1 = ttk.Checkbutton(otoTus,text="Oto Tuşu Başlat",variable=otoTusBasla1, onvalue=1, offvalue=0, command=otoTusCommand1).grid(row=2,column=2)

tusHizValue = StringVar(pencere)
tusHizValue1 = StringVar(pencere)
tusHizi = ["Çok Yavaş",
"Yavaş",
"Orta",
"Hızlı",
"Çok Hızlı",
]

otoTusLabel4 = ttk.Label(otoTus,text="TUŞ")
otoTusLabel4.grid(row=0,column=0)
otoTusLabel5 = ttk.Label(otoTus,text="HIZ")
otoTusLabel5.grid(row=0,column=1)

otoTusButton4 = ttk.Combobox(otoTus, values=tusHizi,width=10,height=5, textvariable=tusHizValue1).grid(row=2,column=1)
otoTusButton2 = ttk.Combobox(otoTus, values=tusHizi,width=10,height=5, textvariable=tusHizValue).grid(row=1,column=1)

otoTusBasla2 = tk.IntVar(pencere)
otoTusBasla2.set(0)
otoTusButton3 = ttk.Checkbutton(otoTus,text="Dönerek Vur",variable=otoTusBasla2, onvalue=1, offvalue=0, command=donerekVurCommand).grid(row=3 ,column=2)
otoTusLabel3 = ttk.Label(otoTus,text="Deaktif")
otoTusLabel3.grid(row=3,column=3)
########################################################################################################

################################################ CHLER ARASI FARM ########################################################
def cokluFarm():
    global seciliKanal
    if secilenKanal.get() == "Kanal 1":
        #seciliKanal = "Kanal {}.PNG".format(1)
        seciliKanal = "Kanal {}".format(1)
    elif secilenKanal.get() == "Kanal 2":
        #seciliKanal = "Kanal{}.PNG".format(2)
        seciliKanal = "Kanal {}".format(2)
    elif secilenKanal.get() == "Kanal 3":
        #seciliKanal = "Kanal{}.PNG".format(3)
        seciliKanal = "Kanal {}".format(3)
    elif secilenKanal.get() == "Kanal 4":
        #seciliKanal = "Kanal{}.PNG".format(4)
        seciliKanal = "Kanal {}".format(4)
    elif secilenKanal.get() == "Kanal 5":
        #seciliKanal = "Kanal{}.PNG".format(5)
        seciliKanal = "Kanal {}".format(5)
    elif secilenKanal.get() == "Kanal 6":
        #seciliKanal = "Kanal{}.PNG".format(6)
        seciliKanal = "Kanal {}".format(6)
    t8 = threading.Thread(target=chlerArasiFarm)
    t8.start()
    
    
chlerArasiFarmBilgi = ttk.Label(otoTus, text="CHLER")
chlerArasiFarmBilgi.grid(row=4,column=0)
chlerArasiFarmBilgi1 = ttk.Label(otoTus, text="ARASI")
chlerArasiFarmBilgi1.grid(row=4,column=1)
chlerArasiFarmBilgi2 = ttk.Label(otoTus, text="FARM")
chlerArasiFarmBilgi2.grid(row=4,column=2)
otoFarm = ttk.Label(otoTus, text="Deaktif")
otoFarm.grid(row=5,column=3)
otoTusButton4Baslat = tk.IntVar(pencere)
otoTusButton4Baslat.set(0)
otoTusButton4 = ttk.Checkbutton(otoTus,text="BAŞLAT", variable=otoTusButton4Baslat, onvalue=1,offvalue=0, command=cokluFarm).grid(row=5,column=2)
otoTusLabel6 = ttk.Label(otoTus,text="Kanal =")
otoTusLabel6.grid(row=5 ,column=0)
secilenKanal = StringVar(pencere)
otoTusButton5 = ttk.Combobox(otoTus, values=channels, textvariable=secilenKanal,width=10,height=5).grid(row=5,column=1)


chlerArasiFarmBilgi3 = ttk.Label(otoTus, text="Bot Durumu: ")
chlerArasiFarmBilgi3.grid(row=6,column=1)
chlerArasiFarmBilgi4 = ttk.Label(otoTus, text="Şuan ki Kanal: ")
chlerArasiFarmBilgi4.grid(row=7,column=1)
chlerArasiFarmBilgi5 = ttk.Label(otoTus, text="Sonra ki Kanal: ")
chlerArasiFarmBilgi5.grid(row=8,column=1)
chlerArasiFarmBilgi6 = ttk.Label(otoTus, text="Deaktif")
chlerArasiFarmBilgi6.grid(row=6,column=2)
chlerArasiFarmBilgi7 = ttk.Label(otoTus, text=" ")
chlerArasiFarmBilgi7.grid(row=7,column=2)
chlerArasiFarmBilgi8 = ttk.Label(otoTus, text=" ")
chlerArasiFarmBilgi8.grid(row=8,column=2)


########################################################################################################

############################################# ETKİNLİK ###########################################################
a = ttk.Label(etkinlik, text="13/14",background="#99b7f6")
a.grid(row=1,column=0)
a = ttk.Label(etkinlik, text="14/15",background="#99b7f6")
a.grid(row=2,column=0)
a = ttk.Label(etkinlik, text="15/16",background="#99b7f6")
a.grid(row=3,column=0)
a = ttk.Label(etkinlik, text="16/17",background="#99b7f6")
a.grid(row=4,column=0)
a = ttk.Label(etkinlik, text="17/18",background="#99b7f6")
a.grid(row=5,column=0)
a = ttk.Label(etkinlik, text="18/19",background="#99b7f6")
a.grid(row=6,column=0)
a = ttk.Label(etkinlik, text="19/20",background="#99b7f6")
a.grid(row=7,column=0)
a = ttk.Label(etkinlik, text="20/21",background="#99b7f6")
a.grid(row=8,column=0)
a = ttk.Label(etkinlik, text="21/22",background="#99b7f6")
a.grid(row=9,column=0)
a = ttk.Label(etkinlik, text="22/23",background="#99b7f6")
a.grid(row=10,column=0)
a = ttk.Label(etkinlik, text="23/24",background="#99b7f6")
a.grid(row=11,column=0)
a = ttk.Label(etkinlik, text="P.tesi",background="#f4c679")
a.grid(row=0,column=1)
a = ttk.Label(etkinlik, text="Harf",background="#bee96a")
a.grid(row=1,column=1)
a = ttk.Label(etkinlik, text="Harf",background="#bee96a")
a.grid(row=2,column=1)
a = ttk.Label(etkinlik, text="Sandk",background="#aafaf7")
a.grid(row=3,column=1)
a = ttk.Label(etkinlik, text="Sanal",background="#f6f566")
a.grid(row=4,column=1)
a = ttk.Label(etkinlik, text="Sandk",background="#aafaf7")
a.grid(row=7,column=1)
a = ttk.Label(etkinlik, text="Sandk",background="#aafaf7")
a.grid(row=8,column=1)
a = ttk.Label(etkinlik, text="Sandk",background="#aafaf7")
a.grid(row=9,column=1)
a = ttk.Label(etkinlik, text="Sanal",background="#f6f566")
a.grid(row=10,column=1)
a = ttk.Label(etkinlik, text="Salı",background="#f4c679")
a.grid(row=0,column=2)
a = ttk.Label(etkinlik, text="Vadi",background="#e897a9")
a.grid(row=1,column=2)
a = ttk.Label(etkinlik, text="Vadi",background="#e897a9")
a.grid(row=2,column=2)
a = ttk.Label(etkinlik, text="Harf",background="#bee96a")
a.grid(row=3,column=2)
a = ttk.Label(etkinlik, text="Sanal",background="#f6f566")
a.grid(row=4,column=2)
a = ttk.Label(etkinlik, text="Vadi",background="#e897a9")
a.grid(row=7,column=2)
a = ttk.Label(etkinlik, text="Vadi",background="#e897a9")
a.grid(row=8,column=2)
a = ttk.Label(etkinlik, text="Harf",background="#bee96a")
a.grid(row=9,column=2)
a = ttk.Label(etkinlik, text="Sanal",background="#f6f566")
a.grid(row=10,column=2)
a = ttk.Label(etkinlik, text="Çarşmb",background="#f4c679")
a.grid(row=0,column=3)
a = ttk.Label(etkinlik, text="Sandk",background="#aafaf7")
a.grid(row=1,column=3)
a = ttk.Label(etkinlik, text="Sandk",background="#aafaf7")
a.grid(row=2,column=3)
a = ttk.Label(etkinlik, text="Sandk",background="#aafaf7")
a.grid(row=3,column=3)
a = ttk.Label(etkinlik, text="Sanal",background="#f6f566")
a.grid(row=4,column=3)
a = ttk.Label(etkinlik, text="Harf",background="#bee96a")
a.grid(row=7,column=3)
a = ttk.Label(etkinlik, text="Harf",background="#bee96a")
a.grid(row=8,column=3)
a = ttk.Label(etkinlik, text="Sandk",background="#aafaf7")
a.grid(row=9,column=3)
a = ttk.Label(etkinlik, text="Sanal",background="#f6f566")
a.grid(row=10,column=3)
a= ttk.Label(etkinlik, text="Perşmb",background="#f4c679")
a.grid(row=0,column=4)
a = ttk.Label(etkinlik, text="Harf",background="#bee96a")
a.grid(row=1,column=4)
a = ttk.Label(etkinlik, text="Vadi",background="#e897a9")
a.grid(row=2,column=4)
a = ttk.Label(etkinlik, text="Vadi",background="#e897a9")
a.grid(row=3,column=4)
a = ttk.Label(etkinlik, text="Sanal",background="#f6f566")
a.grid(row=4,column=4)
a = ttk.Label(etkinlik, text="Harf",background="#bee96a")
a.grid(row=7,column=4)
a = ttk.Label(etkinlik, text="Vadi",background="#e897a9")
a.grid(row=8,column=4)
a = ttk.Label(etkinlik, text="Vadi",background="#e897a9")
a.grid(row=9,column=4)
a = ttk.Label(etkinlik, text="Sanal",background="#f6f566")
a.grid(row=10,column=4)
a= ttk.Label(etkinlik, text="Cuma",background="#f4c679")
a.grid(row=0,column=5)
a = ttk.Label(etkinlik, text="Harf",background="#bee96a")
a.grid(row=1,column=5)
a = ttk.Label(etkinlik, text="Harf",background="#bee96a")
a.grid(row=2,column=5)
a = ttk.Label(etkinlik, text="Sandk",background="#aafaf7")
a.grid(row=3,column=5)
a = ttk.Label(etkinlik, text="Sanal",background="#f6f566")
a.grid(row=4,column=5)
a = ttk.Label(etkinlik, text="Sandk",background="#aafaf7")
a.grid(row=8,column=5)
a = ttk.Label(etkinlik, text="Sandk",background="#aafaf7")
a.grid(row=9,column=5)
a = ttk.Label(etkinlik, text="Sandk",background="#aafaf7")
a.grid(row=10,column=5)
a = ttk.Label(etkinlik, text="Sanal",background="#f6f566")
a.grid(row=11,column=5)
a= ttk.Label(etkinlik, text="C.tesi",background="#f4c679")
a.grid(row=0,column=6)
a = ttk.Label(etkinlik, text="Harf",background="#bee96a")
a.grid(row=1,column=6)
a = ttk.Label(etkinlik, text="Harf",background="#bee96a")
a.grid(row=2,column=6)
a = ttk.Label(etkinlik, text="Vadi",background="#e897a9")
a.grid(row=3,column=6)
a = ttk.Label(etkinlik, text="Vadi",background="#e897a9")
a.grid(row=4,column=6)
a = ttk.Label(etkinlik, text="Sanal",background="#f6f566")
a.grid(row=5,column=6)
a = ttk.Label(etkinlik, text="Harf",background="#bee96a")
a.grid(row=7,column=6)
a = ttk.Label(etkinlik, text="Harf",background="#bee96a")
a.grid(row=8,column=6)
a = ttk.Label(etkinlik, text="Vadi",background="#e897a9")
a.grid(row=9,column=6)
a = ttk.Label(etkinlik, text="Vadi",background="#e897a9")
a.grid(row=10,column=6)
a = ttk.Label(etkinlik, text="Sanal",background="#f6f566")
a.grid(row=11,column=6)
a= ttk.Label(etkinlik, text="Pazar",background="#f4c679")
a.grid(row=0,column=7)
a = ttk.Label(etkinlik, text="Vadi",background="#e897a9")
a.grid(row=1,column=7)
a = ttk.Label(etkinlik, text="Vadi",background="#e897a9")
a.grid(row=2,column=7)
a = ttk.Label(etkinlik, text="Harf",background="#bee96a")
a.grid(row=3,column=7)
a = ttk.Label(etkinlik, text="Harf",background="#bee96a")
a.grid(row=4,column=7)
a = ttk.Label(etkinlik, text="Sanal",background="#f6f566")
a.grid(row=5,column=7)
a = ttk.Label(etkinlik, text="Sanal",background="#f6f566")
a.grid(row=6,column=7)
a = ttk.Label(etkinlik, text="Vadi",background="#e897a9")
a.grid(row=7,column=7)
a = ttk.Label(etkinlik, text="Vadi",background="#e897a9")
a.grid(row=8,column=7)
a = ttk.Label(etkinlik, text="Harf",background="#bee96a")
a.grid(row=9,column=7)
a = ttk.Label(etkinlik, text="Harf",background="#bee96a")
a.grid(row=10,column=7)
a = ttk.Label(etkinlik, text="----")
a.grid(row=5,column=1)
a = ttk.Label(etkinlik, text="----")
a.grid(row=6,column=1)
a = ttk.Label(etkinlik, text="----")
a.grid(row=11,column=1)
a = ttk.Label(etkinlik, text="----")
a.grid(row=5,column=2)
a = ttk.Label(etkinlik, text="----")
a.grid(row=6,column=2)
a = ttk.Label(etkinlik, text="----")
a.grid(row=5,column=3)
a = ttk.Label(etkinlik, text="----")
a.grid(row=6,column=3)
a = ttk.Label(etkinlik, text="----")
a.grid(row=5,column=4)
a = ttk.Label(etkinlik, text="-----")
a.grid(row=6,column=4)
a = ttk.Label(etkinlik, text="-----")
a.grid(row=5,column=5)
a = ttk.Label(etkinlik, text="-----")
a.grid(row=6,column=5)
a = ttk.Label(etkinlik, text="-----")
a.grid(row=7,column=5)
a = ttk.Label(etkinlik, text="-----")
a.grid(row=11,column=2)
a = ttk.Label(etkinlik, text="-----")
a.grid(row=11,column=3)
a = ttk.Label(etkinlik, text="-----")
a.grid(row=11,column=4)
a = ttk.Label(etkinlik, text="-----")
a.grid(row=11,column=7)
a = ttk.Label(etkinlik, text="-----")
a.grid(row=6,column=6)


def pencereyiKapat():
    g=0
    pencere.quit()

def etkinlikSaati():
    noelEtkinligiUyari = ttk.Label(pencere, text= "")
    noelEtkinligiUyari.place(x=125, y=350)
    etkinlikUyari = ttk.Label(pencere, text= "Aktif Etkinlik Yok")
    etkinlikUyari.place(x=100, y=310)
    sonrakiEtkinlik = ttk.Label(pencere, text= "Sonraki Etkinlik: ")
    sonrakiEtkinlik.place(x=0,y=330)
    aaa = ttk.Label(pencere, text= "Şuanki Etkinlik: ")
    aaa.place(x=0,y=310)
    sonrakiEtkinlik1 = ttk.Label(pencere, text= "")
    sonrakiEtkinlik1.place(x=100,y=330)
    saatLabel = ttk.Label(pencere, text= "00.00.00.00")
    saatLabel.place(x=130, y=290)
    kapat = ttk.Button(pencere, text="Kapat", command=pencereyiKapat)
    kapat.pack(side=BOTTOM)
    gunler=[(0,"Pazartesi"),(1,"Salı"),(2,"Çarşamba"),(3,"Perşembe"),(4,"Cuma"),(5,"Cumartesi"),(6,"Pazar")]
    g = 1
    try:
        while g==1:
            try:
                epoch = time.gmtime(time.time())
                saat = epoch.tm_hour+3
                saat1 = epoch.tm_hour+3
                dakika = epoch.tm_min
                saniye = epoch.tm_sec
                gun = epoch.tm_wday
                if saniye>=60:
                    dakika = dakika +1
                    saniye = saniye-60
                if dakika>=60:
                    saat=saat+1
                    dakika=dakika-60
                if saat>=24:
                    saat=saat-24
                    
                for a,b in gunler:
                    if int(gun)==int(a):
                        gunlerden = b
                        if saat1>=24:
                            gunlerden= gunler[a+1]
                            gunlerden = gunlerden[1]
                        break
                
                        
                saatLabel["text"] = "{}: {}:{}:{}".format(gunlerden,saat,dakika,saniye)
                time.sleep(1)
                #### Noel Etkiniği İçin ###
                if saat>=1 and saat<10:
                    noelEtkinligiUyari.config(text = "10.00/12.00  Yılbaşı Etkinliği",background="#f44949")
                elif saat>=10 and saat<12:
                    noelEtkinligi = "Noel Etkinliği"
                    noelEtkinligiUyari.config(text = "10.00/12.00  Yılbaşı Etkinliği Aktif",background="#88e737")
                elif saat>=12 and saat<17:
                    noelEtkinligiUyari.config(text = "17.00/19.00  Yılbaşı Etkinliği",background="#f44949")
                elif saat>=17 and saat<19:
                    noelEtkinligi = "Noel Etkinliği"
                    noelEtkinligiUyari.config(text = "17.00/19.00  Yılbaşı Etkinliği Aktif",background="#88e737")
                elif saat>=19 and saat<23:
                    noelEtkinligiUyari.config(text = "23.00/01.00  Yılbaşı Etkinliği",background="#f44949")
                elif saat1>=23 and saat1<25:
                    noelEtkinligi = "Noel Etkinliği"
                    noelEtkinligiUyari.config(text = "23.00/01.00  Yılbaşı Etkinliği Aktif",background="#88e737")
                else:
                    noelEtkinligi = "Noel Etkinliği"
                    noelEtkinligiUyari.config(text = "Yılbaşı Etkinliği Aktif",background="#e897a9")
                #### Pazar Günü İçin ####
                if gunlerden == "Pazar":
                    if (saat>=13 and saat<15) or (saat>=19 and saat<21):
                        suankiEtkinlik = "Yeşil Vadi Etkinliği"
                        etkinlikUyari.config(text = "Yeşil Vadi Etkinliği Aktif",background="#e897a9")
                    elif (saat>=15 and saat <17) or (saat>=21 and saat<23):
                        suankiEtkinlik = "Harf Etkinliği"
                        etkinlikUyari.config(text = "Harf Etkinliği Aktif",background="#bee96a")
                    elif (saat>=17 and saat <19 and gunlerden=="Pazar"):
                        suankiEtkinlik = "Sanal Evren Etkinliği"
                        etkinlikUyari.config(text = "Sanal Evren Etkinliği Aktif",background="#f6f566")
                    else:
                        etkinlikUyari.config(text = "Aktif Etkinlik Yok")
                    if saat<13:
                        sonrakiEtkinlik1.config(text = "13.00/15.00  Yeşil Vadi Etkinliği",background="#e897a9")
                    elif saat>=13 and saat<15:
                        sonrakiEtkinlik1.config(text = "15.00/17.00  Harf Etkinliği",background="#bee96a")
                    elif saat>=15 and saat<17:
                        sonrakiEtkinlik1.config(text = "17.00/19.00  Sanal Evren Etkinliği",background="#f6f566")
                    elif saat>=17 and saat<19:
                        sonrakiEtkinlik1.config(text = "19.00/21.00  Yeşil Vadi Etkinliği",background="#e897a9")
                    elif saat>=19 and saat<21:
                        sonrakiEtkinlik1.config(text = "21.00/23.00  Harf Etkinliği",background="#bee96a")
                    elif saat1>=21:
                        sonrakiEtkinlik1.config(text = "Pazartesi 13.00/15.00  Harf Etkinliği",background="#bee96a")
                #### Pazartesi Günü İçin ####
                elif gunlerden == "Pazartesi":
                    if (saat>=13 and saat<15):
                        suankiEtkinlik = "Harf Etkinliği"
                        etkinlikUyari.config(text = "Harf Etkinliği Aktif",background="#bee96a")
                    elif (saat>=15 and saat <16) or (saat>=19 and saat<22):
                        suankiEtkinlik = "Kusursuz Sandık Etkinliği"
                        etkinlikUyari.config(text = "Kusursuz Sandık Etkinliği Aktif",background="#aafaf7")
                    elif (saat>=16 and saat <17) or (saat>=22 and saat <23):
                        suankiEtkinlik = "Sanal Evren Etkinliği"
                        etkinlikUyari.config(text = "Sanal Evren Etkinliği Aktif",background="#f6f566")
                    else:
                        etkinlikUyari.config(text = "Aktif Etkinlik Yok")
                    if saat<13:
                        sonrakiEtkinlik1.config(text = "13.00/15.00  Harf Etkinliği",background="#bee96a")
                    elif saat>=13 and saat<15:
                        sonrakiEtkinlik1.config(text = "15.00/16.00  Kusursuz Sandık Etkinliği",background="#aafaf7")
                    elif saat>=15 and saat<16:
                        sonrakiEtkinlik1.config(text = "16.00/17.00  Sanal Evren Etkinliği",background="#f6f566")
                    elif saat>=16 and saat<19:
                        sonrakiEtkinlik1.config(text = "19.00/22.00  Kusursuz Sandık Etkinliği",background="#aafaf7")
                    elif saat>=19 and saat<22:
                        sonrakiEtkinlik1.config(text = "22.00/23.00  Sanal Evren Etkinliği",background="#f6f566")
                    elif saat1>=22:
                        sonrakiEtkinlik1.config(text = "Salı 13.00/15.00  Yeşil Vadi Etkinliği",background="#e897a9")
                #### Salı Günü İçin ####
                if gunlerden == "Salı":
                    if (saat>=13 and saat<15) or (saat>=19 and saat<21):
                        suankiEtkinlik = "Yeşil Vadi Etkinliği"
                        etkinlikUyari.config(text = "Yeşil Vadi Etkinliği Aktif",background="#e897a9")
                    elif (saat>=15 and saat <16) or (saat>=21 and saat<22):
                        suankiEtkinlik = "Harf Etkinliği"
                        etkinlikUyari.config(text = "Harf Etkinliği Aktif",background="#bee96a")
                    elif (saat>=16 and saat <17) or (saat>=22 and saat <23):
                        suankiEtkinlik = "Sanal Evren Etkinliği"
                        etkinlikUyari.config(text = "Sanal Evren Etkinliği Aktif",background="#f6f566")
                    else:
                        etkinlikUyari.config(text = "Aktif Etkinlik Yok")
                    if saat<13:
                        sonrakiEtkinlik1.config(text = "13.00/15.00  Yeşil Vadi Etkinliği",background="#e897a9")
                    elif saat>=13 and saat<15:
                        sonrakiEtkinlik1.config(text = "15.00/16.00  Harf Etkinliği",background="#bee96a")
                    elif saat>=15 and saat<16:
                        sonrakiEtkinlik1.config(text = "16.00/17.00  Sanal Evren Etkinliği",background="#f6f566")
                    elif saat>=16 and saat<19:
                        sonrakiEtkinlik1.config(text = "19.00/21.00  Yeşil Vadi Etkinliği",background="#e897a9")
                    elif saat>=19 and saat<21:
                        sonrakiEtkinlik1.config(text = "21.00/22.00  Harf Etkinliği",background="#bee96a")
                    elif saat>=21 and saat<22:
                        sonrakiEtkinlik1.config(text = "22.00/23.00  Sanal Evren Etkinliği",background="#f6f566")
                    elif saat1>=22:
                        sonrakiEtkinlik1.config(text = "Çarşamba 13.00/16.00  Kusursuz Sandık Etkinliği",background="#aafaf7")
                #### Çarşamba Günü İçin ####
                if gunlerden =="Çarşamba":
                    if (saat>=13 and saat <16) or (saat>=21 and saat<22):
                        suankiEtkinlik = "Kusursuz Sandık Etkinliği"
                        etkinlikUyari.config(text = "Kusursuz Sandık Etkinliği Aktif",background="#aafaf7")
                    elif (saat>=19 and saat <21):
                        suankiEtkinlik = "Harf Etkinliği"
                        etkinlikUyari.config(text = "Harf Etkinliği Aktif",background="#bee96a")
                    elif (saat>=16 and saat <17) or (saat>=22 and saat <23):
                        suankiEtkinlik = "Sanal Evren Etkinliği"
                        etkinlikUyari.config(text = "Sanal Evren Etkinliği Aktif",background="#f6f566")
                    else:
                        etkinlikUyari.config(text = "Aktif Etkinlik Yok")
                    if saat<13:
                        sonrakiEtkinlik1.config(text = "13.00/16.00  Kusursuz Sandık Etkinliği",background="#aafaf7")
                    elif saat>=13 and saat<16:
                        sonrakiEtkinlik1.config(text = "16.00/17.00  Sanal Evren Etkinliği",background="#f6f566")
                    elif saat>=16 and saat<19:
                        sonrakiEtkinlik1.config(text = "19.00/21.00  Harf Etkinliği",background="#bee96a")
                    elif saat>=19 and saat<21:
                        sonrakiEtkinlik1.config(text = "21.00/22.00  Kusursuz Sandık Etkinliği",background="#aafaf7")
                    elif saat>=21 and saat<22:
                        sonrakiEtkinlik1.config(text = "22.00/23.00  Sanal Evren Etkinliği",background="#f6f566")
                    elif saat1>=22:
                        sonrakiEtkinlik1.config(text = "Perşembe 13.00/14.00  Harf Etkinliği",background="#bee96a")
                #### Perşembe Günü İçin ####
                if gunlerden=="Perşembe":
                    if (saat>=13 and saat <14) or (saat>=19 and saat<20):
                        suankiEtkinlik = "Harf Etkinliği"
                        etkinlikUyari.config(text = "Harf Etkinliği Aktif",background="#bee96a")
                    elif (saat>=14 and saat<16) or (saat>=20 and saat<22):
                        suankiEtkinlik = "Yeşil Vadi Etkinliği"
                        etkinlikUyari.config(text = "Yeşil Vadi Etkinliği Aktif",background="#e897a9")
                    elif (saat>=16 and saat <17) or (saat>=22 and saat <23):
                        suankiEtkinlik = "Sanal Evren Etkinliği"
                        etkinlikUyari.config(text = "Sanal Evren Etkinliği Aktif",background="#f6f566")
                    else:
                        etkinlikUyari.config(text = "Aktif Etkinlik Yok")
                    if saat<13:
                        sonrakiEtkinlik1.config(text = "13.00/14.00  Harf Etkinliği",background="#bee96a")
                    elif saat>=13 and saat<14:
                        sonrakiEtkinlik1.config(text = "14.00/16.00  Yeşil Vadi Etkinliği",background="#e897a9")
                    elif saat>=14 and saat<16:
                        sonrakiEtkinlik1.config(text = "16.00/17.00  Sanal Evren Etkinliği",background="#f6f566")
                    elif saat>=16 and saat<19:
                        sonrakiEtkinlik1.config(text = "19.00/20.00  Harf Etkinliği",background="#bee96a")
                    elif saat>=19 and saat<20:
                        sonrakiEtkinlik1.config(text = "20.00/22.00  Yeşil Vadi Etkinliği",background="#e897a9")
                    elif saat>=20 and saat<22:
                        sonrakiEtkinlik1.config(text = "22.00/23.00  Sanal Evren Etkinliği",background="#f6f566")
                    elif saat>=22:
                        sonrakiEtkinlik1.config(text = "Cuma 13.00/15.00  Harf Etkinliği",background="#bee96a")
                #### Cuma Günü İçin ####
                if gunlerden=="Cuma":
                    if (saat>=13 and saat <15):
                        suankiEtkinlik = "Harf Etkinliği"
                        etkinlikUyari.config(text = "Harf Etkinliği Aktif",background="#bee96a")
                    elif (saat>=15 and saat <16) or (saat>=20 and saat<23):
                        suankiEtkinlik = "Kusursuz Sandık Etkinliği"
                        etkinlikUyari.config(text = "Kusursuz Sandık Etkinliği Aktif",background="#aafaf7")
                    elif (saat>=16 and saat <17) or (saat>=23 and saat1<24):
                        suankiEtkinlik = "Sanal Evren Etkinliği"
                        etkinlikUyari.config(text = "Sanal Evren Etkinliği Aktif",background="#f6f566")
                    else:
                        etkinlikUyari.config(text = "Aktif Etkinlik Yok")
                    if saat<13:
                        sonrakiEtkinlik1.config(text = "13.00/15.00  Harf Etkinliği",background="#bee96a")
                    elif saat>= 13 and saat<15:
                        sonrakiEtkinlik1.config(text = "15.00/16.00  Kusursuz Sandık Etkinliği",background="#aafaf7")
                    elif saat>=15 and saat<16:
                        sonrakiEtkinlik1.config(text = "16.00/17.00  Sanal Evren Etkinliği",background="#f6f566")
                    elif saat>=16 and saat<20:
                        sonrakiEtkinlik1.config(text = "20.00/23.00  Kusursuz Sandık Etkinliği",background="#aafaf7")
                    elif saat>=20 and saat<23:
                        sonrakiEtkinlik1.config(text = "23.00/24.00  Sanal Evren Etkinliği",background="#f6f566")
                    elif saat>=23:
                        sonrakiEtkinlik1.config(text = "Cumartesi 13.00/15.00  Harf Etkinliği",background="#bee96a")
                #### Cumartesi Günü İçin ####
                if gunlerden=="Cumartesi":
                    if (saat>=13 and saat <15) or (saat>=19 and saat<21):
                        suankiEtkinlik = "Harf Etkinliği"
                        etkinlikUyari.config(text = "Harf Etkinliği Aktif",background="#bee96a")
                    elif (saat>=15 and saat<17) or (saat>=21 and saat<23):
                        suankiEtkinlik = "Yeşil Vadi Etkinliği"
                        etkinlikUyari.config(text = "Yeşil Vadi Etkinliği Aktif",background="#e897a9")
                    elif (saat>=17 and saat <18) or (saat>=23 and saat1<24):
                        suankiEtkinlik = "Sanal Evren Etkinliği"
                        etkinlikUyari.config(text = "Sanal Evren Etkinliği Aktif",background="#f6f566")
                    else:
                        etkinlikUyari.config(text = "Aktif Etkinlik Yok")
                    if saat<13:
                        sonrakiEtkinlik1.config(text = "13.00/15.00  Harf Etkinliği",background="#bee96a")
                    elif saat>=13 and saat<15:
                        sonrakiEtkinlik1.config(text = "15.00/17.00  Yeşil Vadi Etkinliği",background="#e897a9")
                    elif saat>=15 and saat<17:
                        sonrakiEtkinlik1.config(text = "17.00/18.00  Sanal Evren Etkinliği",background="#f6f566")
                    elif saat>=17 and saat<19:
                        sonrakiEtkinlik1.config(text = "19.00/21.00  Harf Etkinliği",background="#bee96a")
                    elif saat>=19 and saat<21:
                        sonrakiEtkinlik1.config(text = "21.00/23.00  Yeşil Vadi Etkinliği",background="#e897a9")
                    elif saat>=21 and saat<23:
                        sonrakiEtkinlik1.config(text = "23.00/24.00  Sanal Evren Etkinliği",background="#f6f566")
                    elif saat>=23:
                        sonrakiEtkinlik1.config(text = "Pazar 13.00/15.00  Yeşil Vadi Etkinliği",background="#e897a9")
                #############################
                if g==0:
                    break
                    pencere.quit()
            except:
                break
    except:
        print("Hata")
        

    
    
t10 = threading.Thread(target=etkinlikSaati)
t10.start()

########################################################################################################

pencere.resizable(width = False, height = False)
pencere.mainloop()
