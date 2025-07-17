import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from biokit2.data.genetic_code import GENETIC_CODE
from biokit2.data.codon_usage import CODON_USAGE_TABLES
from biokit2.tools.codon_optimization.codon_optimizer_logic import optimize_sequence

def get_codon_frequency(seq: str) -> dict:
    codons = [seq[i:i+3] for i in range(0, len(seq) - 2, 3) if len(seq[i:i+3]) == 3]
    return dict(Counter(codons))

def generate_codon_heatmap(original_freq, optimized_freq):
    all_codons = sorted(set(original_freq.keys()) | set(optimized_freq.keys()))

    data = {
        'Codon': all_codons,
        'Original': [original_freq.get(c, 0) for c in all_codons],
        'Optimized': [optimized_freq.get(c, 0) for c in all_codons],
    }

    freq_data = [data['Original'], data['Optimized']]
    heatmap_data = []

    for i, row in enumerate(freq_data):
        heatmap_data.append(row)

    plt.figure(figsize=(18, 2.5))
    sns.heatmap([data['Original'], data['Optimized']],
                annot=True, fmt="d", cmap="YlGnBu",
                xticklabels=all_codons,
                yticklabels=["Original", "Optimized"],
                cbar=False)
    plt.xticks(rotation=90)
    st.pyplot(plt.gcf())
    plt.clf()


def render_codon_optimizer(seq):
    st.header("🧬 Codon Optimization (Host-Specific)")

    host = st.selectbox("Select Host Organism", list(CODON_USAGE_TABLES.keys()))
    

    if st.button("Optimize Codons"):
        if not seq:
            st.warning("Please enter a DNA sequence.")
            return

        optimized_seq = optimize_sequence(seq, host)
        st.subheader("🔁 Optimized Sequence")
        st.code(optimized_seq, language="text")

        original_freq = get_codon_frequency(seq)
        optimized_freq = get_codon_frequency(optimized_seq)

        st.subheader("📊 Codon Usage Heatmap")
        generate_codon_heatmap(original_freq, optimized_freq)
