import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def run():
    st.title("📏 Exercice : Diagrammes N et Sigma")
    st.markdown("### Étude d'une barre à sections variables")

# --- INSERTION DE L'IMAGE ---
    # Correction : Utilisation d'un 'r' devant le chemin et précision du fichier
    # Assurez-vous que le nom du fichier (ex: image_exercice.png) est correct
    try:
        st.image(r"C:/Users/Administrator/Desktop/RDM/CH1/modules/exercice1.png", 
                 caption="Schéma de la barre et des forces appliquées", 
                 use_container_width=True)
    except:
        st.warning("⚠️ Image non trouvée. Vérifiez que le fichier image est bien dans le dossier 'modules'.")

    # --- DONNÉES DE L'EXERCICE ---
    st.info(r"""
    **Données fournies :**
    - $F = 20\ \text{kN}$
    - $D = 12\ \text{mm}$
    - $L = 200\ \text{mm}$
    - $E = 200\ \text{GPa}$
    """)

    # Paramètres de calcul
    F = 20e3  # Newtons
    D1 = 18.0 # mm (3D/2)
    D2 = 12.0 # mm (D)
    L_tot = 400.0 # mm (L + L/2 + L/2)

    # Surfaces
    S1 = (np.pi * D1**2) / 4
    S2 = (np.pi * D2**2) / 4

    # --- CALCUL DES EFFORTS PAR ZONE ---
    st.header("1. Analyse des efforts normaux (Coupures)")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Zone 1 [0 - L]")
        st.write("Coupure entre 0 et 200 mm")
        st.latex(r"N_1 = 2F = 40\ \text{kN}")
        
    with col2:
        st.subheader("Zone 2 [L - 1.5L]")
        st.write("Coupure entre 200 et 300 mm")
        st.latex(r"N_2 = 2F - F = 20\ \text{kN}")

    with col3:
        st.subheader("Zone 3 [1.5L - 2L]")
        st.write("Coupure entre 300 et 400 mm")
        st.latex(r"N_3 = F = 20\ \text{kN}")

    # --- DIAGRAMMES ---
    st.header("2. Tracé des Diagrammes")

    # Préparation des données pour le graphe
    x = np.array([0, 200, 200, 300, 300, 400])
    N = np.array([40, 40, 20, 20, 20, 20]) # en kN
    Sigma = np.array([40000/S1, 40000/S1, 20000/S2, 20000/S2, 20000/S2, 20000/S2]) # en MPa

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    plt.subplots_adjust(hspace=0.4)

    # Graphe Effort Normal N
    ax1.step(x, N, where='post', color='#00d4ff', lw=2.5)
    ax1.fill_between(x, N, step="post", color='#00d4ff', alpha=0.2)
    ax1.set_title("Diagramme de l'Effort Normal N (kN)", color="white")
    ax1.grid(True, alpha=0.2)

    # Graphe Contrainte Sigma
    ax2.step(x, Sigma, where='post', color='#ff4b4b', lw=2.5)
    ax2.fill_between(x, Sigma, step="post", color='#ff4b4b', alpha=0.2)
    ax2.set_title("Diagramme des Contraintes σ (MPa)", color="white")
    ax2.grid(True, alpha=0.2)

    # Style
    for ax in [ax1, ax2]:
        ax.set_facecolor("#0e1117")
        ax.tick_params(colors='white')
        ax.set_xlabel("x (mm)", color="white")

    fig.patch.set_facecolor("#0e1117")
    st.pyplot(fig)

    # --- CALCUL DE DÉFORMATION ---
    st.header("3. Longueur après déformation")
    deltaL1 = (40000 * 200) / (200000 * S1)
    deltaL2 = (20000 * 100) / (200000 * S2)
    deltaL3 = (20000 * 100) / (200000 * S2)
    deltaL_tot = deltaL1 + deltaL2 + deltaL3
    
    st.latex(rf"\Delta L_{{total}} = {deltaL_tot:.4f}\ \text{{mm}}")
    st.success(rf"Longueur finale : $L_{{f}} = {400 + deltaL_tot:.4f}\ \text{{mm}}$")