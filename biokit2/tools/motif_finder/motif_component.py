from .motif_logic import find_motif_positions
from biokit2.data.motif_data import COMMON_MOTIFS
import streamlit as st

def render_motif_finder(sequence: str):
    st.subheader("Motif Finder")
    use_predefined = st.checkbox("Use predefined motifs", value=True)

    if use_predefined:
        motif_name = st.selectbox("Select a motif", list(COMMON_MOTIFS.keys()))
        motif = COMMON_MOTIFS[motif_name]
    else:
        motif = st.text_input("Enter custom motif")

    if motif:
        positions = find_motif_positions(sequence, motif)
        st.markdown(f"**Motif found at positions:** {positions}")
