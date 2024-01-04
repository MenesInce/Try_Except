def tam_sayiya_cevir():
   girdi = input("Bir ondalik sayi giriniz : ")
   print(f"Yuvarlama işleminin sonucu : {round(float(girdi))}")

tam_sayiya_cevir()

def tam_sayiya_cevir():
    girdi = input("Bir ondalik sayi giriniz : ")
    #print(f"Yuvarlama işleminin sonucu : {round(float(girdi))}")
    try:
       girdi = float(girdi)
       print(f"Yuvarlama işleminin sonucu : {round((girdi))}")
    except:
       print("{} girdisi ondalık tipe çevrilemiyor".format(girdi))

tam_sayiya_cevir()

def tam_sayiya_cevir():
    girdi = input("Bir ondalik sayi giriniz : ")
    status = " "
    try:
        girdi = float(girdi)
        print(f"Yuvarlama işleminin sonucu : {round((girdi))}")
        status = "basarili"
    except:
        print("{} girdisi ondalık tipe çevrilemiyor".format(girdi))
        status = "basarisiz"
    finally:
        print("Tam sayiya cevirme islemi {} olarak tamamlamdı,".format(status))

tam_sayiya_cevir()

def tam_sayiya_cevir_dongu():
    while True :
        girdi = input("Bir ondalik sayi giriniz : ")

        try:
            girdi = float(girdi)
            print(f"Yuvarlama işleminin sonucu : {round((girdi))}")
            break
        except:
            print("{} girdisi ondalık tipe çevrilemiyor".format(girdi))
            pass

tam_sayiya_cevir_dongu()