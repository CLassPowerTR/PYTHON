import win32gui, win32ui, win32con, win32api
import cv2
import numpy as np


def CaptureWindows(hwnd):
    # Belirtilen penecere için sol üst ve sağ alt noktalarını koordinatlarını alır.
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    width = right - left
    height = bottom - top
    width = width 
    height = height 
    
    # Belirtilen pencere için bir DC(Device context) örneği oluşturur.
    hwndDC = win32gui.GetWindowDC(hwnd)
    # GetWindowDC tarafından oluşturulan DC'nin bir MFC (Microsoft Foundation Classes) DC'sine dönüştürülmesi.
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    # Bir bitmap için uyumlu bir DC oluşturu
    saveDC = mfcDC.CreateCompatibleDC()
    
    # Windows API'si kullanarak bir Bitmap objesi oluşturur.
    saveBitMap = win32ui.CreateBitmap()
    # Oluşturduğunuz Bitmap objesine, belirlediğiniz mfcDC'nin yükseklik ve genişliğine uygun bir uyumlu bitmap oluşturur.
    saveBitMap.CreateCompatibleBitmap(mfcDC, width, height)
    # saveDC nesnesinin seçtiği nesnenin saveBitMap olmasını sağlar. Bu, görüntüyü saveBitMap nesnesine kaydetmek için 
    # gerekli olan işlemleri gerçekleştirmeyi mümkün kılar.
    saveDC.SelectObject(saveBitMap)
    
    # MFC DC'den uyumlu DC'ye ekran görüntüsünü kopyalar.
    result = saveDC.BitBlt((0, 0), (width, height), mfcDC, (0, 0), win32con.SRCCOPY)

    # Bitmap verilerini alır ve dizi haline getirir.
    bmp_info = saveBitMap.GetInfo()
    bmp_array = np.frombuffer(saveBitMap.GetBitmapBits(True), np.uint8)
    # Bitmap verilerini bir görüntü matrisine dönüştürür.
    img = bmp_array.reshape(bmp_info['bmHeight'], bmp_info['bmWidth'], 4)
    
    # Oluşturulan DC'leri silerek bellek boşaltır.
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    # Alınan DC'nin serbest bırakılması.
    win32gui.ReleaseDC(hwnd, hwndDC)

    return img

def listWindowNames():
    def winEnumHandler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd):
            print("ID=",hwnd, "TitLe= "+'"' + win32gui.GetWindowText(hwnd) + '"')
    win32gui.EnumWindows(winEnumHandler, None)


def ImgBGmatchTemplate(hwnd, image, matchvalue):
    # benzerlik bulmasını istediğimiz resimi bellekte açar ve nump dizisi olarak döndürür. İstediğiniz resim yolunu parametre olarak gönderiniz
    img1 = cv2.imread(image)
    # belirtilen hwnd değerine sahip bir pencereyi yakalamak için. hwnd değerini yakalanmak istenen pencere değerini parametre olarak gönderiniz.
    img2 = CaptureWindows(hwnd)
    
    # Verilen resmin renk uzayını değiştirmek için. verilen görüntü verilerini RGBA formattan RGB formata dönüştürür.
    img1 = cv2.cvtColor(img1,cv2.COLOR_RGB2RGBA)
    img2 = cv2.cvtColor(img2,cv2.COLOR_RGB2RGBA)

    # verilen resimler arasındaki eşleşme oranını ölçmek için kullanılır. Fonksiyona verilen img1 ve img2 numpy dizisi şeklindeki resimler 
    # arasındaki eşleşme oranını verilen yönteme göre ölçer ve sonuç olarak bir numpy dizisi döndürür.
    result = cv2.matchTemplate(img1,img2,cv2.TM_CCOEFF_NORMED)

    # Benzerliğin ne kadar iyi olduğunu belirtmek için, parametre olarak gönderiniz
    matchvalue = matchvalue
    
    # np.array(img1).shape: verilen numpy dizisi olan img1'in boyutunu belirlemek için kullanılan fonksiyon. Shape fonksiyonu boyutları 
    # yükseklik, genişlik, kanal sayısı şeklinde döndürür.
    w,h = np.array(img1).shape[1], np.array(img1).shape[0]
    
    # numpy dizisi olan result içinde verilen matchvalue değerinden büyük olan değerlerin pozisyonunu belirler. 
    # Pozisyonlar (x,y) şeklinde bir numpy dizisi olarak döndürür.
    y,x = np.where(result >= matchvalue)

    #
    if len(x) > 0:
        for (xloc, yloc) in zip(x,y):
            # Eşleşme oranı belirli bir değerin üzerinde olan bölgeleri belirlemek için img2 üzerinde dikdörtgen çizerek belirler. 
            cv2.rectangle(img2,(xloc,yloc),(xloc+w,yloc+h),(0,255,255),2)
    return img2
    
def ImgBGcolorDetection(hwnd,RGB1,RGB2):
    # 'CaptureWindows' fonksiyonu pencerenin ekran görüntüsünü yakalar ve numpy dizisine dönüştürür.
    img = CaptureWindows(hwnd)
    img = np.array(img)
    
    # 'cv2.cvtColor' fonksiyonu BGR formatındaki resmi RGB formatına dönüştürür.
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    
    RGB1.reverse()
    RGB2.reverse()

    RGB1 = np.array(RGB1)
    RGB2 = np.array(RGB2)

    # cv2.inRange fonksiyonu, verilen RGB değerlerinin aralığını belirleyerek resmin bu değerleri içeren piksellerini beyaz,
    # diğer piksellerini ise siyah olarak filtreler.
    result = cv2.inRange(img, RGB1, RGB2) 
    
    #cv2.bitwise_or fonksiyonu resmi ve maskeyi bitwise OR işlemi ile birleştirir ve belirli bir renkte olan nesneleri çıktı olarak verir
    resultral = cv2.bitwise_or(img,img,mask=result) 
    
    return resultral