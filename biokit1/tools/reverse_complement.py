from Bio.Seq import Seq

def get_reverse_complement(dna_seq: str) -> str: #takes string and returns string
    """
    Returns the reverse complement of a DNA sequence.
    
    Parameters:
    dna_seq (str): Input DNA sequence (should contain A, T, G, C only).
    
    Returns:
    str: Reverse complement of the input sequence.
    """
    # Create a Seq object
    seq = Seq(dna_seq.upper())
    
    # Get reverse complement and convert back to string
    rev_comp = str(seq.reverse_complement())
    
    return rev_comp
