import streamlit as st

def suntik_css(file_css):
    with open(file_css) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

suntik_css("assets/style.css") # <-- Alamat untuk file di dalam 'pages'

# ... sisa kodemu ...
st.set_page_config(
    page_title="Tentang Kreator",
    page_icon="📕"
)
st.title("📕 TENTANG KREATOR EVOLUSIENNA")

col1,col2 = st.columns(2)
with col1 :
    st.image("assets/evolusienna_logo.png",width=200)
with col2 :
    st.header("FELI")
    st.write("Mahasiswi Akuntansi | Punya Visi Sosial Tinggi")
    st.markdown("""
        Boleh banget hubungi gue di :
            [TikTok](https://www.tiktok.com/@dailywithfelicia?_t=ZS-8yF0LA5Gj6G&_r=1)
            [Instagram](https://www.instagram.com/nadia_flciaa?igsh=MW05NTJ2YnB3cGZ1aA==)
    """)
st.subheader("VISI SOSIAL FELI📕")
st.write("""
Hi semua, perkenalkan gue Felicia,18 thn. Gue salah satu orang yg punya visi tinggi tentang pendidikan.
Gue ingin membuka peluang untuk semua orang mendapatkan pelajaran dan informasi yang ga diajarin di sekolah
karena banyak hal penting yang rasanya perlu banget dipelajarin.
""")
st.subheader("Apasih Mimpi Feli?")
st.write("""
Mimpi gue adalah membuka lapangan pekerjaan sebanyak mungkin di perusahaan edukasi yang stabil dan bisa 
membangun sekolah gratis di Indonesia untuk orang yang kurang mampu. Gue juga mau membantu teman-teman online gue
yang merasa 'perlu seseorang' jadi bisa saling menguatkan sama-sama. Semoga nanti bisa buat study group skala luas yaa
(masih mimpi dulu hehehe semoga bisa tercapai)    
""")
st.write("""
Disclaimer : Web ini simple banget karena aku belajar coding sendiri dari awal tanpa bantuan orang lain
Ga perfect tapi semoga web ini bisa membantu kalian yaa!!
""")

