import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from data.data import mensuel, segment, channel
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

    # Titre et contexte
    st.markdown('<div class="page-title">📉 Churn en forte hausse : l\'expérience digitale au cœur du problème</div>', unsafe_allow_html=True)
    st.markdown('<div class="alert-box">⚠️ <strong>Constat principal :</strong> En 6 mois, le taux de churn a doublé (+90 %), porté par l\'effondrement de l\'expérience digitale — qui touche en priorité les segments les plus récents et les plus connectés.</div>', unsafe_allow_html=True)
    # KPIs
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown('<div class="kpi-card"><div class="kpi-label">Taux de churn (Déc)</div><div class="kpi-value kpi-red">4,0 %</div><div class="kpi-delta">vs 2,1 % en juillet</div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="kpi-card"><div class="kpi-label">NPS (Déc)</div><div class="kpi-value kpi-orange">21</div><div class="kpi-delta">vs 41 en juillet (−49 %)</div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="kpi-card"><div class="kpi-label">Incidents app mobile (Déc)</div><div class="kpi-value kpi-red">66</div><div class="kpi-delta">vs 18 en juillet (+267 %)</div></div>', unsafe_allow_html=True)
    with c4:
        st.markdown('<div class="kpi-card"><div class="kpi-label">Plaintes (Déc)</div><div class="kpi-value kpi-orange">6 100</div><div class="kpi-delta">vs 3 200 en juillet (+91 %)</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Graphique synthèse : churn + NPS sur axe dual
    st.markdown('<div class="section-title">Churn et satisfaction évoluent en miroir depuis juillet</div>', unsafe_allow_html=True)

    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Scatter(
        x=mensuel["month"], y=mensuel["churn_rate_pct"],
        name="Taux de churn (%)", line=dict(color=RED, width=3),
        mode="lines+markers", marker=dict(size=8)
    ), secondary_y=False)
    fig.add_trace(go.Scatter(
        x=mensuel["month"], y=mensuel["nps"],
        name="NPS", line=dict(color=BLUE, width=3, dash="dash"),
        mode="lines+markers", marker=dict(size=8)
    ), secondary_y=True)
    fig.update_layout(
        height=320, plot_bgcolor="white", paper_bgcolor="white",
        legend=dict(orientation="h", y=-0.2),
        margin=dict(t=10, b=10, l=10, r=10),
        hovermode="x unified"
    )
    fig.update_yaxes(title_text="Churn (%)", secondary_y=False, ticksuffix="%", gridcolor="#f1f5f9")
    fig.update_yaxes(title_text="NPS", secondary_y=True)
    fig.update_xaxes(gridcolor="#f1f5f9")
    st.plotly_chart(fig, use_container_width=True)

    # Radar synthèse par segment
    st.markdown('<div class="section-title">Les nouveaux clients et jeunes actifs concentrent le risque d\'attrition</div>', unsafe_allow_html=True)

    seg_sorted = segment.sort_values("churn_rate_pct", ascending=True)
    colors = [SEG_COLORS.get(s, BLUE) for s in seg_sorted["segment"]]
    fig2 = go.Figure(go.Bar(
            x=seg_sorted["churn_rate_pct"],
            y=seg_sorted["segment"],
            orientation="h",
            marker_color=colors,
            text=[f"{v}%" for v in seg_sorted["churn_rate_pct"]],
            textposition="outside",
        ))
    fig2.update_layout(
            height=280, plot_bgcolor="white", paper_bgcolor="white",
            margin=dict(t=10, b=10, l=10, r=80),
            xaxis=dict(ticksuffix="%", gridcolor="#f1f5f9"),
            showlegend=False
        )
    st.plotly_chart(fig2, use_container_width=True)



    st.markdown('<div class="insight-box">💡 <strong>Lecture :</strong> Le churn est 3,6× plus élevé chez les nouveaux clients que chez les Premium. L\'app mobile — canal le plus utilisé — affiche le taux de churn le plus fort (5,6 %) et le plus grand volume de contacts (240k).</div>', unsafe_allow_html=True)
