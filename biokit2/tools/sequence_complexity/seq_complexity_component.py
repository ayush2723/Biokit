from biokit2.tools.sequence_complexity.seq_complexity import (
    estimate_sequence_complexity,
    sliding_entropy_profile
)
import streamlit as st
import matplotlib.pyplot as plt
from collections import Counter


def render_sequence_complexity_tool(sequence: str):
    st.subheader("🔍 Sequence Complexity Estimator")

    k = st.slider("Select K-mer length (k)", min_value=2, max_value=6, value=3, step=1)
    result = estimate_sequence_complexity(sequence, k)

    st.markdown("### 📊 Global Complexity Metrics")
    st.metric("Shannon Entropy", result["shannon_entropy"])
    st.metric(f"K-mer Diversity (k={k})", result["kmer_diversity"])

    st.markdown("**Interpretation**")
    st.info(
        "- Higher entropy → More random or diverse sequence\n"
        "- K-mer Diversity → Measures variety of k-mers. 1.0 = all unique, <1 = repetition"
    )

    st.markdown("### 📈 Entropy Along Sequence (Sliding Window)")
    window_size = st.slider("Window size", min_value=10, max_value=100, value=30, step=5)
    step_size = st.slider("Step size", min_value=1, max_value=20, value=5, step=1)
    positions, entropies = sliding_entropy_profile(sequence, window_size, step_size)

    # Use Matplotlib for entropy plot
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(positions, entropies, marker='o', linestyle='-', color='royalblue')
    ax.set_xlabel("Sequence Position")
    ax.set_ylabel("Shannon Entropy")
    ax.set_title("Local Sequence Complexity (Entropy Profile)")
    ax.grid(True)
    st.pyplot(fig)

    with st.expander("🔬 Base Composition"):
        base_counts = Counter(sequence)
        base_data = [base_counts.get(base, 0) for base in "ATGC"]

        fig2, ax2 = plt.subplots(figsize=(4, 3))
        ax2.bar(["A", "T", "G", "C"], base_data, color=["#2ca02c", "#d62728", "#1f77b4", "#ff7f0e"])
        ax2.set_ylabel("Count")
        ax2.set_title("Base Composition")
        st.pyplot(fig2)
