from collections import Counter
import matplotlib.pyplot as plt
import streamlit as st

def calculate_codon_frequency(seq: str) -> dict:
    """
    Calculate the frequency of each codon (triplet) in a DNA/RNA sequence.

    Args:
        seq (str): Input nucleotide sequence (should be divisible by 3 or trimmed).

    Returns:
        dict: Dictionary with codon as key and frequency count as value.
    """
    codons = [seq[i:i+3] for i in range(0, len(seq) - len(seq) % 3, 3)]
    codon_counts = Counter(codons)
    return dict(codon_counts)

def plot_codon_histogram(codon_freq: dict):
    """
    Plot a histogram of codon frequencies using matplotlib and display in Streamlit.

    Args:
        codon_freq (dict): Dictionary with codon as key and frequency as value.
    """
    fig, ax = plt.subplots(figsize=(10, 4))  # Wide and short
    ax.bar(codon_freq.keys(), codon_freq.values(), color='skyblue')
    ax.set_xlabel('Codons')
    ax.set_ylabel('Frequency')
    ax.set_title('Codon Frequency Histogram')
    plt.xticks(rotation=90)
    plt.tight_layout()
    st.pyplot(fig)
