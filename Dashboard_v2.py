import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard Kompetensi", layout="wide",initial_sidebar_state="expanded")

st.markdown("""
<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
""", unsafe_allow_html=True)

# =========================
# CSS
# =========================
st.markdown("""
<style>
.stApp{
    background:
    radial-gradient(circle at top left, rgba(139,92,246,.18), transparent 35%),
    radial-gradient(circle at top right, rgba(14,165,233,.15), transparent 35%),
    #020617;
}

[data-testid="stSidebarNav"] {
    display: none;
}

[data-testid="collapsedControl"]{
    display:none;
}

section[data-testid="stSidebar"]{

    min-width:280px !important;
    max-width:280px !important;

    background:
    linear-gradient(
        180deg,
        #020617,
        #0F172A
    );
}

section[data-testid="stSidebar"] .block-container{
    padding-top:12px;
    padding-left:12px;
    padding-right:12px;
}

.block-container{
    padding-top:1rem;
    max-width:1450px;
}

.title-box{
    background:rgba(15,23,42,.9);
    border:1px solid rgba(99,102,241,.25);
    border-radius:22px;
    padding:20px;
    text-align:center;
    margin-bottom:20px;
    min-height:90px;
}

.title-box h1{
    font-size:28px;
    line-height:1.4;
    color:white;
    margin:0;
}

.metric-card{
    border-radius:18px;
    padding:20px;
    color:white;
    min-height:110px;
}

.metric-title{
    font-size:14px;
    opacity:.9;
}

.metric-value{
    font-size:42px;
    font-weight:bold;
}

div.stButton > button{

    border-radius:14px;

    height:50px;

    font-weight:600;
}

.panel{
    background:rgba(15,23,42,.75);
    border:1px solid rgba(99,102,241,.15);
    border-radius:18px;
    padding:18px;
}

.status-item{
    background:#111827;
    color:white;
    border-radius:14px;
    padding:14px;
    margin-bottom:10px;
    display:flex;
    justify-content:space-between;
}

.program-card{
    background:rgba(15,23,42,.75);
    border:1px solid rgba(99,102,241,.15);
    border-radius:16px;
    padding:14px 18px;
    color:white;
}

.filter-title{

    display:flex;
    align-items:center;

    gap:10px;

    color:#8B5CF6;

    font-size:24px;
    font-weight:700;

    margin-bottom:24px;
}

.filter-title .material-icons{
    font-size:28px;
}

.filter-card{

    background:
    rgba(15,23,42,.75);

    border:
    1px solid rgba(99,102,241,.2);

    border-radius:24px;

    padding:22px;

    box-shadow:
    0 0 30px rgba(59,130,246,.08);

    margin-top:4px;
}

</style>
""", unsafe_allow_html=True)

# data dummy
df = pd.DataFrame({
    "Program":["Pelatihan Data Analyst","Sertifikasi Python","Beasiswa S2","Pelatihan Pengadaan","Workshop Keuangan Negara","Pelatihan Tableau","Sertifikasi Data Science","Pelatihan AI"],
    "Jenis":["Pelatihan","Sertifikasi","Beasiswa","Pelatihan","Pelatihan","Pelatihan","Sertifikasi","Pelatihan"],
    "Status":["Sedang Dibuka","Sedang Dibuka","Akan Dibuka","Ditutup","Sedang Dibuka","Akan Dibuka","Ditutup","Sedang Dibuka"],
    "Penyelenggara":["BPSDM","Dicoding","LPDP","LKPP","Kemenkeu","Tableau","BNSP","Komdigi"]
})

@st.dialog("Tambah Program")
def tambah_program():
    st.text_input("Nama Program")
    st.selectbox("Jenis Program",["Pelatihan","Sertifikasi","Beasiswa"])
    st.text_input("Penyelenggara")
    st.selectbox("Status",["Sedang Dibuka","Akan Dibuka","Ditutup"])
    st.text_input("Link")
    st.text_area("Deskripsi")
    st.button("Simpan")

with st.sidebar:

    st.markdown("""
    <div class="filter-card">

        <div class="filter-title">
            <span class="material-icons">tune</span>
            FILTER
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
        "🔎 TERAPKAN FILTER",
        use_container_width=True
    )

    st.markdown("""
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        "<div style='height:260px'></div>",
        unsafe_allow_html=True
    )

    if st.button(
        "➕ TAMBAH PROGRAM",
        use_container_width=True
    ):
        tambah_program()

filtered = df.copy()
if jenis != "Semua":
    filtered = filtered[filtered["Jenis"] == jenis]
if peny != "Semua":
    filtered = filtered[filtered["Penyelenggara"] == peny]
if status != "Semua":
    filtered = filtered[filtered["Status"] == status]

filtered = filtered.sort_values("Program", ascending=(urut=="A-Z"))

st.markdown("""
<div class="title-box">
<h1>DASHBOARD PENGEMBANGAN KOMPETENSI PEGAWAI<br>BIRO KEUANGAN DAN BARANG MILIK NEGARA</h1>
</div>
""", unsafe_allow_html=True)

c1,c2,c3,c4 = st.columns(4)

cards = [
("🟪 TOTAL PROGRAM",len(filtered),"linear-gradient(135deg,#7C3AED,#4C1D95)"),
("🎓 TOTAL BEASISWA",len(filtered[filtered['Jenis']=='Beasiswa']),"linear-gradient(135deg,#2563EB,#1E40AF)"),
("🏅 TOTAL SERTIFIKASI",len(filtered[filtered['Jenis']=='Sertifikasi']),"linear-gradient(135deg,#0891B2,#155E75)"),
("📖 TOTAL PELATIHAN",len(filtered[filtered['Jenis']=='Pelatihan']),"linear-gradient(135deg,#0EA5E9,#0369A1)")
]

for col, card in zip([c1,c2,c3,c4], cards):
    with col:
        st.markdown(f"""
        <div class="metric-card" style="background:{card[2]};">
            <div class="metric-title">{card[0]}</div>
            <div class="metric-value">{card[1]}</div>
        </div>
        """, unsafe_allow_html=True)

left,right = st.columns([1.2,3.8])

with left:
    st.markdown('<div class="panel"><h3 style="color:white">STATUS PENDAFTARAN</h3>', unsafe_allow_html=True)
    for s in ["Sedang Dibuka","Akan Dibuka","Ditutup"]:
        st.markdown(f'<div class="status-item"><span>{s}</span><b>{len(filtered[filtered["Status"]==s])}</b></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    chart_df = filtered.groupby("Jenis").size().reset_index(name="Jumlah")
    fig = px.bar(chart_df,x="Jenis",y="Jumlah",text="Jumlah")
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="white",
        height=320
    )
    st.plotly_chart(fig, use_container_width=True)

st.markdown(f"### Tersedia {len(filtered)} Program")

for _, row in filtered.iterrows():
    a,b = st.columns([6,1])
    with a:
        st.markdown(
            f"<div class='program-card'><b>{row['Program']}</b><br>"
            f"Jenis: {row['Jenis']} • Status: {row['Status']} • Penyelenggara: {row['Penyelenggara']}</div>",
            unsafe_allow_html=True
        )
    with b:
        st.button("DETAIL", key=row['Program'])
