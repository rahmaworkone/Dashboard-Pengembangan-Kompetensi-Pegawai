import streamlit as st
import pandas as pd

st.title("🎯 Katalog Program Kompetensi")

df = pd.read_csv("data/program.csv")

# SIDEBAR

st.sidebar.header("Filter")

jenis = st.sidebar.multiselect(
    "Jenis Program",
    df["jenis_program"].unique()
)

bidang = st.sidebar.multiselect(
    "Bidang Kompetensi",
    df["bidang_kompetensi"].unique()
)

status = st.sidebar.multiselect(
    "Status",
    df["status"].unique()
)

search = st.sidebar.text_input(
    "Cari Program"
)

# FILTER

filtered = df.copy()

if jenis:
    filtered = filtered[
        filtered["jenis_program"].isin(jenis)
    ]

if bidang:
    filtered = filtered[
        filtered["bidang_kompetensi"].isin(bidang)
    ]

if status:
    filtered = filtered[
        filtered["status"].isin(status)
    ]

if search:
    filtered = filtered[
        filtered["nama_program"]
        .str.contains(search,case=False)
    ]

# KPI

c1,c2,c3 = st.columns(3)

c1.metric(
    "Total Program",
    len(filtered)
)

c2.metric(
    "Pelatihan",
    len(
        filtered[
            filtered["jenis_program"]=="Pelatihan"
        ]
    )
)

c3.metric(
    "Sertifikasi",
    len(
        filtered[
            filtered["jenis_program"]=="Sertifikasi"
        ]
    )
)

st.divider()

# CARD

for _,row in filtered.iterrows():

    with st.container(border=True):

        col1,col2 = st.columns([4,1])

        with col1:

            st.subheader(row["nama_program"])

            st.write(
                f"""
                **Jenis:** {row['jenis_program']}  
                **Bidang:** {row['bidang_kompetensi']}  
                **Penyelenggara:** {row['penyelenggara']}  
                **Metode:** {row['metode']}  
                **Deadline:** {row['deadline']}
                """
            )

        with col2:

            st.badge(row["status"])

            st.link_button(
                "Detail",
                row["link"]
            )