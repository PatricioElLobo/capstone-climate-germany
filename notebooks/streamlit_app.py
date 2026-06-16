# ============================================================
# CELL 1 — SETUP
# streamlit_app.py
# ============================================================
import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# ── Page config ─────────────────────────────────────────────
st.set_page_config(
    page_title="Germany's Climate Bill",
    page_icon="🌡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Paths ────────────────────────────────────────────────────
PROJECT_ROOT = Path(__file__).parent.parent  # go up one level from notebooks/
FIGURES = PROJECT_ROOT / "data" / "figures"

# ── Colors (locked across all notebooks) ────────────────────
COLORS = {
    "positive"   : "#FF7043",
    "negative"   : "#9C6FE4",
    "accent"     : "#E8E8E8",
    "background" : "#1a1a1a",
    "grid"       : "rgba(232,232,232,0.08)",
    "text"       : "#E8E8E8",
    "text_muted" : "rgba(232,232,232,0.45)",
}

# ── Global CSS ───────────────────────────────────────────────
st.markdown("""
<style>
    /* Dark background to match project palette */
    .stApp { background-color: #1a1a1a; }
    section[data-testid="stSidebar"] { background-color: #111111; }

    /* KPI metric cards */
    [data-testid="stMetric"] {
        background-color: #111111;
        border: 0.5px solid rgba(232,232,232,0.12);
        border-radius: 8px;
        padding: 12px 16px;
    }
    [data-testid="stMetricLabel"] { color: rgba(232,232,232,0.55) !important; font-size: 12px !important; }
    [data-testid="stMetricValue"] { color: #FF7043 !important; font-size: 22px !important; }
    [data-testid="stMetricDelta"] { font-size: 11px !important; }

    /* Section headers */
    h1, h2, h3 { color: #E8E8E8 !important; }
    p, li { color: rgba(232,232,232,0.75); }

    /* Popover button — keep it subtle */
    [data-testid="stPopover"] button {
        background: transparent;
        border: 0.5px solid rgba(232,232,232,0.2);
        color: rgba(232,232,232,0.5);
        font-size: 11px;
        padding: 2px 8px;
        border-radius: 4px;
    }
</style>
""", unsafe_allow_html=True)

# ── Sidebar ──────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🌡️ Germany's Climate Bill")
    st.markdown(
        "<p style='color:rgba(232,232,232,0.45); font-size:12px; margin-top:-8px;'>"
        "Data Bootcamp Capstone · 2026</p>",
        unsafe_allow_html=True,
    )
    st.divider()

    section = st.radio(
        "Navigate",
        options=[
            "🌡️ RQ1 — Climate is changing",
            "💶 RQ2 — Losses are growing",
            "📉 RQ3 — What drives losses",
            "⚠️ RQ4 — Cost of inaction",
        ],
        label_visibility="collapsed",
    )

    st.divider()
    st.markdown(
        "<p style='color:rgba(232,232,232,0.3); font-size:11px;'>"
        "Sources: DWD · GDV · Destatis · UBA · CAT</p>",
        unsafe_allow_html=True,
    )

# ============================================================
# CELL 2 — RQ1: CLIMATE IS CHANGING
# ============================================================

# ── Helper function ───────────────────────────────────────────
def load_fig(filename, height=500, scrolling=False):
    """Load a saved Plotly HTML figure and render it."""
    path = FIGURES / filename
    components.html(path.read_text(encoding="utf-8"), height=height, scrolling=scrolling)

if section == "🌡️ RQ1 — Climate is changing":

    st.markdown('<span style="background:#FF7043;color:#1a1a1a;font-size:11px;font-weight:600;padding:3px 8px;border-radius:4px;letter-spacing:0.06em;">RQ1</span>', unsafe_allow_html=True)
    st.markdown("## Is Germany's climate measurably changing?")
    st.markdown('<p style="color:rgba(232,232,232,0.4);margin-top:-10px;font-size:13px;">DWD national temperature records 1881–2025 · Mann-Kendall trend tests</p>', unsafe_allow_html=True)

    # ── KPI strip ────────────────────────────────────────────
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("2025 anomaly", "+1.79°C", "above 1961–1990 baseline")
    k2.metric("Warming rate", "+0.013°C/yr", "Sen's slope")
    k3.metric("Hot days trend", "+0.106 days/yr", "days ≥ 30°C")
    k4.metric("Frost days trend", "−0.376 days/yr", "days ≤ 0°C")

    st.divider()

    # ── BLOCK 1: Hero chart — full width ─────────────────────
    col_t, col_i = st.columns([11, 1])
    with col_t:
        st.markdown('<p style="font-size:20px;font-weight:500;color:#E8E8E8;margin-bottom:4px;">National temperature anomaly 1881–2025</p>', unsafe_allow_html=True)
    with col_i:
        with st.popover("ℹ️"):
            st.markdown("**Baseline:** 1961–1990 (WMO standard)  \n**Trend:** 10-year rolling mean  \n**Source:** DWD national mean temperature")
    load_fig("02_temperature_anomaly_1881_2025.html", height=460)

    st.divider()

    # ── BLOCK 2: Extreme events (left) + fact boxes (right) ──
    st.markdown('<p style="font-size:20px;font-weight:500;color:#E8E8E8;margin-bottom:4px;">Extreme climate indicators 1951–2025</p>', unsafe_allow_html=True)

    col_chart, col_facts = st.columns([3, 2])

    with col_chart:
        indicator = st.selectbox(
            "Select indicator",
            ["Hot days (≥ 30°C)", "Tropical nights (≥ 20°C)", "Frost days (≤ 0°C)", "Heavy rain days","Total precipitation (mm)",],
            key="rq1_indicator",
        )
        indicator_map = {
            "Hot days (≥ 30°C)"        : "02_extreme_hot_days.html",
            "Tropical nights (≥ 20°C)" : "02_extreme_tropical_nights.html",
            "Frost days (≤ 0°C)"       : "02_extreme_frost_days.html",
            "Heavy rain days"           : "02_extreme_heavy_rain_days.html",
            "Total precipitation (mm)"  : "02_extreme_precipitation.html",            
        }
        load_fig(indicator_map[indicator], height=340)

    with col_facts:
        st.markdown('<div style="height:44px;"></div>', unsafe_allow_html=True)
        st.markdown("""
<div style="border-left:2px solid #FF7043;padding:12px 14px;background:#111;border-radius:0 8px 8px 0;margin-bottom:10px;">
  <div style="font-size:24px;font-weight:500;color:#FF7043;">2003</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.6);margin-top:4px;line-height:1.5;">European heatwave — Germany's hottest summer since records began</div>
  <div style="font-size:11px;color:rgba(232,232,232,0.3);margin-top:6px;">20.4 hot days — nearly 3× the 1961–1990 average</div>
</div>
<div style="border-left:2px solid #9C6FE4;padding:12px 14px;background:#111;border-radius:0 8px 8px 0;margin-bottom:10px;">
  <div style="font-size:24px;font-weight:500;color:#9C6FE4;">2018</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.6);margin-top:4px;line-height:1.5;">Drought and record heat — €3.4bn in insured weather losses</div>
  <div style="font-size:11px;color:rgba(232,232,232,0.3);margin-top:6px;">Hottest year in German records at that time</div>
</div>
<div style="border-left:2px solid rgba(232,232,232,0.2);padding:12px 14px;background:#111;border-radius:0 8px 8px 0;">
  <div style="font-size:24px;font-weight:500;color:#E8E8E8;">4 of 6</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.6);margin-top:4px;line-height:1.5;">climate indicators show significant trends — temperature and heat extremes clearly increasing</div>
  <div style="font-size:11px;color:rgba(232,232,232,0.3);margin-top:6px;">Heavy rain days and total precipitation: no significant trend yet — but watch this space</div>
</div>
""", unsafe_allow_html=True)

    st.divider()

    # ── BLOCK 3: MK table (left) + explanation (right) ───────
    col_mk_chart, col_mk_text = st.columns([3, 2])

    with col_mk_chart:
        st.markdown('<p style="font-size:20px;font-weight:500;color:#E8E8E8;margin-bottom:4px;">Mann-Kendall trend test results</p>', unsafe_allow_html=True)
        load_fig("02_mann_kendall_results.html", height=240)

    with col_mk_text:
        st.markdown('<div style="height:44px;"></div>', unsafe_allow_html=True)
        st.markdown("""
<div style="border-left:2px solid #FF7043;padding:16px 18px;background:#111;border-radius:0 8px 8px 0;margin-bottom:10px;">
  <div style="font-size:13px;font-weight:500;color:#E8E8E8;margin-bottom:8px;">What is the Mann-Kendall test?</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.6);line-height:1.6;">A non-parametric test for monotonic trends — no assumption of normality required. It asks: does the variable consistently go up or down over time?</div>
</div>
<div style="border-left:2px solid rgba(232,232,232,0.15);padding:16px 18px;background:#111;border-radius:0 8px 8px 0;margin-bottom:10px;">
  <div style="font-size:13px;font-weight:500;color:#E8E8E8;margin-bottom:8px;">How to read it</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.6);line-height:1.6;"><span style="color:#FF7043;">Tau</span> — direction and strength (−1 to +1)<br><span style="color:#FF7043;">Sen's slope</span> — median rate of change per year<br><span style="color:#FF7043;">p-value</span> — below 0.05 = significant trend</div>
</div>
<div style="border-left:2px solid #9C6FE4;padding:16px 18px;background:#111;border-radius:0 8px 8px 0;">
  <div style="font-size:24px;font-weight:500;color:#9C6FE4;">H₀ rejected</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.6);margin-top:4px;line-height:1.5;">for all four variables — the trends are real, not noise</div>
</div>
""", unsafe_allow_html=True)

    st.divider()

    # ── BLOCK 4: Maps (left) + fact boxes (right) ────────────
    st.markdown('<p style="font-size:20px;font-weight:500;color:#E8E8E8;margin-bottom:4px;">Warming across Germany — animated by Bundesland</p>', unsafe_allow_html=True)

    col_map, col_mapfacts = st.columns([3, 2])

    with col_map:
        map_choice = st.selectbox(
            "Select map",
            ["Temperature anomaly by Bundesland", "Hot days by Bundesland"],
            key="rq1_map",
        )
        if map_choice == "Temperature anomaly by Bundesland":
            load_fig("02_choropleth_temperature_anomaly.html", height=580, scrolling=True)
        else:
            load_fig("02_choropleth_hotdays.html", height=580, scrolling=True)

    with col_mapfacts:
        st.markdown('<div style="height:44px;"></div>', unsafe_allow_html=True)
        st.markdown("""
<div style="border-left:2px solid #FF7043;padding:12px 14px;background:#111;border-radius:0 8px 8px 0;margin-bottom:10px;">
  <div style="font-size:24px;font-weight:500;color:#FF7043;">16 of 16</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.6);margin-top:4px;line-height:1.5;">all Bundesländer show positive temperature anomaly in 2024</div>
  <div style="font-size:11px;color:rgba(232,232,232,0.3);margin-top:6px;">No region is cooling</div>
</div>
<div style="border-left:2px solid #9C6FE4;padding:12px 14px;background:#111;border-radius:0 8px 8px 0;margin-bottom:10px;">
  <div style="font-size:24px;font-weight:500;color:#9C6FE4;">South-west</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.6);margin-top:4px;line-height:1.5;">Baden-Württemberg and Bavaria warming faster than the national average</div>
  <div style="font-size:11px;color:rgba(232,232,232,0.3);margin-top:6px;">Continental interior effect</div>
</div>
<div style="border-left:2px solid rgba(232,232,232,0.2);padding:12px 14px;background:#111;border-radius:0 8px 8px 0;">
  <div style="font-size:24px;font-weight:500;color:#E8E8E8;">1881</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.6);margin-top:4px;line-height:1.5;">start of systematic DWD temperature records — 144 years of data</div>
  <div style="font-size:11px;color:rgba(232,232,232,0.3);margin-top:6px;">Press play to watch Germany warm in real time</div>
</div>
""", unsafe_allow_html=True)
        
# ============================================================
# CELL 3 — RQ2: LOSSES ARE GROWING
# ============================================================

elif section == "💶 RQ2 — Losses are growing":

    st.markdown('<span style="background:#FF7043;color:#1a1a1a;font-size:11px;font-weight:600;padding:3px 8px;border-radius:4px;letter-spacing:0.06em;">RQ2</span>', unsafe_allow_html=True)
    st.markdown("## Are insured losses from natural hazards growing?")
    st.markdown('<p style="color:rgba(232,232,232,0.4);margin-top:-10px;font-size:13px;">GDV Naturgefahrenreport 1973–2024 · nominal and real losses · GVA normalisation</p>', unsafe_allow_html=True)

    # ── KPI strip ────────────────────────────────────────────
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Series length", "52 years", "1973–2024")
    k2.metric("Nominal trend", "p = 0.0007", "significant ✓")
    k3.metric("Real trend", "p = 0.81", "not significant")
    k4.metric("% GVA trend", "p = 0.358", "not significant")

    st.divider()

    # ── BLOCK 1: Hero chart — full width ─────────────────────
    col_t, col_i = st.columns([11, 1])
    with col_t:
        st.markdown('<p style="font-size:20px;font-weight:500;color:#E8E8E8;margin-bottom:4px;">Total insured losses from natural hazards 1973–2024</p>', unsafe_allow_html=True)
    with col_i:
        with st.popover("ℹ️"):
            st.markdown("**Source:** GDV Naturgefahrenreport  \n**Values:** nominal € billion (current prices)  \n**Includes:** storm/hail, flood & heavy rain, motor vehicle  \n**Trend line:** 10-year rolling mean")
    load_fig("03_gdv_total_losses_1973_2024.html", height=460)

    st.divider()

    # ── BLOCK 2: Stacked property (left) + fact boxes (right) ─
    col_chart, col_facts = st.columns([3, 2])

    with col_chart:
        st.markdown('<p style="font-size:20px;font-weight:500;color:#E8E8E8;margin-bottom:4px;">Property losses by hazard type 2002–2024</p>', unsafe_allow_html=True)
        load_fig("03_gdv_stacked_property_2002_2024.html", height=400)

    with col_facts:
        st.markdown('<div style="height:44px;"></div>', unsafe_allow_html=True)
        st.markdown("""
<div style="border-left:2px solid #FF7043;padding:12px 14px;background:#111;border-radius:0 8px 8px 0;margin-bottom:10px;">
  <div style="font-size:24px;font-weight:500;color:#FF7043;">2021</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.6);margin-top:4px;line-height:1.5;">Ahr valley floods — single deadliest weather disaster in modern German history</div>
  <div style="font-size:11px;color:rgba(232,232,232,0.3);margin-top:6px;">€8.5bn in insured losses — largest single-year loss on record</div>
</div>
<div style="border-left:2px solid #9C6FE4;padding:12px 14px;background:#111;border-radius:0 8px 8px 0;margin-bottom:10px;">
  <div style="font-size:24px;font-weight:500;color:#9C6FE4;">Flood & rain</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.6);margin-top:4px;line-height:1.5;">share of property losses growing relative to storm & hail since 2002</div>
  <div style="font-size:11px;color:rgba(232,232,232,0.3);margin-top:6px;">Motor vehicle losses excluded from this chart</div>
</div>
<div style="border-left:2px solid rgba(232,232,232,0.2);padding:12px 14px;background:#111;border-radius:0 8px 8px 0;">
  <div style="font-size:24px;font-weight:500;color:#E8E8E8;">2002–2024</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.6);margin-top:4px;line-height:1.5;">property breakdown available — GDV started reporting categories separately from 2002</div>
  <div style="font-size:11px;color:rgba(232,232,232,0.3);margin-top:6px;">Earlier data is total losses only</div>
</div>
""", unsafe_allow_html=True)

    st.divider()

    # ── BLOCK 3: explanation (left) + dropdown chart (right) ──
    col_text, col_chart2 = st.columns([2, 3])

    with col_text:
        st.markdown('<div style="height:44px;"></div>', unsafe_allow_html=True)
        st.markdown("""
<div style="border-left:2px solid #FF7043;padding:16px 18px;background:#111;border-radius:0 8px 8px 0;margin-bottom:10px;">
  <div style="font-size:13px;font-weight:500;color:#E8E8E8;margin-bottom:8px;">Why adjust for inflation?</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.6);line-height:1.6;">€1bn in 1991 bought more than €1bn today. Without deflation, rising nominal losses could just reflect a more expensive economy — not more physical damage.</div>
</div>
<div style="border-left:2px solid #9C6FE4;padding:16px 18px;background:#111;border-radius:0 8px 8px 0;margin-bottom:10px;">
  <div style="font-size:13px;font-weight:500;color:#E8E8E8;margin-bottom:8px;">What the data shows</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.6);line-height:1.6;">Nominal losses: significant upward trend (p=0.0007). Real losses restricted to 1991–2024: trend disappears (p=0.81). The window matters — pre-1991 CPI is unreliable due to reunification.</div>
</div>
<div style="border-left:2px solid rgba(232,232,232,0.2);padding:16px 18px;background:#111;border-radius:0 8px 8px 0;">
  <div style="font-size:24px;font-weight:500;color:#E8E8E8;">Honest answer</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.6);margin-top:4px;line-height:1.5;">nominal losses are growing; real losses over the comparable period are not — yet</div>
</div>
""", unsafe_allow_html=True)

    with col_chart2:
        lens = st.selectbox(
            "Select lens",
            ["Real losses 1991–2024", "Nominal vs real comparison"],
            key="rq2_lens",
        )
        lens_map = {
            "Real losses 1991–2024"      : ("03_gdv_real_losses_1991_2024.html", 400),
            "Nominal vs real comparison" : ("03_losses_nominal_vs_real_1991_2024.html", 400),
        }
        fname, h = lens_map[lens]
        load_fig(fname, height=h)

    st.divider()

    # ── BLOCK 4: % GVA chart (left) + explanation (right) ────
    col_chart3, col_text2 = st.columns([3, 2])

    with col_chart3:
        st.markdown('<p style="font-size:20px;font-weight:500;color:#E8E8E8;margin-bottom:4px;">Losses as share of economic output 1991–2024</p>', unsafe_allow_html=True)
        load_fig("03_losses_pct_gva_1991_2024.html", height=400)

    with col_text2:
        st.markdown('<div style="height:44px;"></div>', unsafe_allow_html=True)
        st.markdown("""
<div style="border-left:2px solid #FF7043;padding:16px 18px;background:#111;border-radius:0 8px 8px 0;margin-bottom:10px;">
  <div style="font-size:13px;font-weight:500;color:#E8E8E8;margin-bottom:8px;">What is GVA normalisation?</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.6);line-height:1.6;">Dividing losses by Gross Value Added removes both inflation and economic growth effects. If losses grow but GVA grows faster, the ratio stays flat — the economy is absorbing the damage.</div>
</div>
<div style="border-left:2px solid rgba(232,232,232,0.2);padding:16px 18px;background:#111;border-radius:0 8px 8px 0;margin-bottom:10px;">
  <div style="font-size:24px;font-weight:500;color:#E8E8E8;">p = 0.358</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.6);margin-top:4px;line-height:1.5;">no significant trend — losses as a share of GVA have stayed roughly flat since 1991</div>
  <div style="font-size:11px;color:rgba(232,232,232,0.3);margin-top:6px;">Mann-Kendall · 1991–2024</div>
</div>
<div style="border-left:2px solid #9C6FE4;padding:16px 18px;background:#111;border-radius:0 8px 8px 0;">
  <div style="font-size:13px;font-weight:500;color:#9C6FE4;margin-bottom:6px;">The risk is not yet in the GDP signal</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.6);line-height:1.6;">But 2021 alone was 0.23% of GVA. One bad decade could change this picture fast.</div>
</div>
""", unsafe_allow_html=True)

    st.divider()

    # ── BLOCK 5: explanation (left) + MK table (right) ───────
    col_mk_text, col_mk_chart = st.columns([2, 3])

    with col_mk_text:
        st.markdown('<div style="height:44px;"></div>', unsafe_allow_html=True)
        st.markdown("""
<div style="border-left:2px solid #FF7043;padding:16px 18px;background:#111;border-radius:0 8px 8px 0;margin-bottom:10px;">
  <div style="font-size:13px;font-weight:500;color:#E8E8E8;margin-bottom:8px;">Three lenses, three answers</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.6);line-height:1.6;">Nominal (1973–2024): <span style="color:#FF7043;">significant ↑</span><br>Real 2020€ (1991–2024): <span style="color:rgba(232,232,232,0.4);">not significant</span><br>% of GVA (1991–2024): <span style="color:rgba(232,232,232,0.4);">not significant</span></div>
</div>
<div style="border-left:2px solid rgba(232,232,232,0.2);padding:16px 18px;background:#111;border-radius:0 8px 8px 0;">
  <div style="font-size:13px;font-weight:500;color:#E8E8E8;margin-bottom:8px;">Why the window matters</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.6);line-height:1.6;">The nominal trend is partly a window effect — the full 1973–2024 series includes more low-loss years in the 1970s–80s. Restricting to 1991–2024 for real and ratio analysis is the honest choice given the CPI index break at reunification.</div>
</div>
""", unsafe_allow_html=True)

    with col_mk_chart:
        st.markdown('<p style="font-size:20px;font-weight:500;color:#E8E8E8;margin-bottom:4px;">Mann-Kendall trend test results</p>', unsafe_allow_html=True)
        load_fig("03_mann_kendall_summary.html", height=220)

# ============================================================
# CELL 4 — RQ3: WHAT DRIVES LOSSES
# ============================================================

elif section == "📉 RQ3 — What drives losses":

    st.markdown('<span style="background:#FF7043;color:#1a1a1a;font-size:11px;font-weight:600;padding:3px 8px;border-radius:4px;letter-spacing:0.06em;">RQ3</span>', unsafe_allow_html=True)
    st.markdown("## What climate variable drives insured losses?")
    st.markdown('<p style="color:rgba(232,232,232,0.4);margin-top:-10px;font-size:13px;">OLS regression · DWD climate variables · GDV losses 1973–2024 and 1991–2024</p>', unsafe_allow_html=True)

    # ── KPI strip ────────────────────────────────────────────
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Best predictor", "Heavy rain days", "1991–2024 window")
    k2.metric("Coefficient", "+€0.394bn / day", "per extra heavy rain day")
    k3.metric("p-value", "0.020", "significant ✓")
    k4.metric("R²", "0.158", "16% of variance explained")

    st.divider()

    # ── NARRATIVE MOMENT 1 ───────────────────────────────────
    st.markdown("""
<div style="background:#111;border-left:3px solid #9C6FE4;border-radius:0 8px 8px 0;padding:20px 24px;margin-bottom:8px;">
  <div style="font-size:22px;font-weight:500;color:#E8E8E8;line-height:1.4;">We started with the obvious hypothesis.</div>
  <div style="font-size:15px;color:rgba(232,232,232,0.5);margin-top:8px;line-height:1.6;">Warmer temperatures → more extreme weather → higher insured losses. Makes intuitive sense. The data disagreed.</div>
</div>
""", unsafe_allow_html=True)

    st.divider()

    # ── BLOCK 1: Temp scatter (left) + explanation (right) ───
    col_chart, col_facts = st.columns([3, 2])

    with col_chart:
        st.markdown('<p style="font-size:20px;font-weight:500;color:#E8E8E8;margin-bottom:4px;">Temperature anomaly vs insured losses</p>', unsafe_allow_html=True)
        load_fig("04_scatter_temp_vs_losses.html", height=500)

    with col_facts:
        st.markdown('<div style="height:44px;"></div>', unsafe_allow_html=True)
        st.markdown("""
<div style="border-left:2px solid #9C6FE4;padding:12px 14px;background:#111;border-radius:0 8px 8px 0;margin-bottom:10px;">
  <div style="font-size:24px;font-weight:500;color:#9C6FE4;">No pattern</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.6);margin-top:4px;line-height:1.5;">The scatter shows no clear relationship between temperature anomaly and loss magnitude</div>
  <div style="font-size:11px;color:rgba(232,232,232,0.3);margin-top:6px;">1973–2024 · nominal losses</div>
</div>
<div style="border-left:2px solid rgba(232,232,232,0.2);padding:12px 14px;background:#111;border-radius:0 8px 8px 0;margin-bottom:10px;">
  <div style="font-size:24px;font-weight:500;color:#E8E8E8;">2002 · 2013 · 2021</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.6);margin-top:4px;line-height:1.5;">the three largest loss years are flood events — not the hottest years on record</div>
  <div style="font-size:11px;color:rgba(232,232,232,0.3);margin-top:6px;">Elbe flood · Central Europe floods · Ahr valley</div>
</div>
<div style="border-left:2px solid rgba(232,232,232,0.2);padding:12px 14px;background:#111;border-radius:0 8px 8px 0;">
  <div style="font-size:13px;font-weight:500;color:#E8E8E8;margin-bottom:6px;">Already a hint</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.6);line-height:1.5;">The biggest losses cluster around flood years, not heatwave years — suggesting the wrong variable was chosen</div>
</div>
""", unsafe_allow_html=True)

    st.divider()

    # ── BLOCK 2: OLS temp (right) + explanation (left) ───────
    col_text, col_chart2 = st.columns([2, 3])

    with col_text:
        st.markdown('<div style="height:44px;"></div>', unsafe_allow_html=True)
        st.markdown("""
<div style="border-left:2px solid #9C6FE4;padding:16px 18px;background:#111;border-radius:0 8px 8px 0;margin-bottom:10px;">
  <div style="font-size:24px;font-weight:500;color:#9C6FE4;">p = 0.160</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.6);margin-top:4px;line-height:1.5;">temperature anomaly does not significantly predict insured losses</div>
  <div style="font-size:11px;color:rgba(232,232,232,0.3);margin-top:6px;">H₀ not rejected · α = 0.05</div>
</div>
<div style="border-left:2px solid rgba(232,232,232,0.2);padding:16px 18px;background:#111;border-radius:0 8px 8px 0;margin-bottom:10px;">
  <div style="font-size:24px;font-weight:500;color:#E8E8E8;">R² = 0.039</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.6);margin-top:4px;line-height:1.5;">temperature explains less than 4% of the variance in losses</div>
  <div style="font-size:11px;color:rgba(232,232,232,0.3);margin-top:6px;">1973–2024 · OLS</div>
</div>
<div style="border-left:2px solid rgba(232,232,232,0.15);padding:16px 18px;background:#111;border-radius:0 8px 8px 0;">
  <div style="font-size:13px;font-weight:500;color:#E8E8E8;margin-bottom:6px;">Back to the drawing board</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.6);line-height:1.5;">We tested all available DWD climate variables — hot days, tropical nights, frost days, heavy rain days, total precipitation. One stood out.</div>
</div>
""", unsafe_allow_html=True)

    with col_chart2:
        st.markdown('<p style="font-size:20px;font-weight:500;color:#E8E8E8;margin-bottom:4px;">OLS regression — temperature vs losses</p>', unsafe_allow_html=True)
        load_fig("04_ols_temp_vs_losses.html", height=500)

    st.divider()

    # ── BLOCK 3: ALL VARIABLES EXPLORER ──────────────────────
    st.markdown('<p style="font-size:20px;font-weight:500;color:#E8E8E8;margin-bottom:4px;">All 6 climate variables tested against insured losses</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:13px;color:rgba(232,232,232,0.4);margin-top:-8px;margin-bottom:12px;">Full 1973–2024 window · none are significant · but one comes closest</p>', unsafe_allow_html=True)

    col_drop, col_result = st.columns([3, 2])

    with col_drop:
        corr_var = st.selectbox(
            "Select climate variable",
            [
                "Temperature anomaly (°C)",
                "Hot days (≥ 30°C)",
                "Tropical nights (≥ 20°C)",
                "Frost days (≤ 0°C)",
                "Total precipitation (mm)",
                "Heavy rain days",
            ],
            key="rq3_corr",
        )

        corr_map = {
            "Temperature anomaly (°C)"   : ("04_corr_temp_anomaly.html",    "p=0.160 — not significant", "R² = 0.039 — explains 4% of variance"),
            "Hot days (≥ 30°C)"          : ("04_corr_hot_days.html",        "p=0.479 — not significant", "R² = 0.010 — explains 1% of variance"),
            "Tropical nights (≥ 20°C)"   : ("04_corr_tropical_nights.html", "p=0.655 — not significant", "R² = 0.004 — weakest of all"),
            "Frost days (≤ 0°C)"         : ("04_corr_frost_days.html",      "p=0.348 — not significant", "R² = 0.018 — explains 2% of variance"),
            "Total precipitation (mm)"   : ("04_corr_precip_mm.html",       "p=0.243 — not significant", "R² = 0.027 — explains 3% of variance"),
            "Heavy rain days"            : ("04_corr_heavy_rain.html",       "p=0.088 — not significant in full window", "R² = 0.057 — but lowest p-value of all 6 ← hint"),
        }

        fname, result_text, r2_text = corr_map[corr_var]
        load_fig(fname, height=460)

    with col_result:
        st.markdown('<div style="height:44px;"></div>', unsafe_allow_html=True)
        is_hint = corr_var == "Heavy rain days"
        border_color = "#FF7043" if is_hint else "rgba(232,232,232,0.2)"
        val_color = "#FF7043" if is_hint else "rgba(232,232,232,0.5)"

        st.markdown(f"""
<div style="border-left:2px solid {border_color};padding:16px 18px;background:#111;border-radius:0 8px 8px 0;margin-bottom:10px;">
  <div style="font-size:20px;font-weight:500;color:{val_color};">{corr_var}</div>
  <div style="font-size:13px;color:rgba(232,232,232,0.6);margin-top:6px;line-height:1.6;">{result_text}</div>
  <div style="font-size:11px;color:rgba(232,232,232,0.35);margin-top:6px;">{r2_text}</div>
</div>
<div style="border-left:2px solid rgba(232,232,232,0.15);padding:16px 18px;background:#111;border-radius:0 8px 8px 0;margin-bottom:10px;">
  <div style="font-size:13px;font-weight:500;color:#E8E8E8;margin-bottom:8px;">All 6 ranked by p-value</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.6);line-height:1.8;">
    <span style="color:#FF7043;">Heavy rain days: p=0.088</span><br>
    Temperature: p=0.160<br>
    Total precip: p=0.243<br>
    Frost days: p=0.348<br>
    Hot days: p=0.479<br>
    Tropical nights: p=0.655
  </div>
</div>
<div style="border-left:2px solid rgba(232,232,232,0.15);padding:16px 18px;background:#111;border-radius:0 8px 8px 0;">
  <div style="font-size:13px;font-weight:500;color:#E8E8E8;margin-bottom:6px;">Not cherry-picking</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.6);line-height:1.5;">Systematic testing of all available variables. None significant in the full window — but heavy rain days had the strongest signal. That was the lead worth following.</div>
</div>
""", unsafe_allow_html=True)

    st.divider()

    # ── NARRATIVE MOMENT 2 ───────────────────────────────────
    st.markdown("""
<div style="background:#111;border-left:3px solid #FF7043;border-radius:0 8px 8px 0;padding:20px 24px;margin-bottom:8px;">
  <div style="font-size:22px;font-weight:500;color:#E8E8E8;line-height:1.4;">Heavy rain days had the lowest p-value. So we followed the signal.</div>
  <div style="font-size:15px;color:rgba(232,232,232,0.5);margin-top:8px;line-height:1.6;">But the full 1973–2024 window mixes pre- and post-reunification Germany — different insurance markets, different data quality. Restricting to 1991–2024 gives a cleaner, more comparable dataset. And that's where the signal becomes significant.</div>
</div>
""", unsafe_allow_html=True)

    st.divider()

    # ── BLOCK 4: Rain scatter (left) + fact boxes (right) ────
    col_chart3, col_facts2 = st.columns([3, 2])

    with col_chart3:
        st.markdown('<p style="font-size:20px;font-weight:500;color:#E8E8E8;margin-bottom:4px;">Heavy rain days vs insured losses — 1991–2024</p>', unsafe_allow_html=True)
        load_fig("04_scatter_raindays_vs_losses.html", height=500)

    with col_facts2:
        st.markdown('<div style="height:44px;"></div>', unsafe_allow_html=True)
        st.markdown("""
<div style="border-left:2px solid #FF7043;padding:12px 14px;background:#111;border-radius:0 8px 8px 0;margin-bottom:10px;">
  <div style="font-size:24px;font-weight:500;color:#FF7043;">A pattern</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.6);margin-top:4px;line-height:1.5;">More heavy rain days consistently associates with higher insured losses — the relationship is visible in the scatter</div>
  <div style="font-size:11px;color:rgba(232,232,232,0.3);margin-top:6px;">1991–2024 · nominal losses</div>
</div>
<div style="border-left:2px solid rgba(232,232,232,0.2);padding:12px 14px;background:#111;border-radius:0 8px 8px 0;margin-bottom:10px;">
  <div style="font-size:24px;font-weight:500;color:#E8E8E8;">2021</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.6);margin-top:4px;line-height:1.5;">the Ahr valley flood year sits at the top — high rain days, record losses — consistent with the model</div>
  <div style="font-size:11px;color:rgba(232,232,232,0.3);margin-top:6px;">€16.4bn nominal losses</div>
</div>
<div style="border-left:2px solid rgba(232,232,232,0.2);padding:12px 14px;background:#111;border-radius:0 8px 8px 0;">
  <div style="font-size:13px;font-weight:500;color:#E8E8E8;margin-bottom:6px;">Independent from temperature</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.6);line-height:1.5;">Heavy rain days and temperature anomaly are not significantly correlated (r=0.017, p=0.91) — they measure different physical processes</div>
</div>
""", unsafe_allow_html=True)

    st.divider()

    # ── BLOCK 5: explanation (left) + OLS rain (right) ───────
    col_text2, col_chart4 = st.columns([2, 3])

    with col_text2:
        st.markdown('<div style="height:44px;"></div>', unsafe_allow_html=True)
        st.markdown("""
<div style="border-left:2px solid #FF7043;padding:16px 18px;background:#111;border-radius:0 8px 8px 0;margin-bottom:10px;">
  <div style="font-size:24px;font-weight:500;color:#FF7043;">p = 0.020</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.6);margin-top:4px;line-height:1.5;">heavy rain days significantly predict insured losses in the 1991–2024 window</div>
  <div style="font-size:11px;color:rgba(232,232,232,0.3);margin-top:6px;">H₀ rejected · α = 0.05 · 1991–2024</div>
</div>
<div style="border-left:2px solid rgba(232,232,232,0.2);padding:16px 18px;background:#111;border-radius:0 8px 8px 0;margin-bottom:10px;">
  <div style="font-size:24px;font-weight:500;color:#E8E8E8;">+€0.394bn</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.6);margin-top:4px;line-height:1.5;">additional insured losses for every extra heavy rain day per year above the current average</div>
  <div style="font-size:11px;color:rgba(232,232,232,0.3);margin-top:6px;">95% CI: [0.065, 0.723] · OLS</div>
</div>
<div style="border-left:2px solid rgba(232,232,232,0.15);padding:16px 18px;background:#111;border-radius:0 8px 8px 0;">
  <div style="font-size:13px;font-weight:500;color:#E8E8E8;margin-bottom:6px;">R² = 0.158</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.6);line-height:1.5;">16% of variance explained — modest but meaningful for a single-variable model on volatile annual loss data</div>
</div>
""", unsafe_allow_html=True)

    with col_chart4:
        st.markdown('<p style="font-size:20px;font-weight:500;color:#E8E8E8;margin-bottom:4px;">OLS regression — heavy rain days vs losses</p>', unsafe_allow_html=True)
        load_fig("04_ols_raindays_vs_losses.html", height=500)

    st.divider()

    # ── BLOCK 6: model comparison table (right) + explanation (left)
    col_mk_text, col_mk_chart = st.columns([2, 3])

    with col_mk_text:
        st.markdown('<div style="height:44px;"></div>', unsafe_allow_html=True)
        st.markdown("""
<div style="border-left:2px solid #FF7043;padding:16px 18px;background:#111;border-radius:0 8px 8px 0;margin-bottom:10px;">
  <div style="font-size:13px;font-weight:500;color:#E8E8E8;margin-bottom:8px;">All models tested</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.6);line-height:1.8;">
    Temp only (1973–2024): <span style="color:rgba(232,232,232,0.4);">p=0.160 — no</span><br>
    Rain only (1973–2024): <span style="color:rgba(232,232,232,0.4);">p=0.088 — no</span><br>
    Rain only (1991–2024): <span style="color:#FF7043;">p=0.020 — yes ✓</span><br>
    Temp + rain combined: <span style="color:rgba(232,232,232,0.4);">p=0.088 — no</span>
  </div>
</div>
<div style="border-left:2px solid rgba(232,232,232,0.2);padding:16px 18px;background:#111;border-radius:0 8px 8px 0;">
  <div style="font-size:13px;font-weight:500;color:#E8E8E8;margin-bottom:6px;">Why 1991–2024 wins</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.6);line-height:1.5;">The 1991–2024 window aligns climate and economic data post-reunification — consistent insurance market, reliable CPI, comparable loss reporting. That's where the signal becomes significant.</div>
</div>
""", unsafe_allow_html=True)

    with col_mk_chart:
        st.markdown('<p style="font-size:20px;font-weight:500;color:#E8E8E8;margin-bottom:4px;">Model comparison</p>', unsafe_allow_html=True)
        load_fig("04_model_comparison_table.html", height=300)
    st.divider()

    # ── RQ3 CLOSING — bridge to RQ4 ──────────────────────────
    st.markdown("""
<div style="background:#111;border-left:3px solid #FF7043;border-radius:0 8px 8px 0;padding:20px 24px;margin-bottom:10px;">
  <div style="font-size:22px;font-weight:500;color:#E8E8E8;line-height:1.4;">The signal is already in the losses — even before the trend appears in the climate data.</div>
  <div style="font-size:15px;color:rgba(232,232,232,0.5);margin-top:8px;line-height:1.6;">Heavy rain days show no statistically significant upward trend yet (p=0.874). But the three largest insured loss events in German history were all flood events. The regression is already significant. Germany is paying the price of a future that hasn't fully arrived.</div>
</div>
""", unsafe_allow_html=True)

    col_c1, col_c2, col_c3 = st.columns(3)

    with col_c1:
        st.markdown("""
<div style="border-left:2px solid #FF7043;padding:14px 16px;background:#111;border-radius:0 8px 8px 0;height:100%;">
  <div style="font-size:22px;font-weight:500;color:#FF7043;">2002 · 2013 · 2021</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.6);margin-top:6px;line-height:1.5;">Germany's three largest insured loss years — all flood events, not heatwaves</div>
  <div style="font-size:11px;color:rgba(232,232,232,0.3);margin-top:6px;">Elbe · Central Europe · Ahr valley</div>
</div>
""", unsafe_allow_html=True)

    with col_c2:
        st.markdown("""
<div style="border-left:2px solid #9C6FE4;padding:14px 16px;background:#111;border-radius:0 8px 8px 0;height:100%;">
  <div style="font-size:22px;font-weight:500;color:#9C6FE4;">p = 0.874</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.6);margin-top:6px;line-height:1.5;">no significant upward trend in heavy rain days yet — but climate science projects increasing frequency</div>
  <div style="font-size:11px;color:rgba(232,232,232,0.3);margin-top:6px;">Mann-Kendall · 1951–2024 · n=74</div>
</div>
""", unsafe_allow_html=True)

    with col_c3:
        st.markdown("""
<div style="border-left:2px solid rgba(232,232,232,0.2);padding:14px 16px;background:#111;border-radius:0 8px 8px 0;height:100%;">
  <div style="font-size:22px;font-weight:500;color:#E8E8E8;">+€0.394bn</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.6);margin-top:6px;line-height:1.5;">cost of each extra heavy rain day — already measurable, even without a trend in frequency</div>
  <div style="font-size:11px;color:rgba(232,232,232,0.3);margin-top:6px;">OLS 1991–2024 · p=0.020</div>
</div>
""", unsafe_allow_html=True)
# ============================================================
# CELL 5 — RQ4: COST OF INACTION
# ============================================================

elif section == "⚠️ RQ4 — Cost of inaction":

    st.markdown('<span style="background:#FF7043;color:#1a1a1a;font-size:11px;font-weight:600;padding:3px 8px;border-radius:4px;letter-spacing:0.06em;">RQ4</span>', unsafe_allow_html=True)
    st.markdown("## What is Germany doing — and is it enough?")
    st.markdown('<p style="color:rgba(232,232,232,0.4);margin-top:-10px;font-size:13px;">UBA KSG sector emissions 1990–2025 · CAT projections · OLS cost scenarios</p>', unsafe_allow_html=True)

    k1, k2, k3, k4 = st.columns(4)
    k1.metric("2025 emissions", "648.87 Mt", "CO₂eq · UBA")
    k2.metric("KSG target 2030", "438 Mt", "−32% from 2025")
    k3.metric("Current policies", "Off track", "CAT projection")
    k4.metric("Cost per rain day", "+€0.394bn", "OLS coefficient RQ3")

    st.divider()

    col_t, col_i = st.columns([11, 1])
    with col_t:
        st.markdown('<p style="font-size:20px;font-weight:500;color:#E8E8E8;margin-bottom:4px;">Germany\'s emissions pathway vs KSG targets</p>', unsafe_allow_html=True)
    with col_i:
        with st.popover("ℹ️"):
            st.markdown("**Historical:** UBA KSG sector emissions 1990–2025  \n**KSG targets:** legally binding under Klimaschutzgesetz  \n**Current policies:** CAT projection range (midpoint)  \n**Source:** UBA + Climate Action Tracker")
    load_fig("03_ksg_pathway.html", height=520)

    st.divider()

    col_chart, col_facts = st.columns([3, 2])

    with col_chart:
        st.markdown('<p style="font-size:20px;font-weight:500;color:#E8E8E8;margin-bottom:4px;">GHG emissions by KSG sector 1990–2025</p>', unsafe_allow_html=True)
        load_fig("03_uba_emissions_by_sector.html", height=460)

    with col_facts:
        st.markdown('<div style="height:44px;"></div>', unsafe_allow_html=True)
        st.markdown("""
<div style="border-left:2px solid #FF7043;padding:12px 14px;background:#111;border-radius:0 8px 8px 0;margin-bottom:10px;">
  <div style="font-size:22px;font-weight:500;color:#FF7043;">⚡ Energy — on track</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.6);margin-top:4px;line-height:1.5;">Coal phase-out and renewables driving most national progress — from ~470 Mt in 1990 to ~200 Mt in 2025</div>
  <div style="font-size:11px;color:rgba(232,232,232,0.45);margin-top:6px;">Biggest absolute reduction of all sectors</div>
</div>
<div style="border-left:2px solid #9C6FE4;padding:12px 14px;background:#111;border-radius:0 8px 8px 0;margin-bottom:10px;">
  <div style="font-size:22px;font-weight:500;color:#9C6FE4;">🚗 Transport — failing</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.6);margin-top:4px;line-height:1.5;">Only sector with no significant reduction since 1990 — still at ~145 Mt CO₂eq. Gap of 117–191 Mt by 2030</div>
  <div style="font-size:11px;color:rgba(232,232,232,0.45);margin-top:6px;">Source: Independent Council of Experts on Climate Change, 2025</div>
</div>
<div style="border-left:2px solid rgba(232,232,232,0.2);padding:12px 14px;background:#111;border-radius:0 8px 8px 0;">
  <div style="font-size:22px;font-weight:500;color:#E8E8E8;">🏠 Buildings — failing</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.6);margin-top:4px;line-height:1.5;">Fossil fuels still heat 73% of German homes. Heat pump rollout far behind target. Gap of 35 Mt by 2030</div>
  <div style="font-size:11px;color:rgba(232,232,232,0.45);margin-top:6px;">Gas: 56% · Oil: 17% · Heat pumps: only 4% · Source: BDEW 2024</div>
</div>
""", unsafe_allow_html=True)

    st.divider()

    st.markdown("""
<div style="background:#111;border-left:3px solid #9C6FE4;border-radius:0 8px 8px 0;padding:20px 24px;margin-bottom:8px;">
  <div style="font-size:22px;font-weight:500;color:#E8E8E8;line-height:1.4;">The national total looks promising. But look closer.</div>
  <div style="font-size:15px;color:rgba(232,232,232,0.5);margin-top:8px;line-height:1.6;">Energy sector over-performance is masking critical failures in transport and buildings — the two sectors most relevant to everyday emissions and flood infrastructure. The aggregate hides a structural problem.</div>
</div>
""", unsafe_allow_html=True)

    st.divider()

    st.markdown('<p style="font-size:20px;font-weight:500;color:#E8E8E8;margin-bottom:16px;">The two sectors that are failing — in numbers</p>', unsafe_allow_html=True)

    col_b, col_t2, col_e = st.columns(3)

    with col_b:
        st.markdown("""
<div style="background:#111;border:0.5px solid rgba(232,232,232,0.1);border-top:2px solid rgba(232,232,232,0.3);border-radius:0 0 8px 8px;padding:16px;">
  <div style="font-size:12px;font-weight:500;color:rgba(232,232,232,0.45);margin-bottom:12px;letter-spacing:0.05em;">🏠 BUILDINGS</div>
  <div style="font-size:28px;font-weight:500;color:#E8E8E8;margin-bottom:4px;">200k</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.5);margin-bottom:16px;">heat pumps installed in 2024</div>
  <div style="font-size:11px;color:rgba(232,232,232,0.45);padding:8px;background:rgba(255,255,255,0.03);border-radius:4px;line-height:1.8;">
    Target: 500,000 / year<br>
    Actual 2024: ~200,000 (−60%)<br>
    Heat pump share of homes: 4%<br>
    Gas still heats 56% of homes<br>
    CO₂ gap by 2030: ~35 Mt
  </div>
</div>
""", unsafe_allow_html=True)

    with col_t2:
        st.markdown("""
<div style="background:#111;border:0.5px solid rgba(232,232,232,0.1);border-top:2px solid #9C6FE4;border-radius:0 0 8px 8px;padding:16px;">
  <div style="font-size:12px;font-weight:500;color:rgba(232,232,232,0.45);margin-bottom:12px;letter-spacing:0.05em;">🚗 TRANSPORT</div>
  <div style="font-size:28px;font-weight:500;color:#9C6FE4;margin-bottom:4px;">1.65M</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.5);margin-bottom:16px;">EVs on German roads (Jan 2025)</div>
  <div style="font-size:11px;color:rgba(232,232,232,0.45);padding:8px;background:rgba(255,255,255,0.03);border-radius:4px;line-height:1.8;">
    Target: 15 million EVs by 2030<br>
    Actual fleet: 1.65M (11% of target)<br>
    New registrations 2024: 13.5% BEV<br>
    Transport emissions: no trend since 1990<br>
    CO₂ gap by 2030: 117–191 Mt
  </div>
</div>
""", unsafe_allow_html=True)

    with col_e:
        st.markdown("""
<div style="background:#111;border:0.5px solid rgba(232,232,232,0.1);border-top:2px solid #FF7043;border-radius:0 0 8px 8px;padding:16px;">
  <div style="font-size:12px;font-weight:500;color:rgba(232,232,232,0.45);margin-bottom:12px;letter-spacing:0.05em;">⚡ ENERGY</div>
  <div style="font-size:28px;font-weight:500;color:#FF7043;margin-bottom:4px;">−57%</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.5);margin-bottom:16px;">energy sector emissions since 1990</div>
  <div style="font-size:11px;color:rgba(232,232,232,0.45);padding:8px;background:rgba(255,255,255,0.03);border-radius:4px;line-height:1.8;">
    From ~470 Mt (1990) to ~200 Mt (2025)<br>
    Renewables: 59% of electricity in 2024<br>
    Coal phase-out: on track<br>
    But masking failures elsewhere<br>
    EU Effort Sharing gap: 226 Mt 2021–2030
  </div>
</div>
""", unsafe_allow_html=True)

    st.divider()

    col_text, col_chart2 = st.columns([2, 3])

    with col_text:
        st.markdown('<div style="height:44px;"></div>', unsafe_allow_html=True)
        st.markdown("""
<div style="border-left:2px solid #FF7043;padding:16px 18px;background:#111;border-radius:0 8px 8px 0;margin-bottom:10px;">
  <div style="font-size:22px;font-weight:500;color:#FF7043;margin-bottom:6px;">The KSG gap</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.6);line-height:1.6;">Germany's Klimaschutzgesetz sets legally binding sector targets. By 2030 emissions must reach 438 Mt. Current policies project ~550–600 Mt. The gap is over 100 Mt CO₂eq.</div>
</div>
<div style="border-left:2px solid #9C6FE4;padding:16px 18px;background:#111;border-radius:0 8px 8px 0;margin-bottom:10px;">
  <div style="font-size:22px;font-weight:500;color:#9C6FE4;">~150 Mt</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.6);margin-top:4px;line-height:1.5;">estimated gap between current policies and the 1.5°C compatible pathway by 2030</div>
  <div style="font-size:11px;color:rgba(232,232,232,0.45);margin-top:6px;">Source: Climate Action Tracker · July 2025</div>
</div>
<div style="border-left:2px solid rgba(232,232,232,0.2);padding:16px 18px;background:#111;border-radius:0 8px 8px 0;">
  <div style="font-size:22px;font-weight:500;color:#E8E8E8;">Rated "Insufficient"</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.6);margin-top:4px;line-height:1.6;">CAT rates Germany's current climate action as insufficient to meet Paris Agreement goals — progress exists but the pace is too slow</div>
</div>
""", unsafe_allow_html=True)

    with col_chart2:
        st.markdown('<p style="font-size:20px;font-weight:500;color:#E8E8E8;margin-bottom:4px;">Emissions gap — current policies vs targets</p>', unsafe_allow_html=True)
        load_fig("03_emissions_gap.html", height=520)

    st.divider()

    st.markdown("""
<div style="background:#111;border-left:3px solid #FF7043;border-radius:0 8px 8px 0;padding:20px 24px;margin-bottom:8px;">
  <div style="font-size:22px;font-weight:500;color:#E8E8E8;line-height:1.4;">Emissions are falling. Weather losses are not following.</div>
  <div style="font-size:15px;color:rgba(232,232,232,0.5);margin-top:8px;line-height:1.6;">Germany has cut GHG emissions by 48% since 1990. But insured losses from natural hazards have not declined — they have grown. Mitigation addresses the cause. Adaptation addresses the consequence. Germany is doing the first — the second is lagging behind.</div>
</div>
""", unsafe_allow_html=True)

    st.divider()

    col_chart3, col_text2 = st.columns([3, 2])

    with col_chart3:
        st.markdown('<p style="font-size:20px;font-weight:500;color:#E8E8E8;margin-bottom:4px;">Insured losses vs GHG emissions 1991–2024</p>', unsafe_allow_html=True)
        load_fig("03_losses_vs_emissions_dual_axis.html", height=560)

    with col_text2:
        st.markdown('<div style="height:44px;"></div>', unsafe_allow_html=True)
        st.markdown("""
<div style="border-left:2px solid #9C6FE4;padding:12px 14px;background:#111;border-radius:0 8px 8px 0;margin-bottom:10px;">
  <div style="font-size:22px;font-weight:500;color:#9C6FE4;">Emissions ↓</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.6);margin-top:4px;line-height:1.5;">GHG emissions fallen consistently — Tau=−0.940, p&lt;0.001 — one of the strongest trends in this entire study</div>
  <div style="font-size:11px;color:rgba(232,232,232,0.45);margin-top:6px;">Mann-Kendall · UBA 1990–2025</div>
</div>
<div style="border-left:2px solid #FF7043;padding:12px 14px;background:#111;border-radius:0 8px 8px 0;margin-bottom:10px;">
  <div style="font-size:22px;font-weight:500;color:#FF7043;">Losses ↑</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.6);margin-top:4px;line-height:1.5;">nominal insured losses growing in the same period — diverging from the emissions curve. The adaptation gap is widening.</div>
  <div style="font-size:11px;color:rgba(232,232,232,0.45);margin-top:6px;">GDV 1991–2024 · nominal</div>
</div>
<div style="border-left:2px solid rgba(232,232,232,0.2);padding:12px 14px;background:#111;border-radius:0 8px 8px 0;">
  <div style="font-size:22px;font-weight:500;color:#E8E8E8;">Two problems</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.6);margin-top:4px;line-height:1.5;">Cutting emissions addresses the cause. Adapting infrastructure addresses the consequence. Germany is investing in the first — the second is receiving far less attention.</div>
</div>
""", unsafe_allow_html=True)

    st.divider()

    col_cost, col_kpi = st.columns([2, 3])

    with col_cost:
        st.markdown('<div style="height:44px;"></div>', unsafe_allow_html=True)
        st.markdown("""
<div style="border-left:2px solid #FF7043;padding:16px 18px;background:#111;border-radius:0 8px 8px 0;margin-bottom:10px;">
  <div style="font-size:22px;font-weight:500;color:#FF7043;margin-bottom:6px;">How to read this</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.6);line-height:1.6;">Each extra heavy rain day above the current average costs Germany an estimated €0.394bn in insured losses per year. Conservative floor estimate — insured property only.</div>
</div>
<div style="border-left:2px solid rgba(232,232,232,0.2);padding:16px 18px;background:#111;border-radius:0 8px 8px 0;margin-bottom:10px;">
  <div style="font-size:22px;font-weight:500;color:#E8E8E8;">Insured only</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.6);margin-top:4px;line-height:1.5;">uninsured damage, infrastructure, agriculture and health costs not included — total economic losses typically 2–3× insured losses</div>
  <div style="font-size:11px;color:rgba(232,232,232,0.45);margin-top:6px;">Source: OLS model NB04 · 1991–2024</div>
</div>
<div style="border-left:2px solid #9C6FE4;padding:16px 18px;background:#111;border-radius:0 8px 8px 0;">
  <div style="font-size:22px;font-weight:500;color:#9C6FE4;">+4 days/yr</div>
  <div style="font-size:12px;color:rgba(232,232,232,0.6);margin-top:4px;line-height:1.5;">would add ~€1.58bn in annual insured losses — potentially €3–5bn total economic losses including uninsured damage</div>
</div>
""", unsafe_allow_html=True)

    with col_kpi:
        st.markdown('<p style="font-size:20px;font-weight:500;color:#E8E8E8;margin-bottom:4px;">Cost of inaction — projected additional losses</p>', unsafe_allow_html=True)
        load_fig("03_cost_of_inaction_kpi.html", height=420)