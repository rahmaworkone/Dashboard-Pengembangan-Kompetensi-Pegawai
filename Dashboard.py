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
    background:
    radial-gradient(circle at top left,
    rgba(139,92,246,.18),
    transparent 35%),

    radial-gradient(circle at top right,
    rgba(14,165,233,0.15),
    transparent 35%),

    #020617;
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

    background:
    linear-gradient(
        135deg,
        rgba(15,23,42,.95),
        rgba(30,41,59,.95)
    );

    border:1px solid rgba(139,92,246,.15);

    box-shadow:
        0 0 40px rgba(59,130,246,.08);
}

.title-box h1{
    color:white;
}

/* =========================
   METRIC CARD
========================= */

.metric-card{

    border:none;

    height:130px;

    border-radius:22px;

    color:white;

    box-shadow:
        0 0 30px rgba(0,0,0,.25);
}

.metric-title{
    color:#CBD5E1;
}

.metric-value{
    color:white;
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

    background:
    rgba(15,23,42,.75);

    border:
    1px solid rgba(99,102,241,.15);

    border-radius:18px;

    transition:.2s;
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

.glass-card{
    background:rgba(15,23,42,0.75);

    border:1px solid rgba(99,102,241,0.25);

    backdrop-filter:blur(12px);

    border-radius:22px;

    box-shadow:
    0 0 30px rgba(59,130,246,.08);

    padding:20px;
}

/* =========================
   SIDEBAR
========================= */

section[data-testid="stSidebar"]{

    background:
    linear-gradient(
        180deg,
        #020617,
        #0F172A
    );

    border-right:
    1px solid rgba(139,92,246,.2);
}

section[data-testid="stSidebar"] .block-container{
    padding-top:1.5rem;
    padding-left:1rem;
    padding-right:1rem;
}

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3{
    color:white;
}

/* =========================
   SELECTBOX
========================= */

div[data-baseweb="select"]{
    background:#111827;
    border:1px solid rgba(99,102,241,.25);
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
.program-card:hover{

    transform:translateY(-2px);

    border-color:#8B5CF6;

    box-shadow:
    0 0 25px rgba(139,92,246,.15);
}
div.stButton > button:hover{
    transform:translateY(-2px);
}

.add-program-btn{

    position:fixed;

    left:25px;

    bottom:25px;

    width:250px;

    z-index:9999;
}
with st.sidebar:
    if st.button(
        "➕ TAMBAH PROGRAM",
        use_container_width=True
    ):
        tambah_program()
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

.sidebar-title{

    color:white;

    font-size:28px;

    font-weight:700;

    margin-bottom:20px;
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

    st.markdown("""
    <div class="sidebar-title">
        ⚙ FILTER
    </div>
    """, unsafe_allow_html=True)

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

    st.markdown("<div style='height:300px'></div>",
                unsafe_allow_html=True)

    if st.button(
        "➕ TAMBAH PROGRAM",
        use_container_width=True
    ):
        tambah_program()

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

st.markdown(f"""
<div class="status-card">
    <span class="dot purple"></span>
    Sedang Dibuka
    <span class="count">
        {jumlah}
    </span>
</div>
""", unsafe_allow_html=True)

.status-card{

    background:#111827;

    border-radius:16px;

    padding:18px;

    margin-bottom:12px;

    color:white;

    display:flex;
    justify-content:space-between;
    align-items:center;
}

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

    paper_bgcolor="rgba(0,0,0,0)",

    plot_bgcolor="rgba(0,0,0,0)",

    font_color="white",

    xaxis=dict(
        showgrid=False
    ),

    yaxis=dict(
        gridcolor="rgba(255,255,255,.1)"
    )
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
