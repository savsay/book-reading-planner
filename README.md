# book-reading-planner

![alt text]([https://github.com/savsay/book-reading-planner/blob/main/readmeresim.png])

# 365 Günlük Kitap Okuma Planı Oluşturucu

Bu uygulama, günlük okuma hedefinize göre yıllık kitap okuma planı oluşturmanıza yardımcı olur.

## Özellikler

- Günlük sayfa hedefine göre plan oluşturma
- Kitapları sayfa sayısına göre sıralama
- Detaylı istatistikler
- Kullanıcı dostu arayüz

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
- sayfa

