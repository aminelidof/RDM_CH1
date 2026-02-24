import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def run():
    st.title("📝 Application du Cours")
    st.markdown("### Étude d'une poutre avec charges combinées")

# --- INSERTION DE L'IMAGE ---
    # Correction : Utilisation d'un 'r' devant le chemin et précision du fichier
    # Assurez-vous que le nom du fichier (ex: image_exercice.png) est correct
    try:
        st.image("modules/exercice2.png", 
                 caption="Schéma de la barre et des forces appliquées", 
                 use_container_width=True)
    except:
        st.warning("⚠️ Image non trouvée. Vérifiez que le fichier image est bien dans le dossier 'modules'.")



    # --- ENONCE ET FIGURE ---
    st.header("1. Énoncé et Modélisation")
    
    # Schéma de la poutre (Statique)
    
    
    st.info(r"""
    **Données de l'exercice :**
    - Longueur totale : $L = 10\ \text{m}$
    - Charge répartie : $q = 20\ \text{kN/m}$
    - Charge ponctuelle : $Q_1 = 20\ \text{kN}$ située à $x = 3\ \text{m}$
    """)

    # --- CALCUL DES REACTIONS ---
    st.header("2. Calcul des Réactions d'Appuis")
    st.write("Le système est en équilibre. On applique le Principe Fondamental de la Statique (PFS) :")
    
    col_calc1, col_calc2 = st.columns(2)
    
    with col_calc1:
        st.markdown("**Équilibre des moments en B :**")
        st.latex(r"\sum M_B = 0")
        st.latex(r"R_A \cdot 10 - Q_1 \cdot (10 - 3) - q \cdot 10 \cdot \frac{10}{2} = 0")
        st.latex(r"10 R_A = 140 + 1000 \implies R_A = 114\ \text{kN}")
    
    with col_calc2:
        st.markdown("**Équilibre des forces verticales :**")
        st.latex(r"\sum F_y = 0")
        st.latex(r"R_A + R_B = Q_1 + (q \cdot L)")
        st.latex(r"114 + R_B = 20 + 200 \implies R_B = 106\ \text{kN}")
    
    st.success(r"Résultats validés : $R_A = 114\ \text{kN}$ et $R_B = 106\ \text{kN}$")

# --- METHODE ANALYTIQUE ---
    st.header("3. Équations des Efforts Internes (Coupures)")
    
    tab1, tab2 = st.tabs(["Zone 1 : $0 \le x \le 3$", "Zone 2 : $3 < x \le 10$"])
    
    with tab1:
        st.markdown("**Coupure avant la charge ponctuelle :**")
        
        # --- Effort Tranchant ---
        st.markdown(
            """
            <div style="background-color: #e1f5fe; padding: 10px; border-left: 5px solid #01579b; border-radius: 5px;">
            ℹ️ <b>Effort Tranchant :</b> La somme des forces à gauche de la coupure.
            </div>
            """, unsafe_allow_html=True
        )
        st.latex(r"V_1(x) = R_A - q \cdot x = 114 - 20x")
        
        # --- Moment Fléchissant ---
        st.markdown(
            """
            <div style="background-color: #e1f5fe; padding: 10px; border-left: 5px solid #01579b; border-radius: 5px; margin-top: 10px;">
            ℹ️ <b>Somme des moments :</b> $M(x) = R_A \cdot x - q \cdot \\frac{x^2}{2}$
            </div>
            """, unsafe_allow_html=True
        )
        st.latex(r"M_1(x) = 114x - 10x^2")
        
        st.markdown("---")
        
        # --- Résultats ---
        st.markdown("**Résultats détaillés aux limites :**")
        col1, col2 = st.columns(2)
        with col1:
            st.write("**À $x=0\text{ m}$ :**")
            st.write(r"$V = 114\text{ kN}$")
            st.write(r"$M = 0\text{ kNm}$")
        with col2:
            st.write("**À $x=3\text{ m}$ :**")
            st.write(r"$V = 114 - 20(3) = 54\text{ kN}$")
            st.write(r"$M = 114(3) - 10(3)^2 = 252\text{ kNm}$")

    with tab2:
        st.markdown("**Coupure après la charge ponctuelle :**")
        st.info("Prise en compte de $Q_1$ à $x=3$m : $V(x) = R_A - qx - Q_1$")
        st.latex(r"V_2(x) = 114 - 20x - 20 = 94 - 20x")
        
        st.info("Bras de levier de $Q_1$ : $(x-3)$")
        st.latex(r"M_2(x) = 114x - 10x^2 - 20(x-3)")
        st.latex(r"M_2(x) = 94x - 10x^2 + 60")
        
        st.markdown("**Analyse du point de discontinuité ($x=3\text{m}$) :**")
        col1, col2 = st.columns(2)
        with col1:
            st.write(r"**Effort Tranchant :**")
            st.write(r"$V_1(3) = 54\text{ kN}$")
            st.write(r"$V_2(3) = 34\text{ kN}$")
            st.write(r"$\Delta V = 20\text{ kN}$ (Saut)")
        with col2:
            st.write(r"**Moment Fléchissant :**")
            st.write(r"$M_1(3) = 252\text{ kNm}$")
            st.write(r"$M_2(3) = 252\text{ kNm}$")
            st.write(r"Continuité du moment")
    # --- GRAPHIQUES ---
    st.header("4. Diagrammes des Efforts de Cohésion")
    
    x = np.linspace(0, 10, 1000)
    V = np.where(x <= 3, 114 - 20*x, 94 - 20*x)
    M = np.where(x <= 3, 114*x - 10*x**2, 114*x - 20*(x-3) - 10*x**2)

    # Effort Tranchant
    
    fig_v, ax_v = plt.subplots(figsize=(10, 3.5))
    ax_v.plot(x, V, color='#00d4ff', linewidth=2.5)
    ax_v.fill_between(x, V, color='#00d4ff', alpha=0.15)
    ax_v.axhline(0, color="white", linewidth=1)
    ax_v.set_title("Diagramme de l'Effort Tranchant V (kN)", color="white")
    ax_v.set_facecolor("#0e1117")
    fig_v.patch.set_facecolor("#0e1117")
    ax_v.tick_params(colors='white')
    ax_v.grid(True, alpha=0.1)
    st.pyplot(fig_v)

    # Moment Fléchissant
    
    fig_m, ax_m = plt.subplots(figsize=(10, 3.5))
    ax_m.plot(x, M, color='#ff4b4b', linewidth=2.5)
    ax_m.fill_between(x, M, color='#ff4b4b', alpha=0.15)
    ax_m.axhline(0, color="white", linewidth=1)
    ax_m.set_title("Diagramme du Moment Fléchissant M (kNm)", color="white")
    ax_m.set_facecolor("#0e1117")
    fig_m.patch.set_facecolor("#0e1117")
    ax_m.tick_params(colors='white')
    ax_m.grid(True, alpha=0.1)
    st.pyplot(fig_m)

    # --- SYNTHESE FINALE ---
    st.header("5. Conclusion et Point Critique")
    
    col_res1, col_res2 = st.columns(2)
    with col_res1:
        st.write("Le moment maximum est atteint quand l'effort tranchant s'annule ($V(x) = 0$) :")
        st.latex(r"94 - 20x = 0 \implies x = 4.70\ \text{m}")
    with col_res2:
        m_max = 114*4.7 - 20*(4.7-3) - 10*(4.7**2)
        st.metric("Moment Max (M_max)", f"{m_max:.2f} kNm", delta_color="normal")


    st.warning(r"🎯 L'analyse montre que la section la plus sollicitée se trouve à **4.70 mètres** de l'appui A.")




