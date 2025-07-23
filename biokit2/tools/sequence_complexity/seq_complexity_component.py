from biokit2.tools.sequence_complexity.seq_complexity import (
    estimate_sequence_complexity,
    sliding_entropy_profile
)
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
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

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=positions, y=entropies, mode="lines+markers", name="Entropy"))
    fig.update_layout(
        xaxis_title="Sequence Position",
        yaxis_title="Shannon Entropy",
        title="Local Sequence Complexity (Entropy Profile)",
        height=400,
        margin=dict(l=40, r=40, t=60, b=40),
    )
    st.plotly_chart(fig, use_container_width=True)

    with st.expander("🔬 Base Composition"):
        base_counts = Counter(sequence)
        base_data = {base: base_counts.get(base, 0) for base in "ATGC"}
        bar_fig = px.bar(
            x=list(base_data.keys()),
            y=list(base_data.values()),
            labels={"x": "Base", "y": "Count"},
            title="Base Composition"
        )
        st.plotly_chart(bar_fig, use_container_width=True)
