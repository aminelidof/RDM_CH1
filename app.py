import streamlit as st
from ui_utils import load_css
from modules import accueil, appuis, pfs, theorie_ntm, compression, exercice_cours, exercices_ntm, diagrammes

# Configuration
st.set_page_config(page_title="Cours RDM - FODIL", layout="wide", page_icon="🏗️")
load_css()

# Menu ordonné selon votre demande
st.sidebar.title("🏗️ Cours RDM - FODIL")

# --- AJOUT DE VOS INFORMATIONS PERSONNELLES ---
st.sidebar.markdown("""
<div style="background-color: #1e2130; padding: 15px; border-radius: 10px; border-left: 5px solid #00d4ff; margin-bottom: 20px;">
    <h3 style="margin-top:0; color: #00d4ff; font-size: 18px;">👤 Informations</h3>
    <p style="margin: 2px 0; font-size: 14px;"><strong>Nom :</strong> FODIL</p>
    <p style="margin: 2px 0; font-size: 14px;"><strong>Grade :</strong> M.C.A</p>
    <p style="margin: 2px 0; font-size: 14px;"><strong>Univ :</strong> Centre Universitaire Maghnia</p>
    <p style="margin: 2px 0; font-size: 14px;"><strong>Tel :</strong> +213 550 13 99 87</p>
    <p style="margin: 2px 0; font-size: 14px;"><strong>Mail :</strong> fodilmedam@gmail.com</p>
</div>
""", unsafe_allow_html=True)

menu = {
    "🏠 Accueil": "accueil",
    "⚙️ Appuis": "appuis",
    "⚖️ PFS": "pfs",
    "📚 Théorie NTM": "theorie",
    "📉 Compression / Traction": "compression", 
    "📝 Cisaillement / Flexion": "exercice_cours",
    "📚 Exercices NTM": "exercices_ntm", 
    "🔹 Diagramme N": "diag_n",
    "🔹 Diagramme T": "diag_t",
    "🔹 Diagramme M": "diag_m",
    "🚀 Simulateur Universel": "sim"
}

selection = st.sidebar.radio("Navigation", list(menu.keys()))

# Logique d'affichage
if selection == "🏠 Accueil":
    accueil.run()
elif selection == "⚙️ Appuis":
    appuis.run()
elif selection == "⚖️ PFS":
    pfs.run()
elif selection == "📉 Compression / Traction":
    compression.run()
elif selection == "📚 Théorie NTM":
    theorie_ntm.run()
elif selection == "🔹 Diagramme N":
    diagrammes.run("N", key_suffix="solo")
elif selection == "🔹 Diagramme T":
    diagrammes.run("T", key_suffix="solo")
elif selection == "🔹 Diagramme M":
    diagrammes.run("M", key_suffix="solo")
elif selection == "📝 Cisaillement / Flexion":
    exercice_cours.run()
elif selection == "📚 Exercices NTM":
    exercices_ntm.run()
elif selection == "🚀 Simulateur Universel":
    st.title("🚀 Simulateur Multi-Vues")
    diagrammes.run("T", key_suffix="sim_t")
    st.divider()
    diagrammes.run("M", key_suffix="sim_m")

st.sidebar.markdown("---")
st.sidebar.caption("© 2026 - Expertise RDM")