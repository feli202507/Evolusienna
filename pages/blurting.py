import streamlit as st

st.set_page_config(
    page_title="Blurting Method",
    page_icon="⌛️"
)

def suntik_css(file_css):
    with open(file_css) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

suntik_css("assets/style.css") # <-- Alamat untuk file di dalam 'pages'

st.image("assets/evolusienna_logo.png", width=150)

# ... sisa kodemu ...
st.title("Blurting Method")
st.write("Metode yang banyak dipakai dan terbukti seru & berhasil. Gimana caranya?")
st.write("!Ingat! Informasi lo ga akan tersimpan kalo lo keluar ya...")

manual,online = st.tabs(["Blurting Manual","Blurting Online"])
with manual : 
    st.header("Cara pakai Blurting Method")
    st.markdown("""
    1. Siapkan buku catatan,selembar kertas,dan 2 warna pulpen (hitam dan merah / bebas)
    2. Baca buku / catatan kalian selama 10-15 menit. Pasang timer dan tutup bukunya saat timer bunyi.
    3. Tulis semua pemahaman lo sebanyak-banyaknya. Dengan menulis, lo bisa seolah-olah berada di ruang kelas
    lagi nulis jawaban kalian di kertas ujian.
    4. Setelah selesai, review hasilnya dengan catatan lo yg tadi dibaca. Gapapa kalo ga semua yg penting ketulis.
    5. Pakai pulpen warna lain, mulai koreksi dan tambahin informasi yg kelewat dan lo lupa.
    6. Pahami dan ingat kembali informasi yang lo lupain tadi. Artinya lo perlu fokus kesitu
    7. Kalau ada waktu, ulang sampe lo ingat semua materi dan udah dapet "feel" nya buat ngerjain ujian
    """)

with st.expander("⌛️ Klik disini buat tips dan hal pentingnya") :
    st.write("""
    1. Jangan cuma MENGHAFAL. Pahami baik-baik dan ubah pakai bahasa sendiri 
    (kecuali itu informasi yg harus akurat misalnya definisi menurut ahli,dll)
             
    2. Jangan kebiasaan "ngintip" catatannya saat lo udah stuck. Akui lo stuck dan tinggal 
    tambahin informasi itu saat lo koreksi. Jangan ngerasa gamau salah.
             
    3. Pecah topik itu menjadi bagian kecil yang bisa dipahami lebih mudah. Jangan coba semuanya sekaligus.
             
    4. Beri jeda buat otak kalian mikir. Jangan langsung ngulang karena ga akan efisien. Bisa diselang istirahat
    (sekitar 15 menit baru coba lagi)
    """)

with online:
    st.write("Kalau ga ada waktu, coba ketik latihannya, udah yakin baru pindahin ke kertas ya!")
    col_1,col_2 = st.columns(2)
    with col_1 :
        st.subheader("Informasi yg lo ingat")
        ingat = st.text_area("Ketik semua yg lo sudah pelajari",height=400)

    with col_2 :
        st.subheader("Koreksi dan Tambahkan")
        lupa = st.text_area("Ketik informasi yg terlewat",height=400)

    if st.button("Finish") :
        st.success("Yey! Beres! Sekarang buka buku lo dan koreksi!!")
        st.snow()
