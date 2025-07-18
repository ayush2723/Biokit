import streamlit as st
import pandas as pd
import altair as alt
from biokit2.data.restriction_enzyme import restriction_enzymes
from biokit2.tools.restriction_site.restriction_logic import find_restriction_sites

def render_restriction_mapper(sequence):
    st.header("🔪 Restriction Site Mapper")

    with st.expander("About this tool"):
        st.markdown("""
        Identifies known **restriction enzyme sites** within the input DNA sequence.  
        Useful for **cloning strategies**, **plasmid mapping**, and **genome analysis**.
        """)

    selected_enzymes = st.multiselect("Select Enzymes", options=restriction_enzymes.keys(), default=list(restriction_enzymes.keys())[:4])

    if st.button("Map Restriction Sites"):
        if not sequence:
            st.warning("Please input a DNA sequence.")
        elif not selected_enzymes:
            st.warning("Please select at least one enzyme.")
        else:
            result = find_restriction_sites(sequence.upper(), selected_enzymes)

            if not result:
                st.info("No restriction sites found for the selected enzymes.")
            else:
                # Flatten data for table
                table_data = []
                for item in result:
                    for pos in item["positions"]:
                        table_data.append({
                            "Enzyme": item["enzyme"],
                            "Site": item["site"],
                            "Position": pos
                        })

                df = pd.DataFrame(table_data)
                st.success(f"Found restriction sites for {len(result)} enzyme(s).")
                st.dataframe(df.sort_values(by="Position"), use_container_width=True)

                # Altair plot of positions
                chart = alt.Chart(df).mark_circle(size=100).encode(
                    x=alt.X("Position:Q", title="Sequence Position"),
                    y=alt.Y("Enzyme:N", title="Enzyme"),
                    tooltip=["Enzyme", "Site", "Position"]
                ).properties(
                    title="Restriction Site Positions",
                    height=300
                )
                st.altair_chart(chart, use_container_width=True)
