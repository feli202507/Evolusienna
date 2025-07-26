import streamlit as st

def suntik_css(file_css):
    with open(file_css) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

suntik_css("assets/style.css") # <-- Alamat untuk file di dalam 'pages'

# ... sisa kodemu ...
# ... sisa kodemu ...
st.title("Jadwal Belajar Seminggu")
st.write("""
Disusun berdasarkan kesalahan gue selama di SMP dan SMA :
Pengaturan waktunya buruk banget(Jangan ditiru)
Ini disusun versi ringan buat bangun disiplin dulu, bisa diatur sesuai kebutuhan!
-Jangan lupa buka tipsnya ya!!- (bisa copy ke notion)
""")

hari_sekolah,weekend,tips = st.tabs([
    "Hari Sekolah","Weekend","Tips 🎉"
])

checklist_sekolah_list = [
     "🏠 16.00 - 16.45 Istirahat",
     "🧮 16.45 - 17.35 Sesi Belajar 1",
     "🚶‍♂️ 17.35 - 17.45 Istirahat Pendek",
     "🔬 17.45 - 18.35 Sesi Belajar 2",
     "🍽️ 18.35 - 19.30 Istirahat Panjang, Makan Malam & Ibadah",
     "📚 19.30 - 20.20 Sesi Belajar 3",
     "🧘 20.20 - 21.30 Waktu Santai & Hobi",
     "😴 21.30 Waktu Tidur"
]
checklist_sekolah_teks  = """
- 🏠 16.00 - 16.45 Istirahat & Snack
- 🧮 16.45 - 17.35 Sesi Belajar 1
- 🚶‍♂️ 17.35 - 17.45 Istirahat Pendek
- 🔬 17.45 - 18.35 Sesi Belajar 2
- 🍽️ 18.35 - 19.30 Istirahat Panjang, Makan Malam & Ibadah
- 📚 19.30 - 20.20 Sesi Belajar 3
- 🧘 20.20 - 21.30 Waktu Santai & Hobi
- 😴 21.30 Waktu Tidur
"""
checklist_weekend_list = [
    "☀️ 08.00 - 09.00: Bangun & Sarapan Sehat",
    "🎯 09.00 - 09.50: Sesi Belajar 1 (Subjek Paling Sulit)",
    "☕ 09.50 - 10.00: Istirahat Pendek",
    "📚 10.00 - 10.50: Sesi Belajar 2 (Review Total Mingguan)",
    "🌳 10.50 - 11.20: Istirahat Panjang",
    "🧠 11.20 - 12.10: Sesi Belajar 3 (Latihan Ujian/Try Out)",
    "🎉 12.10: Belajar Selesai! Waktu Bebas"
    ]
checklist_weekend_teks = """
- ☀️ 08.00 - 09.00: Bangun & Sarapan Sehat
- 🎯 09.00 - 09.50: Sesi Belajar 1 (Subjek Paling Sulit)
- ☕ 09.50 - 10.00: Istirahat Pendek
- 📚 10.00 - 10.50: Sesi Belajar 2 (Review Total Mingguan)
- 🌳 10.50 - 11.20: Istirahat Panjang
- 🧠 11.20 - 12.10: Sesi Belajar 3 (Latihan Ujian/Try Out)
- 🎉 12.10: Belajar Selesai! Waktu Bebas
Yeayy! Selesai. Sisa hari ini bebas. Boleh untuk main, pergi ke luar!
"""
with hari_sekolah  :
    st.header("Jadwal Belajar Senin - Jumat")
    st.subheader("✅ Checklist Interaktif")
    
    hasil_checklist = []
    for item in checklist_sekolah_list :
        dicentang = st.checkbox(item,key=f"sekolah_{item}")
        hasil_checklist.append(dicentang)

    if all(hasil_checklist):
        st.balloons()
        st.success("JANGAN LUPA KONSISTEN YA! LO PASTI BISA MASUK KAMPUS IMPIAN")
  
    st.subheader("📋 Salin Jadwal Hari Sekolah")
    st.code(checklist_sekolah_teks, language="text")
    


with weekend  :
    st.header("Jadwal Belajar Sabtu & Minggu")
    st.subheader("✅ Checklist Interaktif")

    hasil_checklist = []
    for item in checklist_weekend_list :
        dicentang = st.checkbox(item,key=f"weekend_{item}")
        hasil_checklist.append(dicentang)

    if all(hasil_checklist):
        st.balloons()
        st.success("JANGAN LUPA KONSISTEN YA! LO PASTI BISA MASUK KAMPUS IMPIAN")

    st.subheader("📋 Salin Jadwal Weekend")
    st.code(checklist_weekend_teks, language="text")


with tips :
    st.header("KESALAHAN & TIPS")
    st.markdown("""
    1. Sebisa mungkin atur jadwal harian jadi ga kelupaan tugas atau ujian.
    2. Buat planner dan tulis kapan ujian, ada tugas apa.
    3. Sedia snack dan minum saat belajar. 
    4. Reward diri kalian yang hebat 🎉       
    """)
    st.warning("""
    **Peringatan Burnout:** Belajar itu penting tapi jangan sampe burnout. 
    Dulu gue sepelein hal itu, akhirnya burnout di minggu ujian dan nilainya turun (jangan dicontoh yeaa hehe).
    """)

   