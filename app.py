import streamlit as st

def suntik_css(file_css):
    with open(file_css) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

suntik_css("assets/style.css") # <-- Alamat untuk app.py

# ... sisa kodemu ...
st.set_page_config(
    page_title="Feli's Sharing",
    page_icon="assets/panda_logo.png"
)
# --- Bagian Header ---
st.title("Hi, welcome to Feli's Sharing !")
st.header("Mau belajar efektif, belajar hal baru, dan cari hobby baru???")
# --- Tampilkan Logo Maskot ---
# Pastikan file 'assets/panda_logo.png' ada di folder yang sama
st.image("assets/panda_logo.png", width=200)

st.subheader("---Sedikit tujuan dari website ini---")
st.write(" Pernah ga sih belajar tapi rasanya susah banget? Udah belajar lama tetep aja nilainya segitu. (Permasalahan banyak orang termasuk aku hehe).")
st.write("Tenang aja,aku bakal share pengalaman pembelajaranaku buat membantu kalian (aku bukan ahli yaa, semua sesuai pengalaman)")
