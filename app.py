import streamlit as st
import base64


# Page config
st.set_page_config(page_title="BioKit", layout="wide", page_icon="🧬")

def set_bg_image(image_file):
    with open(image_file, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()
    bg_css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-attachment: fixed;
        background-repeat: no-repeat;   
    }}
    [data-testid="stHeader"] {{
        background-color: rgba(0,0,0,0);    
    }}
    h1, h3 {{
        text-align: center;
        color: #2b4162;
        font-weight: 700;
        font-family: 'Segoe UI', sans-serif;
    }}
    .stTextArea textarea {{
        background-color: #ffffff !important;
        color: #000000 !important;
    }}
    </style>
    """
    st.markdown(bg_css, unsafe_allow_html=True)

# Set the background image (leave unchanged)
set_bg_image("images/pic31.jpg")

# Style
st.markdown(
    """
    <style>
    body {
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    .main {
        background-color: rgba(255, 255, 255, 0.8); /* semi-transparent content area */
        padding: 2rem;
        border-radius: 10px;
    }
    h1, h3 {
        font-family: 'Segoe UI', sans-serif;
        color: #0e1c36;
        margin-top: 0;
        margin-bottom: 0.5rem;
    }
    h3 {
        font-weight: 400;
    }
    </style>
    """,
    unsafe_allow_html=True
)


from biokit1.tools import (
    get_reverse_complement,
    complement_sequence,
    calculate_codon_frequency,
    plot_codon_histogram,
    gc_content_sliding_window,
    plot_gc_distribution,
    transcribe_dna,
    translate_dna,
    display_translation_view,
    count_nucleotides,
    find_palindromes,
    calculate_tm,
    calculate_molecular_weight,
)

from biokit1.components import display_sequence, dna_input_box, plot_nucleotide_composition
from biokit2.tools import (render_motif_finder,render_orf_finder,render_splice_site_predictor,
                           render_codon_optimizer,render_microsatellite_finder,render_restriction_mapper,
                           render_palindrome_inverted,render_sequence_complexity_tool,
                           render_mutation_hotspot_tool,render_optimal_primer_designer_tool)

# Header
st.markdown("""
    <div style='text-align: center; line-height: 1.2;'>
        <h1 style='margin-bottom: 0;'>🧬BioKit</h1>
        <h3 style='margin-top: 5px; color: gray;'>Bioinformatics Toolkit for Modern Biology</h3>
    </div>
""", unsafe_allow_html=True)


# Tabs
tab1, tab2 = st.tabs(["🧬 BioKit 1", "🔥 BioKit 2"])

# ----------------- BioKit 1 -----------------
with tab1:
    st.subheader("BioKit 1: Basic Tools")
    input_mode = st.radio("Choose Input Mode:", ["Upload FASTA File", "Write Your Own", "Use Sample Sequence"], horizontal=True, key="radio_bio1")

    seq = ""

    if input_mode == "Upload FASTA File":
        fasta_file = st.file_uploader("Upload a FASTA file", type=["fasta", "fa", "txt"], key="fasta_bio1")
        if fasta_file:
            content = fasta_file.read().decode("utf-8")
            lines = content.splitlines()
            seq = ''.join([line.strip() for line in lines if not line.startswith(">")])
            st.success("FASTA file uploaded and parsed successfully.")
            st.code(seq, language="text")
        else:
            st.info("Please upload a valid FASTA file.")

    elif input_mode == "Write Your Own":
         seq = dna_input_box(key="biokit1")
        
    elif input_mode == "Use Sample Sequence":
        sample_dict = {
            "Sample: BRCA1 (Partial)": "ATGGATTTTGGGAAGTTTCTGTTGGAAGCTGATTTTTGGAAG",
            "Sample: TP53 (Partial)": "AGGCTGCTCCCCAGGTCAGATCCTAGCGTCGAGCCCCCTCT",
            "Sample: Synthetic Test": "ATGCATGCATGCATGCATGCATGCATGCATGCATGCATGC",
            "Standard: Human Beta-Globin (Exon 1&2)": (
                "ATGGTGCACCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGA"
                "GGCCCTGGGCAGGTTGGTATCAAGGTTACAAGACAGGTTTAAGGAGACCAATAGAAACTGGGCATGTGGAGACAGAGAAG"
                "ACTCTTGGGG"
            ),
            "Standard: Lambda Phage Fragment": (
                "GGGCGGCGACCTCGCGGGTTTCTTCGCGGGGCGCGTTCGCCGACTGCCCGCTGCGCACCGGCGTCTGCGTGTCGTGCTCG"
                "TGGTGTGTCGCGCGCGGCTGTTGGTGTTGCGCGTCGGGCGCTCGCCCGCGTGTG"
            ),
            "Standard: M13mp18 Vector Region": (
                "GTTTTCCCAGTCACGACGTTGTAAAACGACGGCCAGTGAGCGCGCGTAATACGACTCACTATAGGGGAATTGTGAGCGGA"
                "TAACAATTTCACACAGGAAACAGCTATGACCATGATTACGCCAAGCTT"
            ),
            "Standard: pUC19 Plasmid Region": (
                "AGCTCGAATTCACTGGCCGTCGTTTTACAACGTCGTGACTGGGAAAACCCTGGCGTTACCCAACTTAATCGCCTTGCAGC"
                "TATGACCATGATTACGCCAAGCTTGATGCATGCCATGGTACAGTCTAG"
            ),
            "Standard: SARS-CoV-2 Spike Segment": (
                "ATGTTTGTTTTTCTTGTTTTAAGAAGGTTTATACCTTCCCAGGTAACAAACCAACCAACTTTCGATCTCTTGTAGATCT"
                "GTTCTCTAAACGAACTTTAAAATCTGTGTGGCTGTCACTCGGCTG"
            ),
            "Sample: BRCA1 (Partial)": (
                "ATGGATTTTGGGAAGTTTCTGTTGGAAGCTGATTTTTGGAAGAGAAATGGAGTTAAGGAAGCAG"
                "TATTTAGGTGGTTGAGGAAATCTGAGGAGAAATGGAGTTAAGGAAGCAGGTTTGGAGTGTGGA"
            ),

            "Sample: TP53 (Partial)": (
                    "AGGCTGCTCCCCAGGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGAC"
                    "CTAGGTTGGCTCTGACTGTACCACCATCCACTACAACTACATGTGTAACAGTTCCAAAGGC"
            ),

            "Sample: Lambda Phage (Partial)": (
                    "GGGCGGCGACCTCGCCGTGCGGCGACCTGCGCGGACCTCGCCGGGCGGCGGAGGCTGCGCC"
                    "GGGCGGCGACCTCGCCGTGCGGCGACCTGCGCGGACCTCGCCGGGCGGCGGAGGCTGCGCC"
            ),

            "Sample: Synthetic Repeats (AC-GT-CA Mix)": (
                    "ACACACACACACACACACGTGTGTGTGTGTGTGTGTCACACACACACACACACACGTGTGTG"
                    "TGTGTGTGTGTGTGTCACACACACACACACAC"
            ),

            "Sample: Random GC-rich (For Testing)": (
                    "GCGCGCGCGCGCGCGCATATATATATATATATAGCGCGCGCGCGCGCGCGCGCGCGCGCGC"
                    "TATATATATATATATAGCGCGCGCGCGCGCGC"
            )
                
            }

        sample_choice = st.selectbox("Choose a sample sequence", list(sample_dict.keys()), key="sample_bio1")
        seq = sample_dict[sample_choice]
        st.code(seq, language="text")


    tool = st.selectbox("", [
        "Reverse Complement",
        "Complement Sequence",
        "Codon Frequency",
        "GC Content",
        "Transcription (DNA → RNA)",
        "Translation (DNA → Protein)",
        "Nucleotide Count",
        "Find Palindromes",
        "Melting Temperature",
        "Molecular Weight",
    ], key="tool_bio1")

    if seq:
        display_sequence("Original Sequence", seq)

    if tool == "Reverse Complement":
        if seq:
            rev_comp = get_reverse_complement(seq)
            display_sequence("Reverse Complement", rev_comp)
            st.info("""
            **Use case:**  
            The reverse complement is crucial for understanding the complementary DNA strand.  
            It’s often used in designing primers for PCR and studying antisense RNA or double-stranded DNA structures.
            """)

    elif tool == "Complement Sequence":
        if seq:
            comp = complement_sequence(seq)
            display_sequence("Complement Sequence", comp)
            st.info("""
            **Use case:**  
            Finding the complement strand is key in DNA replication and transcription.  
            This helps researchers study interactions between DNA strands and enzymes like DNA polymerase.
            """)

    elif tool == "Codon Frequency":
        if seq:
            freq = calculate_codon_frequency(seq)
            st.subheader("Codon Frequency")
            st.write(freq)
            plot_codon_histogram(freq)
            st.info("""
            **Use case:**  
            Codon usage analysis reveals how organisms preferentially use certain codons over others.  
            This can indicate gene expression levels and optimize synthetic gene design for protein production.
            """)

    elif tool == "GC Content":
        if seq:
            st.markdown("### GC Content Distribution")
            st.write("""
            This graph shows the percentage of guanine (G) and cytosine (C) bases 
            across the DNA sequence, calculated over sliding windows of a chosen size.
            """)
            plot_gc_distribution(seq)
            st.info("""
            **Use case:**  
            GC-rich regions tend to be more thermally stable and often mark functional regions like promoters and CpG islands.
            """)

    elif tool == "Transcription (DNA → RNA)":
        if seq:
            rna = transcribe_dna(seq)
            display_sequence("Transcribed RNA Sequence", rna)
            st.info("""
            **Use case:**  
            Transcription simulates how DNA is copied into messenger RNA (mRNA) in cells.  
            This step is critical for gene expression and understanding how genetic information is read.
            """)

    elif tool == "Translation (DNA → Protein)":
        if seq:
            protein = translate_dna(seq)
            rna = transcribe_dna(seq)
            display_sequence("Protein Sequence", protein)
            display_translation_view(seq, rna, protein)
            st.info("""
            **Use case:**  
            Translation is the process where mRNA is decoded to synthesize proteins.  
            Understanding this helps in protein engineering, disease mutation analysis, and drug target discovery.
            """)

    elif tool == "Nucleotide Count":
        if seq:
            counts = count_nucleotides(seq)
            st.subheader("Nucleotide Counts")
            st.write(counts)
            plot_nucleotide_composition(seq)
            st.info("""
            **Use case:**  
            Nucleotide composition gives insights into DNA sequence characteristics, mutation biases, and genomic signatures.  
            It is also used for sequence quality control and classification of organisms.
            """)

    elif tool == "Find Palindromes":
        if seq:
            length = st.number_input("Palindrome Length", min_value=2, max_value=12, value=4, step=1)
            pals = find_palindromes(seq, length)
            st.subheader(f"Palindromes of length {length}")
            if pals:
                for p in pals:
                    st.code(p)
            else:
                st.write("No palindromes found.")
            st.info("""
            **Use case:**  
            Palindromic sequences in DNA are sites for restriction enzymes and are crucial in gene cloning and genome editing.  
            They also play roles in DNA secondary structures influencing replication and transcription.
            """)

    elif tool == "Melting Temperature":
        if seq:
            tm = calculate_tm(seq)
            st.subheader("Melting Temperature (Tm)")
            st.write(f"{tm} °C")
            st.info("""
            **Use case:**  
            Melting temperature predicts the stability of DNA duplexes and is essential in PCR primer design and hybridization experiments.
            """)

    elif tool == "Molecular Weight":
        if seq:
            mw = calculate_molecular_weight(seq)
            st.subheader("Molecular Weight")
            st.write(f"{mw} Daltons")
            st.info("""
            **Use case:**  
            Molecular weight estimation helps in characterizing nucleic acids and calculating reagent concentrations for experiments like gel electrophoresis and mass spectrometry.
            """)

# ----------------- BioKit 2 -----------------
with tab2:
    st.subheader("BioKit 2: Advanced Tools")

    input_mode = st.radio("Choose Input Mode:", ["Upload FASTA File", "Write Your Own", "Use Sample Sequence"], horizontal=True, key="radio_bio2")

    user_seq = ""

    if input_mode == "Upload FASTA File":
        fasta_file = st.file_uploader("Upload a FASTA file", type=["fasta", "fa", "txt"], key="fasta_bio2")
        if fasta_file:
            content = fasta_file.read().decode("utf-8")
            lines = content.splitlines()
            user_seq = ''.join([line.strip() for line in lines if not line.startswith(">")])
            st.success("FASTA file uploaded and parsed successfully.")
            st.code(user_seq, language="text")
        else:
            st.info("Please upload a valid FASTA file.")

    elif input_mode == "Write Your Own":
        user_seq = dna_input_box(key="biokit2")
    elif input_mode == "Use Sample Sequence":
        sample_dict = {
            "Sample: BRCA1 (Partial)": "ATGGATTTTGGGAAGTTTCTGTTGGAAGCTGATTTTTGGAAG",
            "Sample: TP53 (Partial)": "AGGCTGCTCCCCAGGTCAGATCCTAGCGTCGAGCCCCCTCT",
            "Sample: Synthetic Test": "ATGCATGCATGCATGCATGCATGCATGCATGCATGCATGC",
            "Sample: EcoRI Site ": "ATCGGAATTCGATCG",
            "Sample: Inverted Repeat Example": "GATCCGATATCGGATC",
            "Sample: Mutation Hotspot Example": "ATGCGTACGTAGCTAGCTAGCTAGCGTAGCTAGCTAGCTAGCATGCTAGCTAGCTAGCTAGCTGATCGATCGATCGATCGATGCTAGCTAGCTAGCTAGCTGATCG", 
            "Sample Primer design ": "ATGGATGATGATATCGCCGCGCTCGTCGTCGACAACGGCTCCGGCATGTGCAAGGCCGGCTTCGCGGGCGACGACGGCGGTGGTGACCTGGCCGCCAGAGGTTCCGTTGCCCTCCGGGCCGGCTCGCTGCTGCTGACCGAGGCCGACGACGACGACGACCTGGAGGAGGAGGAGCTGGAGATCGAGCTGGAGGAGGAAGGCCAGGAAGGCGGCGGCGGCGGCGGAGGAAGGAGGAGGAAGC",
            "Sample Motif-finder ":(
                    "AAAGGGCGGTATAAAGCCCAATGTTGCGCCCTTCCCAATAAATCAGTGAATAAA"
            ),
            "Standard: Human Beta-Globin (Exon 1&2)": (
                "ATGGTGCACCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGA"
                "GGCCCTGGGCAGGTTGGTATCAAGGTTACAAGACAGGTTTAAGGAGACCAATAGAAACTGGGCATGTGGAGACAGAGAAG"
                "ACTCTTGGGG"
            ),
            "Standard: Lambda Phage Fragment": (
                "GGGCGGCGACCTCGCGGGTTTCTTCGCGGGGCGCGTTCGCCGACTGCCCGCTGCGCACCGGCGTCTGCGTGTCGTGCTCG"
                "TGGTGTGTCGCGCGCGGCTGTTGGTGTTGCGCGTCGGGCGCTCGCCCGCGTGTG"
            ),
            "Standard: M13mp18 Vector Region": (
                "GTTTTCCCAGTCACGACGTTGTAAAACGACGGCCAGTGAGCGCGCGTAATACGACTCACTATAGGGGAATTGTGAGCGGA"
                "TAACAATTTCACACAGGAAACAGCTATGACCATGATTACGCCAAGCTT"
            ),
            "Standard: pUC19 Plasmid Region": (
                "AGCTCGAATTCACTGGCCGTCGTTTTACAACGTCGTGACTGGGAAAACCCTGGCGTTACCCAACTTAATCGCCTTGCAGC"
                "TATGACCATGATTACGCCAAGCTTGATGCATGCCATGGTACAGTCTAG"
            ),
            "Standard: SARS-CoV-2 Spike Segment": (
                "ATGTTTGTTTTTCTTGTTTTAAGAAGGTTTATACCTTCCCAGGTAACAAACCAACCAACTTTCGATCTCTTGTAGATCT"
                "GTTCTCTAAACGAACTTTAAAATCTGTGTGGCTGTCACTCGGCTG"
            ),
            "Sample: BRCA1 (Partial)": (
                "ATGGATTTTGGGAAGTTTCTGTTGGAAGCTGATTTTTGGAAGAGAAATGGAGTTAAGGAAGCAG"
                "TATTTAGGTGGTTGAGGAAATCTGAGGAGAAATGGAGTTAAGGAAGCAGGTTTGGAGTGTGGA"
            ),

            "Sample: TP53 (Partial)": (
                    "AGGCTGCTCCCCAGGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGAC"
                    "CTAGGTTGGCTCTGACTGTACCACCATCCACTACAACTACATGTGTAACAGTTCCAAAGGC"
            ),

            "Sample: Lambda Phage (Partial)": (
                    "GGGCGGCGACCTCGCCGTGCGGCGACCTGCGCGGACCTCGCCGGGCGGCGGAGGCTGCGCC"
                    "GGGCGGCGACCTCGCCGTGCGGCGACCTGCGCGGACCTCGCCGGGCGGCGGAGGCTGCGCC"
            ),

            "Sample: Synthetic Repeats (AC-GT-CA Mix)": (
                    "ACACACACACACACACACGTGTGTGTGTGTGTGTGTCACACACACACACACACACGTGTGTG"
                    "TGTGTGTGTGTGTGTCACACACACACACACAC"
            ),

            "Sample: Random GC-rich (For Testing)": (
                    "GCGCGCGCGCGCGCGCATATATATATATATATAGCGCGCGCGCGCGCGCGCGCGCGCGCGC"
                    "TATATATATATATATAGCGCGCGCGCGCGCGC"
            )
             

        }

        sample_choice = st.selectbox("Choose a sample sequence", list(sample_dict.keys()), key="sample_bio2")
        user_seq = sample_dict[sample_choice]
        st.code(user_seq, language="text")


    tool2 = st.selectbox("Choose a BioKit 2 Tool", [
        "Motif Finder",
        "ORF Finder",
        "Splice Site Predictor",
        "Codon Optimization",
        "Microsatellite Finder",
        "Restriction Site Mapper",
        "Palindrome & Inverted Repeat Finder",
        "Sequence Complexity Estimator",
        "Mutation Hotspot Detector",
        "Optimal Primer Designer"
    ], key="tool_bio2")

    if user_seq:
        if tool2 == "Motif Finder":
            render_motif_finder(user_seq)
        elif tool2 == "ORF Finder":
            render_orf_finder(user_seq)
        elif tool2 == "Splice Site Predictor":
            render_splice_site_predictor(user_seq)
        elif tool2 == "Codon Optimization":
            render_codon_optimizer(user_seq)
        elif tool2 == "Microsatellite Finder":
            render_microsatellite_finder(user_seq)
        elif tool2 == "Restriction Site Mapper":
            render_restriction_mapper(user_seq)
        elif tool2 == "Palindrome & Inverted Repeat Finder":
            render_palindrome_inverted(user_seq)
        elif tool2 == "Sequence Complexity Estimator":
            render_sequence_complexity_tool(user_seq)
        elif tool2 == "Mutation Hotspot Detector":
            render_mutation_hotspot_tool(user_seq)
        elif tool2 == "Optimal Primer Designer":
            render_optimal_primer_designer_tool(user_seq)
        else:
            st.info(f"`{tool2}` feature coming soon. Stay tuned!")
    else:
        st.warning("Please provide a DNA sequence to proceed.")



# Contact
st.markdown("---")
st.markdown("""
<div style='padding: 10px; background-color: #e8edf3; border-radius: 10px;'>
    <h4>📩 Get in Touch</h4>
    <p>If you have feedback, issues, or ideas, don’t hesitate to contact us!</p>
    <ul>
        <li><strong>Email:</strong> <a href="mailto:ayush1289sharmastdy@gmail.com">ayush1289sharmastdy@gmail.com</a></li>
        <li><strong>GitHub:</strong> <a href="https://github.com/ayush2723/Biokit1.git" target="_blank">Open a GitHub Issue</a></li>
    </ul>
</div>
""", unsafe_allow_html=True)
