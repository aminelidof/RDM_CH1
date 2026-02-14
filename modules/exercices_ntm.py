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

# --- EXERCICE 5 : CAS COMPLET ---
    elif choix == "Ex 5 : Cas Combiné (PFS + NTM)":
        st.subheader("📍 Étude d'une poutre avec charges combinées")

        # Gestion du chemin d'image
        base_path = os.path.dirname(__file__)
        img_path_ex5 = os.path.join(base_path, "exercice5.png")

        if os.path.exists(img_path_ex5):
            st.image(img_path_ex5, caption="Modélisation de la poutre", use_container_width=True)
        else:
            st.error("❌ Image 'exercice5.png' non trouvée dans le dossier modules.")

        # Données et calculs
        L_tot, q_val, Q_val, pos_Q = 10.0, 20.0, 20.0, 3.0
        Ra, Rb = 114.0, 106.0

        st.markdown(f"""
            <div style="background-color: #1e1e1e; padding: 15px; border-radius: 10px; border-left: 5px solid #00d4ff; color: white; margin-bottom: 20px;">
                <h4 style="color: #00d4ff; margin: 0;">Données du Problème</h4>
                <p style="margin: 5px 0;">Portée : <b>{L_tot} m</b> | Charge répartie : <b>{q_val} kN/m</b></p>
                <p style="margin: 5px 0;">Charge ponctuelle : <b>{Q_val} kN</b> à <b>{pos_Q} m</b> de l'appui A</p>
            </div>
        """, unsafe_allow_html=True)

        # Métriques Réactions
        c1, c2 = st.columns(2)
        c1.metric("Réaction en A ($R_A$)", f"{Ra} kN", delta="Verticale Haut")
        c2.metric("Réaction en B ($R_B$)", f"{Rb} kN", delta="Verticale Haut")

        # Génération des diagrammes
        x = np.linspace(0, L_tot, 500)
        # Effort tranchant V(x)
        V = np.where(x <= pos_Q, Ra - q_val*x, (Ra - Q_val) - q_val*x)
        # Moment fléchissant M(x)
        M = np.where(x <= pos_Q, Ra*x - (q_val*x**2)/2, Ra*x - Q_val*(x-pos_Q) - (q_val*x**2)/2)

        # Graphiques
        plt.style.use('dark_background')
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
        fig.patch.set_facecolor('#0e1117')

        # V(x)
        ax1.plot(x, V, color='#00d4ff', lw=2.5)
        ax1.fill_between(x, V, color='#00d4ff', alpha=0.1)
        ax1.axhline(0, color='white', lw=1)
        ax1.set_title("Diagramme de l'Effort Tranchant V(x)", color='#00d4ff')
        ax1.set_ylabel("V (kN)")
        ax1.grid(True, alpha=0.1)

        # M(x)
        ax2.plot(x, M, color='#ff4b4b', lw=2.5)
        ax2.fill_between(x, M, color='#ff4b4b', alpha=0.1)
        ax2.axhline(0, color='white', lw=1)
        ax2.set_title("Diagramme du Moment Fléchissant M(x)", color='#ff4b4b')
        ax2.set_ylabel("M (kNm)")
        ax2.set_xlabel("Position x (m)")
        ax2.grid(True, alpha=0.1)

        plt.tight_layout()
        st.pyplot(fig)
        
        

        # Tableau de synthèse
        with st.expander("📊 Détails des valeurs aux points singuliers", expanded=False):
            data = {
                "Position x (m)": ["0 (Appui A)", "3 (Avant Q)", "3 (Après Q)", "10 (Appui B)"],
                "V (kN)": [Ra, Ra - q_val*3, Ra - q_val*3 - Q_val, -Rb],
                "M (kNm)": [0, Ra*3 - (q_val*3**2)/2, Ra*3 - (q_val*3**2)/2, 0]
            }
            st.table(data)

        # Redirection
        st.divider()
        st.success("📝 **Analyse terminée.** Voulez-vous consulter la démonstration mathématique complète ?")
        
        if st.button("🚀 Ouvrir la correction détaillée"):
            # S'assurer que 'nav_menu' est bien utilisé dans le radio de app.py
            st.session_state.nav_menu = "📝 Cisaillement / Flexion"
            st.rerun()


