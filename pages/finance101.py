import streamlit as st

st.set_page_config(
    page_title="Basic School Finance",
    page_icon="💵"
)

def suntik_css(file_css):
    with open(file_css) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

suntik_css("assets/style.css") # <-- Alamat untuk file di dalam 'pages'

st.header("Haii! Ayo rencanakan finansialmu walau masih sekolah!")
st.write("""
Hal ini adalah salah satu hal yg aku harap aku tau pas masih sekolah,
karena abis lulus SMA langsung terjun ke kuliah, rasanya ga ada basic cara atur keuangan
sedangkan udah mulai harus hidup mandiri, bahkan jauh dari ortu. 
""")

st.warning("""
Jangan ragu untuk sesuaikan sama kebutuhan kalian yaa! Tapi tetep ingat, kesehatan nomor 1 !
""")
#INPUT UANG JAJAN
uang_jajan = st.number_input(
    "Ketik Jumlah Uang Jajan Kamu :",
    min_value=0,
    value=100000,
    step=10000,
    help="Masukkan Total Uang Jajan kamu dalam 1 Periode:"
)
frekuensi = st.radio(
    "Kamu dapat uang ini :",
    ("Harian","Mingguan","Bulanan"),
    horizontal=True
)
kebutuhan_pct = st.slider("Kebutuhan (Transportasi,Jajan,Kuota,dll)",0,100,50)

keinginan_pct= st.slider("Keinginan (Jajan,Hiburan,Game,dll)",0,100-kebutuhan_pct,30)

masa_depan_pct = 100-kebutuhan_pct-keinginan_pct
st.write(f"**Tabungan (Masa Depan)** : '{masa_depan_pct}'")

dana_kebutuhan = uang_jajan * (kebutuhan_pct/100)
dana_keinginan = uang_jajan * (keinginan_pct/100)
dana_masa_depan = uang_jajan * (masa_depan_pct/100)

st.header("Ini Rencana Alokasi dana kamu🎉")
st.write("Jangan ragu buat sesuaikan ulang sesuai kondisi ya🎉")

col1,col2,col3 = st.columns(3)
with col1 :
    st.metric("Dana Kebutuhan",f"Rp {dana_kebutuhan:,.0f}",f"per {frekuensi}")
with col2:
    st.metric("Dana Keinginan",f"Rp {dana_keinginan:,.0f}",f"per {frekuensi}")
with col3 :
    st.metric("Dana Masa Depan",f"Rp {dana_masa_depan:,.0f}",f"per {frekuensi}")

if frekuensi == "Harian" :
    dana_mingguan = dana_masa_depan * 5
elif frekuensi == "Bulanan" :
    dana_mingguan = dana_masa_depan / 4
else : 
    dana_mingguan = dana_masa_depan

proyeksi_1_bulan = dana_mingguan * 4
proyeksi_3_bulan = dana_mingguan * 12
proyeksi_6_bulan = dana_mingguan * 24

st.write(f"Dalam 1 bulan, kamu punya : Rp {proyeksi_1_bulan:,.0f}")
st.write(f"Dalam 3 bulan, kamu punya : Rp {proyeksi_3_bulan:,.0f}")
st.write(f"Dalam 6 bulan, kamu punya : Rp {proyeksi_6_bulan:,.0f}")