import streamlit as st
import pandas as pd
from biokit2.tools.microsatellite_finder.microsatellite_logic import find_microsatellites

def render_microsatellite_finder(sequence):
    st.header("🔍 Microsatellite / STR Finder")

    with st.expander("About this tool"):
        st.markdown("""
        Detects **Short Tandem Repeats (STRs)** — patterns of repeated DNA motifs like `CA`, `GATA`, etc.  
        These are important in **genome annotation**, **forensics**, and **genetic diversity studies**.
        """)

    col1, col2, col3 = st.columns(3)
    with col1:
        min_unit_len = st.number_input("Min Unit Length", 1, 10, 2)
    with col2:
        max_unit_len = st.number_input("Max Unit Length", min_unit_len, 12, 6)
    with col3:
        min_repeats = st.number_input("Min Repeats", 2, 100, 5)

    if st.button("Find Microsatellites"):
        if not sequence:
            st.warning("Please enter a DNA sequence.")
        else:
            results = find_microsatellites(sequence.upper(), min_unit_len, max_unit_len, min_repeats)

            if not results:
                st.info("No microsatellites found with the given criteria.")
            else:
                df = pd.DataFrame(results)
                df["Length"] = df["end"] - df["start"] + 1
                df["Position"] = df["start"].astype(str) + "–" + df["end"].astype(str)
                df_display = df[["motif", "repeats", "Length", "Position"]]
                df_display.columns = ["Motif", "Repeats", "Length", "Position"]

                st.success(f"✅ Found {len(df)} microsatellites!")

                # Use custom HTML table with center-aligned content
                st.markdown("""
                <style>
                .custom-table {
                    border-collapse: collapse;
                    width: 100%;
                }
                .custom-table th, .custom-table td {
                    border: 1px solid #ddd;
                    padding: 8px;
                    text-align: center;
                }
                .custom-table th {
                    background-color: #f2f2f2;
                }
                </style>
                """, unsafe_allow_html=True)

                html_table = "<table class='custom-table'><tr><th>Motif</th><th>Repeats</th><th>Length</th><th>Position</th></tr>"
                for _, row in df_display.iterrows():
                    html_table += f"<tr><td>{row['Motif']}</td><td>{row['Repeats']}</td><td>{row['Length']}</td><td>{row['Position']}</td></tr>"
                html_table += "</table>"

                st.markdown(html_table, unsafe_allow_html=True)
