import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.preprocessing import StandardScaler, MinMaxScaler

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
    color: #22c55e !important;
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
    color: #16a34a !important;
    border: 1px solid #bbf7d0 !important;
    border-radius: 14px !important;
    padding: 10px 22px !important;
    font-weight: 800 !important;
    box-shadow: 0 8px 18px rgba(34, 197, 94, 0.12) !important;
}

.stButton button:hover {
    background: #f0fdf4 !important;
    border-color: #86efac !important;
    color: #15803d !important;
}

.stButton button p {
    color: #16a34a !important;
}

.page-hero {
    background: white;
    border-radius: 30px;
    padding: 46px 52px;
    margin-bottom: 32px;
    border: 1px solid rgba(148, 163, 184, 0.25);
    border-top: 8px solid #22c55e;
    box-shadow: 0 18px 40px rgba(15, 23, 42, 0.10);
}

.page-label {
    display: inline-block;
    background: #dcfce7;
    color: #16a34a !important;
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
    color: #16a34a !important;
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


def add_average_score(dataframe):
    data = dataframe.copy()

    score_columns = [
        "math_score",
        "history_score",
        "physics_score",
        "chemistry_score",
        "biology_score",
        "english_score",
        "geography_score",
    ]

    data["average_score"] = data[score_columns].mean(axis=1)

    return data


def create_removed_variables_table(columns_to_remove):
    reasons = {
        "id": "Identificator tehnic; nu conține informație predictivă utilă.",
        "first_name": "Informație personală; nu este relevantă pentru predicția performanței.",
        "last_name": "Informație personală; nu este relevantă pentru predicția performanței.",
        "email": "Informație personală/de identificare; nu trebuie folosită în model.",
        "career_aspiration": "Variabilă categorială cu multe valori și categorie Unknown; poate introduce zgomot și complexitate în prima versiune a modelului.",
        "math_score": "Scor individual folosit la calcularea targetului average_score; păstrarea lui ar produce data leakage.",
        "history_score": "Scor individual folosit la calcularea targetului average_score; păstrarea lui ar produce data leakage.",
        "physics_score": "Scor individual folosit la calcularea targetului average_score; păstrarea lui ar produce data leakage.",
        "chemistry_score": "Scor individual folosit la calcularea targetului average_score; păstrarea lui ar produce data leakage.",
        "biology_score": "Scor individual folosit la calcularea targetului average_score; păstrarea lui ar produce data leakage.",
        "english_score": "Scor individual folosit la calcularea targetului average_score; păstrarea lui ar produce data leakage.",
        "geography_score": "Scor individual folosit la calcularea targetului average_score; păstrarea lui ar produce data leakage.",
    }

    removed_variables = pd.DataFrame(
        {
            "Variabilă eliminată": columns_to_remove,
            "Motiv": [reasons[column] for column in columns_to_remove],
        }
    )

    return removed_variables


def detect_outliers_iqr(dataframe, column_name, multiplier):
    q1 = dataframe[column_name].quantile(0.25)
    q3 = dataframe[column_name].quantile(0.75)
    iqr = q3 - q1

    lower_limit = q1 - multiplier * iqr
    upper_limit = q3 + multiplier * iqr

    outlier_mask = (dataframe[column_name] < lower_limit) | (
        dataframe[column_name] > upper_limit
    )

    return outlier_mask


def detect_outliers_z_score(dataframe, column_name, threshold):
    mean_value = dataframe[column_name].mean()
    std_value = dataframe[column_name].std()

    if std_value == 0:
        outlier_mask = pd.Series(False, index=dataframe.index)
    else:
        z_scores = (dataframe[column_name] - mean_value) / std_value
        outlier_mask = z_scores.abs() > threshold

    return outlier_mask


def style_plot(fig, title, height=480):
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


def create_scaled_preview(dataframe, columns_to_scale, scaling_method):
    preview_df = dataframe.copy()

    if scaling_method == "StandardScaler":
        scaler = StandardScaler()
        suffix = "_standard_scaled"
    else:
        scaler = MinMaxScaler()
        suffix = "_minmax_scaled"

    scaled_values = scaler.fit_transform(preview_df[columns_to_scale])

    for index, column in enumerate(columns_to_scale):
        preview_df[f"{column}{suffix}"] = scaled_values[:, index]

    return preview_df, suffix


df = load_data()
df = add_average_score(df)


st.markdown(
    """
<div class="page-hero">
<div class="page-label">PAGINA 04</div>
<div class="page-title">Preprocesarea datelor</div>
<div class="page-desc">
Această pagină pregătește dataset-ul pentru etapa de Machine Learning. Începem prin alegerea
variabilelor relevante și construirea unui dataset separat, dedicat modelării predictive.
</div>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-title">Pasul 1 - Alegerea variabilelor pentru Machine Learning</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="warning-box">
<strong>Observație:</strong> pentru construirea modelului de Machine Learning, unele variabile nu sunt utile
sau pot crea probleme. Coloanele de identificare, precum <strong>id</strong>, <strong>first_name</strong>,
<strong>last_name</strong> și <strong>email</strong>, nu conțin informație relevantă. Ele pot fi păstrate
în dataset-ul original și reunite ulterior cu rezultatele modelului, dacă este necesar pentru afișare sau interpretare.
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="explain-box">
<strong>Despre career_aspiration:</strong> această variabilă este eliminată deoarece
are multe categorii și include valori de tip <strong>Unknown</strong>. Deși poate fi interesantă exploratoriu,
în modelare poate crește complexitatea prin multe coloane rezultate din encoding și poate introduce zgomot.
O putem testa separat într-o versiune ulterioară a modelului.
</div>
""",
    unsafe_allow_html=True,
)

columns_to_remove = [
    "id",
    "first_name",
    "last_name",
    "email",
    "career_aspiration",
    "math_score",
    "history_score",
    "physics_score",
    "chemistry_score",
    "biology_score",
    "english_score",
    "geography_score",
]

removed_variables = create_removed_variables_table(columns_to_remove)

st.markdown(
    '<div class="subsection-title">Tabel cu variabilele eliminate</div>',
    unsafe_allow_html=True,
)

st.dataframe(
    removed_variables,
    use_container_width=True,
    hide_index=True,
)

remove_button = st.button("Elimină variabilele")

if remove_button:
    machine_learning_df = df.copy()
    machine_learning_df = machine_learning_df.drop(columns=columns_to_remove)

    st.session_state["machine_learning_df"] = machine_learning_df

    st.markdown(
        """
<div class="success-box">
<strong>Variabilele au fost eliminate din copia pentru Machine Learning.</strong><br>
Dataset-ul original rămâne neschimbat. Toate modificările sunt aplicate doar asupra copiei
<strong>machine_learning_df</strong>.
</div>
""",
        unsafe_allow_html=True,
    )

if "machine_learning_df" not in st.session_state:
    st.markdown(
        """
<div class="explain-box">
Apasă butonul <strong>Elimină variabilele</strong> pentru a crea copia
<strong>machine_learning_df</strong> și pentru a afișa setul de date rezultat.
</div>
""",
        unsafe_allow_html=True,
    )
else:
    machine_learning_df = st.session_state["machine_learning_df"]

    after_col1, after_col2, after_col3 = st.columns(3)

    with after_col1:
        st.markdown(
            f"""
<div class="metric-card">
<div class="metric-value">{machine_learning_df.shape[0]}</div>
<div class="metric-label">Înregistrări</div>
</div>
""",
            unsafe_allow_html=True,
        )

    with after_col2:
        st.markdown(
            f"""
<div class="metric-card">
<div class="metric-value">{machine_learning_df.shape[1]}</div>
<div class="metric-label">Coloane</div>
</div>
""",
            unsafe_allow_html=True,
        )

    with after_col3:
        st.markdown(
            f"""
<div class="metric-card">
<div class="metric-value">{len(columns_to_remove)}</div>
<div class="metric-label">Variabile eliminate</div>
</div>
""",
            unsafe_allow_html=True,
        )

    st.markdown(
        '<div class="subsection-title">Setul de date după modificare</div>',
        unsafe_allow_html=True,
    )

    st.dataframe(
        machine_learning_df.head(10),
        use_container_width=True,
        hide_index=True,
    )

    st.markdown(
        """
<div class="explain-box">
<strong>Rezultat:</strong> dataset-ul <strong>machine_learning_df</strong> conține acum doar variabilele utile
pentru prima versiune a modelului: genul, jobul part-time, numărul de absențe, activitățile extracurriculare,
orele de studiu individual și target-ul <strong>average_score</strong>.
</div>
""",
        unsafe_allow_html=True,
    )

# -------------------------------------------------------------------
# SECTION 2
# -------------------------------------------------------------------

st.markdown(
    '<div class="section-title">Pasul 2 - Identificarea valorilor extreme</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="info-card">
<div class="info-text">
În această etapă verificăm dacă variabilele numerice continue din dataset-ul pentru Machine Learning
conțin valori extreme. Analizăm doar <strong>weekly_self_study_hours</strong> și <strong>average_score</strong>,
deoarece <strong>absence_days</strong> este o variabilă discretă cu un număr mic de valori posibile și nu este
potrivită pentru această analiză a outlierilor.
</div>
</div>
""",
    unsafe_allow_html=True,
)

if "machine_learning_df" not in st.session_state:
    st.markdown(
        """
<div class="warning-box">
Pentru analiza valorilor extreme, trebuie mai întâi să creezi dataset-ul <strong>machine_learning_df</strong>
prin apăsarea butonului <strong>Elimină variabilele</strong> din pasul anterior.
</div>
""",
        unsafe_allow_html=True,
    )
else:
    machine_learning_df = st.session_state["machine_learning_df"]

    numerical_columns_for_outliers = [
        "weekly_self_study_hours",
        "average_score",
    ]

    st.markdown(
        """
<div class="explain-box">
<strong>Proces:</strong> mai întâi alegem variabila, metoda de detectare și tipul de grafic.
Aplicația afișează automat numărul și procentul de outlieri, împreună cu vizualizarea. Abia după această analiză,
dacă există outlieri, putem decide dacă îi eliminăm sau îi păstrăm.
</div>
""",
        unsafe_allow_html=True,
    )

    outlier_col1, outlier_col2, outlier_col3 = st.columns(3)

    with outlier_col1:
        selected_outlier_column = st.selectbox(
            "Variabila analizată",
            options=numerical_columns_for_outliers,
        )

    with outlier_col2:
        detection_method = st.selectbox(
            "Metoda de detectare",
            options=[
                "IQR",
                "Z-score",
            ],
        )

    with outlier_col3:
        plot_type = st.selectbox(
            "Tip grafic",
            options=[
                "Box plot",
                "Histogramă",
                "Violin plot",
            ],
        )

    if detection_method == "IQR":
        iqr_multiplier = st.slider(
            "Multiplicator IQR",
            min_value=1.0,
            max_value=3.0,
            value=1.5,
            step=0.5,
        )

        outlier_mask = detect_outliers_iqr(
            machine_learning_df,
            selected_outlier_column,
            iqr_multiplier,
        )

    else:
        z_threshold = st.slider(
            "Prag Z-score",
            min_value=2.0,
            max_value=4.0,
            value=3.0,
            step=0.5,
        )

        outlier_mask = detect_outliers_z_score(
            machine_learning_df,
            selected_outlier_column,
            z_threshold,
        )

    outlier_count = int(outlier_mask.sum())
    outlier_percentage = round(outlier_count / len(machine_learning_df) * 100, 2)

    stats_col1, stats_col2 = st.columns(2)

    with stats_col1:
        st.markdown(
            f"""
<div class="metric-card">
<div class="metric-value">{outlier_count}</div>
<div class="metric-label">Outlieri identificați</div>
</div>
""",
            unsafe_allow_html=True,
        )

    with stats_col2:
        st.markdown(
            f"""
<div class="metric-card">
<div class="metric-value">{outlier_percentage}%</div>
<div class="metric-label">Procent outlieri</div>
</div>
""",
            unsafe_allow_html=True,
        )

    visual_df = machine_learning_df.copy()
    visual_df["status_valoare"] = "Valoare normală"
    visual_df.loc[outlier_mask, "status_valoare"] = "Outlier"

    if plot_type == "Box plot":
        fig_outlier = px.box(
            visual_df,
            y=selected_outlier_column,
            points="all",
            color="status_valoare",
            title=f"Box plot pentru identificarea outlierilor - {selected_outlier_column}",
            color_discrete_map={
                "Valoare normală": "#22c55e",
                "Outlier": "#f97316",
            },
        )

    elif plot_type == "Histogramă":
        fig_outlier = px.histogram(
            visual_df,
            x=selected_outlier_column,
            color="status_valoare",
            nbins=20,
            title=f"Histogramă pentru identificarea outlierilor - {selected_outlier_column}",
            color_discrete_map={
                "Valoare normală": "#22c55e",
                "Outlier": "#f97316",
            },
        )

    else:
        fig_outlier = px.violin(
            visual_df,
            y=selected_outlier_column,
            color="status_valoare",
            box=True,
            points="all",
            title=f"Violin plot pentru identificarea outlierilor - {selected_outlier_column}",
            color_discrete_map={
                "Valoare normală": "#22c55e",
                "Outlier": "#f97316",
            },
        )

    fig_outlier = style_plot(
        fig_outlier,
        title=f"Vizualizarea outlierilor pentru {selected_outlier_column}",
        height=540,
    )

    st.plotly_chart(fig_outlier, use_container_width=True)

    if outlier_count == 0:
        st.markdown(
            """
<div class="success-box">
Nu au fost identificați outlieri pentru variabila selectată folosind metoda aleasă.
Prin urmare, nu este necesară eliminarea valorilor în această etapă.
</div>
""",
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"""
<div class="warning-box">
Au fost identificați <strong>{outlier_count}</strong> outlieri pentru variabila
<strong>{selected_outlier_column}</strong>. Aceștia nu sunt eliminați automat. După verificarea graficului,
poți decide dacă îi păstrezi sau îi elimini din copia de lucru.
</div>
""",
            unsafe_allow_html=True,
        )

        show_outlier_table = st.checkbox(
            "Afișează tabelul cu outlierii identificați",
            value=False,
        )

        if show_outlier_table:
            outliers_table = machine_learning_df.loc[outlier_mask].copy()

            st.markdown(
                '<div class="subsection-title">Tabel cu outlierii identificați</div>',
                unsafe_allow_html=True,
            )

            st.dataframe(
                outliers_table,
                use_container_width=True,
                hide_index=True,
            )

        outlier_decision = st.radio(
            "Decizie pentru outlierii identificați",
            options=[
                "Păstrează valorile",
                "Elimină outlierii",
            ],
            horizontal=True,
        )

        apply_outlier_decision = st.button("Aplică decizia pentru outlieri")

        if apply_outlier_decision:
            if outlier_decision == "Păstrează valorile":
                st.session_state["machine_learning_df_after_outliers"] = (
                    machine_learning_df.copy()
                )

                st.markdown(
                    """
<div class="success-box">
<strong>Decizie aplicată:</strong> outlierii au fost păstrați. Dataset-ul de lucru nu a fost modificat.
</div>
""",
                    unsafe_allow_html=True,
                )

            else:
                machine_learning_df_after_outliers = machine_learning_df.loc[
                    ~outlier_mask
                ].reset_index(drop=True)

                st.session_state["machine_learning_df_after_outliers"] = (
                    machine_learning_df_after_outliers
                )

                st.markdown(
                    f"""
<div class="success-box">
<strong>Decizie aplicată:</strong> outlierii identificați pentru variabila
<strong>{selected_outlier_column}</strong> au fost eliminați din copia de lucru.
</div>
""",
                    unsafe_allow_html=True,
                )

                rows_col1, rows_col2, rows_col3 = st.columns(3)

                with rows_col1:
                    st.markdown(
                        f"""
<div class="metric-card">
<div class="metric-value">{machine_learning_df.shape[0]}</div>
<div class="metric-label">Rânduri înainte</div>
</div>
""",
                        unsafe_allow_html=True,
                    )

                with rows_col2:
                    st.markdown(
                        f"""
<div class="metric-card">
<div class="metric-value">{machine_learning_df_after_outliers.shape[0]}</div>
<div class="metric-label">Rânduri după</div>
</div>
""",
                        unsafe_allow_html=True,
                    )

                with rows_col3:
                    st.markdown(
                        f"""
<div class="metric-card">
<div class="metric-value">{machine_learning_df.shape[0] - machine_learning_df_after_outliers.shape[0]}</div>
<div class="metric-label">Rânduri eliminate</div>
</div>
""",
                        unsafe_allow_html=True,
                    )

                st.markdown(
                    '<div class="subsection-title">Setul de date după tratarea outlierilor</div>',
                    unsafe_allow_html=True,
                )

                st.dataframe(
                    machine_learning_df_after_outliers.head(10),
                    use_container_width=True,
                    hide_index=True,
                )

# -------------------------------------------------------------------
# SECTION 3
# -------------------------------------------------------------------

st.markdown(
    '<div class="section-title">Pasul 3 - Encoding pentru variabile categoriale</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="info-card">
<div class="info-text">
În această etapă analizăm modul în care variabila categorială <strong>gender</strong> poate fi transformată
într-o formă numerică pentru Machine Learning. Această secțiune este doar un <strong>preview</strong>:
encoding-ul este afișat pentru înțelegere, dar nu este aplicat definitiv pe dataset-ul de lucru.
Transformarea efectivă va fi făcută ulterior, în etapa de Machine Learning.
</div>
</div>
""",
    unsafe_allow_html=True,
)

if "machine_learning_df" not in st.session_state:
    st.markdown(
        """
<div class="warning-box">
Pentru preview-ul de encoding, trebuie mai întâi să creezi dataset-ul <strong>machine_learning_df</strong>
prin apăsarea butonului <strong>Elimină variabilele</strong> din primul pas.
</div>
""",
        unsafe_allow_html=True,
    )
else:
    if "machine_learning_df_after_outliers" in st.session_state:
        encoding_base_df = st.session_state["machine_learning_df_after_outliers"].copy()
    else:
        encoding_base_df = st.session_state["machine_learning_df"].copy()

    st.markdown(
        """
<div class="explain-box">
<strong>Metoda folosită:</strong> pentru variabila <strong>gender</strong> folosim
<strong>One-Hot Encoding</strong>. Această metodă creează coloane binare pentru categoriile existente.
De exemplu, dacă în variabila gender există valorile <strong>female</strong> și <strong>male</strong>,
acestea pot fi transformate în coloane numerice de tip 0/1.
</div>
""",
        unsafe_allow_html=True,
    )

    encoding_option = st.selectbox(
        "Alege varianta de One-Hot Encoding pentru preview",
        options=[
            "Păstrează toate categoriile",
            "Elimină prima categorie (drop_first=True)",
        ],
    )

    drop_first_option = encoding_option == "Elimină prima categorie (drop_first=True)"

    encoded_preview_df = pd.get_dummies(
        encoding_base_df,
        columns=["gender"],
        drop_first=drop_first_option,
        dtype=int,
    )

    created_gender_columns = [
        column for column in encoded_preview_df.columns if column.startswith("gender_")
    ]

    encoding_col1, encoding_col2, encoding_col3 = st.columns(3)

    with encoding_col1:
        st.markdown(
            f"""
<div class="metric-card">
<div class="metric-value">{encoding_base_df.shape[1]}</div>
<div class="metric-label">Coloane înainte</div>
</div>
""",
            unsafe_allow_html=True,
        )

    with encoding_col2:
        st.markdown(
            f"""
<div class="metric-card">
<div class="metric-value">{encoded_preview_df.shape[1]}</div>
<div class="metric-label">Coloane după encoding</div>
</div>
""",
            unsafe_allow_html=True,
        )

    with encoding_col3:
        st.markdown(
            f"""
<div class="metric-card">
<div class="metric-value">{len(created_gender_columns)}</div>
<div class="metric-label">Coloane create</div>
</div>
""",
            unsafe_allow_html=True,
        )

    st.markdown(
        '<div class="subsection-title">Coloane create prin encoding</div>',
        unsafe_allow_html=True,
    )

    if len(created_gender_columns) == 0:
        st.markdown(
            """
<div class="warning-box">
Nu au fost create coloane noi pentru gender. Verifică dacă variabila există în dataset-ul de lucru
sau dacă opțiunea selectată elimină singura categorie disponibilă.
</div>
""",
            unsafe_allow_html=True,
        )
    else:
        encoding_columns_table = pd.DataFrame(
            {
                "Coloană creată": created_gender_columns,
                "Tip": ["Variabilă binară 0/1" for _ in created_gender_columns],
            }
        )

        st.dataframe(
            encoding_columns_table,
            use_container_width=True,
            hide_index=True,
        )

    st.markdown(
        '<div class="subsection-title">Preview - setul de date după encoding</div>',
        unsafe_allow_html=True,
    )

    st.dataframe(
        encoded_preview_df.head(10),
        use_container_width=True,
        hide_index=True,
    )

    st.markdown(
        """
<div class="warning-box">
<strong>Important:</strong> tabelul de mai sus este doar o previzualizare. Dataset-ul salvat în
<strong>session_state</strong> nu este modificat în această secțiune. Encoding-ul real va fi aplicat în etapa
de Machine Learning, pentru a evita modificări premature ale datelor.
</div>
""",
        unsafe_allow_html=True,
    )

# -------------------------------------------------------------------
# SECTION 4
# -------------------------------------------------------------------

st.markdown(
    '<div class="section-title">Pasul 4 - Preview pentru scalarea variabilelor numerice</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="info-card">
<div class="info-text">
În această etapă analizăm cum ar arăta variabilele numerice după scalare. Pentru acest dataset,
scalarea nu este obligatorie pentru toate modelele, dar poate fi utilă pentru algoritmi sensibili la magnitudinea
valorilor, precum KNN, Ridge sau Lasso. 
</div>
</div>
""",
    unsafe_allow_html=True,
)

if "machine_learning_df" not in st.session_state:
    st.markdown(
        """
<div class="warning-box">
Pentru preview-ul de scalare, trebuie mai întâi să creezi dataset-ul <strong>machine_learning_df</strong>
prin apăsarea butonului <strong>Elimină variabilele</strong> din primul pas.
</div>
""",
        unsafe_allow_html=True,
    )
else:
    if "machine_learning_df_after_outliers" in st.session_state:
        scaling_base_df = st.session_state["machine_learning_df_after_outliers"].copy()
    else:
        scaling_base_df = st.session_state["machine_learning_df"].copy()

    st.markdown(
        """
<div class="explain-box">
Scalarea este previzualizată doar pentru predictorii numerici:
<strong>absence_days</strong> și <strong>weekly_self_study_hours</strong>.
Variabila <strong>average_score</strong> nu este scalată, deoarece reprezintă target-ul modelului.
</div>
""",
        unsafe_allow_html=True,
    )

    scaling_method = st.selectbox(
        "Alege metoda de scalare pentru preview",
        options=[
            "StandardScaler",
            "MinMaxScaler",
        ],
    )

    columns_to_scale = [
        "absence_days",
        "weekly_self_study_hours",
    ]

    scaled_preview_df, scaled_suffix = create_scaled_preview(
        scaling_base_df,
        columns_to_scale,
        scaling_method,
    )

    scaled_columns = [f"{column}{scaled_suffix}" for column in columns_to_scale]

    preview_columns = columns_to_scale + scaled_columns + ["average_score"]

    st.markdown(
        '<div class="subsection-title">Preview - valori originale și valori scalate</div>',
        unsafe_allow_html=True,
    )

    st.dataframe(
        scaled_preview_df[preview_columns].head(10).round(3),
        use_container_width=True,
        hide_index=True,
    )

    if scaling_method == "StandardScaler":
        st.markdown(
            """
<div class="explain-box">
<strong>Interpretare StandardScaler:</strong> valorile sunt transformate astfel încât variabila să aibă media
aproximativ 0 și abaterea standard aproximativ 1. Această metodă este utilă pentru modele liniare regularizate
sau modele bazate pe distanță.
</div>
""",
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
<div class="explain-box">
<strong>Interpretare MinMaxScaler:</strong> valorile sunt transformate într-un interval fix, de obicei între
0 și 1. Această metodă este utilă când dorim ca toate variabilele numerice să fie aduse pe aceeași scară.
</div>
""",
            unsafe_allow_html=True,
        )


st.markdown("---")
st.markdown(
    """
<div class="footer">
Student Performance Dashboard · Pagina 04 · Preprocesarea datelor
</div>
""",
    unsafe_allow_html=True,
)
