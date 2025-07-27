import streamlit as st

st.set_page_config(
    page_title="Overthinking Page",
    page_icon="❤️‍🩹"
)

def suntik_css(file_css):
    with open(file_css) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

suntik_css("assets/style.css") # <-- Alamat untuk file di dalam 'pages'

st.image("assets/evolusienna_logo.png",width=150)
st.title("Overthinking Page")
st.subheader("Cara Menghilangkan Overthinking")

st.write("""
Disusun berdasarkan inspirasi quotes "If you still worry about the problem you overthink after praying about it,
it means you don't trust God enough and you're making the problem an idol". 
Bisa lo coba buat menghilangkan ovt lo, ingat ya gue ga save data sama sekali.
""")

nama = st.text_input("Kalo lo bisa milih nama, apa yg akan lo pilih(anggap dia versi lain diri lo)")
ovt = st.text_area ("Apa overthinking lo sekarang?")

if st.button("Selesai") :
    st.write(f"""
    Bagus,{nama},lo udah berhasil menemukan masalah itu. Sekarang Doa ke Tuhan. Minta ketenangan, petunjuk,
    solusi dan serahin semua ke Tuhan. 
    SELESAI DOA. Sekarang hapus semua text itu sama seperti lo menghapus overthinking itu dari otak lo.
    Permintaan dan "tolong" lo udah dindenger Tuhan. Tunggu waktunya dan terus berusaha.
    Percaya, jalannya akan ketemu.
     """)

st.warning("""
Lo hidup di masa sekarang. Liat sekeliling lo,itu mungkin adalah impian orang diluar sana.
Amati dan syukuri semuanya. Jangan buang waktu lo buat khawatir. Lo gak sendirian
""")

