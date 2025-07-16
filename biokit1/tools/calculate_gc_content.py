import streamlit as st
import matplotlib.pyplot as plt
def gc_content_sliding_window(sequence, window_size=100):
    gc_values = []
    positions = []
    for i in range(0, len(sequence) - window_size + 1):
        window = sequence[i:i+window_size]
        gc_count = window.count('G') + window.count('C')
        gc_percent = (gc_count / window_size) * 100
        gc_values.append(gc_percent)
        positions.append(i)
    return positions, gc_values

def plot_gc_distribution(sequence):
    window_size = st.slider("Window Size for GC Content", 5, 500, 100, step=10)
    positions, gc_values = gc_content_sliding_window(sequence, window_size)

    fig, ax = plt.subplots(figsize=(10, 3))
    ax.plot(positions, gc_values, color='green')
    ax.set_xlabel("Position")
    ax.set_ylabel("GC%")
    ax.set_title(f'GC Content Distribution (window={window_size})')
    st.pyplot(fig)
