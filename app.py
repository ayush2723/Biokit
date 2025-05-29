import streamlit as st
import base64
import io  
from Bio import SeqIO



# Set theme before any Streamlit command
st.set_page_config(page_title="BioKit 1 - DNA Sequence Tools", layout="wide",page_icon="🧬")

# 🔧 Function to encode image to base64 and set background
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
    [data-testid = "stHeader"]{{
            background-color: rgba(0,0,0,0);    
        }}
    </style>
    """
    st.markdown(bg_css, unsafe_allow_html=True)

# Set the background image (place 'pic1.jpg' in the same folder)
set_bg_image("pic1.jpg")

# Import your DNA tools
from tools import (
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

# Import your UI components
from components import display_sequence, dna_input_box, plot_nucleotide_composition

# Page header
st.markdown("""
    <h1 style='text-align: center; color: #333;'>🧬BioKit 1</h1>
    <p style='text-align: center; font-size: 18px; color: #666;'>Simple, Reliable DNA Sequence Utilities.</p>
    <br>
""", unsafe_allow_html=True)

# Tool selector label styled and selectbox without label
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("""
       <div style='text-align: center;'>
            <label style='font-size: 22px; font-weight: 900; color: #111; display: block; margin-bottom: 8px;font-family: Courier New'>
                Choose a tool
            </label>
        </div>
    """, unsafe_allow_html=True)

    tool = st.selectbox(
        "",  
        [
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
        ],
    )

# Input mode selector
st.markdown("""
    <h3 style='color:#000000; font-family: Courier New, monospace;'>
         Input DNA Sequence
    </h3>
""", unsafe_allow_html=True)

input_mode = st.radio(
    "Choose DNA input mode:",
    ("Manual input", "Upload FASTA file"),
    index=0,
)

if input_mode == "Manual input":
    with st.form("manual_dna_input"):
        seq = dna_input_box()
        submitted = st.form_submit_button("Submit")
    
    if not submitted:
        st.stop()
    if not seq:
        st.info("Please enter a valid DNA sequence (A, T, G, C only).")
        st.stop()

elif input_mode == "Upload FASTA file":
    uploaded_file = st.file_uploader("Upload a FASTA file", type=["fasta", "fa"])
    if uploaded_file:
        # Wrap the binary uploaded_file in a text wrapper for SeqIO
        text_file = io.TextIOWrapper(uploaded_file, encoding='utf-8')
        
        sequences = list(SeqIO.parse(text_file, "fasta"))
        if not sequences:
            st.error("No sequences found in the FASTA file.")
            st.stop()
        
        seq_options = {seq_rec.id: str(seq_rec.seq) for seq_rec in sequences}
        selected_seq_id = st.selectbox("Select sequence to use", list(seq_options.keys()))
        seq = seq_options[selected_seq_id]
        
        st.write(f"Using sequence: {selected_seq_id} (length {len(seq)})")
    else:
        st.info("Please upload a FASTA file.")
        st.stop()

# Show original sequence
display_sequence("Original Sequence", seq)
st.markdown("---")

# Tool-specific output
with st.container():
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
        Peaks represent GC-rich regions, and valleys indicate GC-poor regions.

        Use: GC content affects DNA stability and gene regulation, 
        and helps identify important genomic features such as promoters or structural domains.
        """)
        plot_gc_distribution(seq)
        st.info("""
        **Use case:**  
        GC-rich regions tend to be more thermally stable and often mark functional regions like promoters and CpG islands.
        Variation in GC content can influence gene expression and genome organization.
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
        It ensures specificity and efficiency in molecular biology protocols.
        """)

    elif tool == "Molecular Weight":
        mw = calculate_molecular_weight(seq)
        st.subheader("Molecular Weight")
        st.write(f"{mw} Daltons")
        st.info("""
        **Use case:**  
        Molecular weight estimation helps in characterizing nucleic acids and calculating reagent concentrations for experiments like gel electrophoresis and mass spectrometry.
        """)

def show_contact():
    st.markdown("---")
    st.markdown("""
        <div style='padding: 10px; background-color: rgba(255,255,255,0.8); border-radius: 10px;'>
            <h3>📩 Get in Touch</h3>
            <p>If you have feedback, issues, or ideas, don’t hesitate to contact us!</p>
            <ul>
                <li><strong>Email:</strong> <a href="mailto:ayush1289sharmastdy@gmail.com">ayush1289sharmastdy@gmail.com</a></li>
                <li><strong>GitHub:</strong> <a href="https://github.com/ayush2723/Biokit1.git">Open a GitHub Issue</a></li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

# Always show contact section, regardless of stop()
show_contact()
