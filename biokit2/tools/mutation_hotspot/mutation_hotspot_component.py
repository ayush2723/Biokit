import streamlit as st
import plotly.express as px
import numpy as np

from biokit2.tools.mutation_hotspot.mutation_hotspot import find_hotspot_windows


def render_mutation_hotspot_tool(sequence: str):
    st.subheader(" Mutation Hotspot Detector")

    mutation_input = st.text_area("Enter known mutation positions (comma-separated)", placeholder="e.g. 5,12,30,31,32,78")

    if mutation_input:
        try:
            mutation_positions = [int(pos.strip()) for pos in mutation_input.split(",") if pos.strip().isdigit()]
        except ValueError:
            st.error("Invalid mutation position input. Please enter only comma-separated integers.")
            return

        window_size = st.slider("Sliding Window Size", min_value=5, max_value=100, value=20, step=5)
        step = st.slider("Step Size", min_value=1, max_value=20, value=5, step=1)
        threshold = st.slider("Mutation Count Threshold", min_value=1, max_value=10, value=3, step=1)

        
        sequence_length = len(sequence)
        full_windows = []
        density_array = []

        
        prefix = [0] * (sequence_length + 1)
        for pos in mutation_positions:
            if 0 <= pos < sequence_length:
                prefix[pos + 1] += 1
        for i in range(1, sequence_length + 1):
            prefix[i] += prefix[i - 1]

        for start in range(0, sequence_length - window_size + 1, step):
            end = start + window_size
            mutation_count = prefix[end] - prefix[start]
            density_array.append(mutation_count)
            full_windows.append(f"{start}-{end}")

        st.markdown("###  Mutation Density Heatmap")
        heatmap_fig = px.imshow(
            np.array([density_array]),
            labels=dict(x="Window Position", color="Mutation Count"),
            x=full_windows,
            y=["Density"],
            aspect="auto",
            color_continuous_scale="Reds"
        )
        heatmap_fig.update_layout(height=200, margin=dict(l=30, r=30, t=30, b=30))
        st.plotly_chart(heatmap_fig, use_container_width=True)

        # Show windows that qualify as hotspots
        hotspots = find_hotspot_windows(mutation_positions, sequence_length, window_size, threshold)

        st.markdown(f"###  {len(hotspots)} Hotspot(s) Above Threshold")
        if hotspots:
            st.dataframe(
                [{"Start": s, "End": e, "Mutation Count": c} for s, e, c in hotspots],
                use_container_width=True
            )
        else:
            st.info("No hotspots exceed the selected mutation threshold.")
