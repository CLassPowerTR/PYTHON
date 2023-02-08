import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set()
plt.style.use("fivethirtyeight")

url = ("https://raw.githubusercontent.com/CLassPowerTR/R/main/Tum_Yillarin_Araba_Satis_Sayilari.txt")
data = pd.read_csv(url)


print(data)
print("***************************************************\n")
print(data.describe())
print("***************************************************\n")
print(data.var())
print("***************************************************\n")
df=data.groupby(["Toplam"])
df=df[["Ocak", "Subat", "Mart"]]
print(df)
print("***************************************************\n")




def Grafik():
    g = sns.catplot("YIL", "Toplam", data=data.head(12), kind="box")
    g.set_axis_labels("Yıllar", "Toplam Satış /1000")
    plt.title("Yıllara Göre Toplam Araç Satış Miktarı")
    plt.show()
Grafik()

def dagilimGrafigi():
    plt.style.use("seaborn-whitegrid")
    x = data["YIL"].head(12)
    y = data["Ocak"].head(12) * 1000
    plt.xlabel("Yıllar")
    plt.ylabel("Ocak Ayındaki Toplam Satış Sayısı")
    plt.title("Dagılım Grafiği")
    plt.plot(x, y, "o")
    plt.show()
dagilimGrafigi()

def kumulatifCizgiGrafigi():
    plt.plot(data["YIL"], data["Ocak"].cumsum() * 1000, "--", label="Ocak")
    plt.plot(data["YIL"], data["Subat"].cumsum() * 1000, "--", label="Subat")
    plt.plot(data["YIL"], data["Mart"].cumsum() * 1000, label="Mart")
    plt.plot(data["YIL"], data["Nisan"].cumsum() * 1000, label="Nisan")
    plt.plot(data["YIL"], data["Mayis"].cumsum() * 1000, "--", label="Mayıs")
    plt.plot(data["YIL"], data["Haziran"].cumsum() * 1000, label="Haziran")
    plt.plot(data["YIL"], data["Temmuz"].cumsum() * 1000, label="Temmuz")
    plt.plot(data["YIL"], data["Agustos"].cumsum()* 1000, label="Ağustos")
    plt.plot(data["YIL"], data["Eylul"].cumsum() * 1000, label="Eylül")
    plt.plot(data["YIL"], data["Ekim"].cumsum() * 1000, label="Ekim")
    plt.plot(data["YIL"], data["Kasim"].cumsum() * 1000, label="Kasım")
    plt.plot(data["YIL"], data["Aralik"].cumsum() * 1000, "--", label="Aralık")
    plt.legend(loc="best")
    plt.xlabel("Yıllar")
    plt.ylabel("Satış Miktarı")
    plt.title("Kümülatif Çizgi Grafiği")
    plt.show()
kumulatifCizgiGrafigi()

def cizgiGrafigi():
    veri = pd.read_csv(url)
    x = veri["YIL"].head(12)
    y = veri["Aralik"].head(12) * 1000
    plt.xlabel("Yıllar")
    plt.ylabel("Aralık Ayındaki Satışlar")
    plt.title("Yıllara Göre Aralık Ayındaki Satışlar")
    plt.plot(x, y)
    plt.show()
cizgiGrafigi()

def barGrafigi():
    plt.style.use("fivethirtyeight")
    plt.figure()
    plt.axes()
    plt.plot(data["YIL"].head(12), data["Ocak"].head(12) * 1000, "--",label="Ocak")
    plt.plot(data["YIL"].head(12), data["Subat"].head(12) * 1000, "--", label="Subat")
    plt.plot(data["YIL"].head(12), data["Mart"].head(12) * 1000, label="Mart")
    plt.plot(data["YIL"].head(12), data["Nisan"].head(12) * 1000, label="Nisan")
    plt.plot(data["YIL"].head(12), data["Mayis"].head(12) * 1000, "--", label="Mayıs")
    plt.plot(data["YIL"].head(12), data["Haziran"].head(12) * 1000, label="Haziran")
    plt.plot(data["YIL"].head(12), data["Temmuz"].head(12) * 1000, label="Temmuz")
    plt.plot(data["YIL"].head(12), data["Agustos"].head(12) * 1000, label="Ağustos")
    plt.plot(data["YIL"].head(12), data["Eylul"].head(12) * 1000, label="Eylül")
    plt.plot(data["YIL"].head(12), data["Ekim"].head(12) * 1000, label="Ekim")
    plt.plot(data["YIL"].head(12), data["Kasim"].head(12) * 1000, label="Kasım")
    plt.plot(data["YIL"].head(12), data["Aralik"].head(12) * 1000, "--", label="Aralık")
    plt.legend()
    plt.title("Aylara Göre Satış Miktarı")
    plt.xlabel("Yıllar")
    plt.ylabel("Satış Miktarı")
    plt.show()
barGrafigi()

def histogramGrafigi():
    plt.style.use("ggplot")
    veri1 = data[["Ocak", "Subat", "Mart", "Nisan", "Mayis", "Haziran", "Temmuz", "Agustos", "Eylul", "Ekim", "Kasim", "Aralik"]] * 1000
    ortanca = np.median(veri1)
    plt.axvline(ortanca, color="red")
    plt.hist(veri1.head(12), facecolor="blue", alpha=0.5)
    plt.show()
histogramGrafigi()

def kutuGrafigi():
    red_square = dict(markerfacecolor='r', marker='s')
    fig1, ax1 = plt.subplots()
    ax1.set_title('Toplam Araç Satış Kutu Grafiği')
    ax1.boxplot(data["Toplam"], vert=False, flierprops=red_square)
    plt.show()
kutuGrafigi()

def pastaGrafigi():
    yillar = data["YIL"].tail(10)
    veri = data["Toplam"].tail(10)
    plt.figure()
    highlight = (0, 0, 0.1, 0.2, 0.1, 0, 0, 0, 0, 0)
    plt.pie(veri, labels=yillar, startangle=90, shadow=True, autopct='%1.1f%%', explode=highlight)
    plt.title("Yıllara Göre Toplam Satış")
    plt.show()
pastaGrafigi()
