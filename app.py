import streamlit as st

def suntik_css(file_css):
    with open(file_css) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

suntik_css("assets/style.css") # <-- Alamat untuk app.py

# ... sisa kodemu ...
st.set_page_config(
    page_title="Evolusienna",
    page_icon="assets/evolusienna_logo.png"
)

st.title("Hi Friends! Welcome to Evolusienna!")


col1,col2 = st.columns(2)
# Pastikan file 'assets/panda_logo.png' ada di folder yang sama
with col1 :
    st.image("assets/evolusienna_logo.png", width=200)

with col2 :
    st.header("Mau belajar efektif, belajar hal baru, dan cari hobby baru?")
    st.write("Menurut gue, metode belajar yg cocok itu tiap orang beda. Jadi, coba sebanyak mungkin dan analisis ya!")


st.write("""
Website ini semuanya dibuat anak accounting tanpa basic pendidikan coding ya, jadii
kalau mau cerita atau ada error tolong hubungi gue yaa bisa lewat tiktok atau instagram berikut :
""")
st.markdown("""
    [TikTok](https://www.tiktok.com/@dailywithfelicia?_t=ZS-8yF0LA5Gj6G&_r=1)
    [Instagram](https://www.instagram.com/nadia_flciaa?igsh=MW05NTJ2YnB3cGZ1aA==)
    [LinkedIn](https://www.linkedin.com/in/nadia-felicia-sujana?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)
""")

st.subheader("Kenapa sih gue ciptakan Evolusienna?")
st.markdown("""
Pernah ngerasain capek belajar lama tapi hasilnya jelek?
Ga ada dana buat belajar selain di sekolah?
Butuh komunitas belajar yang positif?
atau lo ga mau jadi si ambis di SMA, yang setelah lulus hilang arah?
...dan seribu alasan lain lo ga berkembang.

Disini kita ga akan bicara "toxic motivation"
Itu adalah hal yang buat gue jatuh sejatuh-jatuhnya fisik dan mental
Disini kita akan belajar kemajuan jangka panjang
Jadi kalian juga harus extra effort buat kampus dan cita-cita kalian.

Ada pertanyaan ini, KENAPA SEMUA GRATIS?
Karena gue tau gimana rasanya hemat sampe mikir 100x buat jajan di kantin
Karena gue bukan ahli, gue mau membangun dampak dan membantu

Gue cuma perempuan yang punya cita-cita "gila" bagi 9 dari 10 orang
Yang semua orang bilang mustahil, bahkan belajar coding aja dikatain
Gue mau bangun sekolah gratis,panti asuhan,panti jompo,dan shelter
Itu visi yang Tuhan kasih ke gue selama ini.
Saatnya eksekusi. Kalian juga.
""")