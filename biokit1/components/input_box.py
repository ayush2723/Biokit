import streamlit as st

def dna_input_box(label="Enter DNA Sequence", key="dna_input_box", height=100, max_chars=1000, placeholder="e.g. ATGCGTACGTTAGC"): #input box for DNA sequence
    dna_input = st.text_area(label,key=key, height=height, max_chars=max_chars, placeholder=placeholder) #
    seq_str = dna_input.replace(" ", "").replace("\n", "").upper() #replaces  whitespaces and new lines and convert to uppercase
    
    if dna_input and not set(seq_str).issubset({"A", "T", "G", "C"}): #validates sequence non empty strings evaluates to true
        st.error(" Invalid DNA sequence! Please use only letters A, T, G, C.")
        return None
    
    return seq_str if dna_input else None
