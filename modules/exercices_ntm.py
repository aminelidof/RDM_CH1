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

    # --- EXERCICE 1 : TRACTION ---
    if choix == "Ex 1 : Traction (Barre à sections variables)":
        st.subheader("📍 Énoncé : Barre à sections variables (Traction)")
        
        base_path = os.path.dirname(__file__)
        img_path = os.path.join(base_path, "exercice1.png")

        try:
            if os.path.exists(img_path):
                st.image(img_path, caption="Géométrie de la barre et sollicitations", use_container_width=True)
            else:
                st.warning("⚠️ Fichier 'exercice1.png' introuvable dans le dossier 'modules'.")
        except Exception as e:
            st.error(f"Erreur lors du chargement : {e}")

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
        with col_d1: L = st.number_input("Longueur L (m)", value=4.0, step=0.5)
        with col_d2: q = st.number_input("Charge q (kN/m)", value=5.0, step=1.0)

        Ra = Rb = (q * L) / 2
        
        with st.expander("✅ Voir la correction détaillée (NTM)"):
            st.latex(rf"V(x) = {Ra} - {q}x \quad | \quad M(x) = {Ra}x - \frac{{{q}x^2}}{{2}}")
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
        with col2: F_c = st.slider("Force à l'extrémité (kN)", 1, 100, 20)

        with st.expander("✅ Voir la correction détaillée"):
            st.markdown(f"""
            **1. Réactions à l'encastrement (x=0) :**
            - $R_{{Ay}} = F = {F_c}\ kN$
            - $M_A = -F \cdot L = -{F_c * L_c}\ kNm$
            
            **2. Équations :**
            - $V(x) = {F_c}\ kN$
            - $M(x) = -{F_c}({L_c} - x)$
            """)
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
            st.write(f"Réactions : $R_A = R_B = {Ra_f}\ kN$")
            st.latex(rf"M_{{max}} = \frac{{{P_f} \cdot {L_f}}}{{4}} = {P_f*L_f/4}\ kNm")
            x_f = np.linspace(0, L_f, 100)
            v_f = np.where(x_f < L_f/2, Ra_f, -Ra_f)
            m_f = np.where(x_f < L_f/2, Ra_f * x_f, Ra_f * (L_f - x_f))
            fig_f, ax_f = plt.subplots(2, 1, figsize=(8, 6))
            ax_f[0].step(x_f, v_f, color='#00d4ff')
            ax_f[1].plot(x_f, m_f, color='#ff4b4b')
            st.pyplot(fig_f)
# --- EXERCICE 5 : CAS COMBINÉ (VERSION PRO) ---
    elif choix == "Ex 5 : Cas Combiné (PFS + NTM)":
        st.subheader("📍 Étude Approfondie : Poutre Iso-statique avec charges mixtes")

        base_path = os.path.dirname(__file__)
        img_path = os.path.join(base_path, "Ex4.png")

        if os.path.exists(img_path):
            st.image(img_path, caption="Schéma statique : Charge répartie + Charge ponctuelle", use_container_width=True)
        else:
            st.error("❌ Image 'Ex4.png' introuvable.")

        # --- PARAMÈTRES ---
        L1, L2, L3 = 6.0, 2.0, 2.0
        L_tot = L1 + L2 + L3
        q, F = 20.0, 40.0
        dist_F = L1 + L2 

        # --- CALCULS ---
        Rq = q * L1
        Rb = (Rq * (L1/2) + F * dist_F) / L_tot
        Ra = (Rq + F) - Rb
        x0 = Ra / q
        Mmax = Ra * x0 - (q * x0**2) / 2 if x0 <= L1 else 0

        # --- INTERFACE ---
        tab_pfs, tab_equa, tab_diag = st.tabs(["⚖️ 1. Équilibre (PFS)", "✂️ 2. Équations (Coupures)", "📊 3. Diagrammes"])

        with tab_pfs:
            st.markdown("### 1.1 Modélisation de la charge répartie")
            st.write("On remplace la charge répartie $q$ par sa résultante $R_q$ agissant au centre de gravité du rectangle (à 3m de A).")
            st.latex(rf"R_q = q \times L_1 = {q} \times {L1} = {Rq} \text{{ kN}}")

            st.markdown("### 1.2 Calcul des réactions aux appuis")
            st.write("On applique le Principe Fondamental de la Statique (PFS) :")
            
            st.latex(rf"\sum M_{{/A}} = 0 \implies (R_q \times 3) + (F \times 8) - (R_B \times 10) = 0")
            st.latex(rf"R_B = \frac{{{Rq} \times 3 + {F} \times 8}}{{10}} = \mathbf{{{Rb:.2f} \text{{ kN}}}}")
            
            st.latex(rf"\sum F_y = 0 \implies R_A + R_B - R_q - F = 0")
            st.latex(rf"R_A = {Rq} + {F} - {Rb:.2f} = \mathbf{{{Ra:.2f} \text{{ kN}}}}")

        with tab_equa:
            st.markdown("### Analyse par tronçons")
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("<h4 style='color: #ff4b4b;'>Zone I : $x \in [0, 6]$</h4>", unsafe_allow_html=True)
                st.latex(rf"V(x) = R_A - qx = {Ra:.2f} - 20x")
                st.latex(rf"M(x) = R_A x - \frac{{qx^2}}{{2}} = {Ra:.2f}x - 10x^2")
                st.write(f"**Extrémité C (x=6) :** $M(6) = {Ra*6-10*36:.2f} \text{{ kNm}}$")

            with col2:
                st.markdown("<h4 style='color: #ff4b4b;'>Zone II : $x \in [6, 8]$</h4>", unsafe_allow_html=True)
                st.latex(rf"V(x) = R_A - R_q = {Ra-Rq:.2f} \text{{ kN}}")
                st.latex(rf"M(x) = R_A x - R_q(x - 3)")
                st.write(f"**Extrémité D (x=8) :** $M(8) = {Ra*8-Rq*5:.2f} \text{{ kNm}}$")

            st.divider()
            st.success(f"🔍 **Point critique :** L'effort tranchant s'annule à $x_0 = R_A/q = {x0:.2f} \text{{ m}}$.")
            st.latex(rf"M_{{max}} = M({x0:.2f}) = \mathbf{{{Mmax:.2f} \text{{ kNm}}}}")

        with tab_diag:
            x = np.linspace(0, L_tot, 1000)
            V_vals = np.piecewise(x, [x <= L1, (x > L1) & (x <= dist_F), x > dist_F], 
                                 [lambda x: Ra - q*x, lambda x: Ra - Rq, lambda x: Ra - Rq - F])
            M_vals = np.piecewise(x, [x <= L1, (x > L1) & (x <= dist_F), x > dist_F],
                                 [lambda x: Ra*x - (q*x**2)/2, 
                                  lambda x: Ra*x - Rq*(x-3), 
                                  lambda x: Ra*x - Rq*(x-3) - F*(x-8)])

            plt.style.use('dark_background')
            fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 9))
            fig.patch.set_facecolor('#0e1117')
            
            # Effort Tranchant
            ax1.plot(x, V_vals, color='#00d4ff', lw=2.5)
            ax1.fill_between(x, V_vals, color='#00d4ff', alpha=0.15)
            ax1.axhline(0, color='white', lw=0.8)
            ax1.set_title("Effort Tranchant V (kN)", fontsize=14, pad=10)
            
            # Moment Fléchissant
            ax2.plot(x, M_vals, color='#ff4b4b', lw=2.5)
            ax2.fill_between(x, M_vals, color='#ff4b4b', alpha=0.15)
            ax2.axhline(0, color='white', lw=0.8)
            ax2.invert_yaxis() # Fibres tendues vers le bas
            ax2.set_title("Moment Fléchissant M (kNm)", fontsize=14, pad=10)
            
            plt.tight_layout()
            st.pyplot(fig)

        # --- TABLEAU RÉCAPITULATIF ---
        st.markdown("### 📋 Tableau récapitulatif des valeurs")
        st.table({
            "Position x (m)": ["0 (A)", f"{x0:.2f} (V=0)", "6 (C)", "8 (D)", "10 (B)"],
            "Effort Tranchant V (kN)": [f"{Ra:.2f}", "0.00", f"{Ra-Rq:.2f}", f"{Ra-Rq-F:.2f}", f"{-Rb:.2f}"],
            "Moment Fléchissant M (kNm)": ["0.00", f"{Mmax:.2f}", f"{Ra*6-360:.2f}", f"{Ra*8-600:.2f}", "0.00"]
        })
        
        if st.button("📖 Étudier la théorie"):
            st.session_state.nav_menu = "📝 Cisaillement / Flexion"
            st.rerun()
