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

    # --- EXERCICE 5 : CAS COMBINÉ (CORRIGÉ ET ALIGNÉ) ---
    elif choix == "Ex 5 : Cas Combiné (PFS + NTM)":
        st.subheader("📍 Étude Approfondie : Poutre Iso-statique (Ex 3)")

        base_path = os.path.dirname(__file__)
        img_path = os.path.join(base_path, "Ex4.png")

        if os.path.exists(img_path):
            st.image(img_path, caption="Schéma statique original", use_container_width=True)
        else:
            st.error("❌ Fichier 'Ex5.png' introuvable dans le dossier modules.")

        L1, L2, L3 = 6.0, 2.0, 2.0
        L_tot = L1 + L2 + L3
        q, F = 20.0, 40.0
        dist_F = L1 + L2 

        Rq = q * L1
        Rb = (Rq * (L1/2) + F * dist_F) / L_tot
        Ra = (Rq + F) - Rb

        x0 = Ra / q
        Mmax = Ra * x0 - (q * x0**2) / 2 if x0 <= L1 else 0

        tab_diag, tab_pfs, tab_equa = st.tabs(["📊 Graphiques", "⚖️ Équilibre (PFS)", "✂️ Coupures Analytiques"])

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

            plt.style.use('dark_background')
            fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 9))
            fig.patch.set_facecolor('#0e1117')
            ax1.plot(x, V_vals, color='#00d4ff', lw=2.5)
            ax1.fill_between(x, V_vals, color='#00d4ff', alpha=0.15)
            ax1.set_title("Diagramme de l'Effort Tranchant V (kN)")
            
            ax2.plot(x, M_vals, color='#ff4b4b', lw=2.5)
            ax2.fill_between(x, M_vals, color='#ff4b4b', alpha=0.15)
            ax2.invert_yaxis()
            ax2.set_title("Diagramme du Moment Fléchissant M (kNm)")
            st.pyplot(fig)

        with tab_pfs:
            st.markdown(f"""
            <div style="background-color: #1e1e1e; padding: 20px; border-radius: 10px; border: 1px solid #333; color: white;">
                <h3 style="color: #00d4ff;">1. Modélisation</h3>
                <p>$R_q = q \cdot L_1 = {Rq} \text{{ kN}}$ à $x = 3 \text{{ m}}$</p>
                <h3 style="color: #00d4ff;">2. Équilibres</h3>
                <p>$\sum M_{{/A}} = 0 \implies R_B = {Rb:.2f} \text{{ kN}}$</p>
                <p>$\sum F_y = 0 \implies R_A = {Ra:.2f} \text{{ kN}}$</p>
            </div>
            """, unsafe_allow_html=True)

        with tab_equa:
            st.markdown(f"""
            <div style="color: white;">
                <h3 style="color: #ff4b4b;">Tronçon I : [0, 6]</h3>
                <p>$V(x) = {Ra:.2f} - 20x$ | $M(x) = {Ra:.2f}x - 10x^2$</p>
                <h3 style="color: #ff4b4b;">Tronçon II : [6, 8]</h3>
                <p>$V(x) = {Ra-Rq:.2f}$ | $M(x) = {Ra:.2f}x - 120(x-3)$</p>
            </div>
            """, unsafe_allow_html=True)

        st.table({
            "Position x (m)": ["0 (A)", f"{x0:.2f} (V=0)", "6 (C)", "8 (D)", "10 (B)"],
            "Effort V (kN)": [f"{Ra:.2f}", "0.00", f"{Ra-Rq:.2f}", f"{Ra-Rq-F:.2f}", f"{-Rb:.2f}"],
            "Moment M (kNm)": ["0.00", f"{Mmax:.2f}", f"{Ra*6-360:.2f}", f"{Ra*8-600:.2f}", "0.00"]
        })
        
        if st.button("📖 Étudier la théorie"):
            st.session_state.nav_menu = "📝 Cisaillement / Flexion"
            st.rerun()

