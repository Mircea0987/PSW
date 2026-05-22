import streamlit as st
import pandas as pd
import plotly.express as px

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
.stTextInput label,
.stNumberInput label,
.stCheckbox label {
    color: #1e293b !important;
    font-weight: 600 !important;
}

[data-baseweb="select"] > div {
    background-color: white !important;
    border: 1px solid rgba(148, 163, 184, 0.45) !important;
    border-radius: 16px !important;
    color: #1e293b !important;
}

[data-baseweb="select"] span,
[data-baseweb="select"] div {
    color: #1e293b !important;
}

button[data-baseweb="tab"] p {
    color: #1e293b !important;
    font-weight: 700 !important;
}

button[data-baseweb="tab"][aria-selected="true"] p {
    color: #a855f7 !important;
}

[data-testid="stSlider"] * {
    color: #1e293b !important;
}

[data-testid="stDataFrame"] {
    background: white !important;
    border-radius: 18px !important;
}

.stAlert p,
.stAlert div {
    color: #1e293b !important;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #7c3aed 0%, #2563eb 100%) !important;
}

[data-testid="stSidebar"] * {
    color: white !important;
}

/* Expander styling */
[data-testid="stExpander"] {
    background: white !important;
    border: 1px solid rgba(168, 85, 247, 0.35) !important;
    border-radius: 20px !important;
    box-shadow: 0 10px 24px rgba(15, 23, 42, 0.06) !important;
    overflow: hidden !important;
    margin-top: 18px !important;
    margin-bottom: 24px !important;
}

[data-testid="stExpander"] details {
    background: white !important;
}

[data-testid="stExpander"] summary {
    background: #faf5ff !important;
    padding: 18px 22px !important;
    border-radius: 20px !important;
    color: #581c87 !important;
    font-weight: 800 !important;
    font-size: 15px !important;
}

[data-testid="stExpander"] summary:hover {
    background: #f3e8ff !important;
}

[data-testid="stExpander"] summary p {
    color: #581c87 !important;
    font-weight: 800 !important;
}

[data-testid="stExpander"] svg {
    color: #7e22ce !important;
    fill: #7e22ce !important;
}

[data-testid="stExpander"] div[data-testid="stVerticalBlock"] {
    background: white !important;
    padding: 10px 18px 18px 18px !important;
}

/* Code block styling */
[data-testid="stCodeBlock"] {
    background: #f8fafc !important;
    border: 1px solid rgba(148, 163, 184, 0.35) !important;
    border-radius: 18px !important;
    overflow: hidden !important;
}

[data-testid="stCodeBlock"] pre {
    background: #f8fafc !important;
    color: #0f172a !important;
    border-radius: 18px !important;
}

[data-testid="stCodeBlock"] code {
    background: #f8fafc !important;
    color: #0f172a !important;
    font-size: 14px !important;
}

.page-hero {
    background: white;
    border-radius: 30px;
    padding: 46px 52px;
    margin-bottom: 32px;
    border: 1px solid rgba(148, 163, 184, 0.25);
    border-top: 8px solid #a855f7;
    box-shadow: 0 18px 40px rgba(15, 23, 42, 0.10);
}

.page-label {
    display: inline-block;
    background: #f3e8ff;
    color: #9333ea !important;
    padding: 8px 14px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 1.5px;
    margin-bottom: 18px;
}

.page-title {
    font-size: 46px;
    font-weight: 800;
    color: #0f172a !important;
    line-height: 1.1;
    margin-bottom: 16px;
}

.page-desc {
    font-size: 17px;
    color: #64748b !important;
    line-height: 1.7;
    max-width: 900px;
}

.section-title {
    font-size: 30px;
    font-weight: 800;
    color: #0f172a !important;
    margin: 36px 0 18px 0;
}

.info-card {
    background: white;
    border-radius: 24px;
    padding: 26px 30px;
    border: 1px solid rgba(148, 163, 184, 0.25);
    box-shadow: 0 12px 28px rgba(15, 23, 42, 0.08);
    margin-bottom: 22px;
}

.info-title {
    font-size: 22px;
    font-weight: 800;
    color: #0f172a !important;
    margin-bottom: 10px;
}

.info-text {
    font-size: 15px;
    color: #64748b !important;
    line-height: 1.7;
}

.metric-card {
    background: white;
    border-radius: 22px;
    padding: 22px 24px;
    border: 1px solid rgba(148, 163, 184, 0.25);
    box-shadow: 0 10px 24px rgba(15, 23, 42, 0.07);
    text-align: center;
    min-height: 120px;
    width: 100%;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin-bottom: 22px;
}

.metric-value {
    font-size: 34px;
    font-weight: 800;
    color: #a855f7 !important;
    line-height: 1;
    margin-bottom: 12px;
}

.metric-label {
    font-size: 13px;
    color: #64748b !important;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
    line-height: 1.4;
}

.explain-box {
    background: #eff6ff;
    border: 1px solid #bfdbfe;
    border-left: 6px solid #2563eb;
    border-radius: 18px;
    padding: 18px 22px;
    color: #1e3a8a !important;
    font-size: 15px;
    line-height: 1.7;
    margin-top: 18px;
    margin-bottom: 18px;
}

.explain-box strong {
    color: #1e3a8a !important;
}

.feature-box {
    background: #faf5ff;
    border: 1px solid #e9d5ff;
    border-left: 6px solid #a855f7;
    border-radius: 18px;
    padding: 18px 22px;
    color: #581c87 !important;
    font-size: 15px;
    line-height: 1.7;
    margin-top: 18px;
    margin-bottom: 18px;
}

.feature-box strong {
    color: #581c87 !important;
}

.warning-box {
    background: #fff7ed;
    border: 1px solid #fed7aa;
    border-left: 6px solid #f97316;
    border-radius: 18px;
    padding: 18px 22px;
    color: #9a3412 !important;
    font-size: 15px;
    line-height: 1.7;
    margin-top: 18px;
    margin-bottom: 18px;
}

.warning-box strong {
    color: #9a3412 !important;
}
</style>
""",
    unsafe_allow_html=True,
)


@st.cache_data
def load_data():
    return pd.read_csv("data/student-scores.csv")


df = load_data()


st.markdown(
    """
<div class="page-hero">
<div class="page-label">PAGINA 02</div>
<div class="page-title">Feature Engineering</div>
<div class="page-desc">
Această pagină este dedicată creării unei variabile noi pe baza scorurilor existente.
Prin feature engineering, transformăm datele brute într-o formă mai utilă pentru analiză,
vizualizare și Machine Learning.
</div>
</div>
""",
    unsafe_allow_html=True,
)


score_columns = [
    "math_score",
    "history_score",
    "physics_score",
    "chemistry_score",
    "biology_score",
    "english_score",
    "geography_score",
]

df["average_score"] = df[score_columns].mean(axis=1)

st.markdown(
    '<div class="section-title">Pasul 1 - Crearea variabilei average_score</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="feature-box">
<strong>De ce adăugăm această variabilă?</strong><br>
Dataset-ul conține mai multe scoruri separate pentru discipline diferite. Pentru analiza generală a performanței,
este util să avem o singură variabilă care rezumă rezultatele academice ale fiecărui student.
Variabila <strong>average_score</strong> va fi folosită ulterior ca variabilă țintă în etapa de Machine Learning.
</div>
""",
    unsafe_allow_html=True,
)

with st.expander("Vezi codul folosit pentru crearea variabilei average_score"):
    st.code(
        """
score_columns = [
    "math_score",
    "history_score",
    "physics_score",
    "chemistry_score",
    "biology_score",
    "english_score",
    "geography_score",
]

df["average_score"] = df[score_columns].mean(axis=1)
""",
        language="python",
    )

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        f"""
<div class="metric-card">
<div class="metric-value">{df["average_score"].mean():.2f}</div>
<div class="metric-label">Scor mediu general</div>
</div>
""",
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        f"""
<div class="metric-card">
<div class="metric-value">{df["average_score"].min():.2f}</div>
<div class="metric-label">Scor minim</div>
</div>
""",
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        f"""
<div class="metric-card">
<div class="metric-value">{df["average_score"].max():.2f}</div>
<div class="metric-label">Scor maxim</div>
</div>
""",
        unsafe_allow_html=True,
    )

st.markdown(
    """
<div class="explain-box">
<strong>Interpretare:</strong> valorile de mai sus oferă o primă imagine asupra noii variabile.
Media arată nivelul general al performanței în dataset, iar valorile minimă și maximă arată
limitele observate pentru scorul mediu calculat.
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-title">Pasul 2 - Dataset-ul după adăugarea noii variabile</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="info-card">
<div class="info-text">
Tabelul de mai jos prezintă dataset-ul după adăugarea variabilei <strong>average_score</strong>.
Noua coloană este adăugată la final și va fi utilizată în etapele următoare pentru analiză și modelare.
</div>
</div>
""",
    unsafe_allow_html=True,
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
    "average_score",
]

numar_randuri = st.slider(
    "Câte înregistrări vrei să afișezi?",
    min_value=5,
    max_value=100,
    value=10,
    step=5,
)

st.dataframe(
    df[coloane_afisate].head(numar_randuri),
    use_container_width=True,
    hide_index=True,
)

st.markdown(
    '<div class="section-title">Pasul 3 - Distribuția variabilei average_score</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="info-card">
<div class="info-text">
Deoarece <strong>average_score</strong> va fi utilizată ca variabilă țintă în etapa de Machine Learning,
este important să analizăm distribuția ei. O distribuție foarte dezechilibrată sau cu valori extreme
poate influența performanța modelelor predictive.
</div>
</div>
""",
    unsafe_allow_html=True,
)

tip_grafic = st.selectbox(
    "Selectează tipul de grafic pentru analiza distribuției:",
    [
        "Histogramă",
        "Box plot",
        "Violin plot",
    ],
)

if tip_grafic == "Histogramă":
    fig = px.histogram(
        df,
        x="average_score",
        nbins=20,
        title="Distribuția variabilei average_score",
        color_discrete_sequence=["#a855f7"],
    )

    fig.update_layout(
        xaxis_title="Average score",
        yaxis_title="Număr de studenți",
    )

elif tip_grafic == "Box plot":
    fig = px.box(
        df,
        y="average_score",
        title="Box plot pentru variabila average_score",
        color_discrete_sequence=["#a855f7"],
    )

    fig.update_layout(
        yaxis_title="Average score",
    )

else:
    fig = px.violin(
        df,
        y="average_score",
        box=True,
        points="all",
        title="Violin plot pentru variabila average_score",
        color_discrete_sequence=["#a855f7"],
    )

    fig.update_layout(
        yaxis_title="Average score",
    )

fig.update_layout(
    title_font_size=20,
    title_font_color="#0f172a",
    font=dict(
        family="Poppins",
        color="#1e293b",
    ),
    paper_bgcolor="white",
    plot_bgcolor="white",
    margin=dict(l=40, r=40, t=70, b=40),
    height=500,
    xaxis=dict(
        showgrid=False,
        linecolor="#cbd5e1",
        tickfont=dict(color="#334155"),
    ),
    yaxis=dict(
        gridcolor="#e2e8f0",
        linecolor="#cbd5e1",
        tickfont=dict(color="#334155"),
    ),
)

st.plotly_chart(
    fig,
    use_container_width=True,
)

st.markdown(
    """
<div class="explain-box">
<strong>Interpretare:</strong> această vizualizare ajută la observarea formei distribuției noii variabile.
Histograma arată unde sunt concentrate cele mai multe valori, box plot-ul evidențiază mediana,
cuartilele și valorile extreme, iar violin plot-ul combină informații despre distribuție și densitate.
Această variabilă va fi analizată mai detaliat în etapa de Exploratory Data Analysis.
</div>
""",
    unsafe_allow_html=True,
)

st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:#64748b !important; font-size:13px;'>"
    "Student Performance Dashboard · Pagina 02 · Feature Engineering"
    "</p>",
    unsafe_allow_html=True,
)
