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

/* =========================
   BACKGROUND APP
========================= */

.stApp{
    background: #F4F7FC;
}

/* =========================
   CONTAINER
========================= */

.block-container{
    padding-top:1rem;
    padding-left:2rem;
    padding-right:2rem;
}

/* =========================
   HEADER
========================= */

.title-box{
    background:white;
    border-radius:20px;
    padding:30px;
    text-align:center;
    margin-bottom:25px;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
}

.title-box h1{
    color:#1E3A8A;
    font-size:28px;
    font-weight:700;
    margin-bottom:8px;
}

.title-box h2{
    color:#1E3A8A;
    font-size:28px;
    font-weight:700;
    margin-top:0;
    margin-bottom:0;
}

/* =========================
   CARD STATISTIK
========================= */

.metric-card{
    background:white;
    padding:25px;
    border-radius:18px;
    text-align:center;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
    border:1px solid #E2E8F0;
}

.metric-title{
    color:#64748B;
    font-size:14px;
    font-weight:600;
    margin-bottom:10px;
}

.metric-value{
    color:#2563EB;
    font-size:38px;
    font-weight:700;
}

/* =========================
   STATUS CARD
========================= */

.small-status{
    background:white;
    border-radius:18px;
    padding:20px;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
    border:1px solid #E2E8F0;
}

/* =========================
   PROGRAM CARD
========================= */

.program-card{
    background:white;
    border-radius:18px;
    padding:20px;
    margin-bottom:15px;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
    border:1px solid #E2E8F0;
}

.program-card h3{
    color:#1E293B;
    margin-bottom:10px;
}

.program-card p{
    color:#64748B;
    line-height:1.7;
}

/* =========================
   SIDEBAR
========================= */

section[data-testid="stSidebar"]{
    background:#FFFFFF;
    border-right:1px solid #E2E8F0;
}

/* =========================
   BUTTON
========================= */

div.stButton > button{
    background:#2563EB;
    color:white;
    border:none;
    border-radius:12px;
    height:50px;
    font-weight:600;
}

div.stButton > button:hover{
    background:#1D4ED8;
    color:white;
}

/* =========================
   SELECTBOX
========================= */

div[data-baseweb="select"]{
    border-radius:10px;
}

/* =========================
   PLOTLY CHART
========================= */

.js-plotly-plot{
    background:white;
    border-radius:18px;
    padding:10px;
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
<h1>BIRO KEUANGAN DAN BARANG MILIK NEGARA</h1>
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
