# book-reading-planner

<img src="https://raw.githubusercontent.com/savsay/book-reading-planner/refs/heads/main/readmeresim.png" alt="result">

# 365 Günlük Kitap Okuma Planı Oluşturucu

Bu uygulama, "Ölmeden Önce Okunması Gereken 1289 Kitap" listesinden ilham alınarak geliştirilmiştir. günlük okuma hedefinize göre bu liste icinden yıllık kitap okuma planı oluşturmanıza yardımcı olur.

Calisan uygulamaya asagidaki link uzerinden ulasabilirsiniz.

https://books-need-to-read-before-die.streamlit.app/

## Özellikler

- Günlük sayfa hedefine göre plan oluşturma
- Kitapları sayfa sayısına göre sıralama
- Detaylı istatistikler
- Kullanıcı dostu arayüz

## 📖 Nasıl Kullanılır?

1. Excel dosyanızı (`kitap-liste.xlsx`) uygulama ile aynı dizine yerleştirin
2. Uygulamayı çalıştırın
3. Günlük okuyabileceğiniz sayfa sayısını girin
4. "Okuma Planı Oluştur" butonuna tıklayın
5. Size özel oluşturulan okuma planını inceleyin

## 📊 Excel Dosya Formatı

Kitap listeniz aşağıdaki sütunları içermelidir:
- `Sira No`: Kitabın sıra numarası
- `Kitap-tr`: Kitabın Türkçe adı
- `book`: Kitabın orijinal adı
- `writer`: Yazarın adı
- `sayfa`: Kitabın sayfa sayısı
  
## 🔄 Listeyi Özelleştirme

Excel dosyasını düzenleyerek kendi okuma listenizi oluşturabilirsiniz:
1. Okuduğunuz kitapları silebilir
2. Yeni kitaplar ekleyebilir
3. Sayfa sayılarını güncelleyebilirsiniz

## 📱 Örnek Çıktı

Uygulama size şu bilgileri sunar:
- Günlük okuma hedefiniz
- Yıllık toplam sayfa hedefiniz
- Bir yılda bitirebileceğiniz tahmini kitap sayısı
- Her kitap için tahmini okuma süresi

## ⚙️ Gereksinimler

- Python 3.7+
- Streamlit
- Pandas
- Openpyxl

## Kurulum

1. Repository'yi klonlayın:

  bash
git clone https://github.com/savsay/book-reading-planner.git

2. Gerekli kütüphaneleri yükleyin:
   
   bash
pip install -r requirements.txt

3. Uygulamayı çalıştırın:
   
  bash
streamlit run book_reading_planner.py

## Kullanım

1. Excel dosyanızı uygulama ile aynı dizine koyun
2. Günlük okuma hedefinizi girin
3. "Okuma Planı Oluştur" butonuna tıklayın

## Excel Dosya Formatı

Excel dosyanızda şu sütunlar bulunmalıdır:
- Sira No
- Kitap-tr
- book
- writer

## 🤝 Katkıda Bulunma

1. Bu repository'yi fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/yeniOzellik`)
3. Değişikliklerinizi commit edin (`git commit -m 'Yeni özellik eklendi'`)
4. Branch'inizi push edin (`git push origin feature/yeniOzellik`)
5. Pull Request oluşturun

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakınız.

## 🙏 Teşekkür

Bu uygulama, "Ölmeden Önce Okunması Gereken 1289 Kitap" listesinden ilham alınarak geliştirilmiştir.


