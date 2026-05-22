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
.stMultiSelect label,
.stNumberInput label,
.stRadio label,
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
    color: #f97316 !important;
}

[data-testid="stSlider"] * {
    color: #1e293b !important;
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

[data-testid="stSidebar"] [data-baseweb="select"] span,
[data-testid="stSidebar"] [data-baseweb="select"] div {
    color: #1e293b !important;
}

[data-testid="stDataFrame"] {
    background: white !important;
    border-radius: 18px !important;
}

.stButton button {
    background: white !important;
    color: #f97316 !important;
    border: 1px solid #fed7aa !important;
    border-radius: 14px !important;
    padding: 10px 22px !important;
    font-weight: 800 !important;
    box-shadow: 0 8px 18px rgba(249, 115, 22, 0.12) !important;
}

.stButton button:hover {
    background: #fff7ed !important;
    border-color: #fdba74 !important;
    color: #ea580c !important;
}

.stButton button p {
    color: #f97316 !important;
}

.page-hero {
    background: white;
    border-radius: 30px;
    padding: 46px 52px;
    margin-bottom: 32px;
    border: 1px solid rgba(148, 163, 184, 0.25);
    border-top: 8px solid #f97316;
    box-shadow: 0 18px 40px rgba(15, 23, 42, 0.10);
}

.page-label {
    display: inline-block;
    background: #ffedd5;
    color: #ea580c !important;
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
    margin: 38px 0 18px 0;
}

.subsection-title {
    font-size: 23px;
    font-weight: 800;
    color: #0f172a !important;
    margin: 26px 0 14px 0;
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

.control-card {
    background: white;
    border-radius: 24px;
    padding: 24px 28px;
    border: 1px solid rgba(148, 163, 184, 0.25);
    box-shadow: 0 12px 28px rgba(15, 23, 42, 0.08);
    margin-bottom: 22px;
}

.metric-card {
    background: #f8fafc;
    border-radius: 22px;
    padding: 22px 24px;
    border: 1px solid rgba(148, 163, 184, 0.25);
    text-align: center;
    margin-bottom: 20px;
    box-shadow: 0 10px 24px rgba(15, 23, 42, 0.06);
    min-height: 125px;
    width: 100%;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.metric-value {
    font-size: 34px;
    font-weight: 800;
    color: #f97316 !important;
    line-height: 1;
    margin-bottom: 10px;
}

.metric-label {
    font-size: 13px;
    color: #64748b !important;
    font-weight: 700;
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

.success-box {
    background: #f0fdf4;
    border: 1px solid #bbf7d0;
    border-left: 6px solid #22c55e;
    border-radius: 18px;
    padding: 18px 22px;
    color: #14532d !important;
    font-size: 15px;
    line-height: 1.7;
    margin-top: 18px;
    margin-bottom: 18px;
}

.success-box strong {
    color: #14532d !important;
}

.code-box {
    background: #0f172a;
    color: #e2e8f0 !important;
    border-radius: 16px;
    padding: 18px 20px;
    font-size: 14px;
    line-height: 1.7;
    margin-top: 14px;
    margin-bottom: 22px;
    overflow-x: auto;
}

.footer {
    text-align: center;
    color: #64748b !important;
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


def variable_type_label(dtype):
    if pd.api.types.is_integer_dtype(dtype):
        return "Numerică întreagă"
    if pd.api.types.is_float_dtype(dtype):
        return "Numerică zecimală"
    if pd.api.types.is_bool_dtype(dtype):
        return "Booleană"
    return "Categorială / text"


def metric_label(column_name):
    labels = {
        "id": "ID",
        "first_name": "Prenume",
        "last_name": "Nume",
        "email": "Email",
        "gender": "Gen",
        "part_time_job": "Job part-time",
        "absence_days": "Zile de absență",
        "extracurricular_activities": "Activități extracurriculare",
        "weekly_self_study_hours": "Ore de studiu individual / săptămână",
        "career_aspiration": "Aspirație profesională",
        "math_score": "Scor matematică",
        "history_score": "Scor istorie",
        "physics_score": "Scor fizică",
        "chemistry_score": "Scor chimie",
        "biology_score": "Scor biologie",
        "english_score": "Scor engleză",
        "geography_score": "Scor geografie",
    }

    return labels.get(column_name, column_name)


def style_plot(fig, title, height=500):
    fig.update_layout(
        title=title,
        title_font_size=20,
        title_font_color="#0f172a",
        font=dict(
            family="Poppins",
            color="#1e293b",
        ),
        paper_bgcolor="white",
        plot_bgcolor="white",
        margin=dict(l=40, r=40, t=75, b=45),
        height=height,
        legend=dict(
            font=dict(color="#1e293b"),
            bgcolor="rgba(255,255,255,0.7)",
        ),
    )

    fig.update_xaxes(
        showgrid=False,
        linecolor="#cbd5e1",
        tickfont=dict(color="#334155"),
        title_font=dict(color="#1e293b"),
    )

    fig.update_yaxes(
        gridcolor="#e2e8f0",
        linecolor="#cbd5e1",
        tickfont=dict(color="#334155"),
        title_font=dict(color="#1e293b"),
    )

    return fig


df = load_data()

st.markdown(
    """
<div class="page-hero">
<div class="page-label">PAGINA 02</div>
<div class="page-title">Date și statistici</div>
<div class="page-desc">
Această pagină prezintă structura inițială a dataset-ului, tipurile de variabile,
valorile lipsă și statistici descriptive de bază. Scopul este înțelegerea datelor înainte
de etapele de feature engineering, analiză exploratorie, preprocesare și Machine Learning.
</div>
</div>
""",
    unsafe_allow_html=True,
)

# -------------------------------------------------------------------
# SECTION 1 - LOC AND ILOC
# -------------------------------------------------------------------

st.markdown(
    '<div class="section-title">Pasul 1 - Accesarea datelor cu loc și iloc</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="info-card">
<div class="info-text">
În pandas, metodele <strong>loc</strong> și <strong>iloc</strong> sunt folosite pentru accesarea și selectarea datelor.
Metoda <strong>loc</strong> selectează date pe baza etichetelor coloanelor sau a unor condiții logice,
iar metoda <strong>iloc</strong> selectează date pe baza poziției numerice a rândurilor și coloanelor.
</div>
</div>
""",
    unsafe_allow_html=True,
)

loc_tab, iloc_tab = st.tabs(
    [
        "Exemplu interactiv cu loc",
        "Exemplu interactiv cu iloc",
    ]
)

with loc_tab:
    st.markdown(
        '<div class="subsection-title">Selectare condițională cu loc</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
<div class="explain-box">
Aici folosim <strong>loc</strong> pentru a selecta rândurile care respectă o condiție.
Poți alege coloana numerică, operatorul, valoarea de comparație și coloanele care vor fi afișate.
</div>
""",
        unsafe_allow_html=True,
    )

    numeric_columns_for_loc = [
        column
        for column in df.select_dtypes(include=["int64", "float64"]).columns.tolist()
        if column != "id"
    ]

    loc_col1, loc_col2, loc_col3 = st.columns(3)

    with loc_col1:
        loc_condition_column = st.selectbox(
            "Coloană pentru condiție",
            options=numeric_columns_for_loc,
            index=(
                numeric_columns_for_loc.index("math_score")
                if "math_score" in numeric_columns_for_loc
                else 0
            ),
            format_func=metric_label,
        )

    with loc_col2:
        loc_operator = st.selectbox(
            "Operator",
            options=[
                ">=",
                ">",
                "<=",
                "<",
                "==",
            ],
        )

    with loc_col3:
        min_value = float(df[loc_condition_column].min())
        max_value = float(df[loc_condition_column].max())
        default_value = float(df[loc_condition_column].median())

        loc_value = st.slider(
            "Valoare de comparație",
            min_value=min_value,
            max_value=max_value,
            value=default_value,
            step=1.0,
        )

    default_loc_columns = [
        column
        for column in [
            "id",
            "gender",
            "absence_days",
            "weekly_self_study_hours",
            loc_condition_column,
        ]
        if column in df.columns
    ]

    selected_loc_columns = st.multiselect(
        "Coloane afișate",
        options=df.columns.tolist(),
        default=default_loc_columns,
        format_func=metric_label,
    )

    if loc_operator == ">=":
        loc_condition = df[loc_condition_column] >= loc_value
    elif loc_operator == ">":
        loc_condition = df[loc_condition_column] > loc_value
    elif loc_operator == "<=":
        loc_condition = df[loc_condition_column] <= loc_value
    elif loc_operator == "<":
        loc_condition = df[loc_condition_column] < loc_value
    else:
        loc_condition = df[loc_condition_column] == loc_value

    if len(selected_loc_columns) == 0:
        st.warning("Alege cel puțin o coloană pentru afișare.")
    else:
        loc_result = df.loc[
            loc_condition,
            selected_loc_columns,
        ].head(15)

        st.markdown(
            f"""
<div class="code-box">
df.loc[df["{loc_condition_column}"] {loc_operator} {loc_value}, {selected_loc_columns}].head(15)
</div>
""",
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="subsection-title">Rezultat loc</div>',
            unsafe_allow_html=True,
        )

        st.dataframe(
            loc_result,
            use_container_width=True,
            hide_index=True,
        )

        st.markdown(
            f"""
<div class="success-box">
<strong>Rezultat:</strong> au fost identificate <strong>{int(loc_condition.sum())}</strong> rânduri
care respectă condiția <strong>{metric_label(loc_condition_column)} {loc_operator} {loc_value}</strong>.
Tabelul afișează primele 15 rezultate.
</div>
""",
            unsafe_allow_html=True,
        )

with iloc_tab:
    st.markdown(
        '<div class="subsection-title">Selectare pozițională cu iloc</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
<div class="explain-box">
Aici folosim <strong>iloc</strong> pentru a selecta date pe baza poziției numerice.
Poți alege intervalul de rânduri și intervalul de coloane care vor fi afișate.
</div>
""",
        unsafe_allow_html=True,
    )

    iloc_col1, iloc_col2 = st.columns(2)

    with iloc_col1:
        row_interval = st.slider(
            "Interval rânduri",
            min_value=0,
            max_value=int(df.shape[0]),
            value=(0, min(10, int(df.shape[0]))),
            step=1,
        )

    with iloc_col2:
        column_interval = st.slider(
            "Interval coloane",
            min_value=0,
            max_value=int(df.shape[1]),
            value=(0, min(6, int(df.shape[1]))),
            step=1,
        )

    iloc_result = df.iloc[
        row_interval[0] : row_interval[1],
        column_interval[0] : column_interval[1],
    ]

    st.markdown(
        f"""
<div class="code-box">
df.iloc[{row_interval[0]}:{row_interval[1]}, {column_interval[0]}:{column_interval[1]}]
</div>
""",
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="subsection-title">Rezultat iloc</div>',
        unsafe_allow_html=True,
    )

    st.dataframe(
        iloc_result,
        use_container_width=True,
        hide_index=True,
    )

    selected_column_names = df.columns[column_interval[0] : column_interval[1]].tolist()

    st.markdown(
        f"""
<div class="success-box">
<strong>Rezultat:</strong> metoda <strong>iloc</strong> a selectat rândurile de la poziția
<strong>{row_interval[0]}</strong> până la <strong>{row_interval[1] - 1}</strong>
și coloanele de la poziția <strong>{column_interval[0]}</strong> până la
<strong>{column_interval[1] - 1}</strong>. Coloanele selectate sunt:
<strong>{", ".join(selected_column_names)}</strong>.
</div>
""",
        unsafe_allow_html=True,
    )

# -------------------------------------------------------------------
# SECTION 2 - DATASET OVERVIEW
# -------------------------------------------------------------------

st.markdown(
    '<div class="section-title">Pasul 2 - Prezentarea generală a dataset-ului</div>',
    unsafe_allow_html=True,
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        f"""
<div class="metric-card">
<div class="metric-value">{df.shape[0]}</div>
<div class="metric-label">Număr de rânduri</div>
</div>
""",
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        f"""
<div class="metric-card">
<div class="metric-value">{df.shape[1]}</div>
<div class="metric-label">Număr de coloane</div>
</div>
""",
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        f"""
<div class="metric-card">
<div class="metric-value">{int(df.isnull().sum().sum())}</div>
<div class="metric-label">Valori lipsă totale</div>
</div>
""",
        unsafe_allow_html=True,
    )

st.markdown(
    """
<div class="info-card">
<div class="info-text">
În această secțiune sunt prezentate primele înregistrări, tipurile de variabile și valorile lipsă.
Aceste informații sunt necesare pentru înțelegerea structurii dataset-ului înainte de aplicarea
preprocesării și a modelelor de Machine Learning.
</div>
</div>
""",
    unsafe_allow_html=True,
)

tab1, tab2, tab3 = st.tabs(
    [
        "Primele rânduri",
        "Tipuri de variabile",
        "Valori lipsă",
    ]
)

with tab1:
    number_of_rows = st.slider(
        "Câte rânduri vrei să afișezi?",
        min_value=5,
        max_value=min(50, len(df)),
        value=10,
        step=5,
    )

    st.dataframe(
        df.head(number_of_rows),
        use_container_width=True,
        hide_index=True,
    )

with tab2:
    variable_types = pd.DataFrame(
        {
            "Variabilă": df.columns,
            "Tip pandas": df.dtypes.astype(str).values,
            "Tip interpretat": [variable_type_label(dtype) for dtype in df.dtypes],
            "Valori unice": [df[column].nunique() for column in df.columns],
            "Exemplu valoare": [
                (
                    df[column].dropna().iloc[0]
                    if df[column].dropna().shape[0] > 0
                    else None
                )
                for column in df.columns
            ],
        }
    )

    st.dataframe(
        variable_types,
        use_container_width=True,
        hide_index=True,
    )

with tab3:
    missing_values = df.isnull().sum()
    missing_percentages = (df.isnull().mean() * 100).round(2)

    missing_table = pd.DataFrame(
        {
            "Variabilă": missing_values.index,
            "Valori lipsă": missing_values.values,
            "Procent valori lipsă": missing_percentages.values,
        }
    )

    st.dataframe(
        missing_table,
        use_container_width=True,
        hide_index=True,
    )

    if missing_values.sum() == 0:
        st.markdown(
            """
<div class="success-box">
<strong>Nu au fost identificate valori lipsă.</strong><br>
Dataset-ul este complet din punctul de vedere al valorilor lipsă.
</div>
""",
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
<div class="warning-box">
Au fost identificate valori lipsă. Acestea trebuie analizate și tratate în etapa de preprocesare.
</div>
""",
            unsafe_allow_html=True,
        )

# -------------------------------------------------------------------
# SECTION 3 - DESCRIPTIVE STATISTICS
# -------------------------------------------------------------------

st.markdown(
    '<div class="section-title">Pasul 3 - Statistici descriptive</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="info-card">
<div class="info-text">
Statisticile descriptive sunt calculate separat pentru variabilele numerice și pentru variabilele non-numerice.
Coloana <strong>id</strong> este exclusă din statisticile numerice, deoarece reprezintă un identificator,
nu o variabilă de analiză.
</div>
</div>
""",
    unsafe_allow_html=True,
)

numeric_columns = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
numeric_columns = [column for column in numeric_columns if column != "id"]

non_numeric_columns = df.select_dtypes(exclude=["int64", "float64"]).columns.tolist()

stats_tab1, stats_tab2 = st.tabs(
    [
        "Variabile numerice",
        "Variabile non-numerice",
    ]
)

with stats_tab1:
    st.dataframe(
        df[numeric_columns].describe().round(2),
        use_container_width=True,
    )

with stats_tab2:
    if len(non_numeric_columns) == 0:
        st.info("Nu există variabile non-numerice în dataset.")
    else:
        st.dataframe(
            df[non_numeric_columns].describe(),
            use_container_width=True,
        )

# -------------------------------------------------------------------
# SECTION 4 - DISTRIBUTIONS
# -------------------------------------------------------------------

st.markdown(
    '<div class="section-title">Pasul 4 - Distribuții ale variabilelor</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="info-card">
<div class="info-text">
Această secțiune permite vizualizarea distribuției variabilelor relevante. Pentru variabilele categoriale,
folosim grafice de tip bar chart, iar pentru variabilele numerice folosim histogramă sau box plot.
</div>
</div>
""",
    unsafe_allow_html=True,
)

dist_tab1, dist_tab2 = st.tabs(
    [
        "Distribuții categoriale",
        "Distribuții numerice",
    ]
)

with dist_tab1:
    categorical_distribution_columns = [
        column
        for column in [
            "gender",
            "part_time_job",
            "extracurricular_activities",
            "career_aspiration",
        ]
        if column in df.columns
    ]

    selected_categorical_column = st.selectbox(
        "Alege variabila categorială",
        options=categorical_distribution_columns,
        format_func=metric_label,
    )

    categorical_counts = (
        df[selected_categorical_column].value_counts(dropna=False).reset_index()
    )

    categorical_counts.columns = [
        selected_categorical_column,
        "Număr de înregistrări",
    ]

    st.markdown(
        '<div class="subsection-title">Tabel distribuție</div>',
        unsafe_allow_html=True,
    )

    st.dataframe(
        categorical_counts,
        use_container_width=True,
        hide_index=True,
    )

    fig_categorical = px.bar(
        categorical_counts,
        x=selected_categorical_column,
        y="Număr de înregistrări",
        text="Număr de înregistrări",
        color=selected_categorical_column,
        color_discrete_sequence=px.colors.qualitative.Set3,
        title=f"Distribuția variabilei {metric_label(selected_categorical_column)}",
    )

    fig_categorical.update_traces(
        textposition="outside",
    )

    fig_categorical = style_plot(
        fig_categorical,
        title=f"Distribuția variabilei {metric_label(selected_categorical_column)}",
        height=520,
    )

    st.plotly_chart(
        fig_categorical,
        use_container_width=True,
    )

with dist_tab2:
    numerical_distribution_columns = [
        column for column in numeric_columns if column != "id"
    ]

    selected_numeric_column = st.selectbox(
        "Alege variabila numerică",
        options=numerical_distribution_columns,
        format_func=metric_label,
    )

    numeric_plot_type = st.radio(
        "Tip grafic",
        options=[
            "Histogramă",
            "Box plot",
        ],
        horizontal=True,
    )

    st.markdown(
        '<div class="subsection-title">Statistici rapide</div>',
        unsafe_allow_html=True,
    )

    quick_stats = pd.DataFrame(
        {
            "Indicator": [
                "Minim",
                "Maxim",
                "Medie",
                "Mediană",
                "Abatere standard",
            ],
            "Valoare": [
                df[selected_numeric_column].min(),
                df[selected_numeric_column].max(),
                df[selected_numeric_column].mean(),
                df[selected_numeric_column].median(),
                df[selected_numeric_column].std(),
            ],
        }
    )

    st.dataframe(
        quick_stats.round(2),
        use_container_width=True,
        hide_index=True,
    )

    if numeric_plot_type == "Histogramă":
        fig_numeric = px.histogram(
            df,
            x=selected_numeric_column,
            nbins=20,
            title=f"Distribuția variabilei {metric_label(selected_numeric_column)}",
            color_discrete_sequence=["#f97316"],
        )
    else:
        fig_numeric = px.box(
            df,
            y=selected_numeric_column,
            points="all",
            title=f"Box plot pentru {metric_label(selected_numeric_column)}",
            color_discrete_sequence=["#f97316"],
        )

    fig_numeric = style_plot(
        fig_numeric,
        title=f"Distribuția variabilei {metric_label(selected_numeric_column)}",
        height=520,
    )

    st.plotly_chart(
        fig_numeric,
        use_container_width=True,
    )

st.markdown("---")
st.markdown(
    """
<div class="footer">
Student Performance Dashboard · Pagina 02 · Date și statistici
</div>
""",
    unsafe_allow_html=True,
)
