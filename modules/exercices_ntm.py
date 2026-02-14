import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import os

def run():
    st.title("📚 Exercices Corrigés : Diagrammes NTM")
    st.sidebar.info("Utilisez le menu déroulant pour choisir un exercice spécifique.")
    
    choix = st.selectbox("Choisissez un exercice à étudier", [
        "Ex 1 : Traction (Barre à sections variables)",
        "Ex 2 : Flexion (Poutre simple - Charge répartie)",
        "Ex 3 : Console (Charge ponctuelle)",
        "Ex 4 : Flexion (Charge centrée)",
        "Ex 5 : Cas Combiné (PFS + NTM)"
    ])

    base_path = os.path.dirname(__file__)

    # --- EXERCICE 1 : TRACTION ---
    if choix == "Ex 1 : Traction (Barre à sections variables)":
        st.subheader("📍 Énoncé : Barre à sections variables (Traction)")
        img_path = os.path.join(base_path, "exercice1.png")

        if os.path.exists(img_path):
            st.image(img_path, caption="Géométrie de la barre et sollicitations", use_container_width=True)
        else:
            st.warning("⚠️ Image 'exercice1.png' introuvable.")

        

        st.markdown("**Données :** $F = 20\ kN$ ; $D = 12\ mm$ ; $L = 200\ mm$.")

        with st.expander("✅ Voir la correction détaillée (N, σ)"):
            st.info("### 1. Efforts Normaux (N)")
            st.latex(rf"N_1 = 40 \text{{ kN}} \text{ (Zone [0, L])}")
            st.latex(rf"N_2 = 20 \text{{ kN}} \text{ (Zone [L, 2L])}")
            
            st.info("### 2. Contraintes")
            st.latex(rf"\sigma_1 = \frac{{N_1}}{{S_1}} = 157.2 \text{{ MPa}}")
            st.latex(rf"\sigma_2 = \frac{{N_2}}{{S_2}} = 176.8 \text{{ MPa}}")

    # --- EXERCICE 2 : FLEXION RÉPARTIE ---
    elif choix == "Ex 2 : Flexion (Poutre simple - Charge répartie)":
        st.subheader("📍 Énoncé : Poutre bi-appuyée avec charge uniforme")
        col_d1, col_d2 = st.columns(2)
        with col_d1: L = st.number_input("Longueur L (m)", value=4.0, step=0.5)
        with col_d2: q = st.number_input("Charge q (kN/m)", value=5.0, step=1.0)

        

        Ra = Rb = (q * L) / 2
        
        with st.expander("✅ Voir la correction détaillée (NTM)"):
            st.latex(rf"V(x) = {Ra} - {q}x")
            st.latex(rf"M(x) = {Ra}x - \frac{{{q}x^2}}{{2}}")
            
            x_p = np.linspace(0, L, 100)
            fig, ax = plt.subplots(2, 1, figsize=(8, 6))
            ax[0].plot(x_p, Ra - q*x_p, color='#00d4ff')
            ax[0].set_title("Effort Tranchant V (kN)")
            ax[1].plot(x_p, Ra*x_p - (q*x_p**2)/2, color='#ff4b4b')
            ax[1].set_title("Moment Fléchissant M (kNm)")
            st.pyplot(fig)

    # --- EXERCICE 3 : CONSOLE ---
    elif choix == "Ex 3 : Console (Charge ponctuelle)":
        st.subheader("📍 Énoncé : Poutre en console (Encastrée)")
        col1, col2 = st.columns(2)
        with col1: L_c = st.slider("Longueur (m)", 1.0, 10.0, 3.0)
        with col2: F_c = st.slider("Force (kN)", 1, 100, 20)

        

        with st.expander("✅ Voir la correction détaillée"):
            st.latex(rf"R_{{Ay}} = {F_c} \text{{ kN}}")
            st.latex(rf"M_A = -{F_c} \times {L_c} = -{F_c * L_c} \text{{ kNm}}")
            
            x_c = np.linspace(0, L_c, 100)
            fig_c, ax_c = plt.subplots(2, 1, figsize=(8, 6))
            ax_c[0].fill_between(x_c, [F_c]*100, color='#00d4ff', alpha=0.3)
            ax_c[1].fill_between(x_c, -F_c*(L_c - x_c), color='#ff4b4b', alpha=0.3)
            st.pyplot(fig_c)

    # --- EXERCICE 4 : CHARGE CENTRÉE ---
    elif choix == "Ex 4 : Flexion (Charge centrée)":
        st.subheader("📍 Énoncé : Poutre simple avec force au milieu")
        col3, col4 = st.columns(2)
        with col3: L_f = st.number_input("L (m)", value=6.0)
        with col4: P_f = st.number_input("P (kN)", value=40.0)
        
        

        with st.expander("✅ Voir la correction détaillée"):
            Ra_f = P_f / 2
            st.latex(rf"M_{{max}} = \frac{{P \cdot L}}{{4}} = {P_f*L_f/4} \text{{ kNm}}")
            
            x_f = np.linspace(0, L_f, 100)
            v_f = np.where(x_f < L_f/2, Ra_f, -Ra_f)
            m_f = np.where(x_f < L_f/2, Ra_f * x_f, Ra_f * (L_f - x_f))
            fig_f, ax_f = plt.subplots(2, 1, figsize=(8, 6))
            ax_f[0].step(x_f, v_f, color='#00d4ff')
            ax_f[1].plot(x_f, m_f, color='#ff4b4b')
            st.pyplot(fig_f)

    # --- EXERCICE 5 : CAS COMBINÉ ---
    elif choix == "Ex 5 : Cas Combiné (PFS + NTM)":
        st.subheader("📍 Étude Approfondie : Poutre avec charges mixtes")
        img_path = os.path.join(base_path, "Ex4.png") 

        if os.path.exists(img_path):
            st.image(img_path, caption="Schéma statique", use_container_width=True)       

        L1, L2, L3 = 6.0, 2.0, 2.0
        L_tot = L1 + L2 + L3
        q, F = 20.0, 40.0
        dist_F = L1 + L2 

        Rq = q * L1
        Rb = (Rq * (L1/2) + F * dist_F) / L_tot
        Ra = (Rq + F) - Rb
        x0 = Ra / q
        Mmax = Ra * x0 - (q * x0**2) / 2

        st.markdown(f"""
        <div style="background-color: #111; padding: 15px; border-radius: 10px; border-left: 5px solid #00d4ff; color: white;">
            <b>Données de l'exercice :</b><br>
            • $q = {q} \text{{ kN/m}}$ sur $[0, 6]$<br>
            • $F = {F} \text{{ kN}}$ à $x = 8\text{{m}}$<br>
            • Réactions : $R_A = {Ra:.2f} \text{{ kN}}$, $R_B = {Rb:.2f} \text{{ kN}}$
        </div>
        """, unsafe_allow_html=True)

        tab_diag, tab_sol = st.tabs(["📊 Diagrammes NTM", "📝 Résolution Détaillée"])

        with tab_diag:
            x = np.linspace(0, L_tot, 1000)
            V_vals, M_vals = [], []
            for val in x:
                if val <= L1:
                    v, m = Ra - q * val, Ra * val - (q * val**2) / 2
                elif val <= dist_F:
                    v, m = Ra - Rq, Ra * val - Rq * (val - L1/2)
                else:
                    v, m = Ra - Rq - F, Ra * val - Rq * (val - L1/2) - F * (val - dist_F)
                V_vals.append(v)
                M_vals.append(m)

            fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
            plt.style.use('dark_background')
            ax1.plot(x, V_vals, color='#00d4ff', lw=2)
            ax1.fill_between(x, V_vals, color='#00d4ff', alpha=0.1)
            ax1.set_title("Effort Tranchant V (kN)")
            
            ax2.plot(x, M_vals, color='#ff4b4b', lw=2)
            ax2.fill_between(x, M_vals, color='#ff4b4b', alpha=0.1)
            ax2.invert_yaxis()
            ax2.set_title("Moment Fléchissant M (kNm)")
            st.pyplot(fig)

        with tab_sol:
            st.info("### 1. Équilibre Statique")
            st.latex(rf"R_B = \frac{{({Rq} \cdot 3) + ({F} \cdot 8)}}{{10}} = {Rb:.2f} \text{{ kN}}")
            st.info("### 2. Moment Maximum")
            st.write(f"V(x) s'annule à $x = {x0:.2f} \text{{ m}}$")
            st.latex(rf"M_{{max}} = {Mmax:.2f} \text{{ kNm}}")

        st.table({
            "Position x (m)": ["0 (A)", f"{x0:.2f}", "6 (C)", "8 (D)", "10 (B)"],
            "V (kN)": [f"{Ra:.2f}", "0.00", f"{Ra-Rq:.2f}", f"{Ra-Rq-F:.2f}", f"{-Rb:.2f}"],
            "M (kNm)": ["0.00", f"{Mmax:.2f}", f"{Ra*6-360:.2f}", f"{Ra*8-600:.2f}", "0.00"]
        })

    if st.button("📖 Retour au menu théorique"):
        st.session_state.nav_menu = "📝 Cisaillement / Flexion"
        st.rerun()
