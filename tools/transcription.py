from Bio.Seq import Seq

def transcribe_dna(dna_sequence: str) -> str:
    """
    Transcribes a cleaned DNA sequence (A, T, G, C only) into its RNA equivalent.

    Args:
        dna_sequence (str): A validated DNA sequence.

    Returns:
        str: Transcribed RNA sequence (with U instead of T).
    """
    seq = Seq(dna_sequence.upper())  # Ensure the sequence is uppercase
    return str(seq.transcribe())
