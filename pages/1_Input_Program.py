import streamlit as st

st.set_page_config(
    page_title="Input Program",
    layout="wide"
)

st.title("Input Program Pengembangan Kompetensi")

nama = st.text_input("Nama Program")

jenis = st.selectbox(
    "Jenis Program",
    [
        "Pelatihan",
        "Sertifikasi",
        "Beasiswa"
    ]
)

penyelenggara = st.text_input("Penyelenggara")

metode = st.selectbox(
    "Metode",
    [
        "Online",
        "Offline",
        "Hybrid"
    ]
)

tanggal_mulai = st.date_input("Tanggal Mulai")
tanggal_selesai = st.date_input("Tanggal Selesai")

link = st.text_input("Link Pendaftaran")

deskripsi = st.text_area("Deskripsi")

brosur = st.file_uploader(
    "Upload Brosur",
    type=["pdf","jpg","png"]
)

if st.button("Simpan"):
    st.success("Program berhasil disimpan")
