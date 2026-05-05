import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from data.data import segment
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
    }    # Filtre segment
    seg_options = segment["segment"].tolist()
    selected_segs = st.multiselect("Segments à afficher", options=seg_options, default=seg_options)
    df = segment[segment["segment"].isin(selected_segs)]
 
    if df.empty:
        st.warning("Sélectionnez au moins un segment.")
    else:
        st.markdown('<div class="section-title">Les segments les plus digitaux sont aussi les plus exposés au churn</div>', unsafe_allow_html=True)
 
        # Scatter : digital usage vs churn
        fig = px.scatter(
            df, x="digital_usage_pct", y="churn_rate_pct",
            size="customers_count_k", color="segment",
            color_discrete_map=SEG_COLORS,
            text="segment",
            size_max=60,
            labels={"digital_usage_pct": "Usage digital (%)", "churn_rate_pct": "Taux de churn (%)", "segment": "Segment"}
        )
        fig.update_traces(textposition="top center")
        fig.update_layout(
            height=380, plot_bgcolor="white", paper_bgcolor="white",
            margin=dict(t=10, b=10, l=10, r=10),
            showlegend=False
        )
        fig.update_xaxes(ticksuffix="%", gridcolor="#f1f5f9")
        fig.update_yaxes(ticksuffix="%", gridcolor="#f1f5f9")
        st.plotly_chart(fig, use_container_width=True)
 
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="section-title">Les nouveaux clients ont le NPS le plus bas et le taux de réclamation le plus élevé</div>', unsafe_allow_html=True)
            fig2 = make_subplots(specs=[[{"secondary_y": True}]])
            fig2.add_trace(go.Bar(
                name="NPS", x=df["segment"], y=df["nps"],
                marker_color=[SEG_COLORS.get(s, BLUE) for s in df["segment"]],
                opacity=0.75,
                text=df["nps"], textposition="outside"
            ), secondary_y=False)
            fig2.add_trace(go.Scatter(
                name="Taux de réclamation (%)",
                x=df["segment"], y=df["complaint_rate_pct"],
                mode="lines+markers",
                line=dict(color=RED, width=2.5, dash="dot"),
                marker=dict(size=9, color=RED),
                text=[f"{v}%" for v in df["complaint_rate_pct"]],
                textposition="top center"
            ), secondary_y=True)
            fig2.update_layout(
                height=300, plot_bgcolor="white", paper_bgcolor="white",
                margin=dict(t=10, b=60, l=10, r=10),
                legend=dict(orientation="h", y=-0.35),
            )
            fig2.update_yaxes(title_text="NPS", secondary_y=False, gridcolor="#f1f5f9")
            fig2.update_yaxes(title_text="Réclamations (%)", secondary_y=True, ticksuffix="%")
            st.plotly_chart(fig2, use_container_width=True)
 
        with col2:
            st.markdown('<div class="section-title">Churn élevé + valeur client faible : les nouveaux clients représentent le risque le plus urgent</div>', unsafe_allow_html=True)
            fig3 = px.scatter(
                df, x="avg_balance_eur", y="churn_rate_pct",
                size="customers_count_k", color="segment",
                color_discrete_map=SEG_COLORS,
                text="segment",
                size_max=50,
                labels={"avg_balance_eur": "Solde moyen (€)", "churn_rate_pct": "Taux de churn (%)", "segment": "Segment"}
            )
            fig3.update_traces(textposition="top center")
            fig3.update_layout(
                height=280, plot_bgcolor="white", paper_bgcolor="white",
                margin=dict(t=10, b=10, l=10, r=10),
                showlegend=False
            )
            fig3.update_xaxes(tickprefix="€", gridcolor="#f1f5f9")
            fig3.update_yaxes(ticksuffix="%", gridcolor="#f1f5f9")
            st.plotly_chart(fig3, use_container_width=True)
 
        st.markdown('<div class="insight-box">💡 <strong>Priorité d\'action :</strong> Les nouveaux clients (110k) combinent le churn le plus élevé (6,8 %), la satisfaction la plus basse (NPS 17), le taux de réclamation le plus fort (8,4 %) et le solde le plus faible (1 250 €). Ce segment est à la fois le plus vulnérable et le moins rentable — l\'urgence est maximale.</div>', unsafe_allow_html=True)
 
