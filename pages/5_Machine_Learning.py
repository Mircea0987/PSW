import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import statsmodels.formula.api as smf

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

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

.stButton button,
[data-testid="stFormSubmitButton"] button {
    background: white !important;
    color: #a855f7 !important;
    border: 1px solid #e9d5ff !important;
    border-radius: 14px !important;
    padding: 10px 22px !important;
    font-weight: 800 !important;
    box-shadow: 0 8px 18px rgba(168, 85, 247, 0.12) !important;
}

.stButton button:hover,
[data-testid="stFormSubmitButton"] button:hover {
    background: #faf5ff !important;
    border-color: #d8b4fe !important;
    color: #9333ea !important;
}

.stButton button p,
[data-testid="stFormSubmitButton"] button p {
    color: #a855f7 !important;
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
    color: #a855f7 !important;
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

/* Fix pentru expander-ul statsmodels */
[data-testid="stExpander"] {
    background: white !important;
    border: 1px solid rgba(148, 163, 184, 0.35) !important;
    border-radius: 18px !important;
    overflow: hidden !important;
    margin-top: 18px !important;
    margin-bottom: 22px !important;
}

[data-testid="stExpander"] summary {
    background: #f8fafc !important;
    color: #0f172a !important;
    font-weight: 800 !important;
    padding: 16px 20px !important;
}

[data-testid="stExpander"] summary * {
    color: #0f172a !important;
}

[data-testid="stExpander"] details {
    background: white !important;
}

[data-testid="stExpander"] [data-testid="stText"] {
    background: #0f172a !important;
    border-radius: 16px !important;
    padding: 18px 20px !important;
    margin-top: 14px !important;
    overflow-x: auto !important;
}

[data-testid="stExpander"] [data-testid="stText"] pre {
    color: #e2e8f0 !important;
    background: #0f172a !important;
    font-size: 13px !important;
    line-height: 1.55 !important;
    white-space: pre !important;
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


def create_default_machine_learning_df(dataframe):
    data = dataframe.copy()

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

    data = data.drop(columns=columns_to_remove)

    return data


def get_machine_learning_dataset():
    if "machine_learning_df_after_outliers" in st.session_state:
        data = st.session_state["machine_learning_df_after_outliers"].copy()
        source = (
            "Dataset-ul rezultat după tratarea outlierilor din pagina de preprocesare."
        )
    elif "machine_learning_df" in st.session_state:
        data = st.session_state["machine_learning_df"].copy()
        source = "Dataset-ul creat în pagina de preprocesare."
    else:
        raw_data = load_data()
        raw_data = add_average_score(raw_data)
        data = create_default_machine_learning_df(raw_data)
        source = "Dataset implicit creat automat, deoarece nu există încă o copie în session_state."

    return data, source


def prepare_features_and_target(dataframe, encode_gender):
    data = dataframe.copy()

    target_column = "average_score"

    if encode_gender:
        data = pd.get_dummies(
            data,
            columns=["gender"],
            drop_first=False,
            dtype=int,
        )
    else:
        data = data.drop(columns=["gender"])

    feature_columns = [column for column in data.columns if column != target_column]

    X = data[feature_columns]
    y = data[target_column]

    return X, y, feature_columns, data


def apply_scaling(X_train, X_test, scaling_method):
    X_train_scaled = X_train.copy()
    X_test_scaled = X_test.copy()

    columns_to_scale = [
        column
        for column in ["absence_days", "weekly_self_study_hours"]
        if column in X_train_scaled.columns
    ]

    if scaling_method == "StandardScaler":
        scaler = StandardScaler()
    else:
        scaler = MinMaxScaler()

    X_train_scaled[columns_to_scale] = scaler.fit_transform(
        X_train_scaled[columns_to_scale]
    )

    X_test_scaled[columns_to_scale] = scaler.transform(X_test_scaled[columns_to_scale])

    return X_train_scaled, X_test_scaled, columns_to_scale


def build_regression_model(model_name, n_neighbors, n_estimators, random_state):
    if model_name == "Linear Regression":
        return LinearRegression()

    if model_name == "KNN Regressor":
        return KNeighborsRegressor(n_neighbors=n_neighbors)

    return RandomForestRegressor(
        n_estimators=n_estimators,
        random_state=random_state,
    )


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


df_ml, dataset_source = get_machine_learning_dataset()
random_state = 42

st.sidebar.markdown("## 🎓 Student Dashboard")
st.sidebar.markdown("### Pachete Software")
st.sidebar.markdown("---")
st.sidebar.markdown("Pagina 05")
st.sidebar.markdown("Machine Learning")

st.markdown(
    """
<div class="page-hero">
<div class="page-label">PAGINA 05</div>
<div class="page-title">Machine Learning</div>
<div class="page-desc">
Această pagină antrenează modele de regresie pentru estimarea variabilei target
<strong>average_score</strong>. Configurarea modelului se face interactiv,
iar rezultatele sunt evaluate prin metrici specifice regresiei.
</div>
</div>
""",
    unsafe_allow_html=True,
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        f"""
<div class="metric-card">
<div class="metric-value">{df_ml.shape[0]}</div>
<div class="metric-label">Înregistrări disponibile</div>
</div>
""",
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        f"""
<div class="metric-card">
<div class="metric-value">{df_ml.shape[1]}</div>
<div class="metric-label">Coloane disponibile</div>
</div>
""",
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        f"""
<div class="metric-card">
<div class="metric-value">{df_ml["average_score"].mean():.2f}</div>
<div class="metric-label">Media targetului</div>
</div>
""",
        unsafe_allow_html=True,
    )

st.markdown(
    '<div class="section-title">Pasul 1 - Configurarea modelului de regresie</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="warning-box">
<strong>Observație:</strong> target-ul este <strong>average_score</strong>.
Variabilele folosite pentru predicție sunt cele rămase după preprocesare:
<strong>gender</strong>, <strong>part_time_job</strong>, <strong>absence_days</strong>,
<strong>extracurricular_activities</strong> și <strong>weekly_self_study_hours</strong>.
</div>
""",
    unsafe_allow_html=True,
)

model_col1, model_col2 = st.columns(2)

with model_col1:
    selected_model = st.selectbox(
        "Model de regresie",
        options=[
            "Linear Regression",
            "KNN Regressor",
            "Random Forest Regressor",
        ],
    )

n_neighbors = 5
n_estimators = 100

if selected_model == "KNN Regressor":
    with model_col2:
        n_neighbors = st.slider(
            "Număr de vecini",
            min_value=2,
            max_value=15,
            value=5,
            step=1,
        )

elif selected_model == "Random Forest Regressor":
    with model_col2:
        n_estimators = st.slider(
            "Număr de arbori",
            min_value=50,
            max_value=300,
            value=100,
            step=50,
        )

else:
    with model_col2:
        st.markdown(
            """
""",
            unsafe_allow_html=True,
        )

with st.form("regression_model_form"):
    st.markdown("### Configurare antrenare")

    form_col1, form_col2, form_col3 = st.columns(3)

    with form_col1:
        test_size = st.slider(
            "Test size",
            min_value=0.10,
            max_value=0.40,
            value=0.20,
            step=0.05,
        )

    with form_col2:
        encode_gender = st.checkbox(
            "Aplică One-Hot Encoding pentru gender",
            value=True,
        )

    with form_col3:
        apply_scaling_option = st.checkbox(
            "Aplică scaling pentru predictorii numerici",
            value=False,
        )

        if apply_scaling_option:
            scaling_method = st.selectbox(
                "Metoda de scalare",
                options=[
                    "StandardScaler",
                    "MinMaxScaler",
                ],
            )
        else:
            scaling_method = "Fără scaling"

    submit_model = st.form_submit_button("Antrenează modelul")


if submit_model:
    with st.spinner("Pregătesc datele și antrenez modelul..."):
        X, y, feature_columns, prepared_df = prepare_features_and_target(
            df_ml,
            encode_gender,
        )

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=test_size,
            random_state=random_state,
        )

        if selected_model == "KNN Regressor" and n_neighbors > len(X_train):
            n_neighbors = len(X_train)
            st.warning(
                f"Numărul de vecini a fost redus automat la {n_neighbors}, deoarece setul de train are doar {len(X_train)} rânduri."
            )

        scaled_columns = []

        if apply_scaling_option:
            X_train, X_test, scaled_columns = apply_scaling(
                X_train,
                X_test,
                scaling_method,
            )

        model = build_regression_model(
            selected_model,
            n_neighbors,
            n_estimators,
            random_state,
        )

        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)

        r2 = r2_score(y_test, y_pred)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        mae = mean_absolute_error(y_test, y_pred)

        results_df = pd.DataFrame(
            {
                "Valoare reală": y_test.values,
                "Valoare prezisă": y_pred,
                "Eroare": y_pred - y_test.values,
                "Eroare absolută": np.abs(y_pred - y_test.values),
            }
        ).round(3)

    st.markdown(
        """
<div class="success-box">
<strong>Antrenare completă!</strong><br>
Modelul a fost antrenat și evaluat pe setul de test.
</div>
""",
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-title">Pasul 2 - Rezultatele modelului</div>',
        unsafe_allow_html=True,
    )

    metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)

    with metric_col1:
        st.markdown(
            f"""
<div class="metric-card">
<div class="metric-value">{r2:.3f}</div>
<div class="metric-label">R²</div>
</div>
""",
            unsafe_allow_html=True,
        )

    with metric_col2:
        st.markdown(
            f"""
<div class="metric-card">
<div class="metric-value">{rmse:.2f}</div>
<div class="metric-label">RMSE</div>
</div>
""",
            unsafe_allow_html=True,
        )

    with metric_col3:
        st.markdown(
            f"""
<div class="metric-card">
<div class="metric-value">{mae:.2f}</div>
<div class="metric-label">MAE</div>
</div>
""",
            unsafe_allow_html=True,
        )

    with metric_col4:
        st.markdown(
            f"""
<div class="metric-card">
<div class="metric-value">{len(X_train)}</div>
<div class="metric-label">Rânduri train</div>
</div>
""",
            unsafe_allow_html=True,
        )

    if selected_model == "Linear Regression":
        model_details = "Fără parametri suplimentari"
    elif selected_model == "KNN Regressor":
        model_details = f"Număr vecini: {n_neighbors}"
    else:
        model_details = f"Număr arbori: {n_estimators}"

    st.markdown(
        f"""
<div class="explain-box">
<strong>Configurație folosită:</strong><br>
Model: <strong>{selected_model}</strong><br>
Parametri model: <strong>{model_details}</strong><br>
Test size: <strong>{test_size}</strong><br>
Random state: <strong>42</strong><br>
Encoding gender: <strong>{"activat" if encode_gender else "dezactivat"}</strong><br>
Scaling: <strong>{scaling_method}</strong><br>
Variabile folosite: <strong>{", ".join(list(X_train.columns))}</strong>
</div>
""",
        unsafe_allow_html=True,
    )

    if apply_scaling_option and len(scaled_columns) > 0:
        st.markdown(
            f"""
<div class="warning-box">
<strong>Important:</strong> scaler-ul a fost antrenat doar pe setul de train și apoi aplicat pe setul de test.
Acest lucru evită data leakage. Variabile scalate: <strong>{", ".join(scaled_columns)}</strong>.
</div>
""",
            unsafe_allow_html=True,
        )

    st.markdown(
        '<div class="subsection-title">Real vs. Prezis</div>',
        unsafe_allow_html=True,
    )

    fig_pred = px.scatter(
        x=y_test,
        y=y_pred,
        labels={
            "x": "Average score real",
            "y": "Average score prezis",
        },
        title="Valori reale vs. valori prezise",
        color_discrete_sequence=["#a855f7"],
    )

    min_value = min(y_test.min(), y_pred.min())
    max_value = max(y_test.max(), y_pred.max())

    fig_pred.add_shape(
        type="line",
        x0=min_value,
        y0=min_value,
        x1=max_value,
        y1=max_value,
        line=dict(
            color="#64748b",
            dash="dash",
        ),
    )

    fig_pred = style_plot(
        fig_pred,
        title="Real vs. prezis",
        height=520,
    )

    st.plotly_chart(
        fig_pred,
        use_container_width=True,
    )

    st.markdown(
        '<div class="subsection-title">Distribuția erorilor</div>',
        unsafe_allow_html=True,
    )

    fig_error = px.histogram(
        results_df,
        x="Eroare",
        nbins=20,
        title="Distribuția erorilor de predicție",
        color_discrete_sequence=["#c084fc"],
    )

    fig_error.add_vline(
        x=0,
        line_dash="dash",
        line_color="#64748b",
    )

    fig_error = style_plot(
        fig_error,
        title="Distribuția erorilor",
        height=500,
    )

    st.plotly_chart(
        fig_error,
        use_container_width=True,
    )

    st.markdown(
        '<div class="subsection-title">Tabel cu predicțiile pe setul de test</div>',
        unsafe_allow_html=True,
    )

    st.dataframe(
        results_df,
        use_container_width=True,
        hide_index=True,
    )

    if selected_model == "Random Forest Regressor":
        st.markdown(
            '<div class="subsection-title">Importanța variabilelor</div>',
            unsafe_allow_html=True,
        )

        feature_importance = pd.DataFrame(
            {
                "Variabilă": X_train.columns,
                "Importanță": model.feature_importances_,
            }
        ).sort_values(
            "Importanță",
            ascending=True,
        )

        fig_importance = px.bar(
            feature_importance,
            x="Importanță",
            y="Variabilă",
            orientation="h",
            title="Importanța variabilelor în Random Forest",
            color_discrete_sequence=["#a855f7"],
        )

        fig_importance = style_plot(
            fig_importance,
            title="Importanța variabilelor",
            height=450,
        )

        st.plotly_chart(
            fig_importance,
            use_container_width=True,
        )

        st.dataframe(
            feature_importance.sort_values("Importanță", ascending=False).round(4),
            use_container_width=True,
            hide_index=True,
        )

    st.session_state["last_regression_results"] = {
        "model": selected_model,
        "test_size": test_size,
        "random_state": random_state,
        "encoding_gender": encode_gender,
        "scaling": scaling_method,
        "r2": r2,
        "rmse": rmse,
        "mae": mae,
        "train_rows": len(X_train),
        "test_rows": len(X_test),
    }

else:
    st.markdown(
        """
<div class="explain-box">
Configurează modelul și parametrii, apoi apasă
<strong>Antrenează modelul</strong> pentru a vedea rezultatele.
</div>
""",
        unsafe_allow_html=True,
    )

# -------------------------------------------------------------------
# SECTION 3 - STATSMODELS MULTIPLE REGRESSION
# -------------------------------------------------------------------

st.markdown(
    '<div class="section-title">Pasul 3 - Regresie multiplă cu statsmodels</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="info-card">
<div class="info-text">
În această secțiune folosim pachetul <strong>statsmodels</strong> pentru construirea unui model de regresie multiplă.
Spre deosebire de modelele predictive din scikit-learn, acest model este folosit mai ales pentru interpretarea
relației dintre variabile și pentru analizarea coeficienților, valorilor p-value și semnificației statistice.
</div>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="explain-box">
<strong>Obiectiv:</strong> analizăm în ce măsură variabilele rămase după preprocesare pot explica
scorul mediu al unui student (<strong>average_score</strong>). Variabilele categoriale sunt tratate cu
<strong>C(...)</strong>, astfel încât statsmodels să le transforme automat în variabile dummy.
</div>
""",
    unsafe_allow_html=True,
)

statsmodels_df = df_ml.copy()

statsmodels_formula = (
    "average_score ~ weekly_self_study_hours + absence_days + "
    "C(gender) + C(part_time_job) + C(extracurricular_activities)"
)


try:
    stats_model = smf.ols(
        formula=statsmodels_formula,
        data=statsmodels_df,
    ).fit()

    stats_col1, stats_col2, stats_col3 = st.columns(3)

    with stats_col1:
        st.markdown(
            f"""
<div class="metric-card">
<div class="metric-value">{stats_model.rsquared:.3f}</div>
<div class="metric-label">R-squared</div>
</div>
""",
            unsafe_allow_html=True,
        )

    with stats_col2:
        st.markdown(
            f"""
<div class="metric-card">
<div class="metric-value">{stats_model.rsquared_adj:.3f}</div>
<div class="metric-label">Adjusted R-squared</div>
</div>
""",
            unsafe_allow_html=True,
        )

    with stats_col3:
        st.markdown(
            f"""
<div class="metric-card">
<div class="metric-value">{stats_model.f_pvalue:.3f}</div>
<div class="metric-label">Model p-value</div>
</div>
""",
            unsafe_allow_html=True,
        )

    confidence_intervals = stats_model.conf_int()

    coefficients_table = pd.DataFrame(
        {
            "Variabilă": stats_model.params.index,
            "Coeficient": stats_model.params.values,
            "P-value": stats_model.pvalues.values,
            "Interval inferior 95%": confidence_intervals[0].values,
            "Interval superior 95%": confidence_intervals[1].values,
        }
    )

    coefficients_table["Semnificativ la 5%"] = coefficients_table["P-value"].apply(
        lambda value: "Da" if value < 0.05 else "Nu"
    )

    coefficients_table = coefficients_table.round(4)

    st.markdown(
        '<div class="subsection-title">Coeficienții modelului statsmodels</div>',
        unsafe_allow_html=True,
    )

    st.dataframe(
        coefficients_table,
        use_container_width=True,
        hide_index=True,
    )

    st.markdown(
        """
<div class="explain-box">
<strong>Interpretarea coeficienților:</strong><br>
Coeficientul arată direcția relației dintre o variabilă și <strong>average_score</strong>, atunci când celelalte
variabile din model rămân constante. Un coeficient pozitiv sugerează o asociere pozitivă cu scorul mediu,
iar un coeficient negativ sugerează o asociere negativă. Coloana <strong>P-value</strong> ajută la evaluarea
semnificației statistice a fiecărei variabile.
</div>
""",
        unsafe_allow_html=True,
    )

    if stats_model.rsquared < 0.3:
        interpretation_text = (
            "Modelul are o capacitate explicativă redusă spre moderată. Variabilele incluse explică "
            "doar o parte limitată din variația scorului mediu."
        )
    elif stats_model.rsquared < 0.6:
        interpretation_text = (
            "Modelul are o capacitate explicativă moderată. Variabilele incluse surprind o parte importantă "
            "din variația scorului mediu, dar există și alți factori neincluși în model."
        )
    else:
        interpretation_text = (
            "Modelul are o capacitate explicativă bună. Variabilele incluse explică o proporție ridicată "
            "din variația scorului mediu."
        )

    st.markdown(
        f"""
<div class="success-box">
<strong>Interpretare generală:</strong> {interpretation_text}
</div>
""",
        unsafe_allow_html=True,
    )

    with st.expander("Afișează sumarul complet statsmodels"):
        st.text(stats_model.summary().as_text())

except Exception as error:
    st.markdown(
        f"""
<div class="warning-box">
<strong>Modelul statsmodels nu a putut fi estimat.</strong><br>
Eroare: {error}
</div>
""",
        unsafe_allow_html=True,
    )

st.markdown("---")
st.markdown(
    """
<div class="footer">
Student Performance Dashboard · Pagina 05 · Machine Learning
</div>
""",
    unsafe_allow_html=True,
)
