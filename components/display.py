import streamlit as st

def display_sequence(title: str, sequence: str):
    """
    Displays a DNA or RNA sequence with a title.

    Args:
        title (str): Title above the sequence (e.g., "Original Sequence").
        sequence (str): The nucleotide sequence string.
    """
    st.markdown(f"<h3 style='color:#000000; font-family: Courier New, monospace;'>{title}</h3>", unsafe_allow_html=True)
    st.code(sequence, language="text")
