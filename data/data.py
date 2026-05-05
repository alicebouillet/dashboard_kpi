import pandas as pd
mensuel = pd.DataFrame({
    "month": ["Juil", "Août", "Sept", "Oct", "Nov", "Déc"],
    "active_customers_k": [820, 826, 831, 836, 840, 844],
    "new_customers_k": [18, 19, 20, 21, 22, 23],
    "churn_rate_pct": [2.1, 2.3, 2.8, 3.6, 4.2, 4.0],
    "complaints_count": [3200, 3500, 4200, 5600, 6400, 6100],
    "app_incidents_count": [18, 22, 37, 61, 74, 66],
    "mobile_login_success_pct": [98.2, 97.9, 96.8, 94.7, 93.5, 94.1],
    "nps": [41, 39, 34, 25, 19, 21],
    "avg_wait_time_min": [3.6, 3.9, 4.8, 6.3, 7.1, 6.7],
    "digital_adoption_pct": [68, 69, 70, 71, 72, 73],
})

segment = pd.DataFrame({
    "segment": ["Nouveaux clients", "Jeunes actifs", "Standard", "Premium", "Seniors"],
    "customers_count_k": [110, 180, 320, 95, 139],
    "churn_rate_pct": [6.8, 4.5, 3.4, 1.9, 2.6],
    "avg_balance_eur": [1250, 3400, 5200, 18500, 8700],
    "nps": [17, 24, 28, 49, 38],
    "complaint_rate_pct": [8.4, 6.5, 5.3, 2.1, 3.0],
    "digital_usage_pct": [96, 92, 74, 68, 39],
})

channel = pd.DataFrame({
    "service_channel": ["Application mobile", "Site web", "Centre d'appel", "Agence", "Chatbot"],
    "incident_rate_pct": [8.9, 3.6, 2.2, 1.1, 4.8],
    "avg_resolution_time_h": [18.0, 9.5, 11.0, 6.0, 13.2],
    "customer_satisfaction": [2.8, 3.4, 3.1, 4.0, 2.9],
    "contact_volume_k": [240, 110, 85, 42, 64],
    "churn_rate_pct": [5.6, 3.1, 3.9, 1.8, 4.4],
})