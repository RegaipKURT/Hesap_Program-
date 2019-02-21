import os
from tkinter import *
from tkinter import messagebox
import pandas as pd
import datetime

tarih = datetime.datetime.now().strftime("%d/%m/%y")
date_now = datetime.datetime.strptime(tarih, "%d/%m/%y")
firmalar_oku = open("firmalar.csv", "r")
odeme_tipleri = ["Yapılacak Ödeme", "Kasadan Yapılan Ödeme", "Kasa Dışı Ödeme","Kasadan Alınan Miktar", "POS Gün Sonu", "Gider", "Ödeme Al"]

pd.options.display.max_rows = None

class giris_pen():

    def __init__(self, master):
        menu = Menu(master)
        pencere.config(menu=menu)

        altmenu = Menu(menu)
        menu.add_cascade(label="File", menu=altmenu)

        altmenu.add_command(label="New")
        altmenu.add_command(label="Save")

        altmenu.add_separator()
        altmenu.add_command(label="Exit", command=quit)

        menu2 = Menu(menu)
        menu.add_cascade(label="Ekle", menu=menu2)
        menu2.add_command(label="Firma Ekle")

        self.status = Label(master, text="Yükleme Başarılı... Hoşgeldiniz... Tarih:{}".format(tarih), bd=1, relief=SUNKEN, anchor="w")
        self.status.pack(side=BOTTOM, fill=X)

        self.islem_buton = Button(master, text="İşlem Girişi", bd=3)
        self.islem_buton.bind("<Button-1>", self.hesap_penceresi)
        self.islem_buton.place(x=169, y = 20)

        self.ekle_buton = Button(master, text="Firma Ekle", bd=3)
        self.ekle_buton.bind("<Button-1>",self.firma_ekle_pen)
        self.ekle_buton.place(x=171, y = 70)

        self.hesap_buton = Button(master, text="Hesap Yap", bd=3)
        self.hesap_buton.bind("<Button-1>", self.hesap_fonk_pen)
        self.hesap_buton.place(x=170, y = 120)

        self.cikis_buton = Button(master, text="Çıkış Yap", bd=3)
        self.cikis_buton.bind("<Button-1>", self.cikis)
        self.cikis_buton.pack(side=BOTTOM)
        self.firmalar = firmalar_oku.readlines()

    def cikis(self, Event):
        self.answer = messagebox.askokcancel(title="Çıkış", message="Emin misiniz?")
        if self.answer == TRUE:
            sys.exit()
        else:
            pass

    def hesap_penceresi(self, Event):
        
        def uyari(Event):
            try:      
                miktar = float(self.miktar_deger.get())
                firma = self.degis_firma.get()
                tip = str(self.degis_odeme.get())
                if tip == "Gider":
                    file = open("hesap_dosyalari/gider.csv", "a")
                    if firma == "ETT":
                        sonuc = str(tarih+","+str(miktar)+",")
                        file.write(sonuc)
                        file.write(firma+"\n")
                        file.close()
                    else:
                        sonuc = str(tarih+","+str(miktar)+",")
                        file.write(sonuc)
                        file.write(firma)
                        file.close()
                
                elif tip == "Yapılacak Ödeme":
                    file = open("hesap_dosyalari/yapilacak_odeme.csv", "a")
                    if firma == "ETT":
                        sonuc = str(tarih+","+str(miktar)+",")
                        file.write(sonuc)
                        file.write(firma+"\n")
                        file.close()
                    else:
                        sonuc = str(tarih+","+str(miktar)+",")
                        file.write(sonuc)
                        file.write(firma)
                        file.close()
                
                elif tip == "Kasadan Yapılan Ödeme":
                    file = open("hesap_dosyalari/kasadan_odeme.csv", "a")
                    if firma == "ETT":
                        sonuc = str(tarih+","+str(miktar)+",")
                        file.write(sonuc)
                        file.write(firma+"\n")
                        file.close()
                    else:
                        sonuc = str(tarih+","+str(miktar)+",")
                        file.write(sonuc)
                        file.write(firma)
                        file.close()
                
                elif tip == "Kasa Dışı Ödeme":
                    file = open("hesap_dosyalari/kasadisi_odeme.csv", "a")
                    if firma == "ETT":
                        sonuc = str(tarih+","+str(miktar)+",")
                        file.write(sonuc)
                        file.write(firma+"\n")
                        file.close()
                    else:
                        sonuc = str(tarih+","+str(miktar)+",")
                        file.write(sonuc)
                        file.write(firma)
                        file.close()
                
                elif tip == "Kasadan Alınan Miktar":
                    file = open("hesap_dosyalari/kasadan_alinan.csv", "a")
                    if firma == "ETT":
                        sonuc = str(tarih+","+str(miktar)+",")
                        file.write(sonuc)
                        file.write(firma+"\n")
                        file.close()
                    else:
                        sonuc = str(tarih+","+str(miktar)+",")
                        file.write(sonuc)
                        file.write(firma)
                        file.close()
                
                elif tip == "POS Gün Sonu":
                    file = open("hesap_dosyalari/pos_gun_sonu.csv", "a")
                    if firma == "ETT":
                        sonuc = str(tarih+","+str(miktar)+",")
                        file.write(sonuc)
                        file.write(firma+"\n")
                        file.close()
                    else:
                        sonuc = str(tarih+","+str(miktar)+",")
                        file.write(sonuc)
                        file.write(firma)
                        file.close()
                
                if tip != "Seçiniz...":
                    messagebox.showwarning("Sonuç","İşlem Başarılı!")
                else:
                    messagebox.showwarning(title="UYARI!", message="Lütfen Ödeme Tipini Seçiniz!")
            except ValueError:
                messagebox.showwarning(title="UYARI!", message="Yanlış ya da Eksik Değer Girildi!")

        pencere = Tk()
        pencere.title("Hesap Programı")
        pencere.geometry("300x400")
        
        odemetip = Label(pencere, text = "Ödeme Tipi Seçiniz...")
        odemetip.place()
        odemetip.pack()
        
        self.degis_odeme = StringVar(pencere)
        self.degis_odeme.set("Seçiniz...")
        secim_pano_odeme = OptionMenu(pencere, self.degis_odeme, *odeme_tipleri)
        secim_pano_odeme.pack()

        firma_adi = Label(pencere, text="Firma Adı:")
        firma_adi.pack()
        
        self.degis_firma = StringVar(pencere)
        self.degis_firma.set("ETT")
        secim_pano_firma = OptionMenu(pencere, self.degis_firma, *self.firmalar)
        secim_pano_firma.pack()

        miktar = Label(pencere, text="Miktar")
        miktar.pack()
        self.miktar_deger = Entry(pencere)
        self.miktar_deger.pack()
        
        buton = Button(pencere, text="Kaydet",bd=2)
        buton.place(x=10,y=10,relx=0.1,rely=0.2)
        buton.bind("<Button-1>", uyari)
        buton.place(x=80,y=100)
        
        mainloop()
        
    def firma_ekle_pen(self, Event):
        firma_ekle_pencere = Tk()
        firma_ekle_pencere.title("Firma Ekle")
        firma_ekle_pencere.geometry("300x400")
        
        firma_adi_label = Label(firma_ekle_pencere, text="Firma Adı:")
        firma_adi_label.pack()

        self.firma_adi = Entry(firma_ekle_pencere)
        self.firma_adi.delete(0,END)
        self.firma_adi.pack()
        self.firma_adi.focus_get()

        ekleme_buton = Button(firma_ekle_pencere, text="Ekle")
        ekleme_buton.bind("<Button-1>", self.firma_ekle_fonk)
        ekleme_buton.pack(side=BOTTOM)
        #firma_ekle_pencere.pack()

    def firma_ekle_fonk(self,Event):
        self.firma_ismi = self.firma_adi.get()
        if self.firma_ismi == "":
            pass
        else:
            firmalar_yaz = open("firmalar.csv", "r")
            firmalarım = firmalar_yaz.readlines()
            firmalarım.insert(0,self.firma_ismi+"\n")
            firmalar_yaz.close()
            firmalar_yaz = open("firmalar.csv", "w")
            firmalar_yaz.writelines(firmalarım)
            firmalar_yaz.close()
            messagebox.showinfo(title="Firma Başarıyla Eklendi...", message="Programı Yeniden Başlattıktan Sonra Firmayla İlgili İşlem Yapabilirsiniz!")

    def hesap_fonk_pen(self, Event):
        hesap_fon_penceresi = Tk()
        hesap_fon_penceresi.geometry("300x400")
        hesap_fon_penceresi.title("Hesap Penceresi")
        
        firma_adi = Label(hesap_fon_penceresi, text="Firma Adı:")
        firma_adi.place(x=10, y= 10)

        self.degis = StringVar(hesap_fon_penceresi)
        self.degis.set("TÜMÜ")
        
        secim_pano = OptionMenu(hesap_fon_penceresi, self.degis, *self.firmalar)
        secim_pano.place(x=150, y=10)

        baslangic_tarih=Label(hesap_fon_penceresi, text="Başlangıç Tarihi:")
        baslangic_tarih.place(x=10, y=110)

        bas_gun_text = Label(hesap_fon_penceresi,text="Gün   /")
        bas_gun_text.place(x=160, y=80)
        bas_ay_text = Label(hesap_fon_penceresi,text="Ay    /")
        bas_ay_text.place(x=210,y=80)
        bas_yil_text = Label(hesap_fon_penceresi,text="Yıl")
        bas_yil_text.place(x=260,y=80)
        self.bas_gun_gir = Entry(hesap_fon_penceresi, text="05", width=5)
        self.bas_gun_gir.place(x=140, y=110)
        self.bas_ay_gir = Entry(hesap_fon_penceresi, text="01", width=5)
        self.bas_ay_gir.place(x=200, y=110)
        self.bas_yil_gir = Entry(hesap_fon_penceresi, text="19", width=5)
        self.bas_yil_gir.place(x=250, y=110)


        """
        baslangic_tarih_buton = Button(hesap_fon_penceresi, text="Seçiniz")
        baslangic_tarih_buton.place(x=150, y=110)
        """

        bitis_tarih = Label(hesap_fon_penceresi, text="Bitiş Tarihi:")
        bitis_tarih.place(x=10, y=180)
        
        bit_gun_text = Label(hesap_fon_penceresi,text="Gün   /")
        bit_gun_text.place(x=160, y=160)
        bit_ay_text = Label(hesap_fon_penceresi,text="Ay    /")
        bit_ay_text.place(x=210,y=160)
        bit_yil_text = Label(hesap_fon_penceresi,text="Yıl")
        bit_yil_text.place(x=260,y=160)
        self.bit_gun_gir = Entry(hesap_fon_penceresi,width=5)
        self.bit_gun_gir.place(x=140, y=180)
        self.bit_ay_gir = Entry(hesap_fon_penceresi,width=5)
        self.bit_ay_gir.place(x=200, y=180)
        self.bit_yil_gir = Entry(hesap_fon_penceresi,width=5)
        self.bit_yil_gir.place(x=250, y=180)

        """
        bitis_tarih_buton = Button(hesap_fon_penceresi, text="Seçiniz")
        bitis_tarih_buton.place(x=150, y=160)
        """
        
        hesapla_buton = Button(hesap_fon_penceresi, text="Hesapla", bd=2)
        hesapla_buton.bind("<Button-1>", self.hesaplarigetir)
        hesapla_buton.pack(side=BOTTOM)
        #hesap_fon_penceresi.pack()

    def hesaplarigetir(self, Event):
        #işlem dosyaları
        yapilacak_odeme = pd.read_csv("hesap_dosyalari/yapilacak_odeme.csv",encoding = "ISO-8859-1")
        kasadan_odeme = pd.read_csv("hesap_dosyalari/kasadan_odeme.csv",encoding = "ISO-8859-1")
        kasadisi_odeme = pd.read_csv("hesap_dosyalari/kasadisi_odeme.csv",encoding = "ISO-8859-1")
        gider = pd.read_csv("hesap_dosyalari/gider.csv",encoding = "ISO-8859-1")
        kasadan_alinan = pd.read_csv("hesap_dosyalari/kasadan_alinan.csv",encoding = "ISO-8859-1")
        pos_gun_sonu = pd.read_csv("hesap_dosyalari/pos_gun_sonu.csv",encoding = "ISO-8859-1")
        
        #sonuçları içine yazdırmak ve sonradan pencereye eklemek için bir dosya
        sonuc_dosyası = open("hesap_dosyalari/gecici_sonuc_dosyasi.csv","w") #ekrana yazdırırken read modunda alıp satırlarını oku!

        #işlem için firma adi
        firma = self.degis.get()

        #tarih için okunan değerler
        bas_gun = self.bas_gun_gir.get()
        bas_ay = self.bas_ay_gir.get()
        bas_yil = self.bas_yil_gir.get()
        bit_gun = self.bit_gun_gir.get()
        bit_ay = self.bit_ay_gir.get()
        bit_yil = self.bit_yil_gir.get()

        #başta bütün toplamlar sıfır, sonra istediklerimizi ekleyip artıracaz...
        yapilacak_odeme_toplam = 0
        kasadan_odeme_toplam = 0
        kasadisi_odeme_toplam = 0
        gider_toplam = 0
        kasadan_alinan_toplam = 0
        pos_gun_sonu_toplam = 0
        try:
            if bas_gun == "": #tarih olmadığı durumda
                baslangic_tarihi = datetime.datetime.strptime("01/01/19", "%d/%m/%y")
                bitis_tarihi = datetime.datetime.today()
                #bitis_tarihi =  datetime.datetime.strptime(str(bitis_tarihim), "%y/%m/%d")
                gun_araligi = str(bitis_tarihi-baslangic_tarihi)
                b = gun_araligi.index("d")
                gun_araligi = gun_araligi[:b]
                gun_araligi = int(gun_araligi)
                ay_araligi = gun_araligi / 30

                
                
                if firma == "TÜMÜ": #tüm firmlar için
                    pencere = Tk()
                    pencere.title("Göster")
                    pencere.geometry("1060x600")
                    sonuc_labeli_tepe = Label(pencere,text="SONUCLAR:", bg="gray",fg="white")
                    sonuc_labeli_tepe.pack(fill=X)
                    
                    for i in yapilacak_odeme.iloc[:,1:2].values:
                        yapilacak_odeme_toplam = yapilacak_odeme_toplam + i
                    for i in kasadan_odeme.iloc[:,1:2].values:
                        kasadan_odeme_toplam = kasadan_odeme_toplam + i
                    for i in kasadisi_odeme.iloc[:,1:2].values:
                        kasadisi_odeme_toplam = kasadisi_odeme_toplam + i
                    for i in gider.iloc[:,1:2].values:
                        gider_toplam = gider_toplam + i
                    for i in kasadan_alinan.iloc[:,1:2].values:
                        kasadan_alinan_toplam = kasadan_alinan_toplam + i
                    for i in pos_gun_sonu.iloc[:,1:2].values:
                        pos_gun_sonu_toplam = pos_gun_sonu_toplam + i
                    
                    yapilacak_odeme1 = open("hesap_dosyalari/yapilacak_odeme.csv", "r")
                    kasadan_odeme1 = open("hesap_dosyalari/kasadan_odeme.csv", "r")
                    kasadisi_odeme1 = open("hesap_dosyalari/kasadisi_odeme.csv", "r")
                    gider1 = open("hesap_dosyalari/gider.csv", "r")
                    kasadan_alinan1 = open("hesap_dosyalari/kasadan_alinan.csv", "r")
                    #pos_gun_sonu1 = open("hesap_dosyalari/pos_gun_sonu.csv", "r")

                    gecici_yapilacak_odeme = open("hesap_dosyalari/gecici_yapilacak_odeme.csv", "w")
                    gecici_kasadan_odeme = open("hesap_dosyalari/gecici_kasadan_odeme.csv", "w")
                    gecici_kasadisi_odeme = open("hesap_dosyalari/gecici_kasadisi_odeme.csv", "w")
                    gecici_gider = open("hesap_dosyalari/gecici_gider.csv", "w")
                    gecici_kasadan_alinan = open("hesap_dosyalari/gecici_kasadan_alinan.csv", "w")
                    gecici_pos_gun_sonu = open("hesap_dosyalari/gecici_pos_gun_sonu.csv", "w")

                    for i in yapilacak_odeme1:
                        hepsi = "Yapılacak Ödeme, " + str(i)
                        sonuc_dosyası.write(hepsi)
                        gecici_yapilacak_odeme.write(i)
                    for i in kasadan_odeme1:
                        hepsi = "Kasadan Ödeme, " + str(i)
                        sonuc_dosyası.write(hepsi)
                        gecici_kasadan_odeme.write(i)
                    for i in kasadisi_odeme1:
                        hepsi = "Kasa Dışı Ödeme, " + str(i)
                        sonuc_dosyası.write(hepsi)
                        gecici_kasadisi_odeme.write(i)
                    for i in gider1:
                        hepsi = "Gider, " + str(i)
                        sonuc_dosyası.write(hepsi)
                        gecici_gider.write(i)
                    for i in kasadan_alinan1:
                        hepsi = "Kasadan Alınan, " + str(i)
                        sonuc_dosyası.write(hepsi)
                        gecici_kasadan_alinan.write(i)
                    sonuc_dosyası.close()
                    gecici_kasadan_odeme.close()
                    gecici_kasadan_alinan.close()
                    gecici_gider.close()
                    gecici_kasadisi_odeme.close()
                    gecici_pos_gun_sonu.close()
                    gecici_yapilacak_odeme.close()

                    label_yapod = Label(pencere, text="\nYapılacak Ödeme Toplam:")
                    label_yapod_sonuc = Label(pencere, text=float(yapilacak_odeme_toplam))
                    label_yapod.place(x=20, y=40)
                    label_yapod_sonuc.place(x=200, y=57)
                    label_kasod = Label(pencere, text="\nKasadan Ödenen Toplam:")
                    label_kasod_sonuc = Label(pencere, text=float(kasadan_odeme_toplam))
                    label_kasod.place(x=20, y=80)
                    label_kasod_sonuc.place(x=200, y=97)
                    label_kasdis = Label(pencere, text="\nKasa Dışı Ödeme Toplam:")
                    label_kasdis_sonuc = Label(pencere, text=float(kasadisi_odeme_toplam))
                    label_kasdis.place(x=20, y=120)
                    label_kasdis_sonuc.place(x=200, y=137)
                    label_gid = Label(pencere, text="\nGider Toplam:")
                    label_gid_sonuc = Label(pencere, text=float(gider_toplam))
                    label_gid.place(x=300, y=40)
                    label_gid_sonuc.place(x=470, y=57)
                    label_kas_al = Label(pencere, text="\nKasadan Alınan Toplam:")
                    label_kas_al_sonuc = Label(pencere, text=float(kasadan_alinan_toplam))
                    label_kas_al.place(x=300, y=80)
                    label_kas_al_sonuc.place(x=470, y=97)
                    label_pos = Label(pencere, text="\nPos Gün Sonu Toplam:")
                    label_pos_sonuc = Label(pencere, text=float(pos_gun_sonu_toplam))
                    label_pos.place(x=300, y=120)
                    label_pos_sonuc.place(x=470, y=137)
                    
                    ayirma_cizgisi = Label(pencere,text="-------------------------------------------------------------------------------------------------------------")
                    ayirma_cizgisi.place(y=160)

                    toplam_ciro = kasadan_alinan_toplam + kasadan_odeme_toplam + pos_gun_sonu_toplam - (pos_gun_sonu_toplam*0.0245)
                    toplam_odeme = kasadan_odeme_toplam + kasadisi_odeme_toplam
                    kasa_brut = (toplam_ciro - toplam_odeme)
                    kasa_net = kasa_brut - gider_toplam
                    pos_kaybı = pos_gun_sonu_toplam - (pos_gun_sonu_toplam*0.0245)

                    ciro = Label(pencere,text="Toplam Ciro:")
                    ciro_sonucu = Label(pencere,text=float(toplam_ciro))
                    ciro.place(x=20,y=190)
                    ciro_sonucu.place(x=140,y=190)

                    odeme = Label(pencere,text="Toplam Ödeme:")
                    odeme_sonucu = Label(pencere,text=float(toplam_odeme))
                    odeme.place(x=20,y=230)
                    odeme_sonucu.place(x=140,y=230)

                    kasa_br = Label(pencere,text="Kasa Brüt:")
                    kasa_br_sonucu = Label(pencere,text=float(kasa_brut))
                    kasa_br.place(x=300,y=190)
                    kasa_br_sonucu.place(x=400,y=190)

                    kasa_n = Label(pencere,text="Kasa Net:")
                    kasa_n_sonucu = Label(pencere,text=float(kasa_net))
                    kasa_n.place(x=300,y=230)
                    kasa_n_sonucu.place(x=400,y=230)

                    pos_k = Label(pencere,text="POS Kaybı:")
                    pos_k_sonucu = Label(pencere,text=float(pos_kaybı))
                    pos_k.place(x=20,y=270)
                    pos_k_sonucu.place(x=140,y=270)

                    ayirma_cizgisi2 = Label(pencere,text="-------------------------------------------------------------------------------------------------------------")
                    ayirma_cizgisi2.place(y=293)

                    aylik = Label(pencere, text="AYLIK ORTALAMA")
                    gunluk = Label(pencere, text="GUNLUK ORTALAMA")
                    gunluk.place(x=140,y=320)
                    aylik.place(x=400,y=320)
                    
                    ciro = Label(pencere,text="Ciro:")
                    ciro_sonucu_gunluk = Label(pencere,text=str(format(float(toplam_ciro/gun_araligi), ".2f")))
                    ciro_sonucu_aylik = Label(pencere,text=str(format(float(toplam_ciro/ay_araligi), ".2f")))
                    ciro.place(x=20,y=350)
                    ciro_sonucu_gunluk.place(x=140,y=350)
                    ciro_sonucu_aylik.place(x=400,y=350)

                    odeme = Label(pencere,text="Ödeme:")
                    odeme_sonucu_gunluk = Label(pencere,text=str(format(float(toplam_odeme/gun_araligi), ".2f")))
                    odeme_sonucu_aylik = Label(pencere,text=str(format(float(toplam_odeme/ay_araligi), ".2f")))
                    odeme.place(x=20,y=380)
                    odeme_sonucu_gunluk.place(x=140,y=380)
                    odeme_sonucu_aylik.place(x=400,y=380)

                    label_gid = Label(pencere, text="Gider:")
                    label_gid_sonuc_gunluk = Label(pencere, text=str(format(float(gider_toplam/gun_araligi), ".2f")))
                    label_gid_sonuc_aylik = Label(pencere, text=str(format(float(gider_toplam/ay_araligi), ".2f")))
                    label_gid.place(x=20, y=410)
                    label_gid_sonuc_gunluk.place(x=140, y=410)
                    label_gid_sonuc_aylik.place(x=400, y=410)

                    kasa_br = Label(pencere,text="Kasa Brüt:")
                    kasa_br_sonucu_gunluk = Label(pencere,text=str(format(float(kasa_brut/gun_araligi), ".2f")))
                    kasa_br_sonucu_aylik = Label(pencere,text=str(format(float(kasa_brut/ay_araligi), ".2f")))
                    kasa_br.place(x=20,y=440)
                    kasa_br_sonucu_gunluk.place(x=140,y=440)
                    kasa_br_sonucu_aylik.place(x=400,y=440)

                    kasa_n = Label(pencere,text="Kasa Net:")
                    kasa_n_sonucu_gunluk = Label(pencere,text=str(format(float(kasa_net/gun_araligi), ".2f")))
                    kasa_n_sonucu_aylik = Label(pencere,text=str(format(float(kasa_net/ay_araligi), ".2f")))
                    kasa_n.place(x=20,y=470)
                    kasa_n_sonucu_gunluk.place(x=140,y=470)
                    kasa_n_sonucu_aylik.place(x=400,y=470)

                    
                    yazimiz = pd.read_csv("hesap_dosyalari/gecici_sonuc_dosyasi.csv",header=None,encoding = "ISO-8859-1")
                    """
                    try:
                        toplam_tam = 0
                        miktarlar = yazimiz.iloc[:,2:3].values
                        for i in miktarlar:
                            toplam_tam = toplam_tam + i
                        top_lab = Label(pencere, text="Toplam:")
                        topl_lab_son = Label(pencere, text=int(toplam_tam))
                        top_lab.place(x=10,y=480)
                        topl_lab_son.place(x=70, y=480)
                    
                    except pd.errors.EmptyDataError:
                        pass
                    
                    
                    try:
                        kasadan_odenen = pd.read_csv("hesap_dosyalari/gecici_kasadan_odeme.csv",header=None,encoding = "ISO-8859-1")
                        toplam_kas_od = 0
                        miktarlar1 = kasadan_odenen.iloc[:,1:2].values
                        for i in miktarlar1:
                            toplam_kas_od = toplam_kas_od + i

                        top_kas_od_lab = Label(pencere, text="Kasadan Ödeme:")
                        topl_kas_od_lab_son = Label(pencere, text=int(toplam_kas_od))
                        top_kas_od_lab.place(x=220,y=480)
                        topl_kas_od_lab_son.place(x=335, y=480)

                    except pd.errors.EmptyDataError:
                        pass

                    try:
                        kasadan_alinan = pd.read_csv("hesap_dosyalari/gecici_kasadan_alinan.csv",header=None,encoding = "ISO-8859-1")
                        toplam_kas_al = 0
                        miktarlar2 = kasadan_alinan.iloc[:,1:2].values
                        for i in miktarlar2:
                            toplam_kas_al = toplam_kas_al + i

                        top_kas_al_lab = Label(pencere, text="Kasadan Alınan:")
                        topl_kas_al_lab_son = Label(pencere, text=int(toplam_kas_al))
                        top_kas_al_lab.place(x=430,y=480)
                        topl_kas_al_lab_son.place(x=550, y=480)

                    except pd.errors.EmptyDataError:
                        pass

                    try:
                        kasadisi_odenen = pd.read_csv("hesap_dosyalari/gecici_kasadisi_odeme.csv",header=None,encoding = "ISO-8859-1")
                        toplam_kasadisi_od = 0
                        miktarlar3 = kasadisi_odenen.iloc[:,1:2].values
                        for i in miktarlar3:
                            toplam_kasadisi_od = toplam_kasadisi_od + i

                        top_kasadisi_od_lab = Label(pencere, text="Kasa Dışı Ödeme:")
                        topl_kasadisi_od_lab_son = Label(pencere, text=int(toplam_kasadisi_od))
                        top_kasadisi_od_lab.place(x=10,y=520)
                        topl_kasadisi_od_lab_son.place(x=130, y=520)

                    except pd.errors.EmptyDataError:
                        pass

                    try:
                        yapilacak_od = pd.read_csv("hesap_dosyalari/gecici_yapilacak_odeme.csv",header=None,encoding = "ISO-8859-1")
                        toplam_yapilacak_od = 0
                        miktarlar4 = yapilacak_od.iloc[:,1:2].values
                        for i in miktarlar4:
                            toplam_yapilacak_od = toplam_yapilacak_od + i

                        top_yap_od_lab = Label(pencere, text="Yapılacak Ödeme:")
                        topl_yap_od_lab_son = Label(pencere, text=int(toplam_yapilacak_od))
                        top_yap_od_lab.place(x=220,y=520)
                        topl_yap_od_lab_son.place(x=340, y=520)

                    except pd.errors.EmptyDataError:
                        pass

                    try:
                        gid = pd.read_csv("hesap_dosyalari/gecici_gider.csv",header=None,encoding = "ISO-8859-1")
                        toplam_gid = 0
                        miktarlar5 = gid.iloc[:,1:2].values
                        for i in miktarlar5:
                            toplam_gid = toplam_gid + i
                        
                        top_gid_lab = Label(pencere, text="Gider:")
                        topl_gid_son = Label(pencere, text=int(toplam_gid))
                        top_gid_lab.place(x=430,y=520)
                        topl_gid_son.place(x=475, y=520)

                    except pd.errors.EmptyDataError:
                        pass
                    """

                    def tarih_goreceli(Event):
                        yazi_yerimiz = Text(pencere, height=30, width=50, bg="black", fg="green")
                        #yazi_yerimiz.insert(INSERT, yazim)
                        yazi_yerimiz.insert(INSERT, yazimiz.sort_values(by=[1])) #0. kolona göre sıraladık
                        yazi_yerimiz.place(x=600, y=60)
                        kaydir.config(command=yazi_yerimiz.yview)
                    
                    def miktar_goreceli(Event):
                        yazi_yerimiz = Text(pencere, height=30, width=50, bg="black", fg="green")
                        #yazi_yerimiz.insert(INSERT, yazim)
                        yazi_yerimiz.insert(INSERT, yazimiz.sort_values(by=[2])) #1. kolona göre sıraladık
                        yazi_yerimiz.place(x=600, y=60)
                        kaydir.config(command=yazi_yerimiz.yview)
                    
                    tarihe_gore = Button(pencere, text="Tarihe Göre Sırala")
                    miktara_gore = Button(pencere, text="Miktara Göre Sırala")
                    tarihe_gore.bind("<Button-1>", tarih_goreceli)
                    miktara_gore.bind("<Button-1>", miktar_goreceli)
                    tarihe_gore.place(x=830,y=30)
                    miktara_gore.place(x=650, y=30)
                    
                    yazi_yerimiz = Text(pencere, height=30, width=50, bg="black", fg="green")
                    #yazi_yerimiz.insert(INSERT, yazim)
                    yazi_yerimiz.insert(INSERT, yazimiz) #0. kolona göre sıraladık
                    yazi_yerimiz.place(x=600, y=60)

                    kaydir = Scrollbar(pencere)
                    kaydir.pack(side=RIGHT, fill=Y)
                    yazi_yerimiz.config(yscrollcommand=kaydir.set)
                    kaydir.config(command=yazi_yerimiz.yview)
                    

                else: #firma ismine göre
                    pencere = Tk()
                    pencere.title("Göster")
                    pencere.geometry("670x600")
                    sonuc_labeli_tepe = Label(pencere,text="SONUCLAR:", bg="gray",fg="white")
                    sonuc_labeli_tepe.pack(fill=X)
                    #firmaya göre arama stringi sadece ETT için
                    firma_ara = firma + "\n"

                    #burada dosya işlemleri ile yapıyoruz...
                    yapilacak_odeme1 = open("hesap_dosyalari/yapilacak_odeme.csv", "r")
                    kasadan_odeme1 = open("hesap_dosyalari/kasadan_odeme.csv", "r")
                    kasadisi_odeme1 = open("hesap_dosyalari/kasadisi_odeme.csv", "r")
                    gider1 = open("hesap_dosyalari/gider.csv", "r")
                    kasadan_alinan1 = open("hesap_dosyalari/kasadan_alinan.csv", "r")
                    #pos_gun_sonu1 = open("hesap_dosyalari/pos_gun_sonu.csv", "r")

                    gecici_yapilacak_odeme = open("hesap_dosyalari/gecici_yapilacak_odeme.csv", "w")
                    gecici_kasadan_odeme = open("hesap_dosyalari/gecici_kasadan_odeme.csv", "w")
                    gecici_kasadisi_odeme = open("hesap_dosyalari/gecici_kasadisi_odeme.csv", "w")
                    gecici_gider = open("hesap_dosyalari/gecici_gider.csv", "w")
                    gecici_kasadan_alinan = open("hesap_dosyalari/gecici_kasadan_alinan.csv", "w")
                    gecici_pos_gun_sonu = open("hesap_dosyalari/gecici_pos_gun_sonu.csv", "w")

                    if firma == "ETT":
                        for i in yapilacak_odeme1:
                            if i.endswith(firma_ara):
                                hepsi = "Yapılacak Ödeme, " + str(i)
                                sonuc_dosyası.write(hepsi)
                                gecici_yapilacak_odeme.write(i)
                        for i in kasadan_odeme1:
                            if i.endswith(firma_ara):
                                hepsi = "Kasadan Ödeme, " + str(i)
                                sonuc_dosyası.write(hepsi)
                                gecici_kasadan_odeme.write(i)
                        for i in kasadisi_odeme1:
                            if i.endswith(firma_ara):
                                hepsi = "Kasa Dışı Ödeme, " + str(i)
                                sonuc_dosyası.write(hepsi)
                                gecici_kasadisi_odeme.write(i)
                        for i in gider1:
                            if i.endswith(firma_ara):
                                hepsi = "Gider, " + str(i)
                                sonuc_dosyası.write(hepsi)
                                gecici_gider.write(i)
                        for i in kasadan_alinan1:
                            if i.endswith(firma_ara):
                                hepsi = "Kasadan Alınan, " + str(i)
                                sonuc_dosyası.write(hepsi)
                                gecici_kasadan_alinan.write(i)
                    else:
                        for i in yapilacak_odeme1:
                            if i.endswith(firma):
                                hepsi = "Yapılacak Ödeme, " + str(i)
                                sonuc_dosyası.write(hepsi)
                                gecici_yapilacak_odeme.write(i)
                        for i in kasadan_odeme1:
                            if i.endswith(firma):
                                hepsi = "Kasadan Ödeme, " + str(i)
                                sonuc_dosyası.write(hepsi)
                                gecici_kasadan_odeme.write(i)
                        for i in kasadisi_odeme1:
                            if i.endswith(firma):
                                hepsi = "Kasa Dışı Ödeme, " + str(i)
                                sonuc_dosyası.write(hepsi)
                                gecici_kasadisi_odeme.write(i)
                        for i in gider1:
                            if i.endswith(firma):
                                hepsi = "Gider, " + str(i)
                                sonuc_dosyası.write(hepsi)
                                gecici_gider.write(i)
                        for i in kasadan_alinan1:
                            if i.endswith(firma):
                                hepsi = "Kasadan Alınan, " + str(i)
                                sonuc_dosyası.write(hepsi)
                                gecici_kasadan_alinan.write(i)
                    sonuc_dosyası.close()
                    gecici_kasadan_odeme.close()
                    gecici_kasadan_alinan.close()
                    gecici_gider.close()
                    gecici_kasadisi_odeme.close()
                    gecici_pos_gun_sonu.close()
                    gecici_yapilacak_odeme.close()
                    #BURADA VERİNİN İÇİNDEKİ BİR KOLONDAN TOPLAMLARI ALDIK VE YAZDIRDIK.
                    """
                    pencere = Tk()
                    pencere.title("Göster")
                    pencere.geometry("660x600")
                    toplam_label = Label(pencere,text="SONUÇLAR:", bg="gray",fg="white")
                    toplam_label.pack(fill=X)
                    """
                    
                    try:
                        yazimiz = pd.read_csv("hesap_dosyalari/gecici_sonuc_dosyasi.csv",header=None,encoding = "ISO-8859-1")
                        toplam_tam = 0
                        miktarlar = yazimiz.iloc[:,2:3].values
                        for i in miktarlar:
                            toplam_tam = toplam_tam + i
                        
                        top_lab = Label(pencere, text="Toplam:")
                        topl_lab_son = Label(pencere, text=int(toplam_tam))
                        top_lab.place(x=10,y=480)
                        topl_lab_son.place(x=70, y=480)

                    except pd.errors.EmptyDataError:
                        pass
                    
                    try:
                        kasadan_odenen = pd.read_csv("hesap_dosyalari/gecici_kasadan_odeme.csv",header=None,encoding = "ISO-8859-1")
                        toplam_kas_od = 0
                        miktarlar1 = kasadan_odenen.iloc[:,1:2].values
                        for i in miktarlar1:
                            toplam_kas_od = toplam_kas_od + i

                        top_kas_od_lab = Label(pencere, text="Kasadan Ödeme:")
                        topl_kas_od_lab_son = Label(pencere, text=int(toplam_kas_od))
                        top_kas_od_lab.place(x=220,y=480)
                        topl_kas_od_lab_son.place(x=335, y=480)

                    except pd.errors.EmptyDataError:
                        pass

                    try:
                        kasadan_alinan = pd.read_csv("hesap_dosyalari/gecici_kasadan_alinan.csv",header=None,encoding = "ISO-8859-1")
                        toplam_kas_al = 0
                        miktarlar2 = kasadan_alinan.iloc[:,1:2].values
                        for i in miktarlar2:
                            toplam_kas_al = toplam_kas_al + i

                        top_kas_al_lab = Label(pencere, text="Kasadan Alınan:")
                        topl_kas_al_lab_son = Label(pencere, text=int(toplam_kas_al))
                        top_kas_al_lab.place(x=430,y=480)
                        topl_kas_al_lab_son.place(x=550, y=480)

                    except pd.errors.EmptyDataError:
                        pass

                    try:
                        kasadisi_odenen = pd.read_csv("hesap_dosyalari/gecici_kasadisi_odeme.csv",header=None,encoding = "ISO-8859-1")
                        toplam_kasadisi_od = 0
                        miktarlar3 = kasadisi_odenen.iloc[:,1:2].values
                        for i in miktarlar3:
                            toplam_kasadisi_od = toplam_kasadisi_od + i

                        top_kasadisi_od_lab = Label(pencere, text="Kasa Dışı Ödeme:")
                        topl_kasadisi_od_lab_son = Label(pencere, text=int(toplam_kasadisi_od))
                        top_kasadisi_od_lab.place(x=10,y=520)
                        topl_kasadisi_od_lab_son.place(x=130, y=520)

                    except pd.errors.EmptyDataError:
                        pass

                    try:
                        yapilacak_od = pd.read_csv("hesap_dosyalari/gecici_yapilacak_odeme.csv",header=None,encoding = "ISO-8859-1")
                        toplam_yapilacak_od = 0
                        miktarlar4 = yapilacak_od.iloc[:,1:2].values
                        for i in miktarlar4:
                            toplam_yapilacak_od = toplam_yapilacak_od + i

                        top_yap_od_lab = Label(pencere, text="Yapılacak Ödeme:")
                        topl_yap_od_lab_son = Label(pencere, text=int(toplam_yapilacak_od))
                        top_yap_od_lab.place(x=220,y=520)
                        topl_yap_od_lab_son.place(x=340, y=520)

                    except pd.errors.EmptyDataError:
                        pass

                    try:
                        gid = pd.read_csv("hesap_dosyalari/gecici_gider.csv",header=None,encoding = "ISO-8859-1")
                        toplam_gid = 0
                        miktarlar5 = gid.iloc[:,1:2].values
                        for i in miktarlar5:
                            toplam_gid = toplam_gid + i
                        
                        top_gid_lab = Label(pencere, text="Gider:")
                        topl_gid_son = Label(pencere, text=int(toplam_gid))
                        top_gid_lab.place(x=430,y=520)
                        topl_gid_son.place(x=475, y=520)

                    except pd.errors.EmptyDataError:
                        pass

                    def tarih_goreceli(Event):
                        yazi_yerimiz = Text(pencere, bg="black", fg="green")
                        #yazi_yerimiz.insert(INSERT, yazim)
                        yazi_yerimiz.insert(INSERT, yazimiz.sort_values(by=[1])) #0. kolona göre sıraladık
                        yazi_yerimiz.place(x=5, y=60)
                        kaydir.config(command=yazi_yerimiz.yview)
                    
                    def miktar_goreceli(Event):
                        yazi_yerimiz = Text(pencere, bg="black", fg="green")
                        #yazi_yerimiz.insert(INSERT, yazim)
                        yazi_yerimiz.insert(INSERT, yazimiz.sort_values(by=[2])) #1. kolona göre sıraladık
                        yazi_yerimiz.place(x=5, y=60)
                        kaydir.config(command=yazi_yerimiz.yview)
                    
                    tarihe_gore = Button(pencere, text="Tarihe Göre Sırala")
                    miktara_gore = Button(pencere, text="Miktara Göre Sırala")
                    tarihe_gore.bind("<Button-1>", tarih_goreceli)
                    miktara_gore.bind("<Button-1>", miktar_goreceli)
                    tarihe_gore.place(x=150,y=30)
                    miktara_gore.place(x=350, y=30)
                    
                    yazi_yerimiz = Text(pencere, bg="black", fg="green")
                    #yazi_yerimiz.insert(INSERT, yazim)
                    yazi_yerimiz.insert(INSERT, yazimiz) #0. kolona göre sıraladık
                    yazi_yerimiz.place(x=5, y=60)

                    kaydir = Scrollbar(pencere)
                    kaydir.pack(side=RIGHT, fill=Y)
                    yazi_yerimiz.config(yscrollcommand=kaydir.set)
                    kaydir.config(command=yazi_yerimiz.yview)

            else: #tarih olduğu durumda
                try:
                    baslangic = str(bas_gun+"/"+bas_ay+"/"+bas_yil)
                    bitis = str(bit_gun+"/"+bit_ay+"/"+bit_yil)

                    baslangic_tarihi1 = datetime.datetime.strptime(baslangic, "%d/%m/%y")
                    bitis_tarihi1 = datetime.datetime.strptime(bitis, "%d/%m/%y")

                    baslangic_tarihi = datetime.datetime.strptime(baslangic, "%d/%m/%y")
                    bitis_tarihi = datetime.datetime.strptime(bitis, "%d/%m/%y")

                    gun_araligi = str(bitis_tarihi-baslangic_tarihi)
                    b = gun_araligi.index("d")
                    gun_araligi = gun_araligi[:b]
                    gun_araligi = int(gun_araligi)
                    
                    #buradan sonra hesaplamaları yap
                    sonuc_dosyasi = open("hesap_dosyalari/gecici_sonuc_dosyasi.csv","w")
                    yapilacak_odeme = open("hesap_dosyalari/yapilacak_odeme.csv","r")
                    kasadan_odeme = open("hesap_dosyalari/kasadan_odeme.csv","r")
                    kasadisi_odeme = open("hesap_dosyalari/kasadisi_odeme.csv","r")
                    gider = open("hesap_dosyalari/gider.csv","r")
                    kasadan_alinan = open("hesap_dosyalari/kasadan_alinan.csv","r")
                    pos_gun_sonu = open("hesap_dosyalari/pos_gun_sonu.csv","r")
                    
                    gecici_yapilacak_odeme = open("hesap_dosyalari/gecici_yapilacak_odeme.csv", "w")
                    gecici_kasadan_odeme = open("hesap_dosyalari/gecici_kasadan_odeme.csv", "w")
                    gecici_kasadisi_odeme = open("hesap_dosyalari/gecici_kasadisi_odeme.csv", "w")
                    gecici_gider = open("hesap_dosyalari/gecici_gider.csv", "w")
                    gecici_kasadan_alinan = open("hesap_dosyalari/gecici_kasadan_alinan.csv", "w")
                    gecici_pos_gun_sonu = open("hesap_dosyalari/gecici_pos_gun_sonu.csv", "w")

                    if firma == "TÜMÜ":
                        
                        for i in yapilacak_odeme:
                            if i.startswith("tarih"):
                                pass
                            else:
                                yaz = "Yapilacak Ödeme," + i
                                sonuc_dosyasi.write(yaz)
                                gecici_yapilacak_odeme.write(i)

                        for i in kasadan_odeme:
                            if i.startswith("tarih"):
                                pass
                            else:
                                yaz = "Kasadan Ödeme," + i 
                                sonuc_dosyasi.write(yaz)
                                gecici_kasadan_odeme.write(i)

                        for i in kasadisi_odeme:
                            if i.startswith("tarih"):
                                pass
                            else:
                                yaz = "Kasa Dışı Ödeme," + i
                                sonuc_dosyasi.write(yaz)
                                gecici_kasadisi_odeme.write(i)

                        for i in gider:
                            if i.startswith("tarih"):
                                pass
                            else:
                                yaz = "Gider," + i
                                sonuc_dosyasi.write(yaz)
                                gecici_gider.write(i)
                        
                        for i in kasadan_alinan:
                            if i.startswith("tarih"):
                                pass
                            else:
                                yaz = "Kasadan Alınan," + i
                                sonuc_dosyasi.write(yaz)
                                gecici_kasadan_alinan.write(i)
                        
                        for i in pos_gun_sonu:
                            if i.startswith("tarih"):
                                pass
                            else:
                                yaz = "POS Gün Sonu," + i
                                sonuc_dosyasi.write(yaz)
                                gecici_pos_gun_sonu.write(i)
                        
                        sonuc_dosyasi.close()
                        gecici_kasadan_odeme.close()
                        gecici_kasadan_alinan.close()
                        gecici_gider.close()
                        gecici_kasadisi_odeme.close()
                        gecici_pos_gun_sonu.close()
                        gecici_yapilacak_odeme.close()
                        #YAZININ ALINMASI VE TARİHE GÖRE ELENMESİ
                    
                        yazimiz = pd.read_csv("hesap_dosyalari/gecici_sonuc_dosyasi.csv",header=None,encoding = "ISO-8859-1")
                        yazimiz[1] = pd.to_datetime(yazimiz[1])
                        mask = (yazimiz[1] >= baslangic_tarihi1) & (yazimiz[1] <= bitis_tarihi1)
                        yazimiz = yazimiz.loc[mask]

                        pencere = Tk()
                        pencere.title("Göster")
                        pencere.geometry("670x600")
                        label_tepe = Label(pencere,text=str(str(gun_araligi) + " günlük sonuçlar gösteriliyor..."),bg="black",fg="red")
                        label_tepe.pack(fill=X)
                        
                        try:
                            toplamim = pd.read_csv("hesap_dosyalari/gecici_sonuc_dosyasi.csv",header=None,encoding = "ISO-8859-1")
                            toplamim[1] = pd.to_datetime(toplamim[1])
                            mask = (toplamim[1] >= baslangic_tarihi1) & (toplamim[1] <= bitis_tarihi1)
                            toplamim = toplamim.loc[mask]
                            toplam_tam = 0
                            miktarlar = toplamim.iloc[:,2:3].values
                            for i in miktarlar:
                                toplam_tam = toplam_tam + i
                            
                            top_lab = Label(pencere, text="Toplam:")
                            topl_lab_son = Label(pencere, text=int(toplam_tam))
                            top_lab.place(x=10,y=480)
                            topl_lab_son.place(x=70, y=480)

                        except pd.errors.EmptyDataError:
                            pass

                        try:
                            kasadan_odenen = pd.read_csv("hesap_dosyalari/gecici_kasadan_odeme.csv",header=None,encoding = "ISO-8859-1")
                            kasadan_odenen[0] = pd.to_datetime(kasadan_odenen[0])
                            mask = (kasadan_odenen[0] >= baslangic_tarihi1) & (kasadan_odenen[0] <= bitis_tarihi1)
                            kasadan_odenen = kasadan_odenen.loc[mask]
                            toplam_kas_od = 0
                            miktarlar1 = kasadan_odenen.iloc[:,1:2].values
                            for i in miktarlar1:
                                toplam_kas_od = toplam_kas_od + i

                            top_kas_od_lab = Label(pencere, text="Kasadan Ödeme:")
                            topl_kas_od_lab_son = Label(pencere, text=int(toplam_kas_od))
                            top_kas_od_lab.place(x=220,y=480)
                            topl_kas_od_lab_son.place(x=335, y=480)

                        except pd.errors.EmptyDataError:
                            pass

                        try:
                            kasadan_alinan = pd.read_csv("hesap_dosyalari/gecici_kasadan_alinan.csv",header=None,encoding = "ISO-8859-1")
                            kasadan_alinan[0] = pd.to_datetime(kasadan_alinan[0])
                            mask = (kasadan_alinan[0] >= baslangic_tarihi1) & (kasadan_alinan[0] <= bitis_tarihi1)
                            kasadan_alinan = kasadan_alinan.loc[mask]
                            toplam_kas_al = 0
                            miktarlar2 = kasadan_alinan.iloc[:,1:2].values
                            for i in miktarlar2:
                                toplam_kas_al = toplam_kas_al + i

                            top_kas_al_lab = Label(pencere, text="Kasadan Alınan:")
                            topl_kas_al_lab_son = Label(pencere, text=int(toplam_kas_al))
                            top_kas_al_lab.place(x=430,y=480)
                            topl_kas_al_lab_son.place(x=550, y=480)

                        except pd.errors.EmptyDataError:
                            pass

                        try:
                            kasadisi_odenen = pd.read_csv("hesap_dosyalari/gecici_kasadisi_odeme.csv",header=None,encoding = "ISO-8859-1")
                            kasadisi_odenen[0] = pd.to_datetime(kasadisi_odenen[0])
                            mask = (kasadisi_odenen[0] >= baslangic_tarihi1) & (kasadisi_odenen[0] <= bitis_tarihi1)
                            kasadisi_odenen = kasadisi_odenen.loc[mask]
                            toplam_kasadisi_od = 0
                            miktarlar3 = kasadisi_odenen.iloc[:,1:2].values
                            for i in miktarlar3:
                                toplam_kasadisi_od = toplam_kasadisi_od + i

                            top_kasadisi_od_lab = Label(pencere, text="Kasa Dışı Ödeme:")
                            topl_kasadisi_od_lab_son = Label(pencere, text=int(toplam_kasadisi_od))
                            top_kasadisi_od_lab.place(x=10,y=520)
                            topl_kasadisi_od_lab_son.place(x=130, y=520)

                        except pd.errors.EmptyDataError:
                            pass

                        try:
                            yapilacak_od = pd.read_csv("hesap_dosyalari/gecici_yapilacak_odeme.csv",header=None,encoding = "ISO-8859-1")
                            yapilacak_od[0] = pd.to_datetime(yapilacak_od[0])
                            mask = (yapilacak_od[0] >= baslangic_tarihi1) & (yapilacak_od[0] <= bitis_tarihi1)
                            yapilacak_od = yapilacak_od.loc[mask]
                            toplam_yapilacak_od = 0
                            miktarlar4 = yapilacak_od.iloc[:,1:2].values
                            for i in miktarlar4:
                                toplam_yapilacak_od = toplam_yapilacak_od + i

                            top_yap_od_lab = Label(pencere, text="Yapılacak Ödeme:")
                            topl_yap_od_lab_son = Label(pencere, text=int(toplam_yapilacak_od))
                            top_yap_od_lab.place(x=220,y=520)
                            topl_yap_od_lab_son.place(x=340, y=520)

                        except pd.errors.EmptyDataError:
                            pass

                        try:
                            gid = pd.read_csv("hesap_dosyalari/gecici_gider.csv",header=None,encoding = "ISO-8859-1")
                            gid[0] = pd.to_datetime(gid[0])
                            mask = (gid[0] >= baslangic_tarihi1) & (gid[0] <= bitis_tarihi1)
                            gid = gid.loc[mask]
                            toplam_gid = 0
                            miktarlar5 = gid.iloc[:,1:2].values
                            for i in miktarlar5:
                                toplam_gid = toplam_gid + i
                            
                            top_gid_lab = Label(pencere, text="Gider:")
                            topl_gid_son = Label(pencere, text=int(toplam_gid))
                            top_gid_lab.place(x=430,y=520)
                            topl_gid_son.place(x=475, y=520)

                        except pd.errors.EmptyDataError:
                            pass

                        def tarih_goreceli(Event):
                            yazi_yerimiz = Text(pencere, bg="black", fg="green")
                            #yazi_yerimiz.insert(INSERT, yazim)
                            yazi_yerimiz.insert(INSERT, yazimiz.sort_values(by=[1])) #1. kolona göre sıraladık
                            yazi_yerimiz.place(x=5, y=60)
                            kaydir.config(command=yazi_yerimiz.yview)
                            
                        def miktar_goreceli(Event):
                            yazi_yerimiz = Text(pencere, bg="black", fg="green")
                            #yazi_yerimiz.insert(INSERT, yazim)
                            yazi_yerimiz.insert(INSERT, yazimiz.sort_values(by=[2])) #2. kolona göre sıraladık
                            yazi_yerimiz.place(x=5, y=60)
                            kaydir.config(command=yazi_yerimiz.yview)
                        
                        tarihe_gore = Button(pencere, text="Tarihe Göre Sırala")
                        miktara_gore = Button(pencere, text="Miktara Göre Sırala")
                        tarihe_gore.bind("<Button-1>", tarih_goreceli)
                        miktara_gore.bind("<Button-1>", miktar_goreceli)
                        tarihe_gore.place(x=150,y=30)
                        miktara_gore.place(x=350, y=30)
                            
                        yazi_yerimiz = Text(pencere, bg="black", fg="green")
                        #yazi_yerimiz.insert(INSERT, yazim)
                        yazi_yerimiz.insert(INSERT, yazimiz) 
                        yazi_yerimiz.place(x=5, y=60)

                        kaydir = Scrollbar(pencere)
                        kaydir.pack(side=RIGHT, fill=Y)
                        yazi_yerimiz.config(yscrollcommand=kaydir.set)
                        kaydir.config(command=yazi_yerimiz.yview)
                        #yazi_yerimiz.pack(side=BOTTOM, fill=X)

                    else:
                        #firmaya göre arama stringi sadece ETT için
                        firma_ara = firma + "\n"

                        #burada dosya işlemleri ile yapıyoruz...
                        yapilacak_odeme1 = open("hesap_dosyalari/yapilacak_odeme.csv", "r")
                        kasadan_odeme1 = open("hesap_dosyalari/kasadan_odeme.csv", "r")
                        kasadisi_odeme1 = open("hesap_dosyalari/kasadisi_odeme.csv", "r")
                        gider1 = open("hesap_dosyalari/gider.csv", "r")
                        kasadan_alinan1 = open("hesap_dosyalari/kasadan_alinan.csv", "r")
                        #pos_gun_sonu1 = open("hesap_dosyalari/pos_gun_sonu.csv", "r")

                        gecici_yapilacak_odeme = open("hesap_dosyalari/gecici_yapilacak_odeme.csv", "w")
                        gecici_kasadan_odeme = open("hesap_dosyalari/gecici_kasadan_odeme.csv", "w")
                        gecici_kasadisi_odeme = open("hesap_dosyalari/gecici_kasadisi_odeme.csv", "w")
                        gecici_gider = open("hesap_dosyalari/gecici_gider.csv", "w")
                        gecici_kasadan_alinan = open("hesap_dosyalari/gecici_kasadan_alinan.csv", "w")
                        gecici_pos_gun_sonu = open("hesap_dosyalari/gecici_pos_gun_sonu.csv", "w")

                        if firma == "ETT":
                            for i in yapilacak_odeme1:
                                if i.endswith(firma_ara):
                                    hepsi = "Yapılacak Ödeme, " + str(i)
                                    sonuc_dosyası.write(hepsi)
                                    gecici_yapilacak_odeme.write(i)
                            for i in kasadan_odeme1:
                                if i.endswith(firma_ara):
                                    hepsi = "Kasadan Ödeme, " + str(i)
                                    sonuc_dosyası.write(hepsi)
                                    gecici_kasadan_odeme.write(i)
                            for i in kasadisi_odeme1:
                                if i.endswith(firma_ara):
                                    hepsi = "Kasa Dışı Ödeme, " + str(i)
                                    sonuc_dosyası.write(hepsi)
                                    gecici_kasadisi_odeme.write(i)
                            for i in gider1:
                                if i.endswith(firma_ara):
                                    hepsi = "Gider, " + str(i)
                                    sonuc_dosyası.write(hepsi)
                                    gecici_gider.write(i)
                            for i in kasadan_alinan1:
                                if i.endswith(firma_ara):
                                    hepsi = "Kasadan Alınan, " + str(i)
                                    sonuc_dosyası.write(hepsi)
                                    gecici_kasadan_alinan.write(i)
                        else:
                            for i in yapilacak_odeme1:
                                if i.endswith(firma):
                                    hepsi = "Yapılacak Ödeme, " + str(i)
                                    sonuc_dosyası.write(hepsi)
                                    gecici_yapilacak_odeme.write(i)
                            for i in kasadan_odeme1:
                                if i.endswith(firma):
                                    hepsi = "Kasadan Ödeme, " + str(i)
                                    sonuc_dosyası.write(hepsi)
                                    gecici_kasadan_odeme.write(i)
                            for i in kasadisi_odeme1:
                                if i.endswith(firma):
                                    hepsi = "Kasa Dışı Ödeme, " + str(i)
                                    sonuc_dosyası.write(hepsi)
                                    gecici_kasadisi_odeme.write(i)
                            for i in gider1:
                                if i.endswith(firma):
                                    hepsi = "Gider, " + str(i)
                                    sonuc_dosyası.write(hepsi)
                                    gecici_gider.write(i)
                            for i in kasadan_alinan1:
                                if i.endswith(firma):
                                    hepsi = "Kasadan Alınan, " + str(i)
                                    sonuc_dosyası.write(hepsi)
                                    gecici_kasadan_alinan.write(i)
                        sonuc_dosyası.close()
                        gecici_kasadan_odeme.close()
                        gecici_kasadan_alinan.close()
                        gecici_gider.close()
                        gecici_kasadisi_odeme.close()
                        gecici_pos_gun_sonu.close()
                        gecici_yapilacak_odeme.close()
                        #BURADA VERİNİN İÇİNDEKİ BİR KOLONDAN TOPLAMLARI ALDIK VE YAZDIRDIK.
                        
                        yazimiz = pd.read_csv("hesap_dosyalari/gecici_sonuc_dosyasi.csv",header=None,encoding = "ISO-8859-1")
                        yazimiz[1] = pd.to_datetime(yazimiz[1])
                        mask = (yazimiz[1] >= baslangic_tarihi1) & (yazimiz[1] <= bitis_tarihi1)
                        yazimiz = yazimiz.loc[mask]

                        pencere = Tk()
                        pencere.title("Göster")
                        pencere.geometry("670x600")
                        label_tepe = Label(pencere,text=str(str(gun_araligi) + " günlük sonuçlar gösteriliyor..."),bg="black",fg="red")
                        label_tepe.pack(fill=X)
                        
                        try:
                            toplamim = pd.read_csv("hesap_dosyalari/gecici_sonuc_dosyasi.csv",header=None,encoding = "ISO-8859-1")
                            toplamim[1] = pd.to_datetime(toplamim[1])
                            mask = (toplamim[1] >= baslangic_tarihi1) & (toplamim[1] <= bitis_tarihi1)
                            toplamim = toplamim.loc[mask]
                            toplam_tam = 0
                            miktarlar = toplamim.iloc[:,2:3].values
                            for i in miktarlar:
                                toplam_tam = toplam_tam + i
                            
                            top_lab = Label(pencere, text="Toplam:")
                            topl_lab_son = Label(pencere, text=int(toplam_tam))
                            top_lab.place(x=10,y=480)
                            topl_lab_son.place(x=70, y=480)

                        except pd.errors.EmptyDataError:
                            pass

                        try:
                            kasadan_odenen = pd.read_csv("hesap_dosyalari/gecici_kasadan_odeme.csv",header=None,encoding = "ISO-8859-1")
                            kasadan_odenen[0] = pd.to_datetime(kasadan_odenen[0])
                            mask = (kasadan_odenen[0] >= baslangic_tarihi1) & (kasadan_odenen[0] <= bitis_tarihi1)
                            kasadan_odenen = kasadan_odenen.loc[mask]
                            toplam_kas_od = 0
                            miktarlar1 = kasadan_odenen.iloc[:,1:2].values
                            for i in miktarlar1:
                                toplam_kas_od = toplam_kas_od + i

                            top_kas_od_lab = Label(pencere, text="Kasadan Ödeme:")
                            topl_kas_od_lab_son = Label(pencere, text=int(toplam_kas_od))
                            top_kas_od_lab.place(x=220,y=480)
                            topl_kas_od_lab_son.place(x=335, y=480)

                        except pd.errors.EmptyDataError:
                            pass

                        try:
                            kasadan_alinan = pd.read_csv("hesap_dosyalari/gecici_kasadan_alinan.csv",header=None,encoding = "ISO-8859-1")
                            kasadan_alinan[0] = pd.to_datetime(kasadan_alinan[0])
                            mask = (kasadan_alinan[0] >= baslangic_tarihi1) & (kasadan_alinan[0] <= bitis_tarihi1)
                            kasadan_alinan = kasadan_alinan.loc[mask]
                            toplam_kas_al = 0
                            miktarlar2 = kasadan_alinan.iloc[:,1:2].values
                            for i in miktarlar2:
                                toplam_kas_al = toplam_kas_al + i

                            top_kas_al_lab = Label(pencere, text="Kasadan Alınan:")
                            topl_kas_al_lab_son = Label(pencere, text=int(toplam_kas_al))
                            top_kas_al_lab.place(x=430,y=480)
                            topl_kas_al_lab_son.place(x=550, y=480)

                        except pd.errors.EmptyDataError:
                            pass

                        try:
                            kasadisi_odenen = pd.read_csv("hesap_dosyalari/gecici_kasadisi_odeme.csv",header=None,encoding = "ISO-8859-1")
                            kasadisi_odenen[0] = pd.to_datetime(kasadisi_odenen[0])
                            mask = (kasadisi_odenen[0] >= baslangic_tarihi1) & (kasadisi_odenen[0] <= bitis_tarihi1)
                            kasadisi_odenen = kasadisi_odenen.loc[mask]
                            toplam_kasadisi_od = 0
                            miktarlar3 = kasadisi_odenen.iloc[:,1:2].values
                            for i in miktarlar3:
                                toplam_kasadisi_od = toplam_kasadisi_od + i

                            top_kasadisi_od_lab = Label(pencere, text="Kasa Dışı Ödeme:")
                            topl_kasadisi_od_lab_son = Label(pencere, text=int(toplam_kasadisi_od))
                            top_kasadisi_od_lab.place(x=10,y=520)
                            topl_kasadisi_od_lab_son.place(x=130, y=520)

                        except pd.errors.EmptyDataError:
                            pass

                        try:
                            yapilacak_od = pd.read_csv("hesap_dosyalari/gecici_yapilacak_odeme.csv",header=None,encoding = "ISO-8859-1")
                            yapilacak_od[0] = pd.to_datetime(yapilacak_od[0])
                            mask = (yapilacak_od[0] >= baslangic_tarihi1) & (yapilacak_od[0] <= bitis_tarihi1)
                            yapilacak_od = yapilacak_od.loc[mask]
                            toplam_yapilacak_od = 0
                            miktarlar4 = yapilacak_od.iloc[:,1:2].values
                            for i in miktarlar4:
                                toplam_yapilacak_od = toplam_yapilacak_od + i

                            top_yap_od_lab = Label(pencere, text="Yapılacak Ödeme:")
                            topl_yap_od_lab_son = Label(pencere, text=int(toplam_yapilacak_od))
                            top_yap_od_lab.place(x=220,y=520)
                            topl_yap_od_lab_son.place(x=340, y=520)

                        except pd.errors.EmptyDataError:
                            pass

                        try:
                            gid = pd.read_csv("hesap_dosyalari/gecici_gider.csv",header=None,encoding = "ISO-8859-1")
                            gid[0] = pd.to_datetime(gid[0])
                            mask = (gid[0] >= baslangic_tarihi1) & (gid[0] <= bitis_tarihi1)
                            gid = gid.loc[mask]
                            toplam_gid = 0
                            miktarlar5 = gid.iloc[:,1:2].values
                            for i in miktarlar5:
                                toplam_gid = toplam_gid + i
                            
                            top_gid_lab = Label(pencere, text="Gider:")
                            topl_gid_son = Label(pencere, text=int(toplam_gid))
                            top_gid_lab.place(x=430,y=520)
                            topl_gid_son.place(x=475, y=520)

                        except pd.errors.EmptyDataError:
                            pass

                        def tarih_goreceli(Event):
                            yazi_yerimiz = Text(pencere, bg="black", fg="green")
                            #yazi_yerimiz.insert(INSERT, yazim)
                            yazi_yerimiz.insert(INSERT, yazimiz.sort_values(by=[1])) #1. kolona göre sıraladık
                            yazi_yerimiz.place(x=5, y=60)
                            kaydir.config(command=yazi_yerimiz.yview)
                            
                        def miktar_goreceli(Event):
                            yazi_yerimiz = Text(pencere, bg="black", fg="green")
                            #yazi_yerimiz.insert(INSERT, yazim)
                            yazi_yerimiz.insert(INSERT, yazimiz.sort_values(by=[2])) #2. kolona göre sıraladık
                            yazi_yerimiz.place(x=5, y=60)
                            kaydir.config(command=yazi_yerimiz.yview)
                        
                        tarihe_gore = Button(pencere, text="Tarihe Göre Sırala")
                        miktara_gore = Button(pencere, text="Miktara Göre Sırala")
                        tarihe_gore.bind("<Button-1>", tarih_goreceli)
                        miktara_gore.bind("<Button-1>", miktar_goreceli)
                        tarihe_gore.place(x=150,y=30)
                        miktara_gore.place(x=350, y=30)
                            
                        yazi_yerimiz = Text(pencere, bg="black", fg="green")
                        #yazi_yerimiz.insert(INSERT, yazim)
                        yazi_yerimiz.insert(INSERT, yazimiz) 
                        yazi_yerimiz.place(x=5, y=60)

                        kaydir = Scrollbar(pencere)
                        kaydir.pack(side=RIGHT, fill=Y)
                        yazi_yerimiz.config(yscrollcommand=kaydir.set)
                        kaydir.config(command=yazi_yerimiz.yview)
                except ValueError:
                    messagebox.showwarning(title = "UYARI", message="Tarih değeri yanlış ya da eksik girildi. Lütfen kontrol ediniz")
        except UnboundLocalError:
            messagebox.showwarning(title="UYARI!", message="Sonuç Bulunamadı!")

def ilkleme():

    try:
        os.mkdir("hesap_dosyalari")
    except FileExistsError:
        pass
    
    gg=open("hesap_dosyalari/gecici_gider.csv","a")
    gka=open("hesap_dosyalari/gecici_kasadan_alinan.csv","a")
    gko=open("hesap_dosyalari/gecici_kasadan_odeme.csv","a")
    gkdo=open("hesap_dosyalari/gecici_kasadisi_odeme.csv","a")
    gpgs=open("hesap_dosyalari/gecici_pos_gun_sonu.csv","a")
    gsd=open("hesap_dosyalari/gecici_sonuc_dosyasi.csv","a")
    gyo=open("hesap_dosyalari/gecici_yapilacak_odeme.csv","a")
    pgs=open("hesap_dosyalari/pos_gun_sonu.csv","a")
    yo=open("hesap_dosyalari/yapilacak_odeme.csv","a")
    ka=open("hesap_dosyalari/kasadan_alinan.csv","a")
    ko=open("hesap_dosyalari/kasadan_odeme.csv","a")
    kdo=open("hesap_dosyalari/kasadisi_odeme.csv","a")
    g=open("hesap_dosyalari/gider.csv","a")

    gg.close()
    gka.close()
    gko.close()
    gkdo.close()
    gpgs.close()
    gsd.close()
    gyo.close()
    pgs.close()
    yo.close()
    ka.close()
    ko.close()
    kdo.close()
    g.close()

ilkleme()

pencere = Tk()
pencere.title("Market Programı")
pencere.iconbitmap(r"desktop_icon.ico")
pencere.geometry("400x500")
giris_pen(pencere)

mainloop()
