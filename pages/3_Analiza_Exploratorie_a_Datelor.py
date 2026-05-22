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
    color: #06b6d4 !important;
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

[data-testid="stSidebar"] [data-testid="stSlider"] * {
    color: white !important;
}

[data-testid="stDataFrame"] {
    background: white !important;
    border-radius: 18px !important;
}

.stButton button {
    background: white !important;
    color: #2563eb !important;
    border: 1px solid #bfdbfe !important;
    border-radius: 14px !important;
    padding: 10px 22px !important;
    font-weight: 800 !important;
    box-shadow: 0 8px 18px rgba(37, 99, 235, 0.10) !important;
}

.stButton button:hover {
    background: #eff6ff !important;
    border-color: #93c5fd !important;
    color: #1d4ed8 !important;
}

.stButton button p {
    color: #2563eb !important;
}

.page-hero {
    background: white;
    border-radius: 30px;
    padding: 46px 52px;
    margin-bottom: 32px;
    border: 1px solid rgba(148, 163, 184, 0.25);
    border-top: 8px solid #06b6d4;
    box-shadow: 0 18px 40px rgba(15, 23, 42, 0.10);
}

.page-label {
    display: inline-block;
    background: #cffafe;
    color: #0891b2 !important;
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
    color: #2563eb !important;
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


def prepare_data(dataframe):
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

    data["study_category"] = pd.cut(
        data["weekly_self_study_hours"],
        bins=[0, 10, 20, 30, 40, 50],
        labels=[
            "0-10 ore",
            "10-20 ore",
            "20-30 ore",
            "30-40 ore",
            "40-50 ore",
        ],
        include_lowest=True,
    )

    data["part_time_job_label"] = data["part_time_job"].map(
        {
            True: "Da",
            False: "Nu",
        }
    )

    data["extracurricular_activities_label"] = data["extracurricular_activities"].map(
        {
            True: "Da",
            False: "Nu",
        }
    )

    return data


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


def metric_label(column_name):
    labels = {
        "absence_days": "Zile de absență",
        "weekly_self_study_hours": "Ore de studiu individual / săptămână",
        "math_score": "Scor matematică",
        "history_score": "Scor istorie",
        "physics_score": "Scor fizică",
        "chemistry_score": "Scor chimie",
        "biology_score": "Scor biologie",
        "english_score": "Scor engleză",
        "geography_score": "Scor geografie",
        "average_score": "Scor mediu",
        "gender": "Gen",
        "part_time_job_label": "Job part-time",
        "extracurricular_activities_label": "Activități extracurriculare",
        "career_aspiration": "Aspirație profesională",
        "study_category": "Categorie studiu",
    }

    return labels.get(column_name, column_name)


def correlation_method_label(method_name):
    labels = {
        "pearson": "Pearson",
        "spearman": "Spearman",
        "kendall": "Kendall Tau",
    }

    return labels.get(method_name, method_name)


df = load_data()
df = prepare_data(df)


df = load_data()
df = prepare_data(df)

df_filtered = df.copy().reset_index(drop=True)

st.markdown(
    """
<div class="page-hero">
<div class="page-label">PAGINA 03</div>
<div class="page-title">Analiza exploratorie a datelor</div>
<div class="page-desc">
Această pagină urmărește identificarea relațiilor dintre variabilele existente și scorul mediu al studenților.
Analiza exploratorie este realizată pentru a susține decizia de construire a unui model de Machine Learning
și pentru a observa ce variabile pot avea valoare predictivă.
</div>
</div>
""",
    unsafe_allow_html=True,
)

if len(df_filtered) == 0:
    st.warning(
        "Nu există date pentru filtrele selectate. Ajustează filtrele din sidebar."
    )
    st.stop()


st.markdown(
    """
<div class="warning-box">
<strong>Observație importantă pentru Machine Learning:</strong>
scorurile pe discipline sunt folosite pentru calcularea variabilei <strong>average_score</strong>.
Din acest motiv, ele pot fi analizate exploratoriu, dar nu ar trebui folosite ca predictori direcți
într-un model care prezice <strong>average_score</strong>, deoarece ar produce data leakage.
Predictorii mai potriviți pentru model sunt variabile precum orele de studiu, absențele, genul,
jobul part-time, activitățile extracurriculare și aspirația profesională.
</div>
""",
    unsafe_allow_html=True,
)

# -------------------------------------------------------------------
# SECTION 1
# -------------------------------------------------------------------

st.markdown(
    '<div class="section-title">Pasul 1 - Analiză agregată pentru susținerea modelului</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="info-card">
<div class="info-text">
Această secțiune permite compararea unor indicatori prin grupare. Este utilă pentru a înțelege
dacă anumite categorii de studenți au, în medie, scoruri mai mari, mai multe absențe sau mai multe ore de studiu.
Aceste observații pot ghida alegerea variabilelor pentru Machine Learning.
</div>
</div>
""",
    unsafe_allow_html=True,
)

agg_col1, agg_col2, agg_col3 = st.columns(3)

with agg_col1:
    category_variable = st.selectbox(
        "Categoria analizată",
        options=[
            "gender",
            "part_time_job_label",
            "extracurricular_activities_label",
            "career_aspiration",
        ],
        index=3,
        format_func=metric_label,
    )

with agg_col2:
    aggregation_metric = st.selectbox(
        "Indicator analizat",
        options=[
            "average_score",
            "absence_days",
            "weekly_self_study_hours",
            "math_score",
            "history_score",
            "physics_score",
            "chemistry_score",
            "biology_score",
            "english_score",
            "geography_score",
        ],
        index=0,
        format_func=metric_label,
    )

with agg_col3:
    aggregation_type = st.selectbox(
        "Tip agregare",
        options=["Medie", "Mediană", "Maxim", "Minim"],
        index=0,
    )

if aggregation_type == "Medie":
    aggregated_data = (
        df_filtered.groupby(category_variable, observed=False)[aggregation_metric]
        .mean()
        .reset_index()
    )
elif aggregation_type == "Mediană":
    aggregated_data = (
        df_filtered.groupby(category_variable, observed=False)[aggregation_metric]
        .median()
        .reset_index()
    )
elif aggregation_type == "Maxim":
    aggregated_data = (
        df_filtered.groupby(category_variable, observed=False)[aggregation_metric]
        .max()
        .reset_index()
    )
else:
    aggregated_data = (
        df_filtered.groupby(category_variable, observed=False)[aggregation_metric]
        .min()
        .reset_index()
    )

aggregated_data = aggregated_data.dropna().sort_values(
    aggregation_metric,
    ascending=False,
)

visual_type = st.radio(
    "Alege tipul de vizualizare",
    options=[
        "Bar chart",
        "Treemap",
    ],
    horizontal=True,
)

if visual_type == "Bar chart":
    fig_agg = px.bar(
        aggregated_data,
        x=category_variable,
        y=aggregation_metric,
        text=aggregation_metric,
        color=category_variable,
        color_discrete_sequence=px.colors.qualitative.Bold,
        title=f"{aggregation_type} pentru {metric_label(aggregation_metric)} după {metric_label(category_variable)}",
    )

    fig_agg.update_traces(
        texttemplate="%{text:.2f}",
        textposition="outside",
    )

else:
    fig_agg = px.treemap(
        aggregated_data,
        path=[category_variable],
        values=aggregation_metric,
        color=aggregation_metric,
        color_continuous_scale="Blues",
        title=f"Treemap pentru {metric_label(aggregation_metric)} după {metric_label(category_variable)}",
    )

fig_agg = style_plot(
    fig_agg,
    title=f"Analiză agregată: {metric_label(aggregation_metric)} după {metric_label(category_variable)}",
    height=560,
)

st.plotly_chart(fig_agg, use_container_width=True)

st.markdown(
    """
<div class="explain-box">
<strong>Interpretare:</strong> această analiză ajută la observarea diferențelor dintre grupuri.
Dacă anumite categorii au valori medii diferite pentru <strong>average_score</strong> sau pentru alți indicatori,
aceste observații pot susține alegerea variabilelor pentru model. Totuși, agregarea nu demonstrează cauzalitate,
ci oferă o imagine inițială asupra datelor.
</div>
""",
    unsafe_allow_html=True,
)

# -------------------------------------------------------------------
# SECTION 2
# -------------------------------------------------------------------

st.markdown(
    '<div class="section-title">Pasul 2 - Comparația scorului mediu între grupuri</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="info-card">
<div class="info-text">
Această secțiune compară <strong>average_score</strong> între grupuri de studenți.
Aici este inclusă și categoria de studiu, creată pe baza variabilei <strong>weekly_self_study_hours</strong>,
împărțită în intervale de câte 10 ore. Această grupare ajută la observarea modului în care scorul mediu
diferă în funcție de nivelul de studiu individual.
</div>
</div>
""",
    unsafe_allow_html=True,
)

compare_col1, compare_col2 = st.columns(2)

with compare_col1:
    group_variable = st.selectbox(
        "Grupează scorul mediu după",
        options=[
            "gender",
            "part_time_job_label",
            "extracurricular_activities_label",
            "career_aspiration",
            "study_category",
        ],
        index=0,
        format_func=metric_label,
    )

with compare_col2:
    chart_type = st.radio(
        "Tip grafic pentru comparație",
        options=[
            "Bar chart - medie",
            "Box plot",
            "Violin plot",
        ],
    )

if chart_type == "Bar chart - medie":
    grouped_data = (
        df_filtered.groupby(group_variable, observed=False)["average_score"]
        .mean()
        .reset_index()
        .dropna()
        .sort_values("average_score", ascending=False)
    )

    fig_compare = px.bar(
        grouped_data,
        x=group_variable,
        y="average_score",
        text="average_score",
        color=group_variable,
        color_discrete_sequence=px.colors.qualitative.Set3,
        title=f"Media scorului mediu în funcție de {metric_label(group_variable)}",
    )

    fig_compare.update_traces(
        texttemplate="%{text:.2f}",
        textposition="outside",
    )

elif chart_type == "Box plot":
    fig_compare = px.box(
        df_filtered,
        x=group_variable,
        y="average_score",
        color=group_variable,
        points="outliers",
        color_discrete_sequence=px.colors.qualitative.Set3,
        title=f"Distribuția scorului mediu în funcție de {metric_label(group_variable)}",
    )

else:
    fig_compare = px.violin(
        df_filtered,
        x=group_variable,
        y="average_score",
        color=group_variable,
        box=True,
        points=False,
        color_discrete_sequence=px.colors.qualitative.Set3,
        title=f"Forma distribuției scorului mediu în funcție de {metric_label(group_variable)}",
    )

fig_compare = style_plot(
    fig_compare,
    title=f"Comparație pe grupuri: average_score după {metric_label(group_variable)}",
    height=560,
)

st.plotly_chart(fig_compare, use_container_width=True)

if group_variable == "study_category":
    st.markdown(
        """
<div class="explain-box">
<strong>Despre categoria de studiu:</strong> această variabilă a fost creată doar pentru analiza exploratorie
din această secțiune. Ea împarte variabila <strong>weekly_self_study_hours</strong> în intervale:
<strong>0-10</strong>, <strong>10-20</strong>, <strong>20-30</strong>, <strong>30-40</strong> și
<strong>40-50</strong> ore pe săptămână. Astfel putem observa mai clar dacă scorul mediu diferă în funcție
de nivelul de studiu individual.
</div>
""",
        unsafe_allow_html=True,
    )

st.markdown(
    """
<div class="explain-box">
<strong>Interpretare:</strong> dacă între grupuri există diferențe vizibile ale scorului mediu,
această variabilă poate fi utilă în etapa de modelare. Box plot-ul și violin plot-ul sunt utile mai ales
pentru a observa distribuția completă, nu doar media.
</div>
""",
    unsafe_allow_html=True,
)

# -------------------------------------------------------------------
# SECTION 3
# -------------------------------------------------------------------

st.markdown(
    '<div class="section-title">Pasul 3 - Analiza interactivă a corelațiilor</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="info-card">
<div class="info-text">
Această secțiune calculează corelațiile dintre variabilele numerice. Pentru analiza orientată spre
Machine Learning, este important să observăm ce variabile sunt asociate cu <strong>average_score</strong>.
Poți alege metoda de corelație: <strong>Pearson</strong>, <strong>Spearman</strong> sau <strong>Kendall Tau</strong>.
</div>
</div>
""",
    unsafe_allow_html=True,
)


corr_col1, corr_col2, corr_col3 = st.columns(3)

with corr_col1:
    selected_correlation_method = st.radio(
        "Metoda de corelație",
        options=[
            "pearson",
            "spearman",
            "kendall",
        ],
        format_func=correlation_method_label,
        horizontal=True,
    )

with corr_col2:
    correlation_visual_type = st.selectbox(
        "Tip de vizualizare",
        options=[
            "Heatmap",
            "Bar chart față de average_score",
        ],
    )

with corr_col3:
    include_subject_scores = st.checkbox(
        "Include scorurile pe discipline",
        value=False,
    )

model_numeric_columns = [
    "absence_days",
    "weekly_self_study_hours",
    "average_score",
]

subject_score_columns = [
    "math_score",
    "history_score",
    "physics_score",
    "chemistry_score",
    "biology_score",
    "english_score",
    "geography_score",
]

if include_subject_scores:
    available_correlation_columns = model_numeric_columns + subject_score_columns
else:
    available_correlation_columns = model_numeric_columns

correlation_columns = st.multiselect(
    "Alege variabilele pentru matricea de corelație",
    options=available_correlation_columns,
    default=available_correlation_columns,
    format_func=metric_label,
)

if len(correlation_columns) < 2:
    st.warning("Alege cel puțin două variabile pentru analiza de corelație.")
else:
    correlation_matrix = (
        df_filtered[correlation_columns]
        .corr(method=selected_correlation_method)
        .round(2)
    )

    method_name_display = correlation_method_label(selected_correlation_method)

    if correlation_visual_type == "Heatmap":
        fig_corr = px.imshow(
            correlation_matrix,
            text_auto=True,
            color_continuous_scale="RdBu_r",
            zmin=-1,
            zmax=1,
            title=f"Matrice de corelație - metoda {method_name_display}",
        )

        fig_corr.update_layout(
            title_font_size=20,
            title_font_color="#0f172a",
            font=dict(
                family="Poppins",
                color="#1e293b",
            ),
            paper_bgcolor="white",
            plot_bgcolor="white",
            height=620,
            margin=dict(l=40, r=40, t=80, b=40),
            coloraxis_colorbar=dict(
                title=dict(
                    text="Corelație",
                    font=dict(color="#1e293b"),
                ),
                tickfont=dict(color="#334155"),
            ),
        )

        st.plotly_chart(fig_corr, use_container_width=True)

    else:
        if "average_score" not in correlation_columns:
            st.warning(
                "Pentru acest grafic, include variabila average_score în lista de variabile."
            )
        else:
            target_correlations = (
                correlation_matrix["average_score"].drop("average_score").reset_index()
            )

            target_correlations.columns = [
                "Variabilă",
                "Corelație",
            ]

            target_correlations["Corelație absolută"] = target_correlations[
                "Corelație"
            ].abs()

            target_correlations = target_correlations.sort_values(
                "Corelație absolută",
                ascending=False,
            )

            fig_corr_bar = px.bar(
                target_correlations,
                x="Corelație",
                y="Variabilă",
                orientation="h",
                color="Corelație",
                color_continuous_scale="RdBu_r",
                range_color=[-1, 1],
                text="Corelație",
                title=f"Corelațiile variabilelor cu average_score - metoda {method_name_display}",
            )

            fig_corr_bar.update_traces(
                texttemplate="%{text:.2f}",
                textposition="outside",
            )

            fig_corr_bar.add_vline(
                x=0,
                line_dash="dash",
                line_color="#0f172a",
            )

            fig_corr_bar = style_plot(
                fig_corr_bar,
                title=f"Corelații cu average_score - {method_name_display}",
                height=560,
            )

            st.plotly_chart(fig_corr_bar, use_container_width=True)

    st.markdown(
        f"""
<div class="explain-box">
<strong>Metoda selectată:</strong> {method_name_display}. 
Pearson este potrivită pentru relații liniare, Spearman pentru relații monotone bazate pe ranguri,
iar Kendall Tau este o variantă mai robustă pentru asocierea dintre ranguri.
În contextul modelului, cele mai importante corelații sunt cele dintre predictorii disponibili
și <strong>average_score</strong>.
</div>
""",
        unsafe_allow_html=True,
    )

    if "average_score" in correlation_columns and len(correlation_columns) > 1:
        average_score_corr = (
            correlation_matrix["average_score"]
            .drop("average_score")
            .abs()
            .sort_values(ascending=False)
        )

        strongest_variable = average_score_corr.index[0]
        strongest_value = correlation_matrix.loc[strongest_variable, "average_score"]

        if strongest_value > 0:
            direction_text = "pozitivă"
        else:
            direction_text = "negativă"

        st.markdown(
            f"""
<div class="explain-box">
<strong>Observație:</strong> folosind metoda <strong>{method_name_display}</strong>,
cea mai puternică asociere cu <strong>average_score</strong> este pentru
<strong>{metric_label(strongest_variable)}</strong>, cu o corelație de
<strong>{strongest_value:.2f}</strong>. Relația este <strong>{direction_text}</strong>.
</div>
""",
            unsafe_allow_html=True,
        )

    if include_subject_scores:
        st.markdown(
            """
<div class="warning-box">
<strong>Atenție:</strong> scorurile pe discipline au fost incluse doar pentru explorare.
Ele nu trebuie folosite ca predictori direcți pentru <strong>average_score</strong>, deoarece target-ul este calculat
din aceste scoruri. Folosirea lor în model ar produce o estimare artificial de bună.
</div>
""",
            unsafe_allow_html=True,
        )

st.markdown("---")
st.markdown(
    """
<div class="footer">
Student Performance Dashboard · Pagina 03 · Analiza exploratorie a datelor
</div>
""",
    unsafe_allow_html=True,
)
