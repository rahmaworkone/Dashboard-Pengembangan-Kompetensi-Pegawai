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

.title-box h1{
    font-size:32px;
    margin:0;
}

.metric-card{
    background:#bdbdbd;
    padding:20px;
    text-align:center;
    border-radius:5px;
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
    border-radius:5px;
    margin-bottom:15px;
}

.small-status{
    background:#9d9d9d;
    padding:15px;
    border-radius:5px;
}

div[data-testid="stSidebar"]{
    background-color:#e5e5e5;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# DUMMY DATA
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
    "Penyelenggara":[
        "BPSDM","Dicoding","LPDP","LKPP",
        "Kemenkeu","Tableau","BNSP","Komdigi"
    ]
}

df = pd.DataFrame(data)

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
# SIDEBAR
# =====================================================

with st.sidebar:

    st.subheader("🎓 Jenis Pengembangan Kompetensi")

    jenis = st.selectbox(
        "Pilih Skema",
        ["Semua"] + list(df["Jenis"].unique())
    )

    metode = st.selectbox(
        "Metode Pelaksanaan",
        ["Semua","Online","Offline","Hybrid"]
    )

    penyelenggara = st.selectbox(
        "Penyelenggara",
        ["Semua"] + list(df["Penyelenggara"].unique())
    )

    status = st.selectbox(
        "Status Pendaftaran",
        ["Semua"] + list(df["Status"].unique())
    )

    st.markdown("---")

    urutan = st.radio(
        "Urutkan Berdasarkan",
        [
            "Nama A-Z",
            "Nama Z-A"
        ]
    )

    st.markdown("---")

    if st.button("➕ TAMBAH PROGRAM", use_container_width=True):
        st.switch_page

# =====================================================
# FILTER
# =====================================================

filtered = df.copy()

if jenis != "Semua":
    filtered = filtered[filtered["Jenis"] == jenis]

if penyelenggara != "Semua":
    filtered = filtered[
        filtered["Penyelenggara"] == penyelenggara
    ]

if status != "Semua":
    filtered = filtered[
        filtered["Status"] == status
    ]

# =====================================================
# METRIC CARD
# =====================================================

c1,c2,c3,c4 = st.columns(4)

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
# CHART AREA
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
        height=300,
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
            key=row["Program"],
            use_container_width=True
        )
