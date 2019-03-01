import pandas as pd
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import Label
from tkinter import messagebox
from tkinter import Entry
from tkinter import Button, BOTTOM
from tkinter.ttk import Combobox

class grafik_olustur():
    
    def __init__(self, master):
        

        firma_adi = Label(master, text="Firma Adı:")
        firma_adi.place(x=130,y=20)

        arama = Label(master, text="Ara:")
        arama.place(x=10,y=20)
        def on_keyrelease(event):
            value = event.widget.get()
            value = value.strip().lower()

            if value == '':
                data = test_list
            else:
                data = []
                for item in test_list:
                    if value in item.lower():
                        data.append(item)
            listbox_update(data)

        def listbox_update(data):
            self.firm.delete(0, 'end')
            data = sorted(data, key=str.lower)
            for item in data:
                self.firm.insert('end', item)

        firmalar_oku = open("firmalar.csv", "r")
        self.firmalar = firmalar_oku.readlines()
        test_list = self.firmalar

        entry =Entry(master)
        entry.place(x=10,y=40)
        entry.bind('<KeyRelease>', on_keyrelease)

        self.firm = Combobox(master)
        self.firm["values"] = test_list
        self.firm.set("TÜMÜ")
        self.firm.bind('<KeyRelease>', on_keyrelease)
        self.firm.place(x=100,y=40)


        """
        bitis_tarih_buton = Button(grafik_penceresi, text="Seçiniz")
        bitis_tarih_buton.place(x=150, y=160)
        """
        self.pos_oranimiz = format(float(open("hesap_dosyalari/pos_orani.txt","r").readlines()[0]),".4f")
        hesapla_buton = Button(master, text="Hesapla", bd=2)
        hesapla_buton.bind("<Button-1>", self.grafikler_getir)
        hesapla_buton.pack(side=BOTTOM)
        
        hes_lablari=Label(master, text="Lütfen Hesaplanmasını İstediğiniz Alanları Seçiniz:", fg="blue")
        hes_lablari.place(x=20,y=80)

        self.c_mal_al = IntVar()
        mal_al_c=Checkbutton(master,activebackground="green", variable=self.c_mal_al, onvalue=1, offvalue=0, text="Mal ve Hizmet Alımı")
        mal_al_c.place(x=20, y=100)
        self.c_kas_od = IntVar()
        kas_od_c=Checkbutton(master,activebackground="green", variable=self.c_kas_od, onvalue=1, offvalue=0, text="Kasadan Ödeme")
        kas_od_c.place(x=20, y=160)
        self.c_kasd_od = IntVar()
        kasd_od_c=Checkbutton(master,activebackground="green", variable=self.c_kasd_od, onvalue=1, offvalue=0, text="Kasa Dışı Ödeme")
        kasd_od_c.place(x=20, y=140)
        self.c_kas_al = IntVar()
        kas_al_c=Checkbutton(master,activebackground="green", variable=self.c_kas_al, onvalue=1, offvalue=0, text="Kasadan Alınan Miktar")
        kas_al_c.place(x=20, y=220)
        self.c_yap_od = IntVar()
        yap_od_c=Checkbutton(master,activebackground="green", variable=self.c_yap_od, onvalue=1, offvalue=0, text="Yapılacak Ödeme")
        yap_od_c.place(x=20, y=180)
        self.c_pos_gun = IntVar()
        pos_gun_c=Checkbutton(master,activebackground="green", variable=self.c_pos_gun, onvalue=1, offvalue=0, text="Pos Gün Sonu")
        pos_gun_c.place(x=20, y=200)
        self.c_gid = IntVar()
        gid_c=Checkbutton(master,activebackground="green", variable=self.c_gid, onvalue=1, offvalue=0, text="Gider")
        gid_c.place(x=20, y=120)
        self.c_al_od = IntVar()
        al_od_c=Checkbutton(master,activebackground="green", variable=self.c_al_od, onvalue=1, offvalue=0, text="Alınan Ödeme")
        al_od_c.place(x=20, y=240)
        self.c_alin_od = IntVar()
        alin_od_c=Checkbutton(master,activebackground="green", variable=self.c_alin_od, onvalue=1, offvalue=0, text="Alınacak Ödeme")
        alin_od_c.place(x=20, y=260)

        
    def grafikler_getir(self, Event):
        #işlem dosyaları
        yapilacak_odeme = pd.read_csv("hesap_dosyalari/yapilacak_odeme.csv",header=None,encoding = "ISO-8859-1")
        kasadan_odeme = pd.read_csv("hesap_dosyalari/kasadan_odeme.csv",header=None,encoding = "ISO-8859-1")
        kasadisi_odeme = pd.read_csv("hesap_dosyalari/kasadisi_odeme.csv",header=None,encoding = "ISO-8859-1")
        gider = pd.read_csv("hesap_dosyalari/gider.csv",header=None,encoding = "ISO-8859-1")
        kasadan_alinan = pd.read_csv("hesap_dosyalari/kasadan_alinan.csv",header=None,encoding = "ISO-8859-1")
        pos_gun_sonu = pd.read_csv("hesap_dosyalari/pos_gun_sonu.csv",header=None,encoding = "ISO-8859-1")
        alinan_odeme = pd.read_csv("hesap_dosyalari/odeme_al.csv",header=None,encoding = "ISO-8859-1")
        alinacak_odeme = pd.read_csv("hesap_dosyalari/alinacak_odeme.csv",header=None,encoding = "ISO-8859-1")
        kardos = pd.read_csv("hesap_dosyalari/karsilik_dosyasi.csv",header=None,encoding = "ISO-8859-1")

        yapilacak_odeme[0] = pd.to_datetime(yapilacak_odeme[0], errors='coerce')
        kasadan_odeme[0] = pd.to_datetime(kasadan_odeme[0], errors='coerce')
        kasadisi_odeme[0] = pd.to_datetime(kasadisi_odeme[0], errors='coerce')
        gider[0] = pd.to_datetime(gider[0], errors='coerce')
        kasadan_alinan[0] = pd.to_datetime(kasadan_alinan[0], errors='coerce')
        pos_gun_sonu[0] = pd.to_datetime(pos_gun_sonu[0], errors='coerce')
        alinan_odeme[0] = pd.to_datetime(alinan_odeme[0], errors='coerce')
        alinacak_odeme[0] = pd.to_datetime(alinacak_odeme[0], errors='coerce')
        kardos[0] = pd.to_datetime(kardos[0], errors='coerce')
        
        #sonuçları içine yazdırmak ve sonradan pencereye eklemek için bir dosya
        sonuc_dosyası = open("hesap_dosyalari/gecici_sonuc_dosyasi.csv","w") #ekrana yazdırırken read modunda alıp satırlarını oku!

        #işlem için firma adi
        firma = str(self.firm.get())

        #başta bütün toplamlar sıfır, sonra istediklerimizi ekleyip artıracaz...
        yapilacak_odeme_toplam = 0
        kasadan_odeme_toplam = 0
        kasadisi_odeme_toplam = 0
        gider_toplam = 0
        kasadan_alinan_toplam = 0
        pos_gun_sonu_toplam = 0
        alinan_odeme_toplam = 0
        alinacak_odeme_toplam = 0
        karsilik_toplam = 0
        try:
            bitis_tarihi = datetime.datetime.today()
            baslangic_tarihi = datetime.datetime.strptime("26/02/19", "%d/%m/%y")
            #bitis_tarihi =  datetime.datetime.strptime(str(bitis_tarihim), "%y/%m/%d")
            try:
                gun_araligi = str(bitis_tarihi-baslangic_tarihi)
                b = gun_araligi.index("d")
                gun_araligi = gun_araligi[:b]
                gun_araligi = int(gun_araligi) + 1
                ay_araligi = float(gun_araligi/30)
            except ValueError:
                gun_araligi = 1
                ay_araligi = float(gun_araligi/30)
            a=0
            if firma == "TÜMÜ": #tüm firmlar için
                """
                genel_sonuc_dosyasi = open("hesap_dosyalari/genel_sonuc_dosyasi.csv","w")
                while a < gun_araligi:
                    print(baslangic_tarihi)
                    yapilacak_odeme.sort_index()
                    mask = (yapilacak_odeme[0] == baslangic_tarihi)
                    yapilacak_odeme = yapilacak_odeme.loc[mask]
                    print(yapilacak_odeme)
                    print(baslangic_tarihi)
                    for i in yapilacak_odeme.iloc[:,1:2].values:
                        yapilacak_odeme_toplam = yapilacak_odeme_toplam + i
                    mask1 = (kasadan_odeme[0] == baslangic_tarihi)
                    kasadan_odeme = kasadan_odeme.loc[mask1]
                    for i in kasadan_odeme.iloc[:,1:2].values:
                        kasadan_odeme_toplam = kasadan_odeme_toplam + i
                    mask2 = (kasadisi_odeme[0] == baslangic_tarihi)
                    kasadisi_odeme = kasadisi_odeme.loc[mask2]
                    for i in kasadisi_odeme.iloc[:,1:2].values:
                        kasadisi_odeme_toplam = kasadisi_odeme_toplam + i
                    mask3 = (gider[0] == baslangic_tarihi)
                    gider = gider.loc[mask3]
                    for i in gider.iloc[:,1:2].values:
                        gider_toplam = gider_toplam + i
                    mask4 = (kasadan_alinan[0] == baslangic_tarihi)
                    kasadan_alinan = kasadan_alinan.loc[mask4]
                    for i in kasadan_alinan.iloc[:,1:2].values:
                        kasadan_alinan_toplam = kasadan_alinan_toplam + i
                    mask5 = (pos_gun_sonu[0] == baslangic_tarihi)
                    pos_gun_sonu = pos_gun_sonu.loc[mask5]
                    for i in pos_gun_sonu.iloc[:,1:2].values:
                        pos_gun_sonu_toplam = pos_gun_sonu_toplam + i
                    mask6 = (alinan_odeme[0] == baslangic_tarihi)
                    alinan_odeme = alinan_odeme.loc[mask6]
                    for i in alinan_odeme.iloc[:,1:2].values:
                        alinan_odeme_toplam = alinan_odeme_toplam + i
                    
                    toplam_ciro = float(kasadan_alinan_toplam + kasadan_odeme_toplam + pos_gun_sonu_toplam - (pos_gun_sonu_toplam*float(self.pos_oranimiz)) + alinan_odeme_toplam)
                    toplam_odeme = float(kasadan_odeme_toplam + kasadisi_odeme_toplam)
                    kasa_brut = float(toplam_ciro - toplam_odeme)
                    kasa_net = float(kasa_brut - gider_toplam)
                    genel_sonuc_dosyasi.write("Toplam Ciro, " + str(baslangic_tarihi.date())+","+str(toplam_ciro)+"\n")
                    genel_sonuc_dosyasi.write("Toplam Odeme, " + str(baslangic_tarihi.date())+","+str(toplam_odeme)+"\n")
                    genel_sonuc_dosyasi.write("Kasa Brut, " + str(baslangic_tarihi.date())+","+str(kasa_brut)+"\n")
                    genel_sonuc_dosyasi.write("Kasa Net, " + str(baslangic_tarihi.date())+","+str(kasa_net)+"\n")
                    baslangic_tarihi += datetime.timedelta(days=1)
                    baslangic_tarihi = pd.Timestamp(baslangic_tarihi.date())
                    print(baslangic_tarihi)
                    
                    a=a+1
                """
                yapilacak_odeme1 = open("hesap_dosyalari/yapilacak_odeme.csv", "r")
                kasadan_odeme1 = open("hesap_dosyalari/kasadan_odeme.csv", "r")
                kasadisi_odeme1 = open("hesap_dosyalari/kasadisi_odeme.csv", "r")
                gider1 = open("hesap_dosyalari/gider.csv", "r")
                kasadan_alinan1 = open("hesap_dosyalari/kasadan_alinan.csv", "r")
                alinan_odeme1 = open("hesap_dosyalari/odeme_al.csv","r")
                alinacak_odeme1 = open("hesap_dosyalari/alinacak_odeme.csv","r")
                kardos1 = open("hesap_dosyalari/karsilik_dosyasi.csv","r")
                pos_gun_sonu1 = open("hesap_dosyalari/pos_gun_sonu.csv", "r")

                gecici_yapilacak_odeme = open("hesap_dosyalari/gecici_yapilacak_odeme.csv", "w")
                gecici_kasadan_odeme = open("hesap_dosyalari/gecici_kasadan_odeme.csv", "w")
                gecici_kasadisi_odeme = open("hesap_dosyalari/gecici_kasadisi_odeme.csv", "w")
                gecici_gider = open("hesap_dosyalari/gecici_gider.csv", "w")
                gecici_kasadan_alinan = open("hesap_dosyalari/gecici_kasadan_alinan.csv", "w")
                gecici_pos_gun_sonu = open("hesap_dosyalari/gecici_pos_gun_sonu.csv", "w")
                gecici_alinan_odeme = open("hesap_dosyalari/gecici_odeme_al.csv","w")
                gecici_alinacak_odeme = open("hesap_dosyalari/gecici_alinacak_odeme.csv","w")
                gecici_karsilik = open("hesap_dosyalari/gecici_karsilik_dosyasi.csv","w")
                #genel_sonuc_dosyasi.close()
                if self.c_yap_od.get()==1:
                    for i in yapilacak_odeme1:
                        hepsi = "Yapilacak Odeme, " + str(i)
                        sonuc_dosyası.write(hepsi)
                        gecici_yapilacak_odeme.write(i)
                else:
                    pass
                if  self.c_kas_od.get()==1:
                    for i in kasadan_odeme1:
                        hepsi = "Kasadan Odeme, " + str(i)
                        sonuc_dosyası.write(hepsi)
                        gecici_kasadan_odeme.write(i)
                else:
                    pass
                if self.c_kasd_od.get()==1:
                    for i in kasadisi_odeme1:
                        hepsi = "Kasa Disi Odeme, " + str(i)
                        sonuc_dosyası.write(hepsi)
                        gecici_kasadisi_odeme.write(i)
                else:
                    pass
                if self.c_gid.get()==1:
                    for i in gider1:
                        hepsi = "Gider, " + str(i)
                        sonuc_dosyası.write(hepsi)
                        gecici_gider.write(i)
                else:
                    pass
                if self.c_kas_al.get()==1:
                    for i in kasadan_alinan1:
                        hepsi = "Kasadan Alinan, " + str(i)
                        sonuc_dosyası.write(hepsi)
                        gecici_kasadan_alinan.write(i)
                else:
                    pass
                if self.c_al_od.get()==1:
                    for i in alinan_odeme1:
                        hepsi = "Alinan Odeme, " + str(i)
                        sonuc_dosyası.write(hepsi)
                        gecici_alinan_odeme.write(i)
                else:
                    pass
                if self.c_alin_od.get()==1:
                    for i in alinacak_odeme1:
                        hepsi = "Alinacak Odeme, " + str(i)
                        sonuc_dosyası.write(hepsi)
                        gecici_alinacak_odeme.write(i)
                else:
                    pass
                if self.c_mal_al.get()==1:
                    for i in kardos1:
                        hepsi = "Mal ve Hizmet Alimi, " + str(i)
                        sonuc_dosyası.write(hepsi)
                        gecici_karsilik.write(i)
                else:
                    pass
                if self.c_pos_gun.get()==1:
                    for i in pos_gun_sonu1:
                        hepsi = "Pos Gun Sonu, " + str(i)
                        sonuc_dosyası.write(hepsi)
                        gecici_pos_gun_sonu.write(i)
                else:
                    pass

                sonuc_dosyası.close()
                """
                veri1 = pd.read_csv("hesap_dosyalari/genel_sonuc_dosyasi.csv", header=None,encoding = "ISO-8859-1")
                veri1[1] = pd.to_datetime(veri1[1], errors = 'coerce')
                veri1.sort_values(by=[1], inplace=True, ascending=False)
                veri1=veri1.rename(columns={0: 'Odeme Tipleri'})
                sns.lineplot(data=veri1, x=veri1[1], y=veri1[2], hue=veri1["Odeme Tipleri"])
                """
                veri = pd.read_csv("hesap_dosyalari/gecici_sonuc_dosyasi.csv", header=None,encoding = "ISO-8859-1")
                veri[1] = pd.to_datetime(veri[1], errors = 'coerce')
                veri.sort_values(by=[1], inplace=True, ascending=False)
                veri=veri.rename(columns={0: 'Odeme Tipleri'})
                sns.lineplot(data=veri, x=veri[1], y=veri[2], hue=veri["Odeme Tipleri"])
                plt.title("Sonuç Grafiği")
                plt.xlabel("TARİH")
                plt.ylabel("MİKTAR")
                plt.show()
                
            else: #firma ismine göre

                #burada dosya işlemleri ile yapıyoruz...
                yapilacak_odeme1 = open("hesap_dosyalari/yapilacak_odeme.csv", "r")
                kasadan_odeme1 = open("hesap_dosyalari/kasadan_odeme.csv", "r")
                kasadisi_odeme1 = open("hesap_dosyalari/kasadisi_odeme.csv", "r")
                gider1 = open("hesap_dosyalari/gider.csv", "r")
                kasadan_alinan1 = open("hesap_dosyalari/kasadan_alinan.csv", "r")
                alinan_odeme1 = open("hesap_dosyalari/odeme_al.csv","r")
                alinacak_odeme1 = open("hesap_dosyalari/alinacak_odeme.csv","r")
                kardos1 = open("hesap_dosyalari/karsilik_dosyasi.csv","r")
                pos_gun_sonu1 = open("hesap_dosyalari/pos_gun_sonu.csv", "r")

                gecici_yapilacak_odeme = open("hesap_dosyalari/gecici_yapilacak_odeme.csv", "w")
                gecici_kasadan_odeme = open("hesap_dosyalari/gecici_kasadan_odeme.csv", "w")
                gecici_kasadisi_odeme = open("hesap_dosyalari/gecici_kasadisi_odeme.csv", "w")
                gecici_gider = open("hesap_dosyalari/gecici_gider.csv", "w")
                gecici_kasadan_alinan = open("hesap_dosyalari/gecici_kasadan_alinan.csv", "w")
                gecici_pos_gun_sonu = open("hesap_dosyalari/gecici_pos_gun_sonu.csv", "w")
                gecici_alinan_odeme = open("hesap_dosyalari/gecici_odeme_al.csv","w")
                gecici_alinacak_odeme = open("hesap_dosyalari/gecici_alinacak_odeme.csv","w")
                gecici_kardos = open("hesap_dosyalari/gecici_karsilik_dosyasi.csv","w")

                if self.c_yap_od.get()==1:
                    for i in yapilacak_odeme1:
                        if i.endswith(firma):
                            hepsi = "Yapilacak Odeme, " + str(i)
                            sonuc_dosyası.write(hepsi)
                            gecici_yapilacak_odeme.write(i)
                else:
                    pass
                if self.c_alin_od.get()==1:
                    for i in alinacak_odeme1:
                        if i.endswith(firma):
                            hepsi = "Alinacak Odeme, " + str(i)
                            sonuc_dosyası.write(hepsi)
                            gecici_alinacak_odeme.write(i)
                else:
                    pass
                if self.c_kas_od.get()==1:
                    for i in kasadan_odeme1:
                        if i.endswith(firma):
                            hepsi = "Kasadan Odeme, " + str(i)
                            sonuc_dosyası.write(hepsi)
                            gecici_kasadan_odeme.write(i)
                else:
                    pass
                if self.c_kasd_od.get()==1:
                    for i in kasadisi_odeme1:
                        if i.endswith(firma):
                            hepsi = "Kasa Disi Odeme, " + str(i)
                            sonuc_dosyası.write(hepsi)
                            gecici_kasadisi_odeme.write(i)
                else:
                    pass
                if self.c_gid.get()==1:
                    for i in gider1:
                        if i.endswith(firma):
                            hepsi = "Gider, " + str(i)
                            sonuc_dosyası.write(hepsi)
                            gecici_gider.write(i)
                else:
                    pass
                if self.c_kas_al.get()==1:
                    for i in kasadan_alinan1:
                        if i.endswith(firma):
                            hepsi = "Kasadan Alinan, " + str(i)
                            sonuc_dosyası.write(hepsi)
                            gecici_kasadan_alinan.write(i)
                else:
                    pass
                if self.c_al_od.get()==1:
                    for i in alinan_odeme1:
                        if i.endswith(firma):
                            hepsi = "Alinan Odeme, " + str(i)
                            sonuc_dosyası.write(hepsi)
                            gecici_alinan_odeme.write(i)
                else:
                    pass
                if self.c_mal_al.get()==1:
                    for i in kardos1:
                        if i.endswith(firma):
                            hepsi = "Mal ve Hizmet Alimi, " + str(i)
                            sonuc_dosyası.write(hepsi)
                            gecici_kardos.write(i)
                else:
                    pass
                if self.c_pos_gun.get()==1:
                    for i in pos_gun_sonu1:
                        if i.endswith(firma):
                            hepsi = "Pos Gun Sonu, " + str(i)
                            sonuc_dosyası.write(hepsi)
                            gecici_pos_gun_sonu.write(i)
                else:
                    pass
                sonuc_dosyası.close()
                gecici_kasadan_odeme.close()
                gecici_kasadan_alinan.close()
                gecici_gider.close()
                gecici_kasadisi_odeme.close()
                gecici_pos_gun_sonu.close()
                gecici_yapilacak_odeme.close()
                gecici_alinan_odeme.close()
                gecici_alinacak_odeme.close()
                gecici_kardos.close()
                #BURADA VERİNİN İÇİNDEKİ BİR KOLONDAN TOPLAMLARI ALDIK VE YAZDIRDIK.

                veri = pd.read_csv("hesap_dosyalari/gecici_sonuc_dosyasi.csv",header=None,encoding = "ISO-8859-1")
                veri[1] = pd.to_datetime(veri[1], errors = 'coerce')
                veri.sort_values(by=[1], inplace=True, ascending=False)
                veri=veri.rename(columns={0: 'Odeme Tipleri'})
                sns.lineplot(data=veri, x=veri[1], y=veri[2], hue=veri["Odeme Tipleri"])
                plt.title("{} Sonuç Grafiği".format(firma))
                plt.xlabel("TARİH")
                plt.ylabel("MİKTAR")
                plt.show()
           
        except UnboundLocalError:
            messagebox.showwarning(title="UYARI!", message="Sonuç Bulunamadı!")

