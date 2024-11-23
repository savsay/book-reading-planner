import streamlit as st
import pandas as pd
import math
import requests
import urllib.parse
from fuzzywuzzy import fuzz

st.set_page_config(
    page_title="Yıllık Okuma Planı Oluşturucu",
    layout="wide",
    initial_sidebar_state="collapsed"
)

@st.cache_data
def fetch_book_info(book_title, author_name):
    try:
        # API'den fetch ederken yanlış bilgileri çekmemek için fuzzy matching kullanıldı.
        url = f"https://openlibrary.org/search.json?title={urllib.parse.quote(book_title)}&fields=title,author_name,cover_i,first_publish_year,isbn,key"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data['docs']:
                filtered_books = []
                for book in data['docs']:
                    if 'author_name' in book:
                        for author in book['author_name']:
                            if fuzz.ratio(author_name.lower(), author.lower()) >= 70: #farklı değerler denenebilir. 50 ve altı eşleşme oranı ile hatalı kitaplar dönebiliyor. 
                                filtered_books.append(book)
                                break

                if filtered_books:
                    book_data = filtered_books[0]
                    cover_id = book_data.get('cover_i', None)
                    cover_url = (
                        f"https://covers.openlibrary.org/b/id/{cover_id}-L.jpg"
                        if cover_id else "https://via.placeholder.com/150?text=Kapak+Bulunamadı"
                    )
                    
                    description = None
                    if "key" in book_data:
                        details_url = f"https://openlibrary.org{book_data['key']}.json"
                        details_response = requests.get(details_url)
                        if details_response.status_code == 200:
                            details_data = details_response.json()
                            description = details_data.get("description")
                            if isinstance(description, dict):  
                                description = description.get("value")

                    return {
                        'Başlık': book_data.get('title', 'Bilinmiyor'),
                        'Yazar': ', '.join(book_data.get('author_name', ['Bilinmiyor'])),
                        'İlk Yayın Yılı': book_data.get('first_publish_year', 'Bilinmiyor'),
                        'Kapak URL': cover_url,
                        'Açıklama': description or "Bu kitap hakkında bilgi bulunamadı."
                    }
        return None
    except Exception as e:
        st.error(f"Kitap bilgileri alınırken hata oluştu: {str(e)}")
        return None

def create_reading_plan(daily_pages):
    try:        
        df = pd.read_excel('kitap-liste.xlsx')
        df['sayfa'] = pd.to_numeric(df['sayfa'], errors='coerce')
        df = df.dropna(subset=['sayfa'])

        total_pages_yearly = daily_pages * 365
        df_sorted = df.sort_values('sayfa', ascending=True)

        reading_plan = []
        cumulative_pages = 0

        for _, book in df_sorted.iterrows():
            if cumulative_pages + book['sayfa'] <= total_pages_yearly:
                encoded_book_name = urllib.parse.quote(book['book'])
                reading_plan.append({
                    'Sıra': len(reading_plan) + 1,
                    'Kitap Adı': book['Kitap-tr'],
                    'Orijinal Adı': book['book'],
                    'Yazar': book['writer'],
                    'Sayfa': int(book['sayfa']),
                    'Tahmini Okuma Süresi (Gün)': math.ceil(book['sayfa'] / daily_pages),
                    'Detaylı Bilgi': f"/?book={encoded_book_name}&author={urllib.parse.quote(book['writer'])}"
                })
                cumulative_pages += book['sayfa']
            else:
                break

        return reading_plan, cumulative_pages, total_pages_yearly

    except Exception as e:
        st.error(f"Bir hata oluştu: {str(e)}")
        return None, 0, 0

query_params = st.query_params
if 'book' in query_params and 'author' in query_params:
    book_title = query_params['book']
    author_name = query_params['author']
    st.title(f"Kitap Bilgileri: {book_title}")
    book_info = fetch_book_info(book_title, author_name)

    if book_info:
        st.image(book_info['Kapak URL'], caption=book_info['Başlık'], width=200)
        st.markdown(f"**Başlık:** {book_info['Başlık']}")
        st.markdown(f"**Yazar:** {book_info['Yazar']}")
        st.markdown(f"**İlk Yayın Yılı:** {book_info['İlk Yayın Yılı']}")
        st.markdown(f"**Kitap Hakkında:** {book_info['Açıklama']}")
    else:
        st.error("Kitap bilgileri bulunamadı.")
else:
    st.title("365 Günlük Kişiselleştirilmiş Okuma Planı")
    st.markdown("---")

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

            st.markdown("### 📚 Okuma Planınız")
            for plan in reading_plan:
                with st.container():
                    col1, col2, col3 = st.columns([1, 3, 2])
                    with col1:
                        st.write(f"**{plan['Sıra']}**")
                    with col2:
                        st.write(f"**Kitap Adı:** {plan['Kitap Adı']}")
                        st.write(f"**Orijinal Adı:** {plan['Orijinal Adı']}")
                        st.write(f"**Yazar:** {plan['Yazar']}")
                        st.write(f"**Sayfa:** {plan['Sayfa']}")
                        st.write(f"**Tahmini Süre:** {plan['Tahmini Okuma Süresi (Gün)']} gün")
                    with col3:
                        st.markdown(
                            f"[Detaylı Bilgi]({plan['Detaylı Bilgi']})",
                            unsafe_allow_html=True
                        )
                    st.markdown("---")
