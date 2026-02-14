import streamlit as st

def run():
    st.header("⚖️ PFS : Principe Fondamental de la Statique")
    
    st.markdown("""
    Le **PFS** est la base de toute étude en RDM. Il permet de déterminer les réactions aux appuis (inconnues) à partir des charges appliquées (connues). 
    Pour une structure plane (2D), l'équilibre est traduit par trois équations scalaires.
    """)

    # --- SECTION 1 : LES ÉQUATIONS ---
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Les Équations de l'Équilibre")
        st.latex(r"\sum F_x = 0")
        st.latex(r"\sum F_y = 0")
        st.latex(r"\sum M_{/Point} = 0")
    
    with col2:
        st.info("""
        **Pourquoi 3 équations ?**
        En 2D, un corps a 3 degrés de liberté : 
        - 2 translations (x, y) 
        - 1 rotation (z).
        Le PFS "bloque" ces mouvements.
        """)

    # --- SECTION 2 : MÉTHODOLOGIE DÉTAILLÉE ---
    st.divider()
    st.subheader("🔍 Méthodologie pas à pas")
    
    
    
    st.markdown(r"""
    ### 1. Modélisation (Bilan des Actions Extérieures)
    Remplacez chaque appui par sa réaction mécanique :
    - **Appui simple :** 1 force verticale ($R_y$).
    - **Articulation :** 2 forces ($R_x, R_y$).
    - **Encastrement :** 2 forces + 1 moment ($R_x, R_y, M$).

    ### 2. Choix stratégique du point de pivot
    Pour simplifier le calcul des moments ($\sum M = 0$), choisissez un point où se situent **le plus d'inconnues**. 
    *Exemple : Faire la somme des moments au point A permet d'annuler les moments de $R_{Ax}$ et $R_{Ay}$ car leur bras de levier est nul.*

    ### 3. Calcul de la charge équivalente
    Pour les charges réparties ($q$), transformez-les en force ponctuelle équivalente $P$ :
    - **Valeur :** $P = q \times L$
    - **Position :** Centre de gravité de la charge (L/2 pour une charge uniforme).
    """)

    # --- SECTION 3 : CONSEILS SUR LES BRAS DE LEVIER ---
    st.divider()
    with st.expander("💡 Astuce : Ne vous trompez plus sur le Moment !"):
        st.markdown(r"""
        Le moment d'une force est : **$M = \text{Force} \times \text{Bras de levier}$**
        - Le **Bras de levier** est la distance *perpendiculaire* entre le point de pivot et la ligne d'action de la force.
        - **Signe :** Fixez une convention (souvent sens trigonométrique $+$).
        """)
        

    # --- SECTION 4 : AUTO-VÉRIFICATION (INTERACTIF) ---
    st.header("⚡ Vérification Rapide")
    st.markdown("Vérifiez toujours votre calcul avec une équation que vous n'avez pas utilisée.")
    
    test_val = st.checkbox("Afficher la règle de vérification")
    if test_val:
        st.success(r"""
        **La "Contre-Somme" :**
        Si vous avez trouvé $R_A$ et $R_B$ en utilisant les moments en A et B, 
        vérifiez que $\sum F_y = 0$. 
        Si $R_A + R_B \neq \text{Forces descendantes}$, votre calcul est faux !
        """)

    # --- SECTION 5 : RÉSUMÉ GRAPHIQUE ---
    st.markdown("""
    <div style="background-color: #1c1f26; padding: 20px; border-radius: 10px; border-left: 5px solid #ffcc00;">
    <h4>🎓 Ce qu'il faut retenir :</h4>
    <ul>
        <li>On commence toujours par <b>l'équilibre des moments</b> pour isoler une inconnue.</li>
        <li>On finit par <b>l'équilibre des forces verticales</b> pour trouver la seconde.</li>
        <li>Si le résultat est négatif, cela signifie simplement que la réaction réelle est dans le sens opposé à votre flèche de départ.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)