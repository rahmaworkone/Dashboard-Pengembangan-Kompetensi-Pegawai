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
    background: linear-gradient(
        135deg,
        #0F172A 0%,
        #111827 50%,
        #1E1B4B 100%
    );
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
    background:#1E293B;
    border:1px solid rgba(255,255,255,0.1);
    border-radius:20px;
    padding:30px;
}

.title-box h1{
    color:#FFFFFF;
}

/* =========================
   CARD STATISTIK
========================= */

.metric-card{
    background:linear-gradient(
        135deg,
        #8B5CF6,
        #3B82F6
    );
    border:none;
    border-radius:20px;
    padding:25px;
}

.metric-title{
    color:white;
}

.metric-value{
    color:white;
}

/* =========================
   STATUS CARD
========================= */

.small-status{
    background:white;
    border-radius:15px;
    padding:20px;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
    border:1px solid #E2E8F0;
}

/* =========================
   PROGRAM CARD
========================= */

.program-card{
    background:#1E293B;
    border:1px solid rgba(255,255,255,0.08);
    border-radius:20px;
}

.program-card h3{
    color:white;
}

.program-card p{
    color:#CBD5E1;
}

/* =========================
   SIDEBAR
========================= */

section[data-testid="stSidebar"]{
    background:#111827;
    border-right:1px solid rgba(255,255,255,0.1);
}

/* =========================
   BUTTON
========================= */

div.stButton > button{
    background:linear-gradient(
    135deg,
    #8B5CF6,
    #06B6D4
);
    color:white;
    border:none;
    border-radius:15px;
    height:50px;
    font-weight:600;
}

div.stButton > button:hover{
    background:linear-gradient(
    135deg,
    #7C3AED,
    #0891B2
);
    color:white;
}

/* =========================
   SELECTBOX
========================= */

div[data-baseweb="select"]{
    border-radius:15px;
}

/* =========================
   PLOTLY CHART
========================= */

.js-plotly-plot{
    background:white;
    border-radius:15px;
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
    showlegend=False,
    paper_bgcolor="#1E293B",
    plot_bgcolor="#1E293B",
    font_color="white"
    )

    fig.update_traces(
    marker_color="#8B5CF6"
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
