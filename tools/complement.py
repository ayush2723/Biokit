# tools/complement.py

def complement_sequence(seq: str) -> str:
    """
    Return the complement of a DNA sequence.
    A <-> T, C <-> G

    Args:
        seq (str): DNA sequence (A, T, G, C)

    Returns:
        str: Complement DNA sequence
    """
    complement_map = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}

    seq = seq.upper()
    complement_seq = ''.join(complement_map.get(nuc, 'N') for nuc in seq)  # 'N' for unknown chars

    return complement_seq
