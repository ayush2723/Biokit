def calculate_molecular_weight(seq: str) -> float:
    """
    Calculate the approximate molecular weight of a DNA sequence.

    Parameters:
        seq (str): DNA sequence consisting of A, T, G, C characters.

    Returns:
        float: Molecular weight in Daltons (g/mol).
    """
    # Define molecular weights for each nucleotide (in Daltons)
    weights = {
        'A': 313.21,
        'T': 304.2,
        'G': 329.21,
        'C': 289.18
    }

    # Convert sequence to uppercase for consistency
    seq = seq.upper()

    total_weight = 0.0

    # Sum up weights for each nucleotide in the sequence
    for nucleotide in seq:
        if nucleotide in weights:
            total_weight += weights[nucleotide]
        
    return total_weight
