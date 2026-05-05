import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from data.data import channel
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
    st.markdown('<div class="section-title">L\'application mobile concentre tous les signaux d\'alerte à elle seule</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="section-title">L\'app mobile cumule le plus d\'incidents, la satisfaction la plus basse et le temps de résolution le plus long</div>', unsafe_allow_html=True)
        ch_sorted = channel.sort_values("incident_rate_pct", ascending=False)
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        fig.add_trace(go.Bar(
            x=ch_sorted["service_channel"], y=ch_sorted["incident_rate_pct"],
            name="Taux d'incident (%)",
            marker_color=[RED if c == "Application mobile" else ORANGE if c == "Chatbot" else GREY for c in ch_sorted["service_channel"]],
            text=[f"{v}%" for v in ch_sorted["incident_rate_pct"]],
            textposition="outside"
        ), secondary_y=False)
        fig.add_trace(go.Scatter(
            x=ch_sorted["service_channel"], y=ch_sorted["customer_satisfaction"],
            name="Satisfaction (/5)", line=dict(color=BLUE, width=2.5),
            mode="lines+markers", marker=dict(size=9)
        ), secondary_y=True)
        fig.add_trace(go.Scatter(
            x=ch_sorted["service_channel"], y=ch_sorted["avg_resolution_time_h"],
            name="Résolution (h)", line=dict(color=ORANGE, width=2.5, dash="dot"),
            mode="lines+markers", marker=dict(size=9, symbol="diamond")
        ), secondary_y=True)
        fig.update_layout(
            height=340, plot_bgcolor="white", paper_bgcolor="white",
            legend=dict(orientation="h", y=-0.28),
            margin=dict(t=10, b=10, l=10, r=10)
        )
        fig.update_yaxes(title_text="Incidents (%)", secondary_y=False, ticksuffix="%", gridcolor="#f1f5f9")
        fig.update_yaxes(title_text="Satisfaction (/5)  &  Résolution (h)", secondary_y=True)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown('<div class="section-title">L\'app mobile génère 44 % des contacts mais prend 18h à résoudre — le plus long de tous les canaux</div>', unsafe_allow_html=True)
        total_contacts = channel["contact_volume_k"].sum()
        channel["contact_share"] = (channel["contact_volume_k"] / total_contacts * 100).round(1)
        ch_vol = channel.sort_values("contact_volume_k", ascending=False)

        fig2 = make_subplots(specs=[[{"secondary_y": True}]])
        fig2.add_trace(go.Bar(
            x=ch_vol["service_channel"], y=ch_vol["contact_volume_k"],
            name="Volume contacts (k)",
            marker_color=[RED if c == "Application mobile" else BLUE for c in ch_vol["service_channel"]],
            text=[f"{v}k" for v in ch_vol["contact_volume_k"]],
            textposition="outside"
        ), secondary_y=False)
        fig2.add_trace(go.Scatter(
            x=ch_vol["service_channel"], y=ch_vol["avg_resolution_time_h"],
            name="Résolution (h)", line=dict(color=ORANGE, width=2.5, dash="dot"),
            mode="lines+markers", marker=dict(size=9, symbol="diamond", color=ORANGE)
        ), secondary_y=True)
        fig2.update_layout(
            height=340, plot_bgcolor="white", paper_bgcolor="white",
            legend=dict(orientation="h", y=-0.28),
            margin=dict(t=10, b=10, l=10, r=10)
        )
        fig2.update_yaxes(title_text="Volume (k contacts)", secondary_y=False, gridcolor="#f1f5f9")
        fig2.update_yaxes(title_text="Résolution (h)", secondary_y=True)
        st.plotly_chart(fig2, use_container_width=True)

    st.markdown('<div class="section-title">Le canal le plus défaillant est aussi celui avec le churn le plus élevé</div>', unsafe_allow_html=True)

    # Bubble : incident rate × churn × volume
    fig3 = px.scatter(
        channel, x="incident_rate_pct", y="churn_rate_pct",
        size="contact_volume_k", color="service_channel",
        text="service_channel",
        size_max=70,
        color_discrete_sequence=[RED, BLUE, ORANGE, GREEN, GREY],
        labels={"incident_rate_pct": "Taux d'incident (%)", "churn_rate_pct": "Taux de churn (%)", "service_channel": "Canal"}
    )
    fig3.update_traces(textposition="top center")
    fig3.update_layout(
        height=340, plot_bgcolor="white", paper_bgcolor="white",
        margin=dict(t=10, b=10, l=10, r=10),
        showlegend=False
    )
    fig3.update_xaxes(ticksuffix="%", gridcolor="#f1f5f9")
    fig3.update_yaxes(ticksuffix="%", gridcolor="#f1f5f9")
    st.plotly_chart(fig3, use_container_width=True)

    st.markdown('<div class="alert-box">⚠️ L\'application mobile cumule : taux d\'incident le plus élevé (8,9 %), résolution la plus lente (18h), satisfaction la plus faible (2,8/5), churn le plus fort (5,6 %) et volume de contacts dominant (240k). C\'est le point de défaillance principal du parcours client.</div>', unsafe_allow_html=True)
