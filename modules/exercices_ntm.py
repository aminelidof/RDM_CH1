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
        
# --- GESTION ROBUSTE DU CHEMIN D'IMAGE ---
        # Détecte le dossier où se trouve le fichier exercices_ntm.py
        base_path = os.path.dirname(__file__)
        # Crée le chemin vers l'image dans le même dossier
        img_path = os.path.join(base_path, "exercice1.png")

        try:
            if os.path.exists(img_path):
                st.image(img_path, 
                         caption="Géométrie de la barre et sollicitations", 
                         use_container_width=True)
            else:
                st.warning(f"⚠️ Fichier image introuvable. Vérifiez qu'il est nommé 'exercice1.png' dans le dossier 'modules'.")
                # Optionnel : Afficher le chemin testé pour déboguer
                # st.write(f"Chemin testé : {img_path}")
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
        Mmax = (q * L**2) / 8

        with st.expander("✅ Voir la correction détaillée (NTM)"):
            st.latex(rf"V(x) = {Ra} - {q}x \quad | \quad M(x) = {Ra}x - \frac{{{q}x^2}}{{2}}")
            # Graphique (Similaire à votre code précédent)
            x_p = np.linspace(0, L, 100)
            fig, ax = plt.subplots(2, 1)
            ax[0].plot(x_p, Ra - q*x_p, color='#00d4ff')
            ax[1].plot(x_p, Ra*x_p - (q*x_p**2)/2, color='#ff4b4b')
            st.pyplot(fig)

    # --- EXERCICE 3 : CONSOLE (AJOUTÉ & AMÉLIORÉ) ---
    elif choix == "Ex 3 : Console (Charge ponctuelle)":
        st.subheader("📍 Énoncé : Poutre en console (Encastrée)")
        col1, col2 = st.columns(2)
        with col1: L_c = st.slider("Longueur (m)", 1.0, 10.0, 3.0)
        with col2: F_c = st.slider("Force à l'extrémité (kN)", 1, 100, 20)
        
        

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
            ax_c[0].fill_between(x_c, [F_c]*100, color='#00d4ff', alpha=0.3)
            ax_c[0].set_title("Effort Tranchant V (kN)")
            ax_c[1].fill_between(x_c, -F_c*(L_c - x_c), color='#ff4b4b', alpha=0.3)
            ax_c[1].set_title("Moment Fléchissant M (kNm)")
            st.pyplot(fig_c)

    # --- EXERCICE 4 : CHARGE CENTRÉE (AJOUTÉ & AMÉLIORÉ) ---
    elif choix == "Ex 4 : Flexion (Charge centrée)":
        st.subheader("📍 Énoncé : Poutre simple avec force au milieu")
        col3, col4 = st.columns(2)
        with col3: L_f = st.number_input("L (m)", value=6.0)
        with col4: P_f = st.number_input("P (kN)", value=40.0)
        with st.expander("✅ Voir la correction détaillée"):
            Ra_f = P_f / 2
            st.write(f"Réactions : $R_A = R_B = {Ra_f}\ kN$")
            st.latex(rf"M_{{max}} = \frac{{P \cdot L}}{{4}} = \frac{{{P_f} \cdot {L_f}}}{{4}} = {P_f*L_f/4}\ kNm")
            
            x_f = np.linspace(0, L_f, 100)
            v_f = np.where(x_f < L_f/2, Ra_f, -Ra_f)
            m_f = np.where(x_f < L_f/2, Ra_f * x_f, Ra_f * (L_f - x_f))
            
            fig_f, ax_f = plt.subplots(2, 1, figsize=(8, 6))
            ax_f[0].step(x_f, v_f, color='#00d4ff')
            ax_f[1].plot(x_f, m_f, color='#ff4b4b')
            st.pyplot(fig_f)

    elif choix == "Ex 5 : Cas Combiné (PFS + NTM)":
        st.subheader("📍 Étude d'une poutre avec charges combinées (Ex 3)")

        # --- GESTION DE L'IMAGE ---
        import os
        base_path = os.path.dirname(__file__)
        # Assurez-vous de renommer votre fichier en 'exercice3.png' sur GitHub
        img_path_ex3 = os.path.join(base_path, "Ex3.png")

        if os.path.exists(img_path_ex3):
            st.image(img_path_ex3, caption="Schéma statique de la poutre", use_container_width=True)
        else:
            st.error("❌ Image 'exercice3.png' non trouvée dans le dossier modules.")

        # --- DONNÉES DE L'IMAGE ---
        L_ac = 6.0    # Longueur charge répartie
        L_cd = 2.0    # Distance vide
        L_db = 2.0    # Distance charge ponctuelle vers appui B
        L_tot = 10.0  # Longueur totale
        q = 20.0      # kN/m
        F = 40.0      # kN (Charge ponctuelle au point D)

        # Calcul des réactions d'appuis (Somme des moments en A = 0)
        # Rb * 10 = (q * 6 * 3) + (F * 8)
        Rb = ((q * 6 * 3) + (F * 8)) / L_tot
        Ra = (q * 6 + F) - Rb

        st.markdown(f"""
            <div style="background-color: #1e1e1e; padding: 15px; border-radius: 10px; border-left: 5px solid #00d4ff; color: white; margin-bottom: 20px;">
                <h4 style="color: #00d4ff; margin: 0;">Données de l'Exercice</h4>
                <p style="margin: 5px 0;">• Charge répartie <b>q = {q} kN/m</b> sur <b>6m</b> (de A vers C)</p>
                <p style="margin: 5px 0;">• Charge ponctuelle <b>F = {F} kN</b> à <b>8m</b> de A (au point D)</p>
                <p style="margin: 5px 0;">• Portée totale <b>L = {L_tot} m</b></p>
            </div>
        """, unsafe_allow_html=True)

        # --- RÉACTIONS D'APPUIS ---
        c1, c2 = st.columns(2)
        c1.metric("Réaction en A ($R_A$)", f"{Ra:.2f} kN")
        c2.metric("Réaction en B ($R_B$)", f"{Rb:.2f} kN")

        # --- CALCULS DES DIAGRAMMES ---
        x = np.linspace(0, L_tot, 1000)
        V = []
        M = []

        for val in x:
            # Effort Tranchant V(x)
            if val <= 6:
                v_curr = Ra - q * val
                m_curr = Ra * val - (q * val**2) / 2
            elif val <= 8:
                v_curr = Ra - q * 6
                m_curr = Ra * val - (q * 6 * (val - 3))
            else:
                v_curr = Ra - q * 6 - F
                m_curr = Ra * val - (q * 6 * (val - 3)) - F * (val - 8)
            V.append(v_curr)
            M.append(m_curr)

        # --- AFFICHAGE GRAPHIQUE ---
        plt.style.use('dark_background')
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
        fig.patch.set_facecolor('#0e1117')

        # V(x)
        ax1.plot(x, V, color='#00d4ff', lw=2)
        ax1.fill_between(x, V, color='#00d4ff', alpha=0.2)
        ax1.axhline(0, color='white', lw=1)
        ax1.set_title("Effort Tranchant V (kN)", color='#00d4ff')
        ax1.grid(True, alpha=0.1)

        # M(x)
        ax2.plot(x, M, color='#ff4b4b', lw=2)
        ax2.fill_between(x, M, color='#ff4b4b', alpha=0.2)
        ax2.axhline(0, color='white', lw=1)
        ax2.set_title("Moment Fléchissant M (kNm)", color='#ff4b4b')
        ax2.invert_yaxis()  # Convention RDM (Moment vers le bas)
        ax2.grid(True, alpha=0.1)

        st.pyplot(fig)

        # --- TABLEAU DES VALEURS CLÉS ---
        with st.expander("📊 Voir les valeurs remarquables", expanded=True):
            points = {
                "Point": ["A (x=0)", "C (x=6)", "D (x=8)", "B (x=10)"],
                "Effort Tranchant V (kN)": [f"{Ra:.2f}", f"{Ra - q*6:.2f}", f"{Ra - q*6:.2f} / {Ra - q*6 - F:.2f}", f"{-Rb:.2f}"],
                "Moment Fléchissant M (kNm)": ["0.00", f"{Ra*6 - (q*6**2)/2:.2f}", f"{Ra*8 - (q*6*5):.2f}", "0.00"]
            }
            st.table(points)

        st.divider()
        if st.button("🚀 Consulter la méthode de calcul complète"):
            st.session_state.nav_menu = "📝 Cisaillement / Flexion"
            st.rerun()
