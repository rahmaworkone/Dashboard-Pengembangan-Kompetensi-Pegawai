import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Dashboard Kompetensi",
    layout="wide"
)

# =====================================================
# CSS
# =====================================================

st.markdown("""
<style>

.main {
    background-color: #f5f5f5;
}

.block-container {
    padding-top: 1rem;
}

.title-box{
    background:#d9d9d9;
    padding:20px;
    text-align:center;
    margin-bottom:20px;
}

.metric-card{
    background:#bdbdbd;
    padding:20px;
    text-align:center;
    border-radius:8px;
}

.metric-title{
    font-size:18px;
    font-weight:bold;
}

.metric-value{
    font-size:42px;
    font-weight:bold;
}

.program-card{
    background:#bdbdbd;
    padding:20px;
    border-radius:8px;
    margin-bottom:15px;
}

.small-status{
    background:#bdbdbd;
    padding:15px;
    border-radius:8px;
}

div[data-testid="stSidebar"]{
    background-color:#e5e5e5;
}

div.stButton > button {
    height:60px;
    border-radius:15px;
    font-size:20px;
    font-weight:600;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# DATA DUMMY
# =====================================================

data = {
    "Program": [
        "Pelatihan Data Analyst",
        "Sertifikasi Python",
        "Beasiswa S2",
        "Pelatihan Pengadaan",
        "Workshop Keuangan Negara",
        "Pelatihan Tableau",
        "Sertifikasi Data Science",
        "Pelatihan AI"
    ],
    "Jenis": [
        "Pelatihan",
        "Sertifikasi",
        "Beasiswa",
        "Pelatihan",
        "Pelatihan",
        "Pelatihan",
        "Sertifikasi",
        "Pelatihan"
    ],
    "Status": [
        "Sedang Dibuka",
        "Sedang Dibuka",
        "Akan Dibuka",
        "Ditutup",
        "Sedang Dibuka",
        "Akan Dibuka",
        "Ditutup",
        "Sedang Dibuka"
    ],
    "Penyelenggara": [
        "BPSDM",
        "Dicoding",
        "LPDP",
        "LKPP",
        "Kemenkeu",
        "Tableau",
        "BNSP",
        "Komdigi"
    ]
}

df = pd.DataFrame(data)

# =====================================================
# SIDEBAR FILTER
# =====================================================

with st.sidebar:

    st.header("Filter")

    jenis_filter = st.selectbox(
        "Jenis Program",
        ["Semua"] + list(df["Jenis"].unique())
    )

    penyelenggara_filter = st.selectbox(
        "Penyelenggara",
        ["Semua"] + list(df["Penyelenggara"].unique())
    )

    status_filter = st.selectbox(
        "Status",
        ["Semua"] + list(df["Status"].unique())
    )

# =====================================================
# FILTER DATA
# =====================================================

filtered = df.copy()

if jenis_filter != "Semua":
    filtered = filtered[
        filtered["Jenis"] == jenis_filter
    ]

if penyelenggara_filter != "Semua":
    filtered = filtered[
        filtered["Penyelenggara"] == penyelenggara_filter
    ]

if status_filter != "Semua":
    filtered = filtered[
        filtered["Status"] == status_filter
    ]

# =====================================================
# HEADER
# =====================================================

st.markdown("""
<div class="title-box">
<h1>DASHBOARD PENGEMBANGAN KOMPETENSI PEGAWAI</h1>
<h2>BIRO KEUANGAN DAN BARANG MILIK NEGARA</h2>
</div>
""", unsafe_allow_html=True)

# =====================================================
# DIALOG TAMBAH PROGRAM
# =====================================================

@st.dialog("Tambah Program")
def tambah_program():

    st.text_input("Nama Program")

    st.selectbox(
        "Jenis Program",
        [
            "Pelatihan",
            "Sertifikasi",
            "Beasiswa"
        ]
    )

    st.text_input("Penyelenggara")

    st.selectbox(
        "Status Pendaftaran",
        [
            "Sedang Dibuka",
            "Akan Dibuka",
            "Ditutup"
        ]
    )

    st.text_input("Link Pendaftaran")

    st.text_area("Deskripsi Program")

    if st.button("Simpan"):
        st.success("Program berhasil ditambahkan")

# =====================================================
# METRIC
# =====================================================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">TOTAL PROGRAM</div>
        <div class="metric-value">{len(filtered)}</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">TOTAL BEASISWA</div>
        <div class="metric-value">
            {len(filtered[filtered["Jenis"]=="Beasiswa"])}
        </div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">TOTAL SERTIFIKASI</div>
        <div class="metric-value">
            {len(filtered[filtered["Jenis"]=="Sertifikasi"])}
        </div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">TOTAL PELATIHAN</div>
        <div class="metric-value">
            {len(filtered[filtered["Jenis"]=="Pelatihan"])}
        </div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# =====================================================
# CHART
# =====================================================

left, right = st.columns([1,3])

with left:

    st.markdown("""
    <div class="small-status">
    <h3 align="center">STATUS PENDAFTARAN</h3>
    </div>
    """, unsafe_allow_html=True)

    st.metric(
        "Sedang Dibuka",
        len(filtered[
            filtered["Status"]=="Sedang Dibuka"
        ])
    )

    st.metric(
        "Akan Dibuka",
        len(filtered[
            filtered["Status"]=="Akan Dibuka"
        ])
    )

    st.metric(
        "Ditutup",
        len(filtered[
            filtered["Status"]=="Ditutup"
        ])
    )

with right:

    chart_df = (
        filtered.groupby("Jenis")
        .size()
        .reset_index(name="Jumlah")
    )

    fig = px.bar(
        chart_df,
        x="Jenis",
        y="Jumlah",
        text="Jumlah"
    )

    fig.update_layout(
        height=350,
        showlegend=False
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# =====================================================
# LIST PROGRAM
# =====================================================

st.markdown(
    f"<h3 align='center'>TERSEDIA {len(filtered)} PROGRAM</h3>",
    unsafe_allow_html=True
)

for _, row in filtered.iterrows():

    col1, col2 = st.columns([5,1])

    with col1:

        st.markdown(f"""
        <div class="program-card">
            <h3>{row['Program']}</h3>
            <p>
            Jenis : {row['Jenis']}<br>
            Status : {row['Status']}<br>
            Penyelenggara : {row['Penyelenggara']}
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.button(
            "DETAIL",
            key=f"detail_{row['Program']}",
            use_container_width=True
        )

# =====================================================
# TOMBOL TAMBAH PROGRAM
# =====================================================

st.write("")
st.write("")

col1, col2, col3 = st.columns([1,3,1])

with col2:

    if st.button(
        "➕ TAMBAH PROGRAM",
        use_container_width=True
    ):
        tambah_program()
