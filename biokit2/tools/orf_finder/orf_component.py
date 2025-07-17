from .orf_logic import find_orfs, highlight_orfs
import streamlit as st

def render_orf_finder(sequence: str):
    st.subheader("ORF Finder")
    st.markdown("""
    🔍 **What this tool does:**  
    Finds all Open Reading Frames (ORFs) in the forward strand of the input DNA sequence.  
    An ORF starts with `ATG` and ends at the nearest downstream stop codon (`TAA`, `TAG`, or `TGA`) in-frame.
    """)

    orfs = find_orfs(sequence)

    if not orfs:
        st.warning("No ORFs found.")
        return

    st.success(f"Found {len(orfs)} ORF(s)")

    for i, (start, end, orf_seq) in enumerate(orfs, 1):
        st.markdown(f"**ORF {i}:** Position `{start}–{end}`, Length: `{end - start}`")
        st.code(orf_seq, language="text")

    # Highlight all ORFs visually in the original sequence
    highlighted = highlight_orfs(sequence, [(start, end) for start, end, _ in orfs])
    st.markdown("### Highlighted ORFs in Sequence")
    st.code(highlighted, language="text")
