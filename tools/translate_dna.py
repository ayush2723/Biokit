from Bio.Seq import Seq  # import Seq class from Biopython library
import streamlit as st   # assuming you use streamlit for the markdown calls

def translate_dna(dna_sequence: str) -> str:
    """
    Translates a DNA sequence into a protein sequence.

    Args:
        dna_sequence (str): Validated DNA sequence (A, T, G, C only).

    Returns:
        str: Protein sequence (single-letter amino acid codes).
    """
    seq = Seq(dna_sequence)
    protein_seq = seq.translate(to_stop=True)  
    # stops translation at the first stop codon
    return str(protein_seq)


def display_translation_view(dna_seq, rna_seq, protein_seq):
    def chunk_string(s, chunk_size):
        return [s[i:i+chunk_size] for i in range(0, len(s), chunk_size)]

    codons_dna = chunk_string(dna_seq, 3)
    codons_rna = chunk_string(rna_seq, 3)
    protein_chunks = list(protein_seq)

    st.markdown("### Translation Viewer")
    st.markdown("**DNA Codons:** `" + " ".join(codons_dna) + "`")
    st.markdown("**RNA Codons:** `" + " ".join(codons_rna) + "`")
    st.markdown("**Protein:** `" + " ".join(protein_chunks) + "`")
