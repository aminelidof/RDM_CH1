import streamlit as st

def run():
    st.header("⚙️ Modélisation des Appuis (Liaisons)")
    st.markdown("""
    En RDM, un appui est une liaison qui restreint les mouvements d'une structure. 
    Chaque mouvement interdit (translation ou rotation) génère une **force de réaction** ou un **moment**.
    """)

    # --- SECTION 1 : LES TYPES D'APPUIS ---
    st.subheader("1. Les types d'appuis classiques")
    
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 🟢 Appui Simple")
        # 
        st.info("""
        **Mouvements libres :**
        - Translation horizontale (X)
        - Rotation (Z)
        
        **Réaction :**
        - 1 force verticale ($R_y$)
        """)
        st.caption("Exemple : Appui sur rouleaux, glissière.")

    with col2:
        st.markdown("### 🟡 Articulation")
        # 
        st.warning("""
        **Mouvements libres :**
        - Rotation (Z) uniquement
        
        **Réactions :**
        - 1 force verticale ($R_y$)
        - 1 force horizontale ($R_x$)
        """)
        st.caption("Exemple : Rotule, charnière de porte.")

    with col3:
        st.markdown("### 🔴 Encastrement")
        # 
        st.error("""
        **Mouvements libres :**
        - **Aucun**
        
        **Réactions :**
        - 1 force verticale ($R_y$)
        - 1 force horizontale ($R_x$)
        - 1 moment d'encastrement ($M$)
        """)
        st.caption("Exemple : Poteau scellé dans le béton.")

    # --- LE DIVIDER DOIT ÊTRE ALIGNÉ AVEC LE BORD GAUCHE (HORS DES WITH) ---
    st.divider()

    # --- SECTION 2 : PRINCIPE ACTION-RÉACTION ---
    st.subheader("2. Principe d'Action et Réaction")
    
    col_a, col_b = st.columns([1.5, 1])
    with col_a:
        st.markdown(r"""
        Lorsqu'une charge $P$ est appliquée sur une poutre, les appuis s'y opposent pour maintenir l'équilibre.
        - **Action :** Charges appliquées (Forces, Poids, Vent).
        - **Réaction :** Efforts générés par les appuis.
        
        L'équilibre n'est atteint que si :
        $$\sum \vec{F}_{Actions} + \sum \vec{R}_{Réactions} = \vec{0}$$
        """)
    with col_b:
        # 
        st.write("") # Espace pour l'image

    st.divider()

    # --- SECTION 3 : STABILITÉ ---
    with st.expander("🧐 Isostatisme vs Hypostatisme"):
        st.markdown("""
        Pour qu'une poutre soit stable en 2D, il faut au minimum **3 réactions** d'appuis.
        - **Hypostatique (< 3) :** La structure est instable (c'est un mécanisme qui bouge).
        - **Isostatique (= 3) :** Stable et calculable avec le PFS simple.
        - **Hyperstatique (> 3) :** Très stable mais nécessite des méthodes de calcul avancées (Castigliano, Menabrea).
        """)

    st.markdown("""
    <div style="background-color: #1c1f26; padding: 15px; border-radius: 10px; border-top: 3px solid #00d4ff;">
    <strong>💡 Conseil :</strong> Identifiez bien le nombre d'inconnues (Rx, Ry, M) avant de poser vos équations du PFS.
    </div>
    """, unsafe_allow_html=True)