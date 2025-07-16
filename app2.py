import streamlit as st

# Page config
st.set_page_config(page_title="BioKit", layout="wide", page_icon="🧬")

# Style
st.markdown("""
    <style>
    .stApp {
        background-color: #f5f7fa;
        font-family: 'Segoe UI', sans-serif;
    }
    h1, h3 {
        text-align: center;
        color: #2b4162;
        font-weight: 700;
    }
    .stTabs [data-baseweb="tab"] {
        font-size: 16px;
        padding: 0.75rem 1.25rem;
    }
    .stTextArea textarea {
        background-color: #ffffff !important;
        color: #000000 !important;
    }
    </style>
""", unsafe_allow_html=True)
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



# Header
st.markdown("<h1>🧬 BioKit</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='margin-top: -10px;'>Precision Bioinformatics Toolkit for Modern Biology</h3>", unsafe_allow_html=True)

# Functions
def get_reverse_complement(seq): return seq[::-1]
def complement_sequence(seq): return seq.replace("A", "T").replace("T", "A").replace("G", "C").replace("C", "G")
def calculate_codon_frequency(seq): return {"ATG": 2, "TAA": 1}
def transcribe_dna(seq): return seq.replace("T", "U")
def translate_dna(seq): return "MKT"

def display_sequence(label, sequence):
    st.subheader(label)
    st.code(sequence)

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
        seq = st.text_area("Write or Paste DNA Sequence", height=120, key="text_bio1")

    elif input_mode == "Use Sample Sequence":
        sample_dict = {
            "Sample: BRCA1 (Partial)": "ATGGATTTTGGGAAGTTTCTGTTGGAAGCTGATTTTTGGAAG",
            "Sample: TP53 (Partial)": "AGGCTGCTCCCCAGGTCAGATCCTAGCGTCGAGCCCCCTCT",
            "Sample: Synthetic Test": "ATGCATGCATGCATGCATGCATGCATGCATGCATGCATGC"
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
        rev_comp = get_reverse_complement(seq)
        display_sequence("Reverse Complement", rev_comp)
        st.info("""
        **Use case:**  
        The reverse complement is crucial for understanding the complementary DNA strand.  
        It’s often used in designing primers for PCR and studying antisense RNA or double-stranded DNA structures.
        """)

    elif tool == "Complement Sequence":
        comp = complement_sequence(seq)
        display_sequence("Complement Sequence", comp)
        st.info("""
        **Use case:**  
        Finding the complement strand is key in DNA replication and transcription.  
        This helps researchers study interactions between DNA strands and enzymes like DNA polymerase.
        """)

    elif tool == "Codon Frequency":
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
        rna = transcribe_dna(seq)
        display_sequence("Transcribed RNA Sequence", rna)
        st.info("""
        **Use case:**  
        Transcription simulates how DNA is copied into messenger RNA (mRNA) in cells.  
        This step is critical for gene expression and understanding how genetic information is read.
        """)

    elif tool == "Translation (DNA → Protein)":
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
        tm = calculate_tm(seq)
        st.subheader("Melting Temperature (Tm)")
        st.write(f"{tm} °C")
        st.info("""
        **Use case:**  
        Melting temperature predicts the stability of DNA duplexes and is essential in PCR primer design and hybridization experiments.
        """)

    elif tool == "Molecular Weight":
        mw = calculate_molecular_weight(seq)
        st.subheader("Molecular Weight")
        st.write(f"{mw} Daltons")
        st.info("""
        **Use case:**  
        Molecular weight estimation helps in characterizing nucleic acids and calculating reagent concentrations for experiments like gel electrophoresis and mass spectrometry.
        """)

# ----------------- BioKit 2 -----------------
with tab2:
    st.subheader("BioKit 2: Advanced DSA + Creative Tools")

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
        user_seq = st.text_area("Write or Paste DNA Sequence", height=120, key="text_bio2")

    elif input_mode == "Use Sample Sequence":
        sample_dict = {
            "Sample: BRCA1 (Partial)": "ATGGATTTTGGGAAGTTTCTGTTGGAAGCTGATTTTTGGAAG",
            "Sample: TP53 (Partial)": "AGGCTGCTCCCCAGGTCAGATCCTAGCGTCGAGCCCCCTCT",
            "Sample: Synthetic Test": "ATGCATGCATGCATGCATGCATGCATGCATGCATGCATGC"
        }
        sample_choice = st.selectbox("Choose a sample sequence", list(sample_dict.keys()), key="sample_bio2")
        user_seq = sample_dict[sample_choice]
        st.code(user_seq, language="text")
    
    tool2 = st.selectbox("Choose a BioKit 2 Tool", [
        "Motif Finder ",
        "ORF Finder ",
        "Splice Site Predictor ",
        "Codon Optimization ",
        "Microsatellite ",
        "Restriction Site Mapper",
        "Palindrome & Inverted Repeat Finder",
        "Sequence Complexity Estimator",
        "Mutation Hotspot Detector",
        "Optimal Primer Designer "
    ], key="tool_bio2")

    if user_seq:
        if tool2 == "🎵 DNA to Music":
            st.success("🎼 This feature will convert your DNA to music soon!")
            st.markdown("Each nucleotide will correspond to a musical note.")
            st.markdown("Example logic: A = Do, T = Re, G = Mi, C = Fa 🎹")
        else:
            st.info(f"🔬 `{tool2}` feature coming soon. Stay tuned!")
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
