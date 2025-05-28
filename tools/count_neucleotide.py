# tools/count_nucleotides.py

from collections import Counter

def count_nucleotides(seq: str) -> dict:
    """
    Count occurrences of each nucleotide in a DNA sequence.

    Args:
        seq (str): DNA sequence (A, T, G, C)

    Returns:
        dict: Counts of each nucleotide {'A': int, 'T': int, 'G': int, 'C': int}
    """
    seq = seq.upper()
    counts = Counter(seq)
    # Ensure all nucleotides are in the dictionary even if zero count
    return {nuc: counts.get(nuc, 0) for nuc in ['A', 'T', 'G', 'C']}
