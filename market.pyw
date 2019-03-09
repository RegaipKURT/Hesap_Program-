"""
AUTHOR: REGAIP KURT
"""
import os
import datetime

tarih = datetime.datetime.now().strftime("%d/%m/%y")
date_now = datetime.datetime.strptime(tarih, "%d/%m/%y")

def ilkleme():
    
    def dosyalar_ac():
        firma = open("firmalar.csv", "a")
        gkg=open("hesap_dosyalari/gecici_kasadan_gider.csv","a")
        gkdg=open("hesap_dosyalari/gecici_kasadisi_gider.csv","a")
        gka=open("hesap_dosyalari/gecici_kasadan_alinan.csv","a")
        gko=open("hesap_dosyalari/gecici_kasadan_odeme.csv","a")
        gkdo=open("hesap_dosyalari/gecici_kasadisi_odeme.csv","a")
        gpgs=open("hesap_dosyalari/gecici_pos_gun_sonu.csv","a")
        gsd=open("hesap_dosyalari/gecici_sonuc_dosyasi.csv","a")
        gyo=open("hesap_dosyalari/gecici_yapilacak_odeme.csv","a")
        gol=open("hesap_dosyalari/gecici_odeme_al.csv","a")
        gad=open("hesap_dosyalari/gecici_alinacak_odeme.csv","a")
        gkardos = open("hesap_dosyalari/gecici_karsilik_dosyasi.csv","a")
        kg=open("hesap_dosyalari/kasadan_gider.csv","a")
        kdg=open("hesap_dosyalari/kasadisi_gider.csv","a")
        pgs=open("hesap_dosyalari/pos_gun_sonu.csv","a")
        yo=open("hesap_dosyalari/yapilacak_odeme.csv","a")
        ka=open("hesap_dosyalari/kasadan_alinan.csv","a")
        ko=open("hesap_dosyalari/kasadan_odeme.csv","a")
        kdo=open("hesap_dosyalari/kasadisi_odeme.csv","a")
        g=open("hesap_dosyalari/gider.csv","a")
        ol=open("hesap_dosyalari/odeme_al.csv","a")
        ad = open("hesap_dosyalari/alinacak_odeme.csv","a")
        kardos = open("hesap_dosyalari/karsilik_dosyasi.csv","a")
        bas_tar = open("hesap_dosyalari/bas_tar.csv","a")

        firma.close()
        gkg.close()
        gkdg.close()
        gka.close()
        gko.close()
        gkdo.close()
        gpgs.close()
        gsd.close()
        gyo.close()
        gol.close()
        gad.close()
        gkardos.close()
        kg.close()
        kdg.close()
        pgs.close()
        yo.close()
        ka.close()
        ko.close()
        kdo.close()
        g.close()
        ol.close()
        ad.close()
        kardos.close()
        bas_tar.close

    try:
        os.mkdir("hesap_dosyalari")
        dosyalar_ac()
        import platform
        version = platform.architecture()
        if version[0] == "64bit":
            os.system("pip install pandas-0.24.0-cp36-cp36m-win_amd64.whl")
            os.system("pip install seaborn")
        elif version[0] == "32bit":
            os.system("pip install pandas-0.24.0-cp36-cp36m-win32.whl")
            os.system("pip install seaborn")
        else:
            pass
        pos_or = open("hesap_dosyalari/pos_orani.txt","a")
        pos_or.write(str(0.0245))
        pos_or.close()
        bas_tar = open("hesap_dosyalari/bas_tar.csv","w")
        bas_tar.write(str(date_now))
        bas_tar.close()
    except FileExistsError:
        pass

if __name__ == "__main__":
    ilkleme()
    import ana_pencere
