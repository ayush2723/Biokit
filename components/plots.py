import matplotlib.pyplot as plt
from collections import Counter
import streamlit as st

def plot_nucleotide_composition(sequence: str):
    """
    Plots a compact nucleotide composition pie chart of the sequence.
    """
    counts = Counter(sequence.upper())
    labels = ['A', 'T', 'G', 'C']
    values = [counts.get(nuc, 0) for nuc in labels]

    # Create even smaller figure
    fig, ax = plt.subplots(figsize=(2.2, 2.2))  # Smaller than before
    wedges, texts, autotexts = ax.pie(
        values,
        labels=labels,
        autopct='%1.0f%%',
        startangle=90,
        colors=['#4CAF50', '#FF5722', '#2196F3', '#FFC107'],
        wedgeprops={'edgecolor': 'white'},
        textprops={'fontsize': 8}
    )

    ax.axis('equal')  # Ensure it stays a circle
    plt.setp(autotexts, size=7, weight="bold")
    ax.set_title("Nucleotide Composition", fontsize=10, pad=6)

    plt.tight_layout()

    # Center in narrow column
    with st.container():
        col1, col2, col3 = st.columns([2, 1, 2])
        with col2:
            st.pyplot(fig)
