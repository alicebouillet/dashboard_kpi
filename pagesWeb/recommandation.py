import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from data.data import channel
import pandas as pd
def page():
    # Couleurs
    RED = "#e63946"
    ORANGE = "#f4a261"
    BLUE = "#2a9d8f"
    GREY = "#6c757d"
    GREEN = "#16a34a"
    SEG_COLORS = {
        "Premium": "#2a9d8f",
        "Jeunes actifs": "#f4a261",
        "Nouveaux clients": "#e63946",
        "Seniors": "#6c757d"
    }
    st.markdown("#### Synthèse du diagnostic")
    st.markdown('<div class="insight-box">La hausse du churn est directement liée à la dégradation de l\'expérience digitale : incidents en hausse de +267 %, taux de connexion mobile en baisse, plaintes en doublement — dans un contexte où l\'adoption digitale progresse. Les segments les plus connectés (nouveaux clients, jeunes actifs) sont les plus touchés.</div>', unsafe_allow_html=True)

    st.markdown("---")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="kpi-card" style="text-align:left; min-height:280px;">
        <div style="font-size:28px; margin-bottom:8px;">🔧</div>
        <div style="font-size:16px; font-weight:800; color:#dc2626; margin-bottom:8px;">Court terme — Urgence</div>
        <div style="font-size:14px; font-weight:700; margin-bottom:6px;">Stabiliser l'application mobile</div>
        <div style="font-size:13px; color:#374151; line-height:1.6;">
        Déclencher un plan de crise technique sur l'app mobile : audit des incidents, correctifs prioritaires, objectif de retour à 98 %+ de succès de connexion. C'est le levier le plus direct sur le churn.
        </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="kpi-card" style="text-align:left; min-height:280px;">
        <div style="font-size:28px; margin-bottom:8px;">🎯</div>
        <div style="font-size:16px; font-weight:800; color:#f97316; margin-bottom:8px;">Court terme — Rétention</div>
        <div style="font-size:14px; font-weight:700; margin-bottom:6px;">Programme d'accompagnement nouveaux clients</div>
        <div style="font-size:13px; color:#374151; line-height:1.6;">
        Mettre en place un parcours d'onboarding renforcé pour les nouveaux clients (NPS 17, churn 6,8 %) : contact proactif à J+30, alerte sur les clients ayant rencontré un incident, offre de support prioritaire.
        </div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="kpi-card" style="text-align:left; min-height:280px;">
        <div style="font-size:28px; margin-bottom:8px;">📊</div>
        <div style="font-size:16px; font-weight:800; color:#2563eb; margin-bottom:8px;">Moyen terme — Pilotage</div>
        <div style="font-size:14px; font-weight:700; margin-bottom:6px;">Mettre le NPS et les incidents en KPI de direction</div>
        <div style="font-size:13px; color:#374151; line-height:1.6;">
        Intégrer le NPS par segment et le taux d'incident app dans les revues mensuelles du CODIR. La corrélation entre dégradation digitale et hausse du churn doit être suivie en temps réel pour anticiper les prochaines vagues.
        </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("#### Matrice impact / effort")

    reco_df = pd.DataFrame({
        "Action": ["Corriger l'app mobile", "Onboarding nouveaux clients", "NPS en KPI CODIR",
                   "Réduire temps d'attente support", "Améliorer chatbot"],
        "Impact estimé": [5, 4, 3, 3, 2],
        "Effort estimé": [3, 2, 1, 3, 4],
        "Priorité": ["Urgence", "Urgence", "Pilotage", "Moyen terme", "Long terme"]
    })
    color_map = {"Urgence": RED, "Pilotage": BLUE, "Moyen terme": ORANGE, "Long terme": GREY}

    fig = px.scatter(
        reco_df, x="Effort estimé", y="Impact estimé",
        text="Action", color="Priorité",
        color_discrete_map=color_map,
        size=[40]*5, size_max=40,
    )
    fig.update_traces(textposition="top center", marker=dict(size=20, opacity=0.85))
    fig.add_shape(type="line", x0=2.5, x1=2.5, y0=0.5, y1=5.5, line=dict(color=GREY, dash="dash"))
    fig.add_shape(type="line", x0=0.5, x1=5.5, y0=2.5, y1=2.5, line=dict(color=GREY, dash="dash"))
    fig.add_annotation(x=1.2, y=4.8, text="Quick wins", showarrow=False, font=dict(color=GREEN, size=12))
    fig.add_annotation(x=4.2, y=4.8, text="Gros chantiers", showarrow=False, font=dict(color=ORANGE, size=12))
    fig.update_layout(
        height=360, plot_bgcolor="white", paper_bgcolor="white",
        margin=dict(t=10, b=10, l=10, r=10),
        xaxis=dict(title="Effort (1=faible, 5=élevé)", range=[0.5, 5.5], gridcolor="#f1f5f9", dtick=1),
        yaxis=dict(title="Impact (1=faible, 5=élevé)", range=[0.5, 5.5], gridcolor="#f1f5f9", dtick=1),
    )
    st.plotly_chart(fig, use_container_width=True)