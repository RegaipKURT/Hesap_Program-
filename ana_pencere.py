import os
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import datetime
import pandas as pd

odeme_tipleri = ["Yapılacak Ödeme", "Kasadan Yapılan Ödeme", "Kasa Dışı Ödeme","Kasadan Alınan Miktar", "POS Gün Sonu", "Gider", "Ödeme Al", "Alınacak Ödeme"]
odeme_tipleri.sort()
pd.options.display.max_rows = None
tarih = datetime.datetime.now().strftime("%d/%m/%y")
date_now = datetime.datetime.strptime(tarih, "%d/%m/%y")

class giris_pen():

    def __init__(self, master):
        menu = Menu(master)
        pencere.config(menu=menu, bg="#00bc6c")

        altmenu = Menu(menu)
        menu.add_cascade(label="File", menu=altmenu)

        altmenu.add_command(label="Kaydet", command=kayit)
        altmenu.add_command(label="Veri Görselleştirme", command=gorsellestir)

        altmenu.add_separator()
        altmenu.add_command(label="Exit", command=quit)

        menu2 = Menu(menu)
        menu.add_cascade(label="Ayarlar", menu=menu2)
        menu2.add_command(label="Hesaplamaları Göster", command=ayar_goster)
        menu2.add_command(label="POS Oranı Değiştir", command=pos_degis)
        menu2.add_command(label="Firma Sil", command=firma_silme)

        self.status = Label(master, text="Yükleme Başarılı... Hoşgeldiniz...  Tarih:{}".format(tarih), bd=1, relief=SUNKEN, anchor="w",bg="#b1cc00")
        self.status.pack(side=BOTTOM, fill=X)

        self.islem_buton = Button(master, text="İŞLEM\nGİRİŞİ", bd=5,bg="#00bc6c",fg="#071c31",font='Helvetica 12 bold')
        self.islem_buton.bind("<Button-1>", self.hesap_penceresi)
        self.islem_buton.config( height=5, width=10)
        self.islem_buton.place(x=80, y = 100)

        self.ekle_buton = Button(master, text="FİRMA\nEKLE", bd=5, bg="#00bc6c",fg="#071c31",font='Helvetica 12 bold')
        self.ekle_buton.bind("<Button-1>",self.firma_ekle_pen)
        self.ekle_buton.config(height=5, width=10)
        self.ekle_buton.place(x=330, y = 100)

        self.hesap_buton = Button(master, text="HESAP\nYAP", bd=5, bg="#00bc6c",fg="#071c31",font='Helvetica 12 bold')
        self.hesap_buton.bind("<Button-1>", self.hesap_fonk_pen)
        self.hesap_buton.config( height=5, width=10)
        self.hesap_buton.place(x=580, y = 100)

        self.cikis_buton = Button(master, text="Çıkış Yap", bd=5, bg="#00bc6c")
        self.cikis_buton.bind("<Button-1>", self.cikis)
        self.cikis_buton.pack(side=BOTTOM)
        self.firmalar = firmalar_oku.readlines()
        self.pos_oranimiz = format(float(open("hesap_dosyalari/pos_orani.txt","r").readlines()[0]),".4f")

    def cikis(self, Event):
        self.answer = messagebox.askokcancel(title="Çıkış", message="Emin misiniz?")
        if self.answer == TRUE:
            sys.exit()
        else:
            pass

    def hesap_penceresi(self, Event):
        
        def uyari(Event):
            
            try:
                miktar = str(self.miktar_deger.get())
                firma = str(listbox.get())
                tip = str(self.degis_odeme.get())
                miktar = float(miktar.replace(",","."))
                if str(self.bas_gun_gir1.get()) == "":
                    tarih = str(datetime.datetime.now().strftime("%d/%m/%y"))
                else:
                    tarih = str(str(self.bas_gun_gir1.get())+"/"+str(self.bas_ay_gir1.get())+"/"+str(self.bas_yil_gir1.get()))
                if firma not in self.firmalar:
                    messagebox.showwarning("UYARI!","Firma Adı Yanlış Girildi!\nLütfen firma ismini kontrol ediniz!")
                else:
                    if firma != "":
                        if tip == "Gider":
                            file = open("hesap_dosyalari/gider.csv", "a")
                            sonuc = str(tarih+","+str(miktar)+",")
                            file.write(sonuc)
                            file.write(firma)
                            file.close()
                        
                        elif tip == "Yapılacak Ödeme":
                            file = open("hesap_dosyalari/yapilacak_odeme.csv", "a")
                            sonuc = str(tarih+","+str(miktar)+",")
                            file.write(sonuc)
                            file.write(firma)
                            file.close()
                        
                        elif tip == "Ödeme Al":
                            file = open("hesap_dosyalari/odeme_al.csv", "a")
                            sonuc = str(tarih+","+str(miktar)+",")
                            file.write(sonuc)
                            file.write(firma)
                            file.close()

                        elif tip == "Kasadan Yapılan Ödeme":
                            self.answer = messagebox.askquestion(title="Seçim Yapınız", message="Borç İlişksisi Olacak mı?")
                            if self.answer == "yes":
                                file = open("hesap_dosyalari/kasadan_odeme.csv", "a")
                                sonuc = str(tarih+","+str(miktar)+",")
                                file.write(sonuc)
                                file.write(firma)
                                file.close()
                            else:
                                file = open("hesap_dosyalari/kasadan_odeme.csv", "a")
                                sonuc = str(tarih+","+str(miktar)+",")
                                file.write(sonuc)
                                file.write(firma)
                                file.close()

                                file = open("hesap_dosyalari/karsilik_dosyasi.csv", "a")
                                sonuc = str(tarih+","+str(miktar)+",")
                                file.write(sonuc)
                                file.write(firma)
                                file.close()
                        
                        elif tip == "Kasa Dışı Ödeme":
                            self.answer = messagebox.askquestion(title="Seçim Yapınız", message="Borç İlişksisi Olacak mı?")
                            if self.answer == "yes":
                                file = open("hesap_dosyalari/kasadisi_odeme.csv", "a")
                                sonuc = str(tarih+","+str(miktar)+",")
                                file.write(sonuc)
                                file.write(firma)
                                file.close()
                            else:
                                file = open("hesap_dosyalari/kasadisi_odeme.csv", "a")
                                sonuc = str(tarih+","+str(miktar)+",")
                                file.write(sonuc)
                                file.write(firma)
                                file.close()

                                file = open("hesap_dosyalari/karsilik_dosyasi.csv", "a")
                                sonuc = str(tarih+","+str(miktar)+",")
                                file.write(sonuc)
                                file.write(firma)
                                file.close()
                        
                        elif tip == "Kasadan Alınan Miktar":
                            file = open("hesap_dosyalari/kasadan_alinan.csv", "a")
                            sonuc = str(tarih+","+str(miktar)+",")
                            file.write(sonuc)
                            file.write(firma)
                            file.close()
                        
                        elif tip == "POS Gün Sonu":
                            file = open("hesap_dosyalari/pos_gun_sonu.csv", "a")
                            sonuc = str(tarih+","+str(miktar)+",")
                            file.write(sonuc)
                            file.write(firma)
                            file.close()
                        
                        elif tip == "Alınacak Ödeme":
                            file = open("hesap_dosyalari/alinacak_odeme.csv", "a")
                            sonuc = str(tarih+","+str(miktar)+",")
                            file.write(sonuc)
                            file.write(firma)
                            file.close()

                        if tip != "Seçiniz...":
                            messagebox.showinfo("Sonuç","İşlem Başarılı!")
                        else:
                            messagebox.showwarning(title="UYARI!", message="Lütfen Ödeme Tipini Seçiniz!")
                    else:
                        messagebox.showinfo("UYARI!","Lütfen Firma Seçiniz!")
            except ValueError:
                messagebox.showwarning(title="UYARI!", message="Yanlış ya da Eksik Değer Girildi!")

        hesap_ek_pen = Toplevel()
        hesap_ek_pen.title("Hesap Programı")
        hesap_ek_pen.geometry("300x400")
        
        odemetip = Label(hesap_ek_pen, text = "Ödeme Tipi Seçiniz...")
        odemetip.place()
        odemetip.pack()
        
        self.degis_odeme = StringVar(hesap_ek_pen)
        self.degis_odeme.set("Seçiniz...")
        secim_pano_odeme = OptionMenu(hesap_ek_pen, self.degis_odeme, *odeme_tipleri)
        secim_pano_odeme.pack()
        
        miktar = Label(hesap_ek_pen, text="Miktar")
        miktar.pack()
        self.miktar_deger = Entry(hesap_ek_pen)
        self.miktar_deger.pack()
        
        firma_adi = Label(hesap_ek_pen, text="Firma Adı:")
        firma_adi.place(x=130,y=120)

        arama = Label(hesap_ek_pen, text="Ara:")
        arama.place(x=10,y=120)
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
            listbox.delete(0, 'end')
            data = sorted(data, key=str.lower)
            for item in data:
                listbox.insert('end', item)

        test_list = self.firmalar

        entry =Entry(hesap_ek_pen)
        entry.place(x=10,y=150)
        entry.bind('<KeyRelease>', on_keyrelease)

        listbox = Combobox(hesap_ek_pen)
        listbox["values"] = test_list
        listbox.bind('<KeyRelease>', on_keyrelease)
        listbox.place(x=100,y=150)
        #listbox.bind('<Double-Button-1>', on_select)
        
        bas_gun_text1 = Label(hesap_ek_pen,text="Gün   /")
        bas_gun_text1.place(x=140, y=200)
        bas_ay_text1 = Label(hesap_ek_pen,text="Ay    /")
        bas_ay_text1.place(x=190,y=200)
        bas_yil_text1 = Label(hesap_ek_pen,text="Yıl")
        bas_yil_text1.place(x=240,y=200)
        tar_lab1 = Label(hesap_ek_pen, text="Tarih Giriniz:", fg="blue")
        tar_lab1.place(x=20, y=230)
        self.bas_gun_gir1 = Entry(hesap_ek_pen, width=5)
        self.bas_gun_gir1.place(x=120, y=230)
        self.bas_ay_gir1 = Entry(hesap_ek_pen, width=5)
        self.bas_ay_gir1.place(x=180, y=230)
        self.bas_yil_gir1 = Entry(hesap_ek_pen, width=5)
        self.bas_yil_gir1.place(x=230, y=230)
        tar_lab = Label(hesap_ek_pen, text="Bugün İçin Tarih Girmenize Gerek Yoktur.", fg="red")
        tar_lab.place(x=20, y=270)

        buton = Button(hesap_ek_pen, text="Kaydet",bd=2)
        buton.place(x=10,y=10,relx=0.1,rely=0.2)
        buton.bind("<Button-1>", uyari)
        buton.pack(side=BOTTOM)
        
        hesap_ek_pen.mainloop()
        
    def firma_ekle_pen(self, Event):
        firma_ekle_pencere = Toplevel()
        firma_ekle_pencere.title("Firma Ekle")
        firma_ekle_pencere.iconbitmap(r"desktop_icon.ico")
        firma_ekle_pencere.geometry("512x512")
        firma_ekle_pencere.resizable(0,0)
        
        background_image1=PhotoImage(file="connect.png")
        background_label1 = Label(firma_ekle_pencere, image=background_image1)
        background_label1.image = background_image1
        background_label1.place(x=0, y=0, relwidth=1, relheight=1)

        firma_adi_label = Label(background_label1, text="Firma Adı:",font="Helvetica 16 bold", bg="#308bab", fg="#e2e3e4")
        firma_adi_label.place(x=43,y=70)
        
        self.firma_adi = Entry(firma_ekle_pencere,font = "Helvetica 16 bold", bg="#4f5963", fg="#e2e3e4")
        self.firma_adi.delete(0,END)
        self.firma_adi.place(x=43,y=110,width=185, height=35)
        self.firma_adi.focus_get()

        ekleme_buton = Button(firma_ekle_pencere, text="Ekle",font="Helvetica 16 bold",bg="#308bab",fg="#071c31", bd=3)
        ekleme_buton.bind("<Button-1>", self.firma_ekle_fonk)
        ekleme_buton.place(x=43,y=400,width=185, height=35)
        #firma_ekle_pencere.pack()

    def firma_ekle_fonk(self,Event):
        self.firma_ismi = self.firma_adi.get()
        if str(self.firma_ismi + "\n") not in self.firmalar:        
        
            def firma_ilkleme():
                pgs=open("hesap_dosyalari/pos_gun_sonu.csv","a")
                yo=open("hesap_dosyalari/yapilacak_odeme.csv","a")
                ka=open("hesap_dosyalari/kasadan_alinan.csv","a")
                ko=open("hesap_dosyalari/kasadan_odeme.csv","a")
                kdo=open("hesap_dosyalari/kasadisi_odeme.csv","a")
                g=open("hesap_dosyalari/gider.csv","a")
                ol=open("hesap_dosyalari/odeme_al.csv","a")
                ad = open("hesap_dosyalari/alinacak_odeme.csv","a")
                kardos = open("hesap_dosyalari/karsilik_dosyasi.csv","a")

                miktar = 0.0
                firma = self.firma_ismi

                sonuc = str(tarih+","+str(miktar)+",")
                pgs.write(sonuc)
                pgs.write(firma+"\n")
                pgs.close()

                yo.write(sonuc)
                yo.write(firma+"\n")
                yo.close()

                ka.write(sonuc)
                ka.write(firma+"\n")
                ka.close()

                ko.write(sonuc)
                ko.write(firma+"\n")
                ko.close()
                
                kdo.write(sonuc)
                kdo.write(firma+"\n")
                kdo.close()

                g.write(sonuc)
                g.write(firma+"\n")
                g.close()

                ol.write(sonuc)
                ol.write(firma+"\n")
                ol.close()

                ad.write(sonuc)
                ad.write(firma+"\n")
                ad.close()

                kardos.write(sonuc)
                kardos.write(firma+"\n")
                kardos.close()

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
                firma_ilkleme()
                
                messagebox.showinfo(title="Firma Başarıyla Eklendi...", message="Programı Yeniden Başlattıktan Sonra Firmayla İlgili İşlem Yapabilirsiniz!")
        else:
            messagebox.showwarning("UYARI!","Firma Zaten Mevcut. Yeniden Ekleyemezsiniz.")
    
    def hesap_fonk_pen(self, Event):
        hesap_fon_penceresi = Tk()
        hesap_fon_penceresi.geometry("300x400")
        hesap_fon_penceresi.title("Hesap Penceresi")
        
        firma_adi = Label(hesap_fon_penceresi, text="Firma Adı:")
        firma_adi.place(x=130,y=20)

        arama = Label(hesap_fon_penceresi, text="Ara:")
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

        test_list = self.firmalar

        entry =Entry(hesap_fon_penceresi)
        entry.place(x=10,y=40)
        entry.bind('<KeyRelease>', on_keyrelease)

        self.firm = Combobox(hesap_fon_penceresi)
        self.firm["values"] = test_list
        self.firm.set("TÜMÜ")
        self.firm.bind('<KeyRelease>', on_keyrelease)
        self.firm.place(x=100,y=40)
        #listbox.bind('<Double-Button-1>', on_select)

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
        alinan_odeme = pd.read_csv("hesap_dosyalari/odeme_al.csv",encoding = "ISO-8859-1")
        alinacak_odeme = pd.read_csv("hesap_dosyalari/alinacak_odeme.csv",encoding = "ISO-8859-1")
        kardos = pd.read_csv("hesap_dosyalari/karsilik_dosyasi.csv",encoding = "ISO-8859-1")
        
        #sonuçları içine yazdırmak ve sonradan pencereye eklemek için bir dosya
        sonuc_dosyası = open("hesap_dosyalari/gecici_sonuc_dosyasi.csv","w") #ekrana yazdırırken read modunda alıp satırlarını oku!

        #işlem için firma adi
        firma = str(self.firm.get())

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
        alinan_odeme_toplam = 0
        alinacak_odeme_toplam = 0
        karsilik_toplam = 0
        try:

            if bas_gun == "": #tarih olmadığı durumda
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

                if firma == "TÜMÜ": #tüm firmlar için
                    pencere = Tk()
                    pencere.title("Göster")
                    pencere.geometry("1200x600")
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
                    for i in alinan_odeme.iloc[:,1:2].values:
                        alinan_odeme_toplam = alinan_odeme_toplam + i
                    for i in alinacak_odeme.iloc[:,1:2].values:
                        alinacak_odeme_toplam = alinacak_odeme_toplam + i
                    for i in kardos.iloc[:,1:2].values:
                        karsilik_toplam = karsilik_toplam + i
                    
                    
                    yapilacak_odeme1 = open("hesap_dosyalari/yapilacak_odeme.csv", "r")
                    kasadan_odeme1 = open("hesap_dosyalari/kasadan_odeme.csv", "r")
                    kasadisi_odeme1 = open("hesap_dosyalari/kasadisi_odeme.csv", "r")
                    gider1 = open("hesap_dosyalari/gider.csv", "r")
                    kasadan_alinan1 = open("hesap_dosyalari/kasadan_alinan.csv", "r")
                    alinan_odeme1 = open("hesap_dosyalari/odeme_al.csv","r")
                    alinacak_odeme1 = open("hesap_dosyalari/alinacak_odeme.csv","r")
                    kardos1 = open("hesap_dosyalari/karsilik_dosyasi.csv","r")
                    #pos_gun_sonu1 = open("hesap_dosyalari/pos_gun_sonu.csv", "r")

                    gecici_yapilacak_odeme = open("hesap_dosyalari/gecici_yapilacak_odeme.csv", "w")
                    gecici_kasadan_odeme = open("hesap_dosyalari/gecici_kasadan_odeme.csv", "w")
                    gecici_kasadisi_odeme = open("hesap_dosyalari/gecici_kasadisi_odeme.csv", "w")
                    gecici_gider = open("hesap_dosyalari/gecici_gider.csv", "w")
                    gecici_kasadan_alinan = open("hesap_dosyalari/gecici_kasadan_alinan.csv", "w")
                    gecici_pos_gun_sonu = open("hesap_dosyalari/gecici_pos_gun_sonu.csv", "w")
                    gecici_alinan_odeme = open("hesap_dosyalari/gecici_odeme_al.csv","w")
                    gecici_alinacak_odeme = open("hesap_dosyalari/gecici_alinacak_odeme.csv","w")
                    gecici_karsilik = open("hesap_dosyalari/gecici_karsilik_dosyasi.csv","w")


                    for i in yapilacak_odeme1:
                        hepsi = "Yapilacak Odeme, " + str(i)
                        sonuc_dosyası.write(hepsi)
                        gecici_yapilacak_odeme.write(i)
                    for i in kasadan_odeme1:
                        hepsi = "Kasadan Odeme, " + str(i)
                        sonuc_dosyası.write(hepsi)
                        gecici_kasadan_odeme.write(i)
                    for i in kasadisi_odeme1:
                        hepsi = "Kasa Disi Odeme, " + str(i)
                        sonuc_dosyası.write(hepsi)
                        gecici_kasadisi_odeme.write(i)
                    for i in gider1:
                        hepsi = "Gider, " + str(i)
                        sonuc_dosyası.write(hepsi)
                        gecici_gider.write(i)
                    for i in kasadan_alinan1:
                        hepsi = "Kasadan Alinan, " + str(i)
                        sonuc_dosyası.write(hepsi)
                        gecici_kasadan_alinan.write(i)
                    for i in alinan_odeme1:
                        hepsi = "Alinan Odeme, " + str(i)
                        sonuc_dosyası.write(hepsi)
                        gecici_alinan_odeme.write(i)
                    for i in alinacak_odeme1:
                        hepsi = "Alinacak Odeme, " + str(i)
                        sonuc_dosyası.write(hepsi)
                        gecici_alinacak_odeme.write(i)
                    for i in kardos1:
                        hepsi = "Odeme Karsiligi, " + str(i)
                        sonuc_dosyası.write(hepsi)
                        gecici_alinacak_odeme.write(i)
                    
                    sonuc_dosyası.close()
                    gecici_kasadan_odeme.close()
                    gecici_kasadan_alinan.close()
                    gecici_gider.close()
                    gecici_kasadisi_odeme.close()
                    gecici_pos_gun_sonu.close()
                    gecici_yapilacak_odeme.close()
                    gecici_alinan_odeme.close()
                    gecici_alinacak_odeme.close()
                    gecici_karsilik.close()

                    label_yapod = Label(pencere, text="\nYapılacak Ödeme Toplam:")
                    label_yapod_sonuc = Label(pencere, text=format(float((yapilacak_odeme_toplam+karsilik_toplam)-(kasadan_odeme_toplam+kasadisi_odeme_toplam)), ".2f"))
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
                    label_gid = Label(pencere, text="Gider Toplam:")
                    label_gid_sonuc = Label(pencere, text=float(gider_toplam))
                    label_gid.place(x=300, y=190)
                    label_gid_sonuc.place(x=400, y=190)
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

                    toplam_ciro = float(kasadan_alinan_toplam + kasadan_odeme_toplam + pos_gun_sonu_toplam - (pos_gun_sonu_toplam*float(self.pos_oranimiz)) + alinan_odeme_toplam)
                    toplam_odeme = float(kasadan_odeme_toplam + kasadisi_odeme_toplam)
                    kasa_brut = float(toplam_ciro - toplam_odeme)
                    kasa_net = float(kasa_brut - gider_toplam)
                    pos_kaybı = float(pos_gun_sonu_toplam*float(self.pos_oranimiz))

                    ciro = Label(pencere,text="Toplam Ciro:")
                    ciro_sonucu = Label(pencere,text=format(float(toplam_ciro),".2f"))
                    ciro.place(x=20,y=190)
                    ciro_sonucu.place(x=140,y=190)

                    odeme = Label(pencere,text="Toplam Ödeme:")
                    odeme_sonucu = Label(pencere,text=format(float(toplam_odeme),".2f"))
                    odeme.place(x=20,y=230)
                    odeme_sonucu.place(x=140,y=230)

                    kasa_br = Label(pencere,text="Kasa Brüt:")
                    kasa_br_sonucu = Label(pencere,text=format(float(kasa_brut),".2f"))
                    kasa_br.place(x=300,y=230)
                    kasa_br_sonucu.place(x=400,y=230)

                    kasa_n = Label(pencere,text="Kasa Net:")
                    kasa_n_sonucu = Label(pencere,text=format(float(kasa_net),".2f"))
                    kasa_n.place(x=300,y=270)
                    kasa_n_sonucu.place(x=400,y=270)

                    pos_k = Label(pencere,text="POS Kaybı:")
                    pos_k_sonucu = Label(pencere,text=format(float(pos_kaybı),".2f"))
                    pos_k.place(x=20,y=270)
                    pos_k_sonucu.place(x=140,y=270)

                    al_od = Label(pencere,text="Alınan Ödeme:")
                    al_od_sonucu = Label(pencere,text=format(float(alinan_odeme_toplam),".2f"))
                    al_od.place(x=300,y=57)
                    al_od_sonucu.place(x=470,y=57)

                    ayirma_cizgisi2 = Label(pencere,text="-------------------------------------------------------------------------------------------------------------")
                    ayirma_cizgisi2.place(y=293)

                    aylik = Label(pencere, text="AYLIK ORTALAMA")
                    gunluk = Label(pencere, text="GUNLUK ORTALAMA")
                    gunluk.place(x=140,y=320)
                    aylik.place(x=400,y=320)
                    
                    ciro = Label(pencere,text="Ciro:")
                    ciro_sonucu_gunluk = Label(pencere,text=format(float(toplam_ciro/gun_araligi), ".2f"))
                    ciro_sonucu_aylik = Label(pencere,text=format(float(toplam_ciro/ay_araligi), ".2f"))
                    ciro.place(x=20,y=350)
                    ciro_sonucu_gunluk.place(x=140,y=350)
                    ciro_sonucu_aylik.place(x=400,y=350)

                    odeme = Label(pencere,text="Ödeme:")
                    odeme_sonucu_gunluk = Label(pencere,text=format(float(toplam_odeme/gun_araligi), ".2f"))
                    odeme_sonucu_aylik = Label(pencere,text=format(float(toplam_odeme/ay_araligi), ".2f"))
                    odeme.place(x=20,y=380)
                    odeme_sonucu_gunluk.place(x=140,y=380)
                    odeme_sonucu_aylik.place(x=400,y=380)

                    label_gid = Label(pencere, text="Gider:")
                    label_gid_sonuc_gunluk = Label(pencere, text=format(float(gider_toplam/gun_araligi), ".2f"))
                    label_gid_sonuc_aylik = Label(pencere, text=format(float(gider_toplam/ay_araligi), ".2f"))
                    label_gid.place(x=20, y=410)
                    label_gid_sonuc_gunluk.place(x=140, y=410)
                    label_gid_sonuc_aylik.place(x=400, y=410)

                    kasa_br = Label(pencere,text="Kasa Brüt:")
                    kasa_br_sonucu_gunluk = Label(pencere,text=format(float(kasa_brut/gun_araligi), ".2f"))
                    kasa_br_sonucu_aylik = Label(pencere,text=format(float(kasa_brut/ay_araligi), ".2f"))
                    kasa_br.place(x=20,y=440)
                    kasa_br_sonucu_gunluk.place(x=140,y=440)
                    kasa_br_sonucu_aylik.place(x=400,y=440)

                    kasa_n = Label(pencere,text="Kasa Net:")
                    kasa_n_sonucu_gunluk = Label(pencere,text=format(float(kasa_net/gun_araligi), ".2f"))
                    kasa_n_sonucu_aylik = Label(pencere,text=format(float(kasa_net/ay_araligi), ".2f"))
                    kasa_n.place(x=20,y=470)
                    kasa_n_sonucu_gunluk.place(x=140,y=470)
                    kasa_n_sonucu_aylik.place(x=400,y=470)

                    borc_alacak = (kasadan_odeme_toplam + kasadisi_odeme_toplam - (yapilacak_odeme_toplam + karsilik_toplam)) + (alinacak_odeme_toplam - alinan_odeme_toplam)

                    if borc_alacak > 0:
                        veresiye = Label(pencere,text="TOPLAM ALACAĞINIZ VAR:", bg ="red")
                        veresiye_sonucu = Label(pencere,text=format(float(borc_alacak), ".2f"))
                        veresiye.place(x=20,y=520)
                        veresiye.place(x=140,y=520)
                        veresiye_sonucu.place(x=400,y=520)
                    else:
                        veresiye = Label(pencere,text="ALACAĞINIZ YOK / BORÇ:", bg ="green")
                        veresiye_sonucu = Label(pencere,text=format(float(borc_alacak), ".2f"))
                        veresiye.place(x=20,y=520)
                        veresiye.place(x=140,y=520)
                        veresiye_sonucu.place(x=400,y=520)

                    yazimiz = pd.read_csv("hesap_dosyalari/gecici_sonuc_dosyasi.csv",header=None, dayfirst=True,encoding = "ISO-8859-1")
                    
                    def tarih_goreceli(Event):
                        yazi_yerimiz = Text(pencere, height=30, width=80, bg="black", fg="green")
                        #yazi_yerimiz.insert(INSERT, yazim)
                        yazi_yerimiz.insert(INSERT, yazimiz.sort_values(by=[1])) #0. kolona göre sıraladık
                        yazi_yerimiz.place(x=600, y=60)
                        kaydir.config(command=yazi_yerimiz.yview)
                    
                    def miktar_goreceli(Event):
                        yazi_yerimiz = Text(pencere, height=30, width=80, bg="black", fg="green")
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
                    
                    yazi_yerimiz = Text(pencere, height=30, width=80, bg="black", fg="green")
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

                    #burada dosya işlemleri ile yapıyoruz...
                    yapilacak_odeme1 = open("hesap_dosyalari/yapilacak_odeme.csv", "r")
                    kasadan_odeme1 = open("hesap_dosyalari/kasadan_odeme.csv", "r")
                    kasadisi_odeme1 = open("hesap_dosyalari/kasadisi_odeme.csv", "r")
                    gider1 = open("hesap_dosyalari/gider.csv", "r")
                    kasadan_alinan1 = open("hesap_dosyalari/kasadan_alinan.csv", "r")
                    alinan_odeme1 = open("hesap_dosyalari/odeme_al.csv","r")
                    alinacak_odeme1 = open("hesap_dosyalari/alinacak_odeme.csv","r")
                    kardos1 = open("hesap_dosyalari/karsilik_dosyasi.csv","r")
                    #pos_gun_sonu1 = open("hesap_dosyalari/pos_gun_sonu.csv", "r")

                    gecici_yapilacak_odeme = open("hesap_dosyalari/gecici_yapilacak_odeme.csv", "w")
                    gecici_kasadan_odeme = open("hesap_dosyalari/gecici_kasadan_odeme.csv", "w")
                    gecici_kasadisi_odeme = open("hesap_dosyalari/gecici_kasadisi_odeme.csv", "w")
                    gecici_gider = open("hesap_dosyalari/gecici_gider.csv", "w")
                    gecici_kasadan_alinan = open("hesap_dosyalari/gecici_kasadan_alinan.csv", "w")
                    gecici_pos_gun_sonu = open("hesap_dosyalari/gecici_pos_gun_sonu.csv", "w")
                    gecici_alinan_odeme = open("hesap_dosyalari/gecici_odeme_al.csv","w")
                    gecici_alinacak_odeme = open("hesap_dosyalari/gecici_alinacak_odeme.csv","w")
                    gecici_kardos = open("hesap_dosyalari/gecici_karsilik_dosyasi.csv","w")

                    for i in yapilacak_odeme1:
                        if i.endswith(firma):
                            hepsi = "Yapilacak Odeme, " + str(i)
                            sonuc_dosyası.write(hepsi)
                            gecici_yapilacak_odeme.write(i)
                    for i in alinacak_odeme1:
                        if i.endswith(firma):
                            hepsi = "Alinacak Odeme, " + str(i)
                            sonuc_dosyası.write(hepsi)
                            gecici_alinacak_odeme.write(i)
                    for i in kasadan_odeme1:
                        if i.endswith(firma):
                            hepsi = "Kasadan Odeme, " + str(i)
                            sonuc_dosyası.write(hepsi)
                            gecici_kasadan_odeme.write(i)
                    for i in kasadisi_odeme1:
                        if i.endswith(firma):
                            hepsi = "Kasa Disi Odeme, " + str(i)
                            sonuc_dosyası.write(hepsi)
                            gecici_kasadisi_odeme.write(i)
                    for i in gider1:
                        if i.endswith(firma):
                            hepsi = "Gider, " + str(i)
                            sonuc_dosyası.write(hepsi)
                            gecici_gider.write(i)
                    for i in kasadan_alinan1:
                        if i.endswith(firma):
                            hepsi = "Kasadan Alinan, " + str(i)
                            sonuc_dosyası.write(hepsi)
                            gecici_kasadan_alinan.write(i)
                    for i in alinan_odeme1:
                        if i.endswith(firma):
                            hepsi = "Alinan Odeme, " + str(i)
                            sonuc_dosyası.write(hepsi)
                            gecici_alinan_odeme.write(i)
                    for i in kardos1:
                        if i.endswith(firma):
                            hepsi = "Odeme Karsiligi, " + str(i)
                            sonuc_dosyası.write(hepsi)
                            gecici_kardos.write(i)
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

                    yazimiz = pd.read_csv("hesap_dosyalari/gecici_sonuc_dosyasi.csv",header=None,encoding = "ISO-8859-1")
                    
                    
                    try:
                        kasadan_odenen = pd.read_csv("hesap_dosyalari/gecici_kasadan_odeme.csv",header=None,encoding = "ISO-8859-1")
                        toplam_kas_od = 0
                        miktarlar1 = kasadan_odenen.iloc[:,1:2].values
                        for i in miktarlar1:
                            toplam_kas_od = float(toplam_kas_od) + float(i)

                        top_kas_od_lab = Label(pencere, text="Kasadan Ödeme:")
                        topl_kas_od_lab_son = Label(pencere, text=float(format(toplam_kas_od, ".2f")))
                        top_kas_od_lab.place(x=220,y=480)
                        topl_kas_od_lab_son.place(x=335, y=480)

                    except pd.errors.EmptyDataError:
                        pass

                    try:
                        kasadan_alinan = pd.read_csv("hesap_dosyalari/gecici_kasadan_alinan.csv",header=None,encoding = "ISO-8859-1")
                        toplam_kas_al = 0
                        miktarlar2 = kasadan_alinan.iloc[:,1:2].values
                        for i in miktarlar2:
                            toplam_kas_al = float(toplam_kas_al) + float(i)

                        top_kas_al_lab = Label(pencere, text="Kasadan Alınan:")
                        topl_kas_al_lab_son = Label(pencere, text=float(format(toplam_kas_al,".2f")))
                        top_kas_al_lab.place(x=430,y=480)
                        topl_kas_al_lab_son.place(x=550, y=480)

                    except pd.errors.EmptyDataError:
                        pass

                    try:
                        kasadisi_odenen = pd.read_csv("hesap_dosyalari/gecici_kasadisi_odeme.csv",header=None,encoding = "ISO-8859-1")
                        toplam_kasadisi_od = 0
                        miktarlar3 = kasadisi_odenen.iloc[:,1:2].values
                        for i in miktarlar3:
                            toplam_kasadisi_od = float(toplam_kasadisi_od) + float(i)

                        top_kasadisi_od_lab = Label(pencere, text="Kasa Dışı Ödeme:")
                        topl_kasadisi_od_lab_son = Label(pencere, text=float(format(toplam_kasadisi_od,".2f")))
                        top_kasadisi_od_lab.place(x=10,y=520)
                        topl_kasadisi_od_lab_son.place(x=130, y=520)

                    except pd.errors.EmptyDataError:
                        pass
                    
                    try:
                        top_lab = Label(pencere, text="Toplam Ödeme:")
                        topl_lab_son = Label(pencere, text=float(format(toplam_kas_od+toplam_kasadisi_od, ".2f")))
                        top_lab.place(x=10,y=480)
                        topl_lab_son.place(x=130, y=480)

                    except pd.errors.EmptyDataError:
                        pass
                    
                    try:
                        karsilik_dos = pd.read_csv("hesap_dosyalari/gecici_karsilik_dosyasi.csv",header=None,encoding = "ISO-8859-1")
                        toplam_karsilik = 0
                        miktarlar0 = karsilik_dos.iloc[:,1:2].values
                        for i in miktarlar0:
                            toplam_karsilik = float(toplam_karsilik) + float(i)
                    
                    except pd.errors.EmptyDataError:
                        pass

                    try:
                        yapilacak_od = pd.read_csv("hesap_dosyalari/gecici_yapilacak_odeme.csv",header=None,encoding = "ISO-8859-1")
                        toplam_yapilacak_od = 0
                        miktarlar4 = yapilacak_od.iloc[:,1:2].values
                        for i in miktarlar4:
                            toplam_yapilacak_od = float(toplam_yapilacak_od) + float(i)

                        top_yap_od_lab = Label(pencere, text="Yapılacak Ödeme:")
                        topl_yap_od_lab_son = Label(pencere, text=float(format(((toplam_yapilacak_od + toplam_karsilik)-(toplam_kas_od+toplam_kasadisi_od)),".2f")))
                        top_yap_od_lab.place(x=220,y=520)
                        topl_yap_od_lab_son.place(x=340, y=520)

                    except pd.errors.EmptyDataError:
                        pass

                    try:
                        gid = pd.read_csv("hesap_dosyalari/gecici_gider.csv",header=None,encoding = "ISO-8859-1")
                        toplam_gid = 0
                        miktarlar5 = gid.iloc[:,1:2].values
                        for i in miktarlar5:
                            toplam_gid = float(toplam_gid) + float(i)
                        
                        top_gid_lab = Label(pencere, text="Gider:")
                        topl_gid_son = Label(pencere, text=float(format(toplam_gid,".2f")))
                        top_gid_lab.place(x=430,y=520)
                        topl_gid_son.place(x=475, y=520)

                    except pd.errors.EmptyDataError:
                        pass
                    
                    try:
                        alinan_odeme = pd.read_csv("hesap_dosyalari/gecici_odeme_al.csv",header=None,encoding = "ISO-8859-1")
                        toplam_al_od = 0
                        miktarlar1 = alinan_odeme.iloc[:,1:2].values
                        for i in miktarlar1:
                            toplam_al_od = float(toplam_al_od) + float(i)

                        top_al_od_lab = Label(pencere, text="Alınan Ödeme:")
                        topl_al_od_lab_son = Label(pencere, text=float(format(toplam_al_od,".2f")))
                        top_al_od_lab.place(x=10,y=560)
                        topl_al_od_lab_son.place(x=130, y=560)

                    except pd.errors.EmptyDataError:
                        pass
                    
                    try:
                        alinacak_od = pd.read_csv("hesap_dosyalari/gecici_alinacak_odeme.csv",header=None,encoding = "ISO-8859-1")
                        toplam_alinacak_od = 0
                        miktarlar7 = alinacak_od.iloc[:,1:2].values
                        for i in miktarlar7:
                            toplam_alinacak_od = float(toplam_alinacak_od) + float(i)

                        top_alin_od_lab = Label(pencere, text="Alınacak Ödeme:")
                        topl_alin_od_lab_son = Label(pencere, text=float(format((toplam_alinacak_od-toplam_al_od),".2f")))
                        top_alin_od_lab.place(x=220,y=560)
                        topl_alin_od_lab_son.place(x=340, y=560)

                    except pd.errors.EmptyDataError:
                        pass

                    try:
                        sonucum = float(format((float((toplam_kas_od + toplam_kasadisi_od) - (toplam_yapilacak_od+toplam_karsilik))+((float(toplam_alinacak_od) - float(toplam_al_od))))))
                        if sonucum > 0:
                            sonuc = Label(pencere, text="BORÇ YOK/Toplam Alacak:", fg="green")
                            sonuc_son = Label(pencere, fg="green", text=float(format(sonucum,".2f")))
                            sonuc.place(x=430,y=560)
                            sonuc_son.place(x=590, y=560)
                        else:
                            sonuc = Label(pencere, text="Alacak Yok/BORCUNUZ:", fg="red")
                            sonuc_son = Label(pencere, fg="red", text=float(format(-sonucum,".2f")))
                            sonuc.place(x=430,y=560)
                            sonuc_son.place(x=590, y=560)

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
                    try:
                        gun_araligi = str(bitis_tarihi-baslangic_tarihi)
                        b = gun_araligi.index("d")
                        gun_araligi = gun_araligi[:b]
                        gun_araligi = int(gun_araligi) + 1
                        ay_araligi = float(gun_araligi/30)
                    except ValueError:
                        gun_araligi = 1
                        ay_araligi = float(gun_araligi/30)
                    #buradan sonra hesaplamaları yap
                    sonuc_dosyasi = open("hesap_dosyalari/gecici_sonuc_dosyasi.csv","w")
                    yapilacak_odeme = open("hesap_dosyalari/yapilacak_odeme.csv","r")
                    kasadan_odeme = open("hesap_dosyalari/kasadan_odeme.csv","r")
                    kasadisi_odeme = open("hesap_dosyalari/kasadisi_odeme.csv","r")
                    gider = open("hesap_dosyalari/gider.csv","r")
                    kasadan_alinan = open("hesap_dosyalari/kasadan_alinan.csv","r")
                    pos_gun_sonu = open("hesap_dosyalari/pos_gun_sonu.csv","r")
                    alinan_odeme = open("hesap_dosyalari/odeme_al.csv","r")
                    alinacak_odeme = open("hesap_dosyalari/alinacak_odeme.csv","r")
                    
                    gecici_yapilacak_odeme = open("hesap_dosyalari/gecici_yapilacak_odeme.csv", "w")
                    gecici_kasadan_odeme = open("hesap_dosyalari/gecici_kasadan_odeme.csv", "w")
                    gecici_kasadisi_odeme = open("hesap_dosyalari/gecici_kasadisi_odeme.csv", "w")
                    gecici_gider = open("hesap_dosyalari/gecici_gider.csv", "w")
                    gecici_kasadan_alinan = open("hesap_dosyalari/gecici_kasadan_alinan.csv", "w")
                    gecici_pos_gun_sonu = open("hesap_dosyalari/gecici_pos_gun_sonu.csv", "w")
                    gecici_alinan_odeme = open("hesap_dosyalari/gecici_odeme_al.csv","w")
                    gecici_alinacak_odeme = open("hesap_dosyalari/gecici_alinacak_odeme.csv","w")

                    if firma == "TÜMÜ":
                        
                        for i in yapilacak_odeme:
                            yaz = "Yapilacak Odeme," + i
                            sonuc_dosyasi.write(yaz)
                            gecici_yapilacak_odeme.write(i)
                        
                        for i in alinan_odeme:
                            yaz = "Alinan Odeme," + i
                            sonuc_dosyasi.write(yaz)
                            gecici_alinan_odeme.write(i)
                        
                        for i in alinacak_odeme:
                            yaz = "Alinacak Odeme," + i
                            sonuc_dosyasi.write(yaz)
                            gecici_alinacak_odeme.write(i)

                        for i in kasadan_odeme:
                            yaz = "Kasadan Odeme," + i 
                            sonuc_dosyasi.write(yaz)
                            gecici_kasadan_odeme.write(i)

                        for i in kasadisi_odeme:
                            yaz = "Kasa Disi Odeme," + i
                            sonuc_dosyasi.write(yaz)
                            gecici_kasadisi_odeme.write(i)

                        for i in gider:
                            yaz = "Gider," + i
                            sonuc_dosyasi.write(yaz)
                            gecici_gider.write(i)
                        
                        for i in kasadan_alinan:
                            yaz = "Kasadan Alinan," + i
                            sonuc_dosyasi.write(yaz)
                            gecici_kasadan_alinan.write(i)
                        
                        for i in pos_gun_sonu:
                            yaz = "POS Gun Sonu," + i
                            sonuc_dosyasi.write(yaz)
                            gecici_pos_gun_sonu.write(i)
                        
                        sonuc_dosyasi.close()
                        gecici_kasadan_odeme.close()
                        gecici_kasadan_alinan.close()
                        gecici_gider.close()
                        gecici_kasadisi_odeme.close()
                        gecici_pos_gun_sonu.close()
                        gecici_yapilacak_odeme.close()
                        gecici_alinan_odeme.close()
                        gecici_alinacak_odeme.close()
                        #YAZININ ALINMASI VE TARİHE GÖRE ELENMESİ
                    
                        yazimiz = pd.read_csv("hesap_dosyalari/gecici_sonuc_dosyasi.csv",header=None,encoding = "ISO-8859-1")
                        yazimiz[1] = pd.to_datetime(yazimiz[1],dayfirst=True)
                        mask = (yazimiz[1] >= baslangic_tarihi1) & (yazimiz[1] <= bitis_tarihi1)
                        yazimiz = yazimiz.loc[mask]

                        pencere = Tk()
                        pencere.title("Göster")
                        pencere.geometry("1200x600")
                        label_tepe = Label(pencere,text=str(str(gun_araligi) + " günlük sonuçlar gösteriliyor..."),bg="black",fg="red")
                        label_tepe.pack(fill=X)

                        
                        
                        try:
                            toplamim = pd.read_csv("hesap_dosyalari/gecici_sonuc_dosyasi.csv",header=None,encoding = "ISO-8859-1")
                            toplamim[1] = pd.to_datetime(toplamim[1],dayfirst=True)
                            mask = (toplamim[1] >= baslangic_tarihi1) & (toplamim[1] <= bitis_tarihi1)
                            toplamim = toplamim.loc[mask]
                            toplam_tam = 0
                            miktarlar = toplamim.iloc[:,1:2].values
                            for i in miktarlar:
                                toplam_tam = float(toplam_tam) + float(i)
                            """
                            top_lab = Label(pencere, text="Toplam:")
                            topl_lab_son = Label(pencere, text=int(toplam_tam))
                            top_lab.place(x=10,y=480)
                            topl_lab_son.place(x=70, y=480)
                            """
                        except pd.errors.EmptyDataError:
                            pass
                        
                        try:
                            kasadan_odenen = pd.read_csv("hesap_dosyalari/gecici_kasadan_odeme.csv",header=None,encoding = "ISO-8859-1")
                            kasadan_odenen[0] = pd.to_datetime(kasadan_odenen[0],dayfirst=True)
                            mask = (kasadan_odenen[0] >= baslangic_tarihi1) & (kasadan_odenen[0] <= bitis_tarihi1)
                            kasadan_odenen = kasadan_odenen.loc[mask]
                            toplam_kas_od = 0
                            miktarlar1 = kasadan_odenen.iloc[:,1:2].values
                            for i in miktarlar1:
                                toplam_kas_od = float(toplam_kas_od) + float(i)
                            """
                            top_kas_od_lab = Label(pencere, text="Kasadan Ödeme:")
                            topl_kas_od_lab_son = Label(pencere, text=int(toplam_kas_od))
                            top_kas_od_lab.place(x=220,y=480)
                            topl_kas_od_lab_son.place(x=335, y=480)
                            """
                        except pd.errors.EmptyDataError:
                            pass

                        try:
                            kasadan_alinan = pd.read_csv("hesap_dosyalari/gecici_kasadan_alinan.csv",header=None,encoding = "ISO-8859-1")
                            kasadan_alinan[0] = pd.to_datetime(kasadan_alinan[0],dayfirst=True)
                            mask = (kasadan_alinan[0] >= baslangic_tarihi1) & (kasadan_alinan[0] <= bitis_tarihi1)
                            kasadan_alinan = kasadan_alinan.loc[mask]
                            toplam_kas_al = 0
                            miktarlar2 = kasadan_alinan.iloc[:,1:2].values
                            for i in miktarlar2:
                                toplam_kas_al = float(toplam_kas_al) + float(i)
                            """
                            top_kas_al_lab = Label(pencere, text="Kasadan Alınan:")
                            topl_kas_al_lab_son = Label(pencere, text=int(toplam_kas_al))
                            top_kas_al_lab.place(x=430,y=480)
                            topl_kas_al_lab_son.place(x=550, y=480)
                            """
                        except pd.errors.EmptyDataError:
                            pass

                        try:
                            kasadisi_odenen = pd.read_csv("hesap_dosyalari/gecici_kasadisi_odeme.csv",header=None,encoding = "ISO-8859-1")
                            kasadisi_odenen[0] = pd.to_datetime(kasadisi_odenen[0],dayfirst=True)
                            mask = (kasadisi_odenen[0] >= baslangic_tarihi1) & (kasadisi_odenen[0] <= bitis_tarihi1)
                            kasadisi_odenen = kasadisi_odenen.loc[mask]
                            toplam_kasadisi_od = 0
                            miktarlar3 = kasadisi_odenen.iloc[:,1:2].values
                            for i in miktarlar3:
                                toplam_kasadisi_od = float(toplam_kasadisi_od) + float(i)
                            """
                            top_kasadisi_od_lab = Label(pencere, text="Kasa Dışı Ödeme:")
                            topl_kasadisi_od_lab_son = Label(pencere, text=int(toplam_kasadisi_od))
                            top_kasadisi_od_lab.place(x=10,y=520)
                            topl_kasadisi_od_lab_son.place(x=130, y=520)
                            """
                        except pd.errors.EmptyDataError:
                            pass

                        try:
                            yapilacak_od = pd.read_csv("hesap_dosyalari/gecici_yapilacak_odeme.csv",header=None,encoding = "ISO-8859-1")
                            yapilacak_od[0] = pd.to_datetime(yapilacak_od[0],dayfirst=True)
                            mask = (yapilacak_od[0] >= baslangic_tarihi1) & (yapilacak_od[0] <= bitis_tarihi1)
                            yapilacak_od = yapilacak_od.loc[mask]
                            toplam_yapilacak_od = 0
                            miktarlar4 = yapilacak_od.iloc[:,1:2].values
                            for i in miktarlar4:
                                toplam_yapilacak_od = float(toplam_yapilacak_od) + float(i)
                            """
                            top_yap_od_lab = Label(pencere, text="Yapılacak Ödeme:")
                            topl_yap_od_lab_son = Label(pencere, text=int(toplam_yapilacak_od))
                            top_yap_od_lab.place(x=220,y=520)
                            topl_yap_od_lab_son.place(x=340, y=520)
                            """
                        except pd.errors.EmptyDataError:
                            pass

                        try:
                            gid = pd.read_csv("hesap_dosyalari/gecici_gider.csv",header=None,encoding = "ISO-8859-1")
                            gid[0] = pd.to_datetime(gid[0],dayfirst=True)
                            mask = (gid[0] >= baslangic_tarihi1) & (gid[0] <= bitis_tarihi1)
                            gid = gid.loc[mask]
                            toplam_gid = 0
                            miktarlar5 = gid.iloc[:,1:2].values
                            for i in miktarlar5:
                                toplam_gid = float(toplam_gid) + float(i)
                            """
                            top_gid_lab = Label(pencere, text="Gider:")
                            topl_gid_son = Label(pencere, text=int(toplam_gid))
                            top_gid_lab.place(x=430,y=520)
                            topl_gid_son.place(x=475, y=520)
                            """
                        except pd.errors.EmptyDataError:
                            pass
                        
                        try:
                            al_od = pd.read_csv("hesap_dosyalari/gecici_odeme_al.csv",header=None,encoding = "ISO-8859-1")
                            al_od[0] = pd.to_datetime(al_od[0],dayfirst=True)
                            mask = (al_od[0] >= baslangic_tarihi1) & (al_od[0] <= bitis_tarihi1)
                            al_od = al_od.loc[mask]
                            toplam_al_od = 0
                            miktarlar6 = al_od.iloc[:,1:2].values
                            for i in miktarlar6:
                                toplam_al_od = float(toplam_al_od) + float(i)
                            """
                            top_al_od_lab = Label(pencere, text="Alınan Ödeme:")
                            topl_al_od_lab_son = Label(pencere, text=int(toplam_al_od))
                            top_al_od_lab.place(x=10,y=560)
                            topl_al_od_lab_son.place(x=130, y=560)
                            """
                        except pd.errors.EmptyDataError:
                            pass

                        try:
                            alin_od = pd.read_csv("hesap_dosyalari/gecici_alinacak_odeme.csv",header=None,encoding = "ISO-8859-1")
                            alin_od[0] = pd.to_datetime(alin_od[0],dayfirst=True)
                            mask = (alin_od[0] >= baslangic_tarihi1) & (alin_od[0] <= bitis_tarihi1)
                            alin_od = alin_od.loc[mask]
                            toplam_alin_od = 0
                            miktarlar7 = alin_od.iloc[:,1:2].values
                            for i in miktarlar7:
                                toplam_alin_od = float(toplam_alin_od) + float(i)
                            """
                            top_alin_od_lab = Label(pencere, text="Alınacak Ödeme:")
                            topl_alin_od_lab_son = Label(pencere, text=int(toplam_alin_od))
                            top_alin_od_lab.place(x=220,y=560)
                            topl_alin_od_lab_son.place(x=340, y=560)
                            """
                        except pd.errors.EmptyDataError:
                            pass

                        try:
                            pos_gun_sonu = pd.read_csv("hesap_dosyalari/gecici_pos_gun_sonu.csv",header=None,encoding = "ISO-8859-1")
                            pos_gun_sonu[0] = pd.to_datetime(pos_gun_sonu[0],dayfirst=True)
                            mask = (pos_gun_sonu[0] >= baslangic_tarihi1) & (pos_gun_sonu[0] <= bitis_tarihi1)
                            pos_gun_sonu = pos_gun_sonu.loc[mask]
                            pos_gun_sonu_toplam = 0
                            miktarlar11 = pos_gun_sonu.iloc[:,1:2].values
                            for i in miktarlar11:
                                pos_gun_sonu_toplam = float(pos_gun_sonu_toplam) + float(i)
                            """
                            top_lab = Label(pencere, text="Toplam:")
                            topl_lab_son = Label(pencere, text=int(toplam_tam))
                            top_lab.place(x=10,y=480)
                            topl_lab_son.place(x=70, y=480)
                            """
                        except pd.errors.EmptyDataError:
                            pass
                        """
                        try:
                            
                            sonucum = ((toplam_kas_od + toplam_kasadisi_od) - toplam_yapilacak_od) + (toplam_alin_od - toplam_al_od)
                            if sonucum < 0:
                                sonucum = -1*sonucum
                                sonuc = Label(pencere, text="Toplam Alacak:", fg="green")
                                sonuc_son = Label(pencere, fg="green", text=float(format(sonucum,".2f")))
                                sonuc.place(x=430,y=560)
                                sonuc_son.place(x=550, y=560)
                            else:
                                sonuc = Label(pencere, text="Toplam Borç:", fg="red")
                                sonuc_son = Label(pencere, fg="red", text=float(format(sonucum,".2f")))
                                sonuc.place(x=430,y=560)
                                sonuc_son.place(x=550, y=560)

                        except pd.errors.EmptyDataError:
                            pass
                        """
                        label_yapod = Label(pencere, text="\nYapılacak Ödeme Toplam:")
                        label_yapod_sonuc = Label(pencere, text=format(float(toplam_yapilacak_od),".2f"))
                        label_yapod.place(x=20, y=40)
                        label_yapod_sonuc.place(x=200, y=57)
                        label_kasod = Label(pencere, text="\nKasadan Ödenen Toplam:")
                        label_kasod_sonuc = Label(pencere, text=format(float(toplam_kas_od),".2f"))
                        label_kasod.place(x=20, y=80)
                        label_kasod_sonuc.place(x=200, y=97)
                        label_kasdis = Label(pencere, text="\nKasa Dışı Ödeme Toplam:")
                        label_kasdis_sonuc = Label(pencere, text=format(float(toplam_kasadisi_od),".2f"))
                        label_kasdis.place(x=20, y=120)
                        label_kasdis_sonuc.place(x=200, y=137)
                        label_gid = Label(pencere, text="Gider Toplam:")
                        label_gid_sonuc = Label(pencere, text=format(float(toplam_gid),".2f"))
                        label_gid.place(x=300, y=190)
                        label_gid_sonuc.place(x=400, y=190)
                        label_kas_al = Label(pencere, text="\nKasadan Alınan Toplam:")
                        label_kas_al_sonuc = Label(pencere, text=format(float(toplam_kas_al),".2f"))
                        label_kas_al.place(x=300, y=80)
                        label_kas_al_sonuc.place(x=470, y=97)
                        label_pos = Label(pencere, text="\nPos Gün Sonu Toplam:")
                        label_pos_sonuc = Label(pencere, text=format(float(pos_gun_sonu_toplam),".2f"))
                        label_pos.place(x=300, y=120)
                        label_pos_sonuc.place(x=470, y=137)
                        
                        ayirma_cizgisi = Label(pencere,text="-------------------------------------------------------------------------------------------------------------")
                        ayirma_cizgisi.place(y=160)

                        toplam_ciro = toplam_kas_al + toplam_kas_od + pos_gun_sonu_toplam - (pos_gun_sonu_toplam*0.0245) + toplam_al_od
                        toplam_odeme = toplam_kas_od + toplam_kasadisi_od
                        kasa_brut = (toplam_ciro - toplam_odeme)
                        kasa_net = kasa_brut - toplam_gid
                        pos_kaybı = pos_gun_sonu_toplam*0.0245

                        ciro = Label(pencere,text="Toplam Ciro:")
                        ciro_sonucu = Label(pencere,text=format(float(toplam_ciro),".2f"))
                        ciro.place(x=20,y=190)
                        ciro_sonucu.place(x=140,y=190)

                        odeme = Label(pencere,text="Toplam Ödeme:")
                        odeme_sonucu = Label(pencere,text=format(float(toplam_odeme),".2f"))
                        odeme.place(x=20,y=230)
                        odeme_sonucu.place(x=140,y=230)

                        kasa_br = Label(pencere,text="Kasa Brüt:")
                        kasa_br_sonucu = Label(pencere,text=format(float(kasa_brut),".2f"))
                        kasa_br.place(x=300,y=230)
                        kasa_br_sonucu.place(x=400,y=230)

                        kasa_n = Label(pencere,text="Kasa Net:")
                        kasa_n_sonucu = Label(pencere,text=format(float(kasa_net),".2f"))
                        kasa_n.place(x=300,y=270)
                        kasa_n_sonucu.place(x=400,y=270)

                        pos_k = Label(pencere,text="POS Kaybı:")
                        pos_k_sonucu = Label(pencere,text=format(float(pos_kaybı),".2f"))
                        pos_k.place(x=20,y=270)
                        pos_k_sonucu.place(x=140,y=270)

                        al_od = Label(pencere,text="Alınan Ödeme:")
                        al_od_sonucu = Label(pencere,text=format(float(alinan_odeme_toplam),".2f"))
                        al_od.place(x=300,y=57)
                        al_od_sonucu.place(x=470,y=57)

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
                        """
                        borc_alacak = (toplam_alin_od - toplam_al_od)

                        if borc_alacak > 0:
                            veresiye = Label(pencere,text="TOPLAM BORCUNUZ VAR:", bg ="red")
                            veresiye_sonucu = Label(pencere,text=str(format(float(borc_alacak), ".2f")))
                            veresiye.place(x=20,y=520)
                            veresiye.place(x=140,y=520)
                            veresiye_sonucu.place(x=400,y=520)
                        else:
                            veresiye = Label(pencere,text="TOPLAM ALACAĞINIZ ALACAĞINIZ VAR:", bg ="green")
                            veresiye_sonucu = Label(pencere,text=str(format(float(borc_alacak), ".2f")))
                            veresiye.place(x=20,y=520)
                            veresiye.place(x=140,y=520)
                            veresiye_sonucu.place(x=400,y=520)
                        """
                        def tarih_goreceli(Event):
                            yazi_yerimiz = Text(pencere, bg="black", fg="green")
                            #yazi_yerimiz.insert(INSERT, yazim)
                            yazi_yerimiz.insert(INSERT, yazimiz.sort_values(by=[1])) #1. kolona göre sıraladık
                            yazi_yerimiz.place(x=600, y=60)
                            kaydir.config(command=yazi_yerimiz.yview)
                            
                        def miktar_goreceli(Event):
                            yazi_yerimiz = Text(pencere, bg="black", fg="green")
                            #yazi_yerimiz.insert(INSERT, yazim)
                            yazi_yerimiz.insert(INSERT, yazimiz.sort_values(by=[2])) #2. kolona göre sıraladık
                            yazi_yerimiz.place(x=600, y=60)
                            kaydir.config(command=yazi_yerimiz.yview)
                        
                        tarihe_gore = Button(pencere, text="Tarihe Göre Sırala")
                        miktara_gore = Button(pencere, text="Miktara Göre Sırala")
                        tarihe_gore.bind("<Button-1>", tarih_goreceli)
                        miktara_gore.bind("<Button-1>", miktar_goreceli)
                        tarihe_gore.place(x=830,y=30)
                        miktara_gore.place(x=650, y=30)
                            
                        yazi_yerimiz = Text(pencere, bg="black", fg="green")
                        #yazi_yerimiz.insert(INSERT, yazim)
                        yazi_yerimiz.insert(INSERT, yazimiz) 
                        yazi_yerimiz.place(x=600, y=60)

                        kaydir = Scrollbar(pencere)
                        kaydir.pack(side=RIGHT, fill=Y)
                        yazi_yerimiz.config(yscrollcommand=kaydir.set)
                        kaydir.config(command=yazi_yerimiz.yview)
                        #yazi_yerimiz.pack(side=BOTTOM, fill=X)

                    else:

                        #burada dosya işlemleri ile yapıyoruz...
                        yapilacak_odeme1 = open("hesap_dosyalari/yapilacak_odeme.csv", "r")
                        kasadan_odeme1 = open("hesap_dosyalari/kasadan_odeme.csv", "r")
                        kasadisi_odeme1 = open("hesap_dosyalari/kasadisi_odeme.csv", "r")
                        gider1 = open("hesap_dosyalari/gider.csv", "r")
                        kasadan_alinan1 = open("hesap_dosyalari/kasadan_alinan.csv", "r")
                        alinan_odeme1 = open("hesap_dosyalari/odeme_al.csv","r")
                        alinacak_odeme1 = open("hesap_dosyalari/alinacak_odeme.csv","r")
                        #pos_gun_sonu1 = open("hesap_dosyalari/pos_gun_sonu.csv", "r")

                        gecici_yapilacak_odeme = open("hesap_dosyalari/gecici_yapilacak_odeme.csv", "w")
                        gecici_kasadan_odeme = open("hesap_dosyalari/gecici_kasadan_odeme.csv", "w")
                        gecici_kasadisi_odeme = open("hesap_dosyalari/gecici_kasadisi_odeme.csv", "w")
                        gecici_gider = open("hesap_dosyalari/gecici_gider.csv", "w")
                        gecici_kasadan_alinan = open("hesap_dosyalari/gecici_kasadan_alinan.csv", "w")
                        gecici_pos_gun_sonu = open("hesap_dosyalari/gecici_pos_gun_sonu.csv", "w")
                        gecici_alinan_odeme = open("hesap_dosyalari/gecici_odeme_al.csv","w")
                        gecici_alinacak_odeme = open("hesap_dosyalari/gecici_alinacak_odeme.csv","w")

                        for i in yapilacak_odeme1:
                            if i.endswith(firma):
                                hepsi = "Yapılacak Ödeme, " + str(i)
                                sonuc_dosyası.write(hepsi)
                                gecici_yapilacak_odeme.write(i)
                        for i in alinan_odeme1:
                            if i.endswith(firma):
                                hepsi = "Alınan Ödeme, " + str(i)
                                sonuc_dosyası.write(hepsi)
                                gecici_alinan_odeme.write(i)
                        for i in alinacak_odeme1:
                            if i.endswith(firma):
                                hepsi = "Alınacak Ödeme, " + str(i)
                                sonuc_dosyası.write(hepsi)
                                gecici_alinacak_odeme.write(i)
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
                        gecici_alinan_odeme.close()
                        gecici_alinacak_odeme.close()
                        #BURADA VERİNİN İÇİNDEKİ BİR KOLONDAN TOPLAMLARI ALDIK VE YAZDIRDIK.
                        
                        yazimiz = pd.read_csv("hesap_dosyalari/gecici_sonuc_dosyasi.csv",header=None,encoding = "ISO-8859-1")
                        yazimiz[1] = pd.to_datetime(yazimiz[1],dayfirst=True)
                        mask = (yazimiz[1] >= baslangic_tarihi1) & (yazimiz[1] <= bitis_tarihi1)
                        yazimiz = yazimiz.loc[mask]

                        pencere = Tk()
                        pencere.title("Göster")
                        pencere.geometry("670x600")
                        label_tepe = Label(pencere,text=str(str(gun_araligi) + " günlük sonuçlar gösteriliyor..."),bg="black",fg="red")
                        label_tepe.pack(fill=X)
                        
                        try:
                            kasadan_odenen = pd.read_csv("hesap_dosyalari/gecici_kasadan_odeme.csv",header=None,encoding = "ISO-8859-1")
                            kasadan_odenen[0] = pd.to_datetime(kasadan_odenen[0],dayfirst=True)
                            mask = (kasadan_odenen[0] >= baslangic_tarihi1) & (kasadan_odenen[0] <= bitis_tarihi1)
                            kasadan_odenen = kasadan_odenen.loc[mask]
                            toplam_kas_od = 0
                            miktarlar1 = kasadan_odenen.iloc[:,1:2].values
                            for i in miktarlar1:
                                toplam_kas_od = float(toplam_kas_od) + float(i)

                            top_kas_od_lab = Label(pencere, text="Kasadan Ödeme:")
                            topl_kas_od_lab_son = Label(pencere, text=int(toplam_kas_od))
                            top_kas_od_lab.place(x=220,y=480)
                            topl_kas_od_lab_son.place(x=335, y=480)

                        except pd.errors.EmptyDataError:
                            pass

                        try:
                            kasadan_alinan = pd.read_csv("hesap_dosyalari/gecici_kasadan_alinan.csv",header=None,encoding = "ISO-8859-1")
                            kasadan_alinan[0] = pd.to_datetime(kasadan_alinan[0],dayfirst=True)
                            mask = (kasadan_alinan[0] >= baslangic_tarihi1) & (kasadan_alinan[0] <= bitis_tarihi1)
                            kasadan_alinan = kasadan_alinan.loc[mask]
                            toplam_kas_al = 0
                            miktarlar2 = kasadan_alinan.iloc[:,1:2].values
                            for i in miktarlar2:
                                toplam_kas_al = float(toplam_kas_al) + float(i)

                            top_kas_al_lab = Label(pencere, text="Kasadan Alınan:")
                            topl_kas_al_lab_son = Label(pencere, text=int(toplam_kas_al))
                            top_kas_al_lab.place(x=430,y=480)
                            topl_kas_al_lab_son.place(x=550, y=480)

                        except pd.errors.EmptyDataError:
                            pass

                        try:
                            kasadisi_odenen = pd.read_csv("hesap_dosyalari/gecici_kasadisi_odeme.csv",header=None,encoding = "ISO-8859-1")
                            kasadisi_odenen[0] = pd.to_datetime(kasadisi_odenen[0],dayfirst=True)
                            mask = (kasadisi_odenen[0] >= baslangic_tarihi1) & (kasadisi_odenen[0] <= bitis_tarihi1)
                            kasadisi_odenen = kasadisi_odenen.loc[mask]
                            toplam_kasadisi_od = 0
                            miktarlar3 = kasadisi_odenen.iloc[:,1:2].values
                            for i in miktarlar3:
                                toplam_kasadisi_od = float(toplam_kasadisi_od) + float(i)

                            top_kasadisi_od_lab = Label(pencere, text="Kasa Dışı Ödeme:")
                            topl_kasadisi_od_lab_son = Label(pencere, text=int(toplam_kasadisi_od))
                            top_kasadisi_od_lab.place(x=10,y=520)
                            topl_kasadisi_od_lab_son.place(x=130, y=520)

                        except pd.errors.EmptyDataError:
                            pass

                        
                        try:
                            
                            top_lab = Label(pencere, text="Toplam Ödeme:")
                            topl_lab_son = Label(pencere, text=format(float(toplam_kasadisi_od + toplam_kas_od), ".2f"))
                            top_lab.place(x=10,y=480)
                            topl_lab_son.place(x=120, y=480)

                        except pd.errors.EmptyDataError:
                            pass
                        
                        try:
                            yapilacak_od = pd.read_csv("hesap_dosyalari/gecici_yapilacak_odeme.csv",header=None,encoding = "ISO-8859-1")
                            yapilacak_od[0] = pd.to_datetime(yapilacak_od[0],dayfirst=True)
                            mask = (yapilacak_od[0] >= baslangic_tarihi1) & (yapilacak_od[0] <= bitis_tarihi1)
                            yapilacak_od = yapilacak_od.loc[mask]
                            toplam_yapilacak_od = 0
                            miktarlar4 = yapilacak_od.iloc[:,1:2].values
                            for i in miktarlar4:
                                toplam_yapilacak_od = float(toplam_yapilacak_od) + float(i)

                            top_yap_od_lab = Label(pencere, text="Yapılacak Ödeme:")
                            topl_yap_od_lab_son = Label(pencere, text=int(toplam_yapilacak_od))
                            top_yap_od_lab.place(x=220,y=520)
                            topl_yap_od_lab_son.place(x=340, y=520)

                        except pd.errors.EmptyDataError:
                            pass

                        try:
                            gid = pd.read_csv("hesap_dosyalari/gecici_gider.csv",header=None,encoding = "ISO-8859-1")
                            gid[0] = pd.to_datetime(gid[0],dayfirst=True)
                            mask = (gid[0] >= baslangic_tarihi1) & (gid[0] <= bitis_tarihi1)
                            gid = gid.loc[mask]
                            toplam_gid = 0
                            miktarlar5 = gid.iloc[:,1:2].values
                            for i in miktarlar5:
                                toplam_gid = float(toplam_gid) + float(i)
                            
                            top_gid_lab = Label(pencere, text="Gider:")
                            topl_gid_son = Label(pencere, text=int(toplam_gid))
                            top_gid_lab.place(x=430,y=520)
                            topl_gid_son.place(x=475, y=520)

                        except pd.errors.EmptyDataError:
                            pass

                        try:
                            al_od = pd.read_csv("hesap_dosyalari/gecici_odeme_al.csv",header=None,encoding = "ISO-8859-1")
                            al_od[0] = pd.to_datetime(al_od[0],dayfirst=True)
                            mask = (al_od[0] >= baslangic_tarihi1) & (al_od[0] <= bitis_tarihi1)
                            al_od = al_od.loc[mask]
                            toplam_al_od = 0
                            miktarlar6 = al_od.iloc[:,1:2].values
                            for i in miktarlar6:
                                toplam_al_od = float(toplam_al_od) + float(i)
                            
                            top_al_od_lab = Label(pencere, text="Alınan Ödeme:")
                            topl_al_od_son = Label(pencere, text=int(toplam_al_od))
                            top_al_od_lab.place(x=10,y=560)
                            topl_al_od_son.place(x=130, y=560)

                        except pd.errors.EmptyDataError:
                            pass
                        
                        try:
                            alin_od = pd.read_csv("hesap_dosyalari/gecici_alinacak_odeme.csv",header=None,encoding = "ISO-8859-1")
                            alin_od[0] = pd.to_datetime(alin_od[0],dayfirst=True)
                            mask = (alin_od[0] >= baslangic_tarihi1) & (alin_od[0] <= bitis_tarihi1)
                            alin_od = alin_od.loc[mask]
                            toplam_alin_od = 0
                            miktarlar7 = alin_od.iloc[:,1:2].values
                            for i in miktarlar7:
                                toplam_alin_od = float(toplam_alin_od) + float(i)
                            
                            top_alin_od_lab = Label(pencere, text="Alınacak Ödeme:")
                            topl_alin_od_son = Label(pencere, text=int(toplam_alin_od))
                            top_alin_od_lab.place(x=220,y=560)
                            topl_alin_od_son.place(x=340, y=560)

                        except pd.errors.EmptyDataError:
                            pass
                        """
                        try:
                            sonucum = float(format((float(toplam_kas_od + toplam_kasadisi_od - toplam_yapilacak_od)+((float(toplam_alin_od) - float(toplam_al_od))))))
                            if sonucum > 0:
                                sonuc = Label(pencere, text="BORÇ YOK/Toplam Alacağınız:", fg="green")
                                sonuc_son = Label(pencere, fg="green", text=float(format(sonucum,".2f")))
                                sonuc.place(x=430,y=560)
                                sonuc_son.place(x=600, y=560)
                            else:
                                sonuc = Label(pencere, text="Alacağınız Yok/BORÇ:", fg="red")
                                sonuc_son = Label(pencere, fg="red", text=float(format(sonucum,".2f")))
                                sonuc.place(x=430,y=560)
                                sonuc_son.place(x=570, y=560)
                        except pd.errors.EmptyDataError:
                            pass
                        """
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

def ayar_goster():
    
    import hesaplar
    ayar_pencere = Toplevel()
    ayar_pencere.title("Formulasyonları Göster")
    ayar_pencere.iconbitmap(r"desktop_icon.ico")
    ayar_pencere.geometry("700x300")
    hesaplar.ayarpen(ayar_pencere)

    ayar_pencere.mainloop()

def pos_degis():
    
    import hesaplar
    pen = Tk()
    pen.title("POS Oranı")
    pen.geometry("230x200")
    hesaplar.pos_pen(pen)

    pen.mainloop()

def firma_silme():
    
    import hesaplar
    pen = Tk()
    pen.title("Firma Silme Penceresi")
    pen.geometry("310x150")
    hesaplar.firma_sil(pen)

    pen.mainloop()

def kayit():
    messagebox.showwarning("UYARI!","Programı yeniden başlattıktan sonra kayıtlarınız güncellenecektir.")

def gorsellestir():
    
    import gorsel
    master = Toplevel()
    master.geometry("300x400")
    master.title("Veri Görselleştirme")
    master.iconbitmap(r"desktop_icon.ico")
    gorsel.grafik_olustur(master)

    master.mainloop()

firmalar_oku = open("firmalar.csv", "r")
pencere = Tk()
pencere.title("Market Programı")
pencere.iconbitmap(r"desktop_icon.ico")
pencere.geometry("780x350")
background_image=PhotoImage(file="Wallpaper-1.png")
background_label = Label(pencere, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=0, relwidth=1, relheight=1)
pencere.attributes('-alpha', 0.95)
pencere.resizable(0,0)
giris_pen(pencere)

mainloop()
