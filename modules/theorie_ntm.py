import streamlit as st

def run():
    st.title("📚 Théorie des Efforts Internes (N, T, M)")
    
    st.markdown("""
    La **Résistance des Matériaux (RDM)** étudie la relation entre les charges extérieures appliquées à une structure 
    et les efforts qui naissent à l'intérieur de la matière. Pour trouver ces efforts, on utilise la **méthode des coupures**.
    """)

    # --- SECTION 1: LA MÉTHODE DES COUPURES ---
    st.header("1. La Méthode des Coupures")
    st.write("""
    Le principe est simple : si une poutre est en équilibre sous l'action de forces extérieures, chaque morceau de cette poutre est aussi en équilibre.
    En coupant fictivement la poutre en un point $x$, on fait apparaître le **Torseur des efforts de cohésion**.
    """)
    
    

    # --- SECTION 2: DÉFINITION DES COMPOSANTES ---
    st.header("2. Les trois sollicitations de base")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("🔹 Effort Normal (N)")
        st.markdown("""
        **Action :** Étire ou comprime la poutre.
        * **N > 0 (Traction) :** Les forces s'éloignent de la section.
        * **N < 0 (Compression) :** Les forces "écrasent" la section.
        """)
        

    with col2:
        st.subheader("🔹 Effort Tranchant (T)")
        st.markdown("""
        **Action :** Tente de cisailler la poutre.
        * Représente la somme des forces perpendiculaires à l'axe.
        * Une force ponctuelle crée un **saut** brusque dans le diagramme.
        """)
        

    with col3:
        st.subheader("🔹 Moment Fléchissant (M)")
        st.markdown("""
        **Action :** Courbe la poutre.
        * **M > 0 :** La poutre "sourit" (fibres du bas tendues).
        * **M < 0 :** La poutre "fait la tête" (fibres du haut tendues).
        """)
        

    # --- SECTION 3: FOCUS CHARGES RÉPARTIES ---
    st.divider()
    st.header("3. 💡 Focus : Charges Réparties ($q$)")
    
    col_q1, col_q2 = st.columns([1, 1.5])
    
    with col_q1:
        st.write("""
        Une charge répartie (poids propre, pression) change la nature mathématique des diagrammes :
        * **Unité :** kN/m.
        * **Résultante :** $P = q \cdot L$ agissant au milieu.
        """)
        
    
    with col_q2:
        st.info("**Évolution de la forme des courbes :**")
        st.markdown(r"""
        - **Sans charge répartie :** $T(x)$ est constant, $M(x)$ est linéaire (droite).
        - **Avec charge répartie $q$ :** $T(x)$ devient linéaire, $M(x)$ devient **parabolique** (degré 2).
        """)

    # --- SECTION 4: RELATIONS DIFFÉRENTIELLES ---
    st.header("4. Les Relations d'Équilibre (Clés de vérification)")
    st.success("Ces relations sont le secret pour vérifier vos diagrammes en un coup d'œil !")
    
    c1, c2 = st.columns(2)
    with c1:
        st.latex(r"T(x) = \frac{dM(x)}{dx}")
        st.caption("L'effort tranchant est la pente du moment fléchissant.")
    with c2:
        st.latex(r"q(x) = -\frac{dT(x)}{dx}")
        st.caption("La charge répartie est la pente (négative) de l'effort tranchant.")

    st.warning("⚠️ **Règle d'or :** Là où l'effort tranchant $T(x) = 0$, le moment fléchissant $M(x)$ est **maximum**.")

    # --- SECTION 5: CONVENTIONS DE SIGNE ---
    st.header("5. Convention de Signe (Méthode de la Partie Gauche)")
    
    st.markdown("""
    <div style="background-color: #1c1f26; padding: 25px; border-radius: 15px; border: 1px solid #58a6ff;">
    On regarde tout ce qui se trouve à <b>gauche</b> de la coupure $x$ :
    <ol>
        <li><b>N(x) :</b> Somme des forces horizontales vers la gauche.</li>
        <li><b>T(x) :</b> Somme des forces verticales (vers le haut = positif).</li>
        <li><b>M(x) :</b> Somme des moments au point de coupure (sens horaire = positif).</li>
    </ol>
    </div>
    """, unsafe_allow_html=True)
    
    

    # --- SECTION 6: ASTUCES D'INGÉNIEUR ---
    st.divider()
    st.header("6. 🛠️ Astuces pour le tracé")
    
    with st.expander("Comment interpréter les résultats ?"):
        st.write("""
        1. **Continuité :** Le moment $M(x)$ est toujours continu (sauf s'il y a un couple ponctuel).
        2. **Sauts :** Chaque force ponctuelle $F$ crée un saut de valeur $F$ dans le diagramme $T(x)$.
        3. **Extremum :** Pour trouver le moment maximal, cherchez toujours l'endroit où $T(x)$ coupe l'axe zéro.
        """)