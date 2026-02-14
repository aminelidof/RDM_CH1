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

    # --- CHEMIN DYNAMIQUE POUR LES IMAGES (ROBUSTE POUR GITHUB) ---
    base_path = os.path.dirname(__file__)

    # --- EXERCICE 1 : TRACTION ---
    if choix == "Ex 1 : Traction (Barre à sections variables)":
        st.subheader("📍 Énoncé : Barre à sections variables (Traction)")
        
        img_path_ex1 = os.path.join(base_path, "Ex1.png")
        if os.path.exists(img_path_ex1):
            st.image(img_path_ex1, caption="Géométrie de la barre et sollicitations", use_container_width=True)
        else:
            st.warning("⚠️ Image 'Ex1.png' non trouvée dans le dossier modules.")

        st.markdown("**Données :** $F = 20\ kN$ ; $D = 12\ mm$ ; $L = 200\ mm$ ; $E = 200\ GPa$.")

        

        with st.expander("✅ Voir la correction détaillée (N, σ et ΔL)"):
            st.markdown("""
            **1. Efforts Normaux (N) :**
            - **Zone 1 [0, L]** : $N_1 = 2F = 40\ kN$ (Traction)
            - **Zone 2 [L, 1.5L]** : $N_2 = 2F - F = 20\ kN$
            - **Zone 3 [1.5L, 2L]** : $N_3 = F = 20\ kN$

            **2. Contraintes (σ = N/S) :**
            - $S_1 = \pi(1.5D)^2 / 4 = 254.5\ mm^2 \implies \sigma_1 = 157.2\ MPa$
            - $S_2 = \pi D^2 / 4 = 113.1\ mm^2 \implies \sigma_2 = 176.8\ MPa$
            """)

    # --- EXERCICE 2 : FLEXION RÉPARTIE ---
    elif choix == "Ex 2 : Flexion (Poutre simple - Charge répartie)":
        st.subheader("📍 Énoncé : Poutre bi-appuyée avec charge uniforme")
        col_d1, col_d2 = st.columns(2)
        with col_d1: L = st.number_input("Longueur L (m)", value=4.0, step=0.5, key="L2")
        with col_d2: q = st.number_input("Charge q (kN/m)", value=5.0, step=1.0, key="q2")

        Ra = Rb = (q * L) / 2
        Mmax = (q * L**2) / 8

        

[Image of a simply supported beam with a uniformly distributed load]


        with st.expander("✅ Voir la correction détaillée (NTM)"):
            st.latex(rf"V(x) = {Ra} - {q}x \quad | \quad M(x) = {Ra}x - \frac{{{q}x^2}}{{2}}")
            
            x_p = np.linspace(0, L, 100)
            fig, ax = plt.subplots(2, 1, figsize=(8, 6))
            plt.subplots_adjust(hspace=0.5)
            
            ax[0].plot(x_p, Ra - q*x_p, color='#00d4ff', lw=2)
            ax[0].axhline(0, color='white', lw=1, alpha=0.5)
            ax[0].set_title("Effort Tranchant V (kN)")
            ax[0].grid(True, alpha=0.2)
            
            ax[1].plot(x_p, Ra*x_p - (q*x_p**2)/2, color='#ff4b4b', lw=2)
            ax[1].axhline(0, color='white', lw=1, alpha=0.5)
            ax[1].set_title("Moment Fléchissant M (kNm)")
            ax[1].grid(True, alpha=0.2)
            
            st.pyplot(fig)

    # --- EXERCICE 3 : CONSOLE ---
    elif choix == "Ex 3 : Console (Charge ponctuelle)":
        st.subheader("📍 Énoncé : Poutre en console (Encastrée)")
        col1, col2 = st.columns(2)
        with col1: L_c = st.slider("Longueur (m)", 1.0, 10.0, 3.0, key="L3")
        with col2: F_c = st.slider("Force à l'extrémité (kN)", 1, 100, 20, key="F3")
        
        

        with st.expander("✅ Voir la correction détaillée"):
            st.markdown(f"""
            **1. Réactions à l'encastrement (x=0) :**
            - $R_{{Ay}} = F = {F_c}\ kN$
            - $M_A = -F \cdot L = -{F_c * L_c}\ kNm$ (Moment horaire)
            
            **2. Équations :**
            - $V(x) = {F_c}\ kN$ (Constant)
            - $M(x) = -{F_c}({L_c} - x)$
            """)
            
            x_c = np.linspace(0, L_c, 100)
            fig_c, ax_c = plt.subplots(2, 1, figsize=(8, 6))
            plt.subplots_adjust(hspace=0.5)
            
            ax_c[0].fill_between(x_c, [F_c]*100, color='#00d4ff', alpha=0.3)
            ax_c[0].set_title("Effort Tranchant V (kN)")
            ax_c[0].grid(True, alpha=0.2)
            
            ax_c[1].fill_between(x_c, -F_c*(L_c - x_c), color='#ff4b4b', alpha=0.3)
            ax_c[1].set_title("Moment Fléchissant M (kNm)")
            ax_c[1].grid(True, alpha=0.2)
            
            st.pyplot(fig_c)

    # --- EXERCICE 4 : CHARGE CENTRÉE ---
    elif choix == "Ex 4 : Flexion (Charge centrée)":
        st.subheader("📍 Énoncé : Poutre simple avec force au milieu")
        col3, col4 = st.columns(2)
        with col3: L_f = st.number_input("L (m)", value=6.0, key="L4")
        with col4: P_f = st.number_input("P (kN)", value=40.0, key="P4")

        

        with st.expander("✅ Voir la correction détaillée"):
            Ra_f = P_f / 2
            st.write(f"Réactions : $R_A = R_B = {Ra_f}\ kN$")
            st.latex(rf"M_{{max}} = \frac{{P \cdot L}}{{4}} = \frac{{{P_f} \cdot {L_f}}}{{4}} = {P_f*L_f/4}\ kNm")
            
            x_f = np.linspace(0, L_f, 100)
            v_f = np.where(x_f < L_f/2, Ra_f, -Ra_f)
            m_f = np.where(x_f < L_f/2, Ra_f * x_f, Ra_f * (L_f - x_f))
            
            fig_f, ax_f = plt.subplots(2, 1, figsize=(8, 6))
            plt.subplots_adjust(hspace=0.5)
            ax_f[0].step(x_f, v_f, where='post', color='#00d4ff', lw=2)
            ax_f[0].set_title("Effort Tranchant V (kN)")
            ax_f[1].plot(x_f, m_f, color='#ff4b4b', lw=2)
            ax_f[1].set_title("Moment Fléchissant M (kNm)")
            st.pyplot(fig_f)

    # --- EXERCICE 5 : CAS COMPLET ---
    elif choix == "Ex 5 : Cas Combiné (PFS + NTM)":
        st.subheader("📍 Étude d'une poutre avec charges combinées")

        img_path_ex5 = os.path.join(base_path, "Ex3.png") # Utilisant votre schéma Ex3
        if os.path.exists(img_path_ex5):
            st.image(img_path_ex5, caption="Géométrie de la barre et sollicitations", use_container_width=True)
        else:
            st.warning("⚠️ Image 'Ex3.png' non trouvée.")

        # Données de l'exercice
        L_tot, q_val, Q_val, pos_Q = 10.0, 20.0, 40.0, 8.0
        Rb = ((20 * 6 * 3) + (40 * 8)) / 10.0
        Ra = (20 * 6 + 40) - Rb

        st.info(f"**Configuration :** Poutre $L={L_tot}m$ | Charge $q={q_val}kN/m$ | Charge $Q={Q_val}kN$ à $x=8m$")

        c1, c2 = st.columns(2)
        c1.metric("Réaction d'appui A ($R_A$)", f"{Ra:.2f} kN")
        c2.metric("Réaction d'appui B ($R_B$)", f"{Rb:.2f} kN")

        with st.expander("📊 Voir le tableau des valeurs clés", expanded=True):
            data = {
                "Position x (m)": ["0 (Appui A)", "6 (Fin charge q)", "8 (Charge Q)", "10 (Appui B)"],
                "Effort Tranchant V (kN)": [f"{Ra:.2f}", f"{Ra - 120:.2f}", f"{Ra - 120:.2f} / {Ra - 160:.2f}", f"{-Rb:.2f}"],
                "Moment M (kNm)": ["0", f"{Ra*6 - 360:.2f}", f"{Ra*8 - 120*5:.2f}", "0"]
            }
            st.table(data)

        # Diagrammes robustes
        x = np.linspace(0, L_tot, 500)
        V = np.piecewise(x, [x <= 6, (x > 6) & (x <= 8), x > 8], 
                        [lambda x: Ra - 20*x, lambda x: Ra - 120, lambda x: Ra - 160])
        M = np.piecewise(x, [x <= 6, (x > 6) & (x <= 8), x > 8],
                        [lambda x: Ra*x - 10*x**2, lambda x: Ra*x - 120*(x-3), lambda x: Ra*x - 120*(x-3) - 40*(x-8)])

        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
        plt.subplots_adjust(hspace=0.4)
        ax1.plot(x, V, color='#00d4ff', lw=2); ax1.set_ylabel("V (kN)"); ax1.grid(True, alpha=0.2)
        ax1.axhline(0, color='white', lw=1, alpha=0.5)
        
        ax2.plot(x, M, color='#ff4b4b', lw=2); ax2.set_ylabel("M (kNm)"); ax2.grid(True, alpha=0.2)
        ax2.axhline(0, color='white', lw=1, alpha=0.5)
        ax2.invert_yaxis()
        st.pyplot(fig)

        st.divider()
        if st.button("👉 Ouvrir la correction détaillée"):
            st.session_state.nav_menu = "📝 Cisaillement / Flexion" 
            st.rerun()
