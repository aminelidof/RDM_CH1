import streamlit as st
import matplotlib.pyplot as plt

def load_css():
    st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stMetric { background-color: #1c1f26; border: 1px solid #30363d; border-radius: 10px; padding: 15px; }
    .course-card { background: #161b22; padding: 25px; border-radius: 15px; border-left: 5px solid #58a6ff; margin-bottom: 20px; border: 1px solid #30363d; }
    </style>
    """, unsafe_allow_html=True)

def plot_diagram(x, y, title, unit, color):
    fig, ax = plt.subplots(figsize=(10, 3.5))
    ax.plot(x, y, color=color, linewidth=2.5)
    ax.fill_between(x, y, color=color, alpha=0.2)
    ax.axhline(0, color="white", linewidth=1)
    ax.set_facecolor("#0e1117")
    fig.patch.set_facecolor("#0e1117")
    ax.set_title(title, color="white", fontsize=14, fontweight='bold')
    ax.tick_params(colors='white', labelsize=9)
    ax.grid(True, alpha=0.1, linestyle='--')
    return fig