import streamlit as st
import numpy as np
from engine import RDMEngine
from ui_utils import plot_diagram

def run(type_diag, key_suffix=""):
    st.header(f"📊 Analyse : Diagramme {type_diag}")
    
    col_p1, col_p2, col_p3 = st.columns(3)
    with col_p1: 
        L = st.slider("Longueur (m)", 1.0, 50.0, 12.0, key=f"L_{type_diag}_{key_suffix}")
    
    with col_p2:
        # On adapte le libellé selon le type de diagramme
        label_f = "Force Axiale (kN)" if type_diag == "N" else "Force Verticale (kN)"
        F = st.number_input(label_f, value=150.0, key=f"F_{type_diag}_{key_suffix}")
    
    with col_p3: 
        pos = st.slider("Position (m)", 0.0, L, L/3, key=f"pos_{type_diag}_{key_suffix}")

    engine = RDMEngine(L)
    
    # LOGIQUE SELON LE TYPE
    if type_diag == "N":
        # Pour l'effort normal, on simule une charge axiale
        # On génère un tableau de l'effort N : de 0 à 'pos', l'effort est F (traction/compression)
        x = np.linspace(0, L, 500)
        # N est présent uniquement entre l'appui fixe (0) et le point d'application (pos)
        N_vals = np.where(x <= pos, -F, 0) # -F pour compression par défaut
        
        st.subheader("Diagnostic des Réactions Axiales")
        st.metric("Réaction Horizontale Ha", f"{F:.2f} kN")
        st.pyplot(plot_diagram(x, N_vals, "Effort Normal (N)", "kN", "#00ffaa"))
        
    else:
        # Logique standard pour T et M (Charges verticales)
        engine.add_point_load(F, pos)
        x, V, M, (Ra, Rb) = engine.solve()

        st.subheader("Diagnostic des Réactions")
        c1, c2, c3 = st.columns(3)
        c1.metric("Réaction A (Ry)", f"{Ra:.2f} kN")
        c2.metric("Réaction B (Ry)", f"{Rb:.2f} kN")
        c3.metric("Moment Max", f"{np.max(np.abs(M)):.2f} kNm")

        if type_diag == "T":
            st.pyplot(plot_diagram(x, V, "Effort Tranchant (T)", "kN", "#00d4ff"))
        elif type_diag == "M":
            st.pyplot(plot_diagram(x, M, "Moment Fléchissant (M)", "kNm", "#ff4b4b"))

    st.subheader("Analyse Ingénieur")
    st.info(f"Vérifiez la stabilité locale au point x = {pos:.2f} m.")