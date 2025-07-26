import streamlit as st

def suntik_css(file_css):
    with open(file_css) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

suntik_css("assets/style.css") # <-- Alamat untuk file di dalam 'pages'

# ... sisa kodemu ...
st.set_page_config(
    page_title="Metode Pomodoro",
    page_icon="🍅"
)
#JUDUL 
st.title("🍅TEKNIK BELAJAR POMODORO")

col1,col2 = st.columns(2)
with col1 :
    st.image("assets/evolusienna_logo.png",width=150)
with col2 :
    st.subheader("Pasti kalian udah pernah denger metode ini!")
    st.write("Metode belajar super fokus,ga bikin ngantuk!")

#PENJELASAN
st.header("Apa itu teknik Pomodoro?")
st.write("""
    Teknik pomodoro itu teknik yg membagi waktu belajar menjadi 4 sesi masing-masing 25 menit.
    Setelah 1 sesi, lo boleh istirahat 5 menit. Setelah 4 sesi, lo boleh istirahat panjang!!
""")
#CARA PAKAI
st.subheader("CARA PAKAI TEKNIK POMODORO ")
st.markdown("""
1. **Pilih 1 tugas** 
2. **Setel timer 25 menit di HP**
3. **Kerjain tugas sampe timer lo bunyi**
4. **Istirahat 5 menit**
5. **Ulangi sebanyak 4 kali, setelah itu boleh istirahat panjang (misalnya sekitar 30 menit)**
""")
with st.expander("🍅Klik disini untuk tipsnya!!") :
    st.write("""
             
    1. Fokus ke 1 tugas aja, jangan multitasking kalau ga biasa.
            
    2. Silent hp lo, matiin notif semua sosmed
            
    3. Jangan pake waktu istirahat buat scroll sosmed. Itu bakal buat kalian males lanjutin sesi berikutnya 
    (karena otak kalian ngerasa lebih mudah dan menyenangkan scroll sosmed dibanding belajar, jadi otak kalian jadi lebih 
    'malas' untuk mikir keras)         
""")
#TEMPLATE
st.subheader("👇Salin template pomodoro kalian!")
jadwal_pomodoro = """
JADWAL BELAJAR TEKNIK POMODORO :
--------------------------------------------------------------
TOPIK : [Isi pakai nama mapel/tugas]
SESI  :
- Sesi 1 (25 menit)   :
Istirahat 1 (5 menit) :

- Sesi 2 (25 menit)   :
Istirahat 2 (5 menit) :

- Sesi 3 (25 menit)   :
Istirahat 3 (5 menit) :

- Sesi 4 (25 menit)   :
Istirahat 4 (30 menit) :
----------------------------------------------------------------
GREAT JOB! 
"""
st.code(jadwal_pomodoro,language="text")