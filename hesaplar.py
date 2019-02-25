from tkinter import Tk
from tkinter import Label
from tkinter import messagebox
from tkinter import Entry
from tkinter import Button, BOTTOM
from tkinter.ttk import Combobox

class ayarpen():

    def __init__(self, master):
        pos_orani = format(float(open("hesap_dosyalari/pos_orani.txt","r").readlines()[0]),".4f")
        self.formulasyon_tarif=str("\n\nToplam Ciro: \nKasadan Alınan + Alınan Ödeme + Kasadan Ödeme + Pos Gün Sonu - Pos Kaybı \n\nToplam Ödeme: \nKasadan Ödeme + Kasadışı Ödeme\n\nKasa Brut: \nToplam Ciro - Toplam Ödeme\n\nKasa Net: \nKasa Brut - Gider\n\nPos Kaybı: \nPos Gün Sonu* Pos Kesilme Oranı ==> (Oran:{0})\n\nAlınacak Ödeme: Firmaya veya kişiye borç yazar. (Hesaplamalara etki etmez.)\nÖdeme Al: Firmanın veya kişinin borcunu siler. (Hesaplara etki eder.)".format(pos_orani))
        self.tarif_label = Label(master, text= self.formulasyon_tarif)
        self.tarif_label.pack()

class pos_pen():

    def __init__(self, master):
        pos_orani = format(float(open("hesap_dosyalari/pos_orani.txt","r").readlines()[0]),".4f")
        eski_pos_text= Label(master, text="Eski Pos Oranı:")
        eski_pos = Label(master, text=str(pos_orani))
        eski_pos_text.place(x=20,y=20)
        eski_pos.place(x=110, y=20)
        yeni_pos_text= Label(master, text="Yeni Oranı Giriniz:  (Ör: 0.0237)")
        yeni_pos_text.place(x=20, y=70)
        self.yeni_pos = Entry(master)
        self.yeni_pos.place(x=20, y=100)
        kaydet_but = Button(master, text="KAYDET", bd=2)
        kaydet_but.bind("<Button-1>", self.pos_oran_degis)
        kaydet_but.pack(side=BOTTOM)
    
    def pos_oran_degis(self, Event):
        yeni_oran = str(self.yeni_pos.get())
        yeni_oran = yeni_oran.replace(",",".")
        pos_dos = open("hesap_dosyalari/pos_orani.txt","w")
        pos_dos.write(yeni_oran)
        pos_dos.close()
        messagebox.showwarning("Kayıt Başarılı","Yeni POS Oranı ({}) Başarıyla Kaydedildi.".format(yeni_oran))

class firma_sil():


    def __init__(self,master):
        firma_adi = Label(master, text="Firma Adı:")
        firma_adi.place(x=130,y=20)

        arama = Label(master, text="Ara:")
        arama.place(x=20,y=20)
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
            self.listbox.delete(0, 'end')
            data = sorted(data, key=str.lower)
            for item in data:
                self.listbox.insert('end', item)
        
        firmalar_oku = open("firmalar.csv", "r")
        self.firmalar = firmalar_oku.readlines()
        test_list = self.firmalar

        entry =Entry(master)
        entry.place(x=20,y=50)
        entry.bind('<KeyRelease>', on_keyrelease)

        self.listbox = Combobox(master)
        self.listbox["values"] = test_list
        self.listbox.bind('<KeyRelease>', on_keyrelease)
        self.listbox.place(x=100,y=50)
        #listbox.bind('<Double-Button-1>', on_select)
        buton = Button(master, text="Seçimi Sil",bd=2)
        buton.place(x=10,y=10,relx=0.1,rely=0.2)
        buton.bind("<Button-1>", self.firma_sil_fonk)
        buton.pack(side=BOTTOM)
    
    def firma_sil_fonk(self, Event):

        firma_adi = str(self.listbox.get())
        firmalar_ok = open("firmalar.csv","r")
        firmalar_oku = firmalar_ok.readlines()
        firmalar_ok.close
        firmalar_yaz = open("firmalar.csv","w")
        for i in firmalar_oku:
            if firma_adi != i:
                firmalar_yaz.write(i)
        firmalar_yaz.close()
        messagebox.showwarning("İşlem Tamamlandı!","Firma Başarıyla Silindi.\nProgramı Yeniden Başlatın!")

