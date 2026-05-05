import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from data.data import mensuel
def page():
    # Couleurs
    RED = "#e63946"
    ORANGE = "#f4a261"
    BLUE = "#2a9d8f"
    GREY = "#6c757d"
    SEG_COLORS = {
        "Premium": "#2a9d8f",
        "Jeunes actifs": "#f4a261",
        "Nouveaux clients": "#e63946",
        "Seniors": "#6c757d"
    }
# Filtre mois
    mois_options = mensuel["month"].tolist()
    mois_range = st.select_slider("Période analysée", options=mois_options,
                                   value=(mois_options[0], mois_options[-1]))
    idx_start = mois_options.index(mois_range[0])
    idx_end = mois_options.index(mois_range[1]) + 1
    df = mensuel.iloc[idx_start:idx_end].copy()

    st.markdown('<div class="section-title">Le churn accélère à partir de septembre, en même temps que les incidents explosent</div>', unsafe_allow_html=True)

    # Churn + incidents dual axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Scatter(
        x=df["month"], y=df["churn_rate_pct"],
        name="Churn (%)", line=dict(color=RED, width=3),
        mode="lines+markers", marker=dict(size=9), fill="tozeroy",
        fillcolor="rgba(220,38,38,0.08)"
    ), secondary_y=False)
    fig.add_trace(go.Bar(
        x=df["month"], y=df["app_incidents_count"],
        name="Incidents app mobile", marker_color="rgba(249,115,22,0.7)",
        opacity=0.8
    ), secondary_y=True)
    fig.update_layout(
        height=340, plot_bgcolor="white", paper_bgcolor="white",
        legend=dict(orientation="h", y=-0.2),
        margin=dict(t=10, b=10, l=10, r=10),
        hovermode="x unified", barmode="overlay"
    )
    fig.update_yaxes(title_text="Churn (%)", secondary_y=False, ticksuffix="%", gridcolor="#f1f5f9")
    fig.update_yaxes(title_text="Incidents", secondary_y=True)
    st.plotly_chart(fig, use_container_width=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="section-title">Les plaintes et l\'attente au support double entre juillet et novembre</div>', unsafe_allow_html=True)
        fig2 = make_subplots(specs=[[{"secondary_y": True}]])
        fig2.add_trace(go.Scatter(
            x=df["month"], y=df["complaints_count"],
            name="Plaintes", line=dict(color=RED, width=2.5),
            mode="lines+markers", marker=dict(size=7)
        ), secondary_y=False)
        fig2.add_trace(go.Scatter(
            x=df["month"], y=df["avg_wait_time_min"],
            name="Attente support (min)", line=dict(color=ORANGE, width=2.5, dash="dot"),
            mode="lines+markers", marker=dict(size=7)
        ), secondary_y=True)
        fig2.update_layout(
            height=280, plot_bgcolor="white", paper_bgcolor="white",
            legend=dict(orientation="h", y=-0.25),
            margin=dict(t=10, b=10, l=10, r=10),
            hovermode="x unified"
        )
        fig2.update_yaxes(title_text="Plaintes", secondary_y=False, gridcolor="#f1f5f9")
        fig2.update_yaxes(title_text="Attente (min)", secondary_y=True)
        st.plotly_chart(fig2, use_container_width=True)

    with col2:
        st.markdown('<div class="section-title">La qualité de connexion mobile se dégrade au moment où l\'usage digital progresse</div>', unsafe_allow_html=True)
        fig3 = make_subplots(specs=[[{"secondary_y": True}]])
        fig3.add_trace(go.Scatter(
            x=df["month"], y=df["mobile_login_success_pct"],
            name="Succès connexion mobile (%)", line=dict(color=RED, width=2.5),
            mode="lines+markers", marker=dict(size=7)
        ), secondary_y=False)
        fig3.add_trace(go.Scatter(
            x=df["month"], y=df["digital_adoption_pct"],
            name="Adoption digitale (%)", line=dict(color=BLUE, width=2.5, dash="dash"),
            mode="lines+markers", marker=dict(size=7)
        ), secondary_y=True)
        fig3.update_layout(
            height=280, plot_bgcolor="white", paper_bgcolor="white",
            legend=dict(orientation="h", y=-0.25),
            margin=dict(t=10, b=10, l=10, r=10),
            hovermode="x unified"
        )
        fig3.update_yaxes(title_text="Succès connexion (%)", secondary_y=False, ticksuffix="%", gridcolor="#f1f5f9")
        fig3.update_yaxes(title_text="Adoption digitale (%)", secondary_y=True, ticksuffix="%")
        st.plotly_chart(fig3, use_container_width=True)

    st.markdown('<div class="alert-box">⚠️ Paradoxe clé : l\'adoption digitale progresse régulièrement (+5 pts en 6 mois) pendant que la qualité de l\'application se dégrade. Plus les clients utilisent le digital, plus ils subissent les incidents — ce qui amplifie le churn.</div>', unsafe_allow_html=True)
