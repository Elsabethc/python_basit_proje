to_do_list = []   #boş liste oluşturma


def ekle (to_do_list):
    task = input("Yapılacak görevi giriniz:")
    to_do_list.append(task)
    print("Görev eklendi")

def goster (to_do_list):
    print("Yapılacak Görevler: ")
    for task in to_do_list:
        print("-" + task)

def sil (to_do_list):
    silmek = input("Silmek istediğiniz görevi giriniz: ")
    if silmek in to_do_list:
        to_do_list.remove(silmek)
        print("Görev silindi")

    else:
        print("Bu isimde bir görev bulunmamaktadır.")

while True:
  print("""İşlemler:
1-Görev Ekleme
2-Görev Listesini Gösterme
3-Görev Silme
4-Çıkış""")
  islem = input("Yapmak istediğiniz işlemi seçiniz(1/2/3/4):")

  if islem == "1":
    ekle(to_do_list)
  elif islem == "2":
    goster(to_do_list)
  elif islem == "3":
    sil(to_do_list)
  elif islem == "4":
    print("Çıkış yapılıyor...")
    break
  else:
    print("Yanlış Seçim")



