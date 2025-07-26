import streamlit as st

st.set_page_config(
    page_title="Template Tugas",
    page_icon="⌛️"
)

def suntik_css(file_css):
    with open(file_css) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

suntik_css("assets/style.css") # <-- Alamat untuk file di dalam 'pages'


jadwal_tugas,jadwal_ujian = st.tabs(["Jadwal Tugas","Jadwal Ujian"])

with jadwal_tugas :
    st.header("Template Tugas")
    st.write("""
    Ini bisa disalin untuk dikirim ke temen, ke grup kelas, bahkan
    bisa dimasukkin Notion lo.
    (Memang sederhana karena web ini ga simpan database lo, jadi gue buat yg 
    bisa disalin aja yaa!)
    """)

    template_jadwal = """
    Hari, tanggal :
    Mapel :
    Tanggal pengumpulan :
    Jenis tugas :
    Tugas :
    keterangan tambahan :
    """
    st.code(template_jadwal,language="text")
with jadwal_ujian :
    st.header("Template Jadwal Ujian")
    st.write("""
    Ini bisa disalin untuk dikirim ke temen, ke grup kelas, bahkan
    bisa dimasukkin Notion lo.
    (Memang sederhana karena web ini ga simpan database kamu, jadi aku buat yg 
    bisa disalin aja yaa!)
    """)

    template_ujian = """
    Hari, tanggal :
    Mapel :
    Tanggal ujian :
    Jenis ujian :
    keterangan tambahan :
    """
    st.code(template_ujian,language="text")