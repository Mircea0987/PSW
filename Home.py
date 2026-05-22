import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Student Performance Dashboard", page_icon="🎓", layout="wide"
)

st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
    color: #1e293b !important;
}

.stApp {
    background: linear-gradient(135deg, #fff7ed 0%, #eff6ff 45%, #fdf2f8 100%) !important;
}

.block-container {
    background: transparent !important;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #7c3aed 0%, #2563eb 100%) !important;
}

[data-testid="stSidebar"] * {
    color: white !important;
}

[data-testid="stMarkdownContainer"] p,
[data-testid="stMarkdownContainer"] li,
[data-testid="stMarkdownContainer"] span,
[data-testid="stMarkdownContainer"] h1,
[data-testid="stMarkdownContainer"] h2,
[data-testid="stMarkdownContainer"] h3,
[data-testid="stMarkdownContainer"] h4,
[data-testid="stMarkdownContainer"] strong {
    color: #1e293b !important;
}

label,
.stSlider label,
.stSelectbox label,
.stMultiSelect label,
.stNumberInput label {
    color: #1e293b !important;
    font-weight: 600 !important;
}

[data-testid="stSidebar"] label,
[data-testid="stSidebar"] .stSlider label,
[data-testid="stSidebar"] .stMultiSelect label,
[data-testid="stSidebar"] .stSelectbox label {
    color: white !important;
    font-weight: 700 !important;
}

[data-testid="stSidebar"] [data-baseweb="select"] span,
[data-testid="stSidebar"] [data-baseweb="select"] div {
    color: #1e293b !important;
}

[data-testid="stSidebar"] [data-testid="stSlider"] * {
    color: white !important;
}

[data-baseweb="select"] span,
[data-baseweb="select"] div {
    color: #1e293b !important;
}

.hero {
    background: linear-gradient(135deg, #7c3aed 0%, #2563eb 45%, #06b6d4 100%);
    padding: 58px 60px;
    border-radius: 30px;
    margin-bottom: 32px;
    box-shadow: 0 20px 45px rgba(37, 99, 235, 0.25);
    color: white;
    position: relative;
    overflow: hidden;
}

.hero::after {
    content: "";
    position: absolute;
    width: 260px;
    height: 260px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.16);
    right: -80px;
    top: -80px;
}

.hero::before {
    content: "";
    position: absolute;
    width: 180px;
    height: 180px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.13);
    left: 45%;
    bottom: -90px;
}

.hero-label {
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 18px;
    opacity: 0.9;
    color: white !important;
}

.hero-title {
    font-size: 62px;
    font-weight: 800;
    line-height: 1.05;
    margin-bottom: 20px;
    position: relative;
    z-index: 2;
    color: white !important;
}

.hero-sub {
    font-size: 18px;
    line-height: 1.7;
    max-width: 780px;
    opacity: 0.95;
    position: relative;
    z-index: 2;
    color: white !important;
}

.badge-row {
    display: flex;
    gap: 14px;
    flex-wrap: wrap;
    margin-top: 28px;
    position: relative;
    z-index: 2;
}

.badge {
    background: rgba(255,255,255,0.18);
    border: 1px solid rgba(255,255,255,0.35);
    color: white !important;
    padding: 9px 16px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 600;
}

.section-title {
    font-size: 34px;
    font-weight: 800;
    color: #0f172a !important;
    margin: 38px 0 22px 0;
}

.intro-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 18px;
    margin-bottom: 34px;
}

.info-card {
    background: white;
    border-radius: 24px;
    padding: 24px 26px;
    border: 1px solid rgba(148, 163, 184, 0.25);
    box-shadow: 0 12px 28px rgba(15, 23, 42, 0.08);
}

.info-icon {
    font-size: 34px;
    margin-bottom: 10px;
}

.info-title {
    font-size: 18px;
    font-weight: 800;
    margin-bottom: 8px;
    color: #0f172a !important;
}

.info-text {
    font-size: 14.5px;
    line-height: 1.65;
    color: #64748b !important;
}

.page-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 18px;
}

.page-card {
    background: white;
    border-radius: 26px;
    padding: 28px 30px;
    box-shadow: 0 14px 34px rgba(15, 23, 42, 0.09);
    border: 1px solid rgba(148, 163, 184, 0.22);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.page-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 20px 44px rgba(15, 23, 42, 0.14);
}

.card-1 {
    border-top: 7px solid #f97316;
}

.card-2 {
    border-top: 7px solid #06b6d4;
}

.card-3 {
    border-top: 7px solid #a855f7;
}

.card-4 {
    border-top: 7px solid #22c55e;
}

.page-number {
    display: inline-block;
    padding: 7px 13px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 1px;
    margin-bottom: 14px;
}

.num-1 {
    background: #ffedd5;
    color: #ea580c !important;
}

.num-2 {
    background: #cffafe;
    color: #0891b2 !important;
}

.num-3 {
    background: #f3e8ff;
    color: #9333ea !important;
}

.num-4 {
    background: #dcfce7;
    color: #16a34a !important;
}

.page-title {
    font-size: 23px;
    font-weight: 800;
    color: #0f172a !important;
    margin-bottom: 10px;
}

.page-desc {
    font-size: 15px;
    line-height: 1.7;
    color: #64748b !important;
}

.dataset-title {
    font-size: 42px;
    font-weight: 800;
    color: #0f172a !important;
    margin-top: 50px;
    margin-bottom: 12px;
}

.dataset-desc {
    font-size: 17px;
    line-height: 1.75;
    color: #64748b !important;
    max-width: 1050px;
    margin-bottom: 28px;
}

.dataset-metric-card {
    background: #f8fafc;
    border-radius: 22px;
    padding: 24px 24px;
    border: 1px solid rgba(148, 163, 184, 0.25);
    text-align: center;
    margin-bottom: 22px;
    box-shadow: 0 10px 24px rgba(15, 23, 42, 0.06);
    min-height: 165px;
    width: 100%;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.dataset-metric-value {
    font-size: 34px;
    font-weight: 800;
    color: #2563eb !important;
    line-height: 1;
    margin-bottom: 16px;
}

.dataset-metric-label {
    font-size: 13px;
    color: #64748b !important;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
    line-height: 1.6;
    min-height: 42px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.footer {
    text-align: center;
    color: #64748b;
    font-size: 13px;
    margin-top: 38px;
}
</style>
""",
    unsafe_allow_html=True,
)


@st.cache_data
def load_data():
    return pd.read_csv("data/student-scores.csv")


df = load_data()


st.sidebar.markdown("---")
st.sidebar.markdown("### 🔎 Filtre dataset")

genuri_disponibile = sorted(df["gender"].dropna().unique().tolist())
genuri_selectate = st.sidebar.multiselect(
    "Gen",
    options=genuri_disponibile,
    default=genuri_disponibile,
)

job_disponibil = sorted(df["part_time_job"].dropna().unique().tolist())
job_selectat = st.sidebar.multiselect(
    "Job part-time",
    options=job_disponibil,
    default=job_disponibil,
    format_func=lambda x: "Da" if x else "Nu",
)

activitati_disponibile = sorted(
    df["extracurricular_activities"].dropna().unique().tolist()
)
activitati_selectate = st.sidebar.multiselect(
    "Activități extracurriculare",
    options=activitati_disponibile,
    default=activitati_disponibile,
    format_func=lambda x: "Da" if x else "Nu",
)

aspiratii_disponibile = sorted(df["career_aspiration"].dropna().unique().tolist())
aspiratii_selectate = st.sidebar.multiselect(
    "Aspirație profesională",
    options=aspiratii_disponibile,
    default=aspiratii_disponibile,
)

absente_min = int(df["absence_days"].min())
absente_max = int(df["absence_days"].max())
interval_absente = st.sidebar.slider(
    "Interval zile de absență",
    min_value=absente_min,
    max_value=absente_max,
    value=(absente_min, absente_max),
)

studiu_min = int(df["weekly_self_study_hours"].min())
studiu_max = int(df["weekly_self_study_hours"].max())
interval_studiu = st.sidebar.slider(
    "Ore de studiu individual / săptămână",
    min_value=studiu_min,
    max_value=studiu_max,
    value=(studiu_min, studiu_max),
)

math_min = int(df["math_score"].min())
math_max = int(df["math_score"].max())
interval_math = st.sidebar.slider(
    "Interval scor matematică",
    min_value=math_min,
    max_value=math_max,
    value=(math_min, math_max),
)

english_min = int(df["english_score"].min())
english_max = int(df["english_score"].max())
interval_english = st.sidebar.slider(
    "Interval scor engleză",
    min_value=english_min,
    max_value=english_max,
    value=(english_min, english_max),
)

df_filtrat = df[
    (df["gender"].isin(genuri_selectate))
    & (df["part_time_job"].isin(job_selectat))
    & (df["extracurricular_activities"].isin(activitati_selectate))
    & (df["career_aspiration"].isin(aspiratii_selectate))
    & (df["absence_days"] >= interval_absente[0])
    & (df["absence_days"] <= interval_absente[1])
    & (df["weekly_self_study_hours"] >= interval_studiu[0])
    & (df["weekly_self_study_hours"] <= interval_studiu[1])
    & (df["math_score"] >= interval_math[0])
    & (df["math_score"] <= interval_math[1])
    & (df["english_score"] >= interval_english[0])
    & (df["english_score"] <= interval_english[1])
].reset_index(drop=True)

st.markdown(
    """
<div class="hero">
<div class="hero-title">Student Performance<br>Dashboard</div>
<div class="hero-sub">
O aplicație interactivă pentru analiza factorilor care influențează performanța academică:
obiceiuri de studiu, stil de viață, prezență, activitate și rezultate educaționale.
</div>
<div class="badge-row">
<div class="badge">📊 Explorare date</div>
<div class="badge">📈 Vizualizări interactive</div>
<div class="badge">🧹 Preprocesare</div>
<div class="badge">🤖 Machine Learning</div>
</div>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="intro-grid">
<div class="info-card">
<div class="info-icon">🎯</div>
<div class="info-title">Scopul proiectului</div>
<div class="info-text">
Analiza performanței studenților și identificarea factorilor care pot influența rezultatele academice.
</div>
</div>

<div class="info-card">
<div class="info-icon">🧠</div>
<div class="info-title">Abordare</div>
<div class="info-text">
Combinarea analizei exploratorii, cu modele de Machine Learning într-o aplicație Streamlit interactivă.
</div>
</div>

<div class="info-card">
<div class="info-icon">🛠️</div>
<div class="info-title">Tehnologii</div>
<div class="info-text">
Pandas, Matplotlib, Plotly, scikit-learn și Streamlit pentru o aplicație interactivă multi-pagină.
</div>
</div>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown('<div class="section-title">Cuprins</div>', unsafe_allow_html=True)

st.markdown(
    """
<div class="page-grid">
<div class="page-card card-1">
<div class="page-number num-1">PAGINA 01</div>
<div class="page-title">Date și statistici</div>
<div class="page-desc">
Prezentarea dataset-ului, previzualizarea datelor, tipurile de variabile,
valorile lipsă, statisticile descriptive și indicatorii cheie.
</div>
</div>

<div class="page-card card-2">
<div class="page-number num-2">PAGINA 02</div>
<div class="page-title">Vizualizarea datelor</div>
<div class="page-desc">
Grafice statice și interactive pentru observarea relațiilor dintre variabilele
legate de studiu, stil de viață și performanță.
</div>
</div>

<div class="page-card card-3">
<div class="page-number num-3">PAGINA 03</div>
<div class="page-title">Preprocesarea datelor</div>
<div class="page-desc">
Codificarea variabilelor categoriale,
scalarea datelor și pregătirea dataset-ului pentru Machine Learning.
</div>
</div>

<div class="page-card card-4">
<div class="page-number num-4">PAGINA 04</div>
<div class="page-title">Machine Learning</div>
<div class="page-desc">
Aplicarea algoritmilor de Machine Learning pentru analizarea și estimarea
performanței academice a studenților.
</div>
</div>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="dataset-title">Să descoperim setul de date</div>
<div class="dataset-desc">
Folosește filtrele din sidebar pentru a explora rapid dataset-ul. Tabelul de mai jos se actualizează
în funcție de gen, job part-time, activități extracurriculare, aspirație profesională,
zile de absență, ore de studiu individual și scoruri la discipline.
</div>
""",
    unsafe_allow_html=True,
)

if len(df_filtrat) == 0:
    st.warning(
        "Nu există studenți care corespund filtrelor selectate. Ajustează filtrele din sidebar."
    )
else:
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            f"""
<div class="dataset-metric-card">
<div class="dataset-metric-value">{len(df_filtrat)}</div>
<div class="dataset-metric-label">Studenți selectați</div>
</div>
""",
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            f"""
<div class="dataset-metric-card">
<div class="dataset-metric-value">{df_filtrat["weekly_self_study_hours"].mean():.1f}</div>
<div class="dataset-metric-label">Ore medii de studiu / săptămână</div>
</div>
""",
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            f"""
<div class="dataset-metric-card">
<div class="dataset-metric-value">{df_filtrat["absence_days"].mean():.1f}</div>
<div class="dataset-metric-label">Zile medii de absență</div>
</div>
""",
            unsafe_allow_html=True,
        )

    numar_randuri = st.slider(
        "Câte înregistrări vrei să afișezi?",
        min_value=5,
        max_value=min(100, len(df_filtrat)),
        value=min(10, len(df_filtrat)),
        step=5,
    )

    coloane_afisate = [
        "id",
        "gender",
        "part_time_job",
        "absence_days",
        "extracurricular_activities",
        "weekly_self_study_hours",
        "career_aspiration",
        "math_score",
        "history_score",
        "physics_score",
        "chemistry_score",
        "biology_score",
        "english_score",
        "geography_score",
    ]

    st.dataframe(
        df_filtrat[coloane_afisate].head(numar_randuri),
        use_container_width=True,
        hide_index=True,
    )

st.markdown(
    """
<div class="footer">
Student Performance Dashboard · Proiect Pachete Software
</div>
""",
    unsafe_allow_html=True,
)
