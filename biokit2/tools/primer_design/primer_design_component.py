import streamlit as st
import matplotlib.pyplot as plt
from .primer_design import design_optimal_primers

def plot_primer_binding_sites(sequence, forward_start, reverse_start, primer_length):
    fig, ax = plt.subplots(figsize=(10, 1))
    colors = ['lightgray'] * len(sequence)

    for i in range(forward_start, min(forward_start + primer_length, len(sequence))):
        colors[i] = '#636EFA'  # Blue for forward

    for i in range(reverse_start, min(reverse_start + primer_length, len(sequence))):
        colors[i] = '#EF553B'  # Red for reverse

    ax.bar(range(len(sequence)), [1]*len(sequence), color=colors, edgecolor='black', linewidth=0.2)
    ax.set_yticks([])
    ax.set_xlim(0, len(sequence))
    ax.set_xlabel("Nucleotide Position")
    ax.set_title("Primer Binding Sites")
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    
    return fig

def render_optimal_primer_designer_tool(sequence: str):
    st.subheader("🧬 Optimal Primer Designer")

    if len(sequence) < 200:
        st.warning("⚠️ Input sequence is too short for primer design. Please use at least 200bp.")
        return

    primer_len = st.slider("Primer length", min_value=16, max_value=30, value=20)
    tm_tol = st.slider("Tm difference tolerance (°C)", min_value=1, max_value=10, value=2)

    result = design_optimal_primers(sequence, primer_length=primer_len, tm_tolerance=tm_tol)

    if result:
        st.success("✅ Primer pair successfully designed.")
        st.code(f"Forward Primer: 5' - {result['forward_primer']} - 3'\n"
                f"Reverse Primer: 5' - {result['reverse_primer']} - 3'")

        st.write(f"**Forward Primer Tm:** {result['forward_tm']} °C | **GC%:** {result['forward_gc']:.2f}%")
        st.write(f"**Reverse Primer Tm:** {result['reverse_tm']} °C | **GC%:** {result['reverse_gc']:.2f}%")

        if abs(result["forward_gc"] - result["reverse_gc"]) > 10:
            st.warning("⚠️ Large GC% difference between primers. Consider revising length or tolerance.")

        fig = plot_primer_binding_sites(sequence, result["forward_start"], result["reverse_start"], primer_len)
        st.pyplot(fig)

        st.caption("🔵 Forward primer | 🔴 Reverse primer")
        if st.checkbox("Show full sequence"):
            st.code(sequence, language="text")
    else:
        st.error("❌ Could not find optimal primer pair within given parameters.")
