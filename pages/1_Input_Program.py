import streamlit as st
import pandas as pd

st.title("➕ Input Program")

with st.form("form_program"):

    nama_program = st.text_input("Nama Program")

    jenis_program = st.selectbox(
        "Jenis Program",
        [
            "Pelatihan",
            "Sertifikasi",
            "Webinar",
            "Workshop",
            "Beasiswa"
        ]
    )

    bidang = st.selectbox(
        "Bidang Kompetensi",
        [
            "Data Digital",
            "Keuangan",
            "SDM",
            "Kearsipan",
            "Administrasi",
            "Kepemimpinan"
        ]
    )

    penyelenggara = st.text_input("Penyelenggara")

    metode = st.selectbox(
        "Metode",
        ["Online","Offline","Hybrid"]
    )

    status = st.selectbox(
        "Status",
        ["Dibuka","Akan Dibuka","Ditutup"]
    )

    deadline = st.date_input("Deadline")

    link = st.text_input("Link Informasi")

    submit = st.form_submit_button("Simpan")

if submit:

    df = pd.read_csv("data/program.csv")

    data_baru = pd.DataFrame(
        [{
            "nama_program":nama_program,
            "jenis_program":jenis_program,
            "bidang_kompetensi":bidang,
            "penyelenggara":penyelenggara,
            "metode":metode,
            "status":status,
            "deadline":deadline,
            "link":link
        }]
    )

    df = pd.concat([df,data_baru],ignore_index=True)

    df.to_csv("data/program.csv",index=False)

    st.success("Program berhasil disimpan")