import streamlit as st
from .splice_logic import find_splice_sites

def render_splice_site_predictor(seq):
    donor_sites, acceptor_sites = find_splice_sites(seq)

    st.subheader("🔍 Splice Site Prediction Results")
    st.markdown(f"**Donor Sites (GT)**: {donor_sites}")
    st.markdown(f"**Acceptor Sites (AG)**: {acceptor_sites}")
    
    highlighted_seq = list(seq.upper())
    for i in donor_sites:
        highlighted_seq[i] = f":green[{highlighted_seq[i]}]"
        highlighted_seq[i+1] = f":green[{highlighted_seq[i+1]}]"
    for i in acceptor_sites:
        highlighted_seq[i] = f":blue[{highlighted_seq[i]}]"
        highlighted_seq[i+1] = f":blue[{highlighted_seq[i+1]}]"

    st.markdown("**Highlighted Sequence**:")
    st.write("".join(highlighted_seq))
