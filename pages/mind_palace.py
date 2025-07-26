import streamlit as st

def suntik_css(file_css):
    with open(file_css) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

suntik_css("assets/style.css") # <-- Alamat untuk file di dalam 'pages'

# ... sisa kodemu ...
st.set_page_config(
    page_title="Mind Palace",
    page_icon="🧠"
)
st.image("assets/evolusienna_logo.png",width=200)
st.title("Metode Menghafal Mind Palace")
st.write("Teknik yang underrated dan dibilang banyak orang susah. Emang iya?")
tab_penjelasan,tab_latihan = st.tabs(["💡Penjelasan","✍️Latihan"])
with tab_penjelasan :
    st.header("Apa itu Mind Palace?")
    st.write("Mind Palace adalah teknik mnemonik yang menggunakan visualisasi ruang atau tempat yang familiar untuk membantu mengingat informasi")
    st.subheader("Itu bisa dipelajarin atau cuma beberapa orang yang bisa?")
    st.write("Jawabannya bisa dipelajari kokk. Kuncinya latihan dan fokus")
    st.subheader("Cara Belajar Mind Palace")
    st.markdown("""
    1.**Pilih 'lokasi(istana)' kalian. Bisa rumah, sekolah, kelas,kamar.**
    (semakin lo kenal posisi lokasi itu, semakin mudah ngebayanginnya)
            
    2.**Jelajahi tempat itu dan tentukan tempat spesifik dan jelas.** 
    (Misalnya : rumah : masuk dari pagar,ke ruang tamu, ke dapur, naik tangga, ke kamar) 
                 
    3.**Taruh informasi di salah satu tempat istana lo.**
    (Misalnya lo mau ingat daftar belanjaan. Bayangkan: susu ada di meja dapur, roti ada di atas rak,telur digantung di ruang lo)
    4. **Buat cerita aneh dan ga masuk akal jadi lebih mudah diingat**
    (Seperti contohnya telur digantung di lampu ruang tamu. Aneh kan? Tapi lo akan lebih mudah ingetnya!)
            
    5. **Jelajahi kembali istana kalian sambil mengingat informasi yang kalian taruh.**
    """)
with tab_latihan :
    st.subheader("Latihan : (jangan lupa untuk berpikir se-kreatif mungkin buat mempermudah ya)")
    item_1 =st.checkbox("Item #1: Gajah (misalnya:bayangin gajah masuk ke kulkas kalian)")
    item_2 = st.checkbox("Item #2: kupu-kupu (misalnya:bayangin banyak kupu-kupu masuk ke area dapur)")
    item_3 =st.checkbox("Item #3: kucing (misalnya:bayangin ada kucing warna pink lagi makan roti di meja makan)")
    item_4 =st.checkbox("Item #4: ikan (misalnya:bayangin ikan yang lagi minta tolong karena lagi digoreng)")
    item_5 =st.checkbox("Item #5: kelinci (misalnya: bayangin kelinci pakai seragam dan sarapan di meja makan bareng kucing tadi)")

    if item_1 and item_2 and item_3 and item_4 and item_5 :
        st.balloons()
        st.success("KEREN BANGET BERHASIL! Jangan lupa coba terus yaa")

       