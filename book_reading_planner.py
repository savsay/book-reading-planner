import streamlit as st
import pandas as pd
import math

# Streamlit konfigürasyonu - sayfa başında olmalı
st.set_page_config(
    page_title="Yıllık Okuma Planı Oluşturucu",
    layout="wide",
    initial_sidebar_state="collapsed"
)


def create_reading_plan(daily_pages):
    try:
        # Excel dosyasını oku
        df = pd.read_excel('kitap-liste.xlsx')

        # Sayfa sayısını sayısal değere çevir
        df['sayfa'] = pd.to_numeric(df['sayfa'], errors='coerce')
        df = df.dropna(subset=['sayfa'])

        # Yıllık toplam okuyabileceği sayfa sayısı
        total_pages_yearly = daily_pages * 365

        # Sayfa sayısına göre sırala (az sayfadan çoğa)
        df_sorted = df.sort_values('sayfa', ascending=True)

        # Okuma planı oluştur
        reading_plan = []
        cumulative_pages = 0

        for _, book in df_sorted.iterrows():
            if cumulative_pages + book['sayfa'] <= total_pages_yearly:
                reading_plan.append({
                    'Sıra': len(reading_plan) + 1,
                    'Kitap Adı': book['Kitap-tr'],
                    'Orijinal Adı': book['book'],
                    'Yazar': book['writer'],
                    'Sayfa': int(book['sayfa']),
                    'Tahmini Okuma Süresi (Gün)': math.ceil(book['sayfa'] / daily_pages)
                })
                cumulative_pages += book['sayfa']
            else:
                break

        return reading_plan, cumulative_pages, total_pages_yearly

    except Exception as e:
        st.error(f"Bir hata oluştu: {str(e)}")
        return None, 0, 0


# Başlık ve açıklama
st.title("365 Günlük Kişiselleştirilmiş Okuma Planı")
st.markdown("---")

# Kullanıcı girişi
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    daily_pages = st.number_input(
        "Günlük kaç sayfa okuyabilirsiniz?",
        min_value=1,
        max_value=1000,
        value=30,
        step=1,
        help="Günlük okuyabileceğiniz sayfa sayısını girin"
    )

if st.button("Okuma Planı Oluştur"):
    reading_plan, cumulative_pages, total_pages_yearly = create_reading_plan(daily_pages)

    if reading_plan:
        # İstatistikleri göster
        st.markdown("### 📊 Plan İstatistikleri")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Günlük Hedef", f"{daily_pages} sayfa")
        with col2:
            st.metric("Yıllık Hedef", f"{total_pages_yearly:,} sayfa")
        with col3:
            st.metric("Planlanan Kitap", f"{len(reading_plan)} adet")
        with col4:
            st.metric("Toplam Sayfa", f"{int(cumulative_pages):,}")

        # Okuma planını tablo olarak göster
        st.markdown("### 📚 Okuma Planınız")
        df_plan = pd.DataFrame(reading_plan)

        # Tabloyu özelleştir
        st.dataframe(
            df_plan,  # Tüm satırları göster
            column_config={
                "Sıra": st.column_config.NumberColumn(
                    "Sıra",
                    help="Kitap sırası",
                    format="%d"
                ),
                "Kitap Adı": st.column_config.TextColumn(
                    "Kitap Adı",
                    help="Kitabın Türkçe adı",
                    width="large"
                ),
                "Orijinal Adı": st.column_config.TextColumn(
                    "Orijinal Adı",
                    help="Kitabın orijinal adı",
                    width="large"
                ),
                "Yazar": st.column_config.TextColumn(
                    "Yazar",
                    help="Kitabın yazarı",
                    width="medium"
                ),
                "Sayfa": st.column_config.NumberColumn(
                    "Sayfa",
                    help="Kitabın sayfa sayısı",
                    format="%d"
                ),
                "Tahmini Okuma Süresi (Gün)": st.column_config.NumberColumn(
                    "Tahmini Süre (Gün)",
                    help="Tahmini okuma süresi",
                    format="%d"
                )
            },
            hide_index=True,
            use_container_width=True,
            height=5000  # Tablo yüksekliğini artır (piksel cinsinden)
        )