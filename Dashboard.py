import streamlit as st
import pandas as pd
import plotly.express as px

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Dashboard Kompetensi",
    layout="wide"
)

# =====================================================
# CSS
# =====================================================

st.markdown("""
<style>

/* =====================================================
   GLOBAL
===================================================== */

.stApp{
    background:
    radial-gradient(
        circle at top left,
        rgba(139,92,246,.18),
        transparent 35%
    ),

    radial-gradient(
        circle at top right,
        rgba(14,165,233,.15),
        transparent 35%
    ),

    #020617;
}

.block-container{
    max-width:1500px;
    padding-top:1rem;
    padding-left:2rem;
    padding-right:2rem;
}

/* =====================================================
   HEADER
===================================================== */

.title-box{

    background:
    rgba(15,23,42,.90);

    border:
    1px solid rgba(99,102,241,.20);

    border-radius:24px;

    padding:24px;

    margin-bottom:24px;

    box-shadow:
    0 0 30px rgba(59,130,246,.08);
}

.title-box h1{

    color:white;

    font-size:30px;

    text-align:center;

    line-height:1.4;

    margin:0;
}

/* =====================================================
   FILTER PANEL
===================================================== */

.filter-title{

    color:#8B5CF6;

    font-size:28px;

    font-weight:700;

    margin-bottom:24px;
}

/* =====================================================
   SELECTBOX
===================================================== */

label[data-testid="stWidgetLabel"]{

    color:#E2E8F0 !important;

    font-size:15px !important;

    font-weight:600 !important;
}

div[data-baseweb="select"]{

    border-radius:14px;
}

/* =====================================================
   BUTTON
===================================================== */

div.stButton > button{

    height:48px;

    border-radius:14px;

    font-weight:600;

    border:none;
}

/* =====================================================
   KPI CARD
===================================================== */

.metric-card{

    border-radius:20px;

    padding:18px;

    min-height:120px;

    color:white;
}

.metric-title{

    font-size:14px;

    opacity:.9;

    margin-bottom:10px;
}

.metric-value{

    font-size:42px;

    font-weight:700;
}

/* =====================================================
   STATUS PANEL
===================================================== */

.status-panel{

    background:
    rgba(15,23,42,.85);

    border:
    1px solid rgba(99,102,241,.15);

    border-radius:20px;

    padding:18px;
}

.status-title{

    color:white;

    font-weight:700;

    margin-bottom:14px;
}

.status-item{

    background:#111827;

    color:white;

    border-radius:12px;

    padding:14px;

    margin-bottom:10px;

    display:flex;

    justify-content:space-between;
}

/* =====================================================
   PROGRAM CARD
===================================================== */

.program-card{

    background:
    rgba(15,23,42,.85);

    border:
    1px solid rgba(99,102,241,.15);

    border-radius:18px;

    padding:16px 18px;

    color:white;

    transition:.2s;
}

.program-card:hover{

    border-color:#8B5CF6;

    transform:translateY(-2px);
}

.program-title{

    font-size:18px;

    font-weight:700;

    margin-bottom:8px;
}

.program-meta{

    color:#CBD5E1;

    font-size:14px;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# DATA DUMMY
# =====================================================

data = {
    "Program":[
        "Pelatihan Data Analyst",
        "Sertifikasi Python",
        "Beasiswa S2",
        "Pelatihan Pengadaan",
        "Workshop Keuangan Negara",
        "Pelatihan Tableau",
        "Sertifikasi Data Science",
        "Pelatihan AI"
    ],

    "Jenis":[
        "Pelatihan",
        "Sertifikasi",
        "Beasiswa",
        "Pelatihan",
        "Pelatihan",
        "Pelatihan",
        "Sertifikasi",
        "Pelatihan"
    ],

    "Status":[
        "Sedang Dibuka",
        "Sedang Dibuka",
        "Akan Dibuka",
        "Ditutup",
        "Sedang Dibuka",
        "Akan Dibuka",
        "Ditutup",
        "Sedang Dibuka"
    ],

    "Penyelenggara":[
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
# DIALOG TAMBAH PROGRAM
# =====================================================

@st.dialog("Tambah Program")
def tambah_program():

    st.text_input("Nama Program")

    st.selectbox(
        "Jenis Program",
        ["Pelatihan","Sertifikasi","Beasiswa"]
    )

    st.text_input("Penyelenggara")

    st.selectbox(
        "Status",
        ["Sedang Dibuka","Akan Dibuka","Ditutup"]
    )

    st.text_input("Link Pendaftaran")

    st.text_area("Deskripsi Program")

    st.button("Simpan")

# =====================================================
# HEADER
# =====================================================

st.markdown("""
<div class="title-box">
<h1>
DASHBOARD PENGEMBANGAN KOMPETENSI PEGAWAI
<br>
BIRO KEUANGAN DAN BARANG MILIK NEGARA
</h1>
</div>
""", unsafe_allow_html=True)

# =====================================================
# LAYOUT
# =====================================================

filter_col, main_col = st.columns(
    [1.15, 4]
)

# =====================================================
# FILTER PANEL
# =====================================================

with filter_col:

    filter_box = st.container(border=True)

    with filter_box:

        st.markdown("""
        <div class="filter-title">
        🎛 FILTER
        </div>
        """, unsafe_allow_html=True)

        jenis = st.selectbox(
            "Jenis Program",
            ["Semua"] + list(df["Jenis"].unique())
        )

        peny = st.selectbox(
            "Penyelenggara",
            ["Semua"] + list(df["Penyelenggara"].unique())
        )

        status = st.selectbox(
            "Status",
            ["Semua"] + list(df["Status"].unique())
        )

        urut = st.selectbox(
            "Urutkan",
            ["A-Z", "Z-A"]
        )

        st.button(
            "🔎 Terapkan Filter",
            use_container_width=True
        )

        st.markdown("<br><br><br><br><br><br>", unsafe_allow_html=True)

        if st.button(
            "➕ Tambah Program",
            use_container_width=True
        ):
            tambah_program()
# =====================================================
# FILTER DATA
# =====================================================

filtered = df.copy()

if jenis != "Semua":
    filtered = filtered[
        filtered["Jenis"] == jenis
    ]

if peny != "Semua":
    filtered = filtered[
        filtered["Penyelenggara"] == peny
    ]

if status != "Semua":
    filtered = filtered[
        filtered["Status"] == status
    ]

filtered = filtered.sort_values(
    "Program",
    ascending=(urut=="A-Z")
)
