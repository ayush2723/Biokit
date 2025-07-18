import streamlit as st
import pandas as pd
from biokit2.tools.palindrome_inverted.palindrome_inverted import (
    find_perfect_palindromes, find_inverted_repeats
)

def render_palindrome_inverted(sequence):
    st.header("Palindrome & Inverted Repeat Finder")

    with st.expander("About this tool"):
        st.markdown("""
        This tool identifies:
        - 🧬 **Perfect palindromes**: regions that are reverse-complement symmetric
        - 🧬 **Inverted repeats**: left and right arms that are nearly reverse-complement with optional spacer/mismatches
        
        Such regions can form **hairpin loops** or **cruciform DNA**, impacting gene regulation and structure.
        """)

    col1, col2 = st.columns(2)
    with col1:
        min_len = st.number_input("Minimum Arm Length", 4, 20, 6)
        max_len = st.number_input("Maximum Arm Length", min_len, 30, 12)
    with col2:
        max_spacer = st.number_input("Max Spacer Length (Inverted Repeat)", 0, 10, 3)
        max_mismatches = st.number_input("Max Mismatches (Inverted Repeat)", 0, 5, 1)

    if st.button("Analyze Sequence"):
        if not sequence:
            st.warning("Please enter a DNA sequence.")
            return

        st.subheader("Perfect Palindromes")
        palins = find_perfect_palindromes(sequence.upper(), min_len, max_len)
        if not palins:
            st.text("No perfect palindromes found.")
        else:
            df_palin = pd.DataFrame(palins)
            df_palin["Position"] = df_palin["start"].astype(str) + "–" + df_palin["end"].astype(str)
            st.success(f"{len(df_palin)} palindromes found.")
            st.dataframe(df_palin[["sequence", "length", "Position"]], use_container_width=True)

        st.subheader("Inverted Repeats")
        invr = find_inverted_repeats(sequence.upper(), min_len, max_len, max_spacer, max_mismatches)
        if not invr:
            st.text("No inverted repeats found.")
        else:
            df_invr = pd.DataFrame(invr)
            df_invr["Arms"] = df_invr["left_arm"] + " ... " + df_invr["right_arm"]
            df_invr["Position"] = df_invr["start"].astype(str) + "–" + df_invr["end"].astype(str)
            st.success(f"{len(df_invr)} inverted repeats found.")
            st.dataframe(df_invr[["Arms", "length", "spacer", "mismatches", "Position"]], use_container_width=True)

            # Visual preview of potential hairpin
            st.subheader("Hairpin-Like Preview")
            match = df_invr.iloc[0]
            st.code(f"{match['left_arm']} ←spacer→ {match['right_arm']}", language="text")
