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
   APP
========================= */

.stApp{
    background:#F1F5F9;
}

.block-container{
    padding-top:1.2rem;
    padding-bottom:2rem;
    padding-left:2rem;
    padding-right:2rem;
    max-width:1400px;
}

/* =========================
   HEADER
========================= */

.title-box{
    background:white;
    border-radius:24px;
    padding:24px 32px;
    text-align:center;
    margin-bottom:24px;

    box-shadow:
        0px 4px 20px rgba(0,0,0,0.06);
}

.title-box h1{
    line-height:1.25;
    color:#1E3A8A;
    font-size:26px;
    font-weight:700;

    line-height:1.35;
    margin:0;
}

/* =========================
   METRIC CARD
========================= */

.metric-card{
    background:white;

    height:160px;
    width:100%;
    border-radius:20px;

    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;

    box-shadow:
        0px 4px 15px rgba(0,0,0,0.06);

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
    font-size:40px;
    font-weight:700;
}

/* =========================
   STATUS
========================= */

.small-status{
    background:white;

    border-radius:20px;

    padding:20px;

    border:1px solid #E2E8F0;

    box-shadow:
        0px 4px 15px rgba(0,0,0,0.06);
}

.small-status h3{
    margin:0;
    color:#334155;
}

/* =========================
   PROGRAM CARD
========================= */

.program-card{
    background:white;

    border-radius:20px;

    padding:18px 24px;

    margin-bottom:14px;

    border:1px solid #E2E8F0;

    box-shadow:
        0px 4px 15px rgba(0,0,0,0.06);
}

.program-card h3{
    margin-top:0;
    margin-bottom:8px;

    color:#0F172A;

    font-size:22px;
}

.program-card p{
    margin:0;

    color:#64748B;

    line-height:1.8;
}

/* =========================
   SIDEBAR
========================= */

section[data-testid="stSidebar"]{
    background:white;
    border-right:1px solid #E2E8F0;
}

section[data-testid="stSidebar"] .block-container{
    padding-top:1.5rem;
    padding-left:1rem;
    padding-right:1rem;
}

section[data-testid="stSidebar"] h1{
    color:#1E293B;
}

/* =========================
   SELECTBOX
========================= */

div[data-baseweb="select"]{
    border-radius:14px;
}

/* =========================
   BUTTON
========================= */

div.stButton > button{

    border:none;

    border-radius:14px;

    height:52px;

    font-weight:600;

    transition:0.2s;
}

div.stButton > button:hover{
    transform:translateY(-2px);
}

/* =========================
   METRIC STREAMLIT
========================= */

[data-testid="stMetric"]{
    background:white;

    border-radius:16px;

    padding:12px;

    border:1px solid #E2E8F0;

    margin-bottom:10px;
}

/* =========================
   PLOTLY
========================= */

.js-plotly-plot{
    background:white;
    border-radius:20px;
    border:1px solid #E2E8F0;
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

    st.markdown("### 🔎 Filter Program")

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
    <h1>
        DASHBOARD PENGEMBANGAN KOMPETENSI PEGAWAI
        <br>
        BIRO KEUANGAN DAN BARANG MILIK NEGARA
    </h1>
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

st.markdown(
    "<div style='height:16px'></div>",
    unsafe_allow_html=True
)

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
    showlegend=False,
    paper_bgcolor="white",
    plot_bgcolor="white",
    font_color="#334155"
    margin=dict(
        l=20,
        r=20,
        t=30,
        b=20
    )

    fig.update_traces(
    marker_color="#2563EB"
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

st.markdown(
    "<div style='height:16px'></div>",
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns([1,3,1])

with col2:

    if st.button(
        "➕ TAMBAH PROGRAM",
        use_container_width=True
    ):
        tambah_program()
