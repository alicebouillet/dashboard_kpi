import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from pagesWeb import (
    vue_ensemble,
    tendances_mensuelles,
    analyse_segment,
    canaux_services,
    recommandations
)
st.set_page_config(page_title="NovaBank — Analyse", layout="wide", page_icon="🏦")


# ── Couleurs ──────────────────────────────────────────────────────────────────
BLUE = "#2563eb"
RED = "#dc2626"
ORANGE = "#f97316"
GREEN = "#16a34a"
GREY = "#94a3b8"
BG = "#f8fafc"
SEG_COLORS = {
    "Nouveaux clients": RED,
    "Jeunes actifs": ORANGE,
    "Standard": BLUE,
    "Premium": GREEN,
    "Seniors": GREY,
}

# ── Style CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    [data-testid="stAppViewContainer"] { background: #f8fafc; }
    .block-container { padding-top: 1.5rem; padding-bottom: 2rem; }

    /* Navigation pills */
    div[data-testid="stHorizontalBlock"] button {
        border-radius: 999px !important;
    }

    .kpi-card {
        background: white;
        border-radius: 12px;
        padding: 20px 24px;
        box-shadow: 0 1px 4px rgba(0,0,0,0.08);
        text-align: center;
    }
    .kpi-label { font-size: 13px; color: #64748b; font-weight: 600; margin-bottom: 4px; }
    .kpi-value { font-size: 32px; font-weight: 800; line-height: 1.1; }
    .kpi-delta { font-size: 13px; margin-top: 4px; color: #64748b; }
    .kpi-red { color: #dc2626; }
    .kpi-orange { color: #f97316; }
    .kpi-blue { color: #2563eb; }
    .kpi-green { color: #16a34a; }

    .section-title {
        font-size: 18px; font-weight: 700; color: #0f172a;
        margin: 8px 0 16px 0; border-left: 4px solid #2563eb;
        padding-left: 10px;
    }
    .alert-box {
        background: #fef2f2; border-left: 4px solid #dc2626;
        padding: 14px 18px; border-radius: 8px; margin-bottom: 16px;
        font-size: 14px; color: #7f1d1d;
    }
    .insight-box {
        background: #eff6ff; border-left: 4px solid #2563eb;
        padding: 14px 18px; border-radius: 8px; margin-bottom: 16px;
        font-size: 14px; color: #1e3a5f;
    }
    .nav-container {
        background: white;
        border-radius: 12px;
        padding: 10px 16px;
        box-shadow: 0 1px 4px rgba(0,0,0,0.08);
        margin-bottom: 24px;
        display: flex;
        gap: 8px;
    }
    div[data-testid="column"] > div[data-testid="stVerticalBlock"] > div[data-testid="stHorizontalBlock"] {
        gap: 8px;
    }
</style>
""", unsafe_allow_html=True)

# ── Navigation ────────────────────────────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "Vue d'ensemble"

pages = ["Vue d'ensemble", "Tendances mensuelles", "Analyse par segment", "Canaux & services", "Recommandations"]

st.markdown("### 🏦 NovaBank — Tableau de bord")

cols = st.columns(len(pages))
for i, p in enumerate(pages):
    with cols[i]:
        if st.button(p, key=f"nav_{i}", use_container_width=True,
                     type="primary" if st.session_state.page == p else "secondary"):
            st.session_state.page = p
            st.rerun()

st.markdown("---")
page = st.session_state.page

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 1 — VUE D'ENSEMBLE
# ══════════════════════════════════════════════════════════════════════════════
if page == "Vue d'ensemble":
    
    vue_ensemble.page()
# ══════════════════════════════════════════════════════════════════════════════
# PAGE 2 — TENDANCES MENSUELLES
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Tendances mensuelles":
    tendances_mensuelles.page()

# PAGE 3 — ANALYSE PAR SEGMENT
elif page == "Analyse par segment":
    analyse_segment.page()

  
# PAGE 4 — CANAUX & SERVICES
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Canaux & services":
    canaux_services.page()



# ══════════════════════════════════════════════════════════════════════════════
# PAGE 5 — RECOMMANDATIONS
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Recommandations":
    recommandations.page()
