def calculate_tm(seq: str) -> float:
    """
    Calculate melting temperature (Tm) of a DNA sequence.

    For sequences shorter than 14 bases, uses Wallace Rule:
        Tm = 2*(A+T) + 4*(G+C)
    For longer sequences:
        Tm = 64.9 + 41 * (G+C - 16.4) / length

    Args:
        seq (str): DNA sequence (only A, T, G, C, uppercase recommended)

    Returns:
        float: Estimated melting temperature in Celsius
    """
    seq = seq.upper()
    A = seq.count("A")
    T = seq.count("T")
    G = seq.count("G")
    C = seq.count("C")

    length = len(seq)

    if length < 14:
        tm = 2 * (A + T) + 4 * (G + C)
    else:
        tm = 64.9 + 41 * (G + C - 16.4) / length

    return round(tm, 2) #answer rounded to 2 decimal places
