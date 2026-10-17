import streamlit as st

# Pengaturan halaman browser (Judul Tab & Layout)
st.set_page_config(page_title="Kuis Interaktif Python", page_icon="🧠", layout="centered")

# CSS Tambahan untuk Merapikan Tampilan (Diperbaiki: unsafe_allow_html)
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 3em;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Header Aplikasi
st.title("🧠 Kuis Biologi Interaktif")
st.caption("Uji pengetahuanmu seputar dunia hewan dan sains!")

# Panel Samping (Sidebar) untuk Informasi & Bantuan
with st.sidebar:
    st.header("📋 Petunjuk Kuis")
    st.write("1. Isi data diri dengan benar.")
    st.write("2. Masukkan password akses (`QUIZ900`).")
    st.write("3. Jawab 5 pertanyaan kuis.")
    st.write("4. Klik tombol **Submit** untuk melihat nilai akhir.")
    st.markdown("---")
    st.info("💡 **Tips:** Setiap jawaban benar bernilai +20 poin, sedangkan jawaban salah bernilai -20 poin.")

# Section 1: Data Diri Peserta
with st.container():
    st.subheader("👤 Data Peserta")
    col1, col2 = st.columns(2)
    with col1:
        nama = st.text_input("Nama Lengkap :", placeholder="Contoh: Budi")
        usia = st.text_input("Usia Kamu :", placeholder="Contoh: 19")
    with col2:
        nim = st.text_input("NIM / NPM :", placeholder="Contoh: 230101001")
        password = st.text_input("Password Quiz :", type="password", placeholder="Masukkan password di sini")

# Validasi Akses
password_benar = "QUIZ900"

if nama and usia and nim:
    if password == password_benar:
        st.success(f"🔓 Akses Diberikan! Selamat datang, **{nama}**. Silakan jawab pertanyaan di bawah.")
        st.markdown("---")
        
        # --- SOAL KUIS ---
        st.subheader("📝 Soal Kuis")
        st.progress(100, text="Seluruh soal siap dijawab!")

        with st.container(border=True):
            st.markdown("### **Soal 1**")
            st.write("Sebutkan salah satu hewan Mamalia?")
            q1 = st.radio(
                "Pilihan Jawaban:",
                ("A. PLATYPUS", "B. LION FISH", "C. AXOLOTL", "D. GREAT WHITE SHARK"),
                key="q1"
            )

        with st.container(border=True):
            st.markdown("### **Soal 2**")
            st.write("Jenis Bisa Ular Yang Bisa Menyebabkan Pembusukan/Nekrosis Pada Area yang tergigit:")
            q2 = st.radio(
                "Pilihan Jawaban:",
                ("A. NEUROTOKSIN", "B. SITOTOKSIN", "C. HEMOTOKSIN", "D. TETRODOTOKSIN"),
                key="q2"
            )

        with st.container(border=True):
            st.markdown("### **Soal 3**")
            st.write("Pilih Salah Satu Yang Benar! Mana Hewan **INVERTEBRATA**?")
            q3 = st.radio(
                "Pilihan Jawaban:",
                ("A. CICAK", "B. TIKUS", "C. UNGGAS", "D. CAPUNG"),
                key="q3"
            )

        with st.container(border=True):
            st.markdown("### **Soal 4**")
            st.write("Sebutkan Hewan **Mollusca**... Pilih Satu Yang Benar!")
            q4 = st.radio(
                "Pilihan Jawaban:",
                ("A. Kupu-Kupu", "B. Laba-Laba", "C. Nautilus", "D. Kelomang Laut"),
                key="q4"
            )

        with st.container(border=True):
            st.markdown("### **Soal 5**")
            st.write("Pilih Hewan Yang Merupakan **ARTHROPODA**!")
            q5 = st.radio(
                "Pilihan Jawaban:",
                ("A. KECOA", "B. TIKUS", "C. ULAR PYTHON", "D. OARFISH"),
                key="q5"
            )

        st.markdown("---")

        # --- Aksi Tombol Evaluasi & Ulang ---
        col_btn1, col_btn2 = st.columns(2)
        
        with col_btn1:
            submit = st.button("🚀 Submit & Lihat Nilai", type="primary")
        with col_btn2:
            reset = st.button("🔄 Ulang Kuis dari Awal")

        if reset:
            st.rerun()

        if submit:
            skor = 0
            
            st.markdown("---")
            st.subheader("📊 Pembahasan & Evaluasi Jawaban")
            
            # Penilaian Soal 1
            if q1.startswith("A"):
                skor += 20
                st.success("✅ **Soal 1:** Benar! Platypus adalah mamalia bertelur (Monotremata).")
            else:
                st.error("❌ **Soal 1:** Salah. Jawaban yang benar adalah **A. PLATYPUS**.")

            # Penilaian Soal 2
            if q2.startswith("C"):
                skor += 20
                st.success("✅ **Soal 2:** Benar! Hemotoksin merusak sel darah dan jaringan hingga nekrosis.")
            else:
                skor -= 20
                st.error("❌ **Soal 2:** Salah. Jawaban yang benar adalah **C. HEMOTOKSIN**.")

            # Penilaian Soal 3
            if q3.startswith("D"):
                skor += 20
                st.success("✅ **Soal 3:** Benar! Capung adalah hewan Invertebrata (tanpa tulang belakang).")
            else:
                skor -= 20
                st.error("❌ **Soal 3:** Salah. Jawaban yang benar adalah **D. CAPUNG**.")

            # Penilaian Soal 4
            if q4.startswith("C"):
                skor += 20
                st.success("✅ **Soal 4:** Benar! Nautilus adalah Mollusca bertubuh lunak yang memiliki cangkang.")
            else:
                skor -= 20
                st.error("❌ **Soal 4:** Salah. Jawaban yang benar adalah **C. Nautilus**.")

            # Penilaian Soal 5
            if q5.startswith("A"):
                skor += 20
                st.success("✅ **Soal 5:** Benar! Kecoa adalah Arthropoda (hewan berbuku-buku/beruas).")
            else:
                skor -= 20
                st.error("❌ **Soal 5:** Salah. Jawaban yang benar adalah **A. KECOA**.")

            # Display Ringkasan Nilai Akhir
            st.markdown("---")
            with st.expander("🎓 **LIHAT HASIL AKHIR & KARTU NILAI**", expanded=True):
                st.write(f"**Nama Peserta :** {nama}")
                st.write(f"**Usia :** {usia} Tahun")
                st.write(f"**NIM / NPM :** {nim}")
                st.markdown(f"## **Total Skor:** `{skor}` / 100")

                if skor == 100:
                    st.balloons()
                    st.success("🎉 **PERFECT!** Luar biasa, semua jawaban kamu benar sempurna!")
                elif skor >= 60:
                    st.snow()
                    st.info("👍 **BAGUS!** Nilai kamu sudah cukup baik, tingkatkan lagi!")
                else:
                    st.warning("💪 **JANGAN MENYERAH!** Pelajari lagi materi hewan dan coba lagi ya!")

    elif password != "":
        st.error("🔒 **AKSES DITOLAK!** Password yang dimasukkan salah.")
else:
    st.info("👋 Silakan lengkapi Data Peserta (Nama, Usia, NIM) terlebih dahulu untuk membuka kuis.")